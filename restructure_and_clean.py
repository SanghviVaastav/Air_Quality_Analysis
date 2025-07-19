import os
import pandas as pd
import numpy as np
import re
import time

def get_year_from_filename(filename):
    """Extracts the year from the filename using regex."""
    match = re.search(r'(\d{4})', filename)
    if match:
        return int(match.group(1))
    return None

def restructure_and_clean_data(output_file='AQI_Data_Cleaned.csv'):
    """
    Restructures the data from wide to long format, cleans it, and saves it as a CSV file.
    """
    # Remove the output file if it exists, with retries for file locks
    if os.path.exists(output_file):
        for i in range(3):
            try:
                os.remove(output_file)
                print(f"Removed existing file: {output_file}")
                break
            except PermissionError:
                if i < 2:
                    print(f"Permission denied. Retrying in 2 seconds...")
                    time.sleep(2)
                else:
                    print("Could not remove file. Please ensure it is not open in another program.")
                    return
    all_city_data = []
    cities = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]

    for city in cities:
        city_path = os.path.join(os.getcwd(), city)
        files = [f for f in os.listdir(city_path) if f.endswith('.xlsx') and not f.startswith('~$')]

        for file in files:
            year = get_year_from_filename(file)
            if not year:
                continue

            df = pd.read_excel(os.path.join(city_path, file))
            df.rename(columns={'Date': 'Day'}, inplace=True)
            
            # Melt the dataframe to long format
            df_melted = df.melt(id_vars=['Day'], var_name='Month', value_name='AQI')
            df_melted.dropna(subset=['AQI'], inplace=True)

            # Create a proper date column
            month_map = {
                'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
            }
            df_melted['Month'] = df_melted['Month'].map(month_map)
            df_melted['Year'] = year
            
            # Combine to create the date
            df_melted['Date'] = pd.to_datetime(df_melted[['Year', 'Month', 'Day']], errors='coerce')
            df_melted.dropna(subset=['Date'], inplace=True)
            
            df_melted['City'] = city
            all_city_data.append(df_melted[['City', 'Date', 'AQI']])

    # Concatenate all data
    if not all_city_data:
        print("No data processed.")
        return

    final_df = pd.concat(all_city_data, ignore_index=True)
    final_df.sort_values(by=['City', 'Date'], inplace=True)

    # --- Data Cleaning ---
    final_df.set_index('Date', inplace=True)
    final_df['AQI'] = final_df.groupby('City')['AQI'].transform(
        lambda x: x.interpolate(method='time')
    )

    # Recalculate AQI Bucket
    def get_aqi_bucket(x):
        if x <= 50: return 'Good'
        elif x <= 100: return 'Satisfactory'
        elif x <= 200: return 'Moderate'
        elif x <= 300: return 'Poor'
        elif x <= 400: return 'Very Poor'
        else: return 'Severe'
    final_df['AQI_Bucket'] = final_df['AQI'].apply(get_aqi_bucket)

    # Remove Outliers
    for city in final_df['City'].unique():
        city_filter = final_df['City'] == city
        Q1 = final_df.loc[city_filter, 'AQI'].quantile(0.25)
        Q3 = final_df.loc[city_filter, 'AQI'].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        final_df.loc[city_filter, 'AQI'] = final_df.loc[city_filter, 'AQI'].clip(lower, upper)

    final_df.reset_index(inplace=True)
    
    # --- Feature Engineering ---
    final_df['Year'] = final_df['Date'].dt.year
    final_df['Month'] = final_df['Date'].dt.month
    final_df['Day'] = final_df['Date'].dt.day

    # Add Global AQI Bucket
    def get_global_aqi_bucket(x):
        if x <= 15: return 'Good'
        elif x <= 35: return 'Moderate'
        elif x <= 55: return 'Unhealthy for Sensitive Groups'
        elif x <= 150: return 'Unhealthy'
        elif x <= 250: return 'Very Unhealthy'
        else: return 'Hazardous'
    final_df['Global_AQI_Bucket'] = final_df['AQI'].apply(get_global_aqi_bucket)

    # Save to CSV
    final_df.to_csv(output_file, index=False)
    print(f"Data restructuring and cleaning complete. Saved to '{output_file}'.")

if __name__ == "__main__":
    restructure_and_clean_data()
