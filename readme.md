# Air Quality Analysis of Major Indian Cities

## 1. Introduction

This project performs an in-depth analysis of the Air Quality Index (AQI) across several major Indian cities: Bengaluru, Chennai, Delhi, Madikeri, and Mumbai. The primary objective is to uncover trends, patterns, and comparative insights into the air quality of these cities over several years.

The analysis involves data extraction, cleaning, restructuring, and visualization to provide a comprehensive overview of the air pollution landscape.

## 2. Dataset

The data for this project is sourced from two main places:

*   **Daily AQI Data**: Daily city-level AQI data is provided in `.xlsx` files, organized by city and year. These files are located in their respective city folders (`Bengaluru/`, `Chennai/`, etc.).The files are downloaded from Central Pollution Control Board (CPCB) website **"https://airquality.cpcb.gov.in/ccr/"**.

The cleaned and consolidated dataset used for the final analysis is `AQI_Data_Cleaned.csv`.

## 3. Project Structure

The project is organized as follows:

```

├── Bengaluru/                         # Daily AQI data for Bengaluru
│   ├── AQI_daily_city_level_bengaluru_2017_bengaluru_2017.xlsx
│   └── ...
├── Chennai/                           # Daily AQI data for Chennai
├── Delhi/                             # Daily AQI data for Delhi
├── Madikeri/                          # Daily AQI data for Madikeri
├── Mumbai/                            # Daily AQI data for Mumbai
├── extract_pdf_data.py                # Script to extract data from PDFs
├── restructure_and_clean.py           # Script to clean and merge all data sources
├── AQI_Data_Cleaned.csv               # The final, cleaned dataset for analysis
├── AQI_Analysis.ipynb                 # Jupyter Notebook with the data analysis
└── readme.md                          # This file
```

## 4. Data Processing Pipeline

The raw data is processed in two main steps:

1.  **PDF Data Extraction**: The `extract_pdf_data.py` script is used to parse the `.pdf` files from the `Annual average Pollutants values/` directory and extract the relevant pollutant data.
2.  **Data Cleaning and Restructuring**: The `restructure_and_clean.py` script takes the daily AQI data from the city-specific `.xlsx` files and merges it with the extracted PDF data. It performs cleaning operations like handling missing values, standardizing formats, and creates the final `AQI_Data_Cleaned.csv` file.

## 5. Analysis Overview

The core analysis is conducted in the `AQI_Analysis.ipynb` Jupyter Notebook. The key analytical steps include:

*   **Descriptive Statistics**: Calculating summary statistics for AQI, both overall and on a per-city basis.
*   **Time Series Analysis**: Plotting the AQI values over time for each city to observe long-term trends.
*   **Comparative Analysis**: Using boxplots to compare the AQI distributions among the different cities.
*   **Data Visualization**: Creating heatmaps of monthly average AQI to visualize seasonal patterns.
*   **Seasonal Decomposition**: Breaking down the time series data into trend, seasonal, and residual components to understand underlying patterns.
*   **Rolling Averages**: Calculating and plotting 90-day rolling averages to smooth out short-term fluctuations and highlight long-term trends.
*   **Year-over-Year Comparison**: Comparing monthly average AQI levels across different years for each city.

## 6. How to Run the Project

To replicate the analysis, follow these steps:

1.  **Install Dependencies**: Make sure you have Python and the required libraries installed. You can install them using pip:
    ```bash
    pip install pandas numpy matplotlib seaborn statsmodels
    ```
    You might also need libraries for reading `.xlsx` files (`openpyxl`) and `.pdf` files (`PyPDF2` or `pdfplumber`), depending on the implementation in the scripts.

2.  **Run the Data Processing Scripts**:
    *   Execute `extract_pdf_data.py` to process the PDFs.
    *   Execute `restructure_and_clean.py` to generate `AQI_Data_Cleaned.csv`.

3.  **Run the Analysis**: Open and run the `AQI_Analysis.ipynb` notebook in a Jupyter environment to see the full analysis and visualizations.

## 7. Visualizations and Insights

This section details the key visualizations from the analysis and the insights derived from each.

**Note**: Please save the plots generated from the `AQI_Analysis.ipynb` notebook into the `images/` directory to have them displayed here.

### a. Time Series of AQI Levels

![AQI Over Time](images/aqi_over_time.png)

**Insight**: This plot shows the daily AQI values from 2017 to 2024 for all cities. It is evident that Delhi consistently experiences the highest AQI levels, often reaching hazardous levels, while cities like Madikeri maintain relatively good air quality. The plot also reveals seasonal spikes, particularly during the winter months across most cities.

### b. AQI Distribution by City

![AQI Distribution](images/aqi_distribution.png)

**Insight**: The boxplot provides a comparative view of the AQI distribution for each city. Delhi's boxplot is significantly higher and more spread out, indicating not only worse air quality on average but also greater variability. In contrast, Madikeri shows a much lower and tighter distribution, confirming its better and more stable air quality.

### c. Monthly Average AQI Heatmap

![Monthly AQI Heatmap](images/monthly_aqi_heatmap.png)

**Insight**: The heatmap visualizes the monthly average AQI for each city across the years. The darker colors, representing higher AQI, are predominantly seen in the winter months (October to January), especially for northern cities like Delhi. This confirms a strong seasonal pattern in air pollution.

### d. Seasonal Decomposition of AQI

![Seasonal Decomposition](images/seasonal_decomposition.png)

**Insight**: This analysis breaks down the AQI time series into its trend, seasonal, and residual components. The trend component for most cities shows fluctuations over the years, while the seasonal component clearly highlights a recurring yearly pattern, with peaks in winter and troughs during the monsoon season.

### e. 90-Day Rolling Average AQI

![Rolling Average AQI](images/rolling_average_aqi.png)

**Insight**: By smoothing out daily fluctuations, the 90-day rolling average provides a clearer view of the long-term trends. This visualization makes it easier to see the overall rise or fall in AQI levels over the years for each city, abstracting away the day-to-day noise.

### f. Year-over-Year AQI Comparison

![Year-over-Year Comparison](images/year_over_year_comparison.png)

**Insight**: This plot allows for a direct comparison of monthly AQI levels across different years within the same city. It is useful for identifying whether air quality in a particular month is improving or worsening over the years. For example, it can help answer questions like, "Was January 2023 better or worse than January 2022 in Delhi?"
