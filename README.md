# Stock Analysis Pipeline

## Project Overview
The Stock Analysis Pipeline is a Python-based data analysis project designed to perform stock price analysis using historical stock data. The pipeline includes data loading, cleaning, analysis, and visualization of stock prices. This project aims to provide insights into stock performance and trends over time.

## Table of Contents
- Features
- Technologies Used
- Installation
- Usage
- Data Structure
- Analysis Techniques
- Visualizations
- Contributing
- License

## Features
- Load stock price data from CSV files.
- Clean and preprocess the data (handle missing values, duplicates, and standardize column names).
- Perform exploratory data analysis (EDA) to summarize the data.
- Identify top and bottom performing stocks.
- Check for inconsistencies in stock price data.
- Generate visualizations to represent stock price trends and correlations.

## Technologies Used
- Python: The primary programming language used for the analysis.
- Pandas: For data manipulation and analysis.
- NumPy: For numerical operations.
- Matplotlib: For creating static, animated, and interactive visualizations.
- Seaborn: For statistical data visualization.

## Installation
To set up the project locally, follow these steps:

Clone the repository:

```bash
git clone https://github.com/b-kenneth/Group3-Week1-Lab.git
cd stock_analysis_pipeline
```

Install the required packages:

```bash
pip install pandas numpy matplotlib seaborn
```

Ensure you have the stock data CSV files in the `data/` directory.

## Usage
To run the stock analysis pipeline, execute the following command in your terminal:

```bash
python data_analysis_pipeline.py
```

## Data Loading
The script loads stock price data from CSV files located in the specified directory. Each CSV file should contain historical stock data with columns such as Date, Open, High, Low, Close, and Volume.

## Data Cleaning
The pipeline performs the following cleaning steps:
- Converts column names to lowercase and replaces spaces with underscores.
- Checks for and handles missing values.
- Identifies and removes duplicate rows.

## Data Analysis
The analysis includes:
- Summary statistics of the dataset.
- Identification of the top 10 highest closing stocks.
- Checking for inconsistencies in high and low prices.

## Visualizations
The project generates visualizations to represent:
- Closing price trends over time for specific stocks.
- Correlation heatmaps for numeric columns in the dataset.

## Data Structure
The expected structure of the CSV files is as follows:

| Column | Description |
|--------|-------------|
| Date   | The date of the stock price. |
| Open   | The opening price of the stock. |
| High   | The highest price of the stock during the day. |
| Low    | The lowest price of the stock during the day. |
| Close  | The closing price of the stock. |
| Volume | The number of shares traded. |

## Analysis Techniques
- Sorting: To find the top and bottom performing stocks.
- Grouping: To analyze stock performance by company.
- Statistical Analysis: To compute summary statistics and correlations.

## Visualizations
- Time series plots for stock closing prices.
- Heatmaps for correlation between different stock metrics.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
