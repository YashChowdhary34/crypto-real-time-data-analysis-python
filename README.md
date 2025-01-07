# Crypto Real-Time Data Analysis and Reporting

<div align="center">
    <img src="https://github.com/user-attachments/assets/e5a594ab-ce2b-4a42-a071-28806c29e833" alt="Coingecko Logo" height="300" width="500">
</div>

---

## Overview

This project automates the process of fetching real-time cryptocurrency data, performing basic analysis, generating forecasts, and sending daily reports via email. The daily report includes a CSV file containing the complete dataset and a Jupyter Notebook with visualizations and forecasts for the cryptocurrency market.

---

## Table of Contents

- [Project Workflow](#Project-Workflow)
- [Tech Stack](#Tech-Stack)
- [Outputs](#Outputs)
- [Example Outputs](#Example-Outputs)
- [Future Work](#future-work)
- [Conclusion](#conclusion)

---

## Introduction

## Project Workflow

### 1. **Data Fetching**
Real-time cryptocurrency data is fetched using the CoinGecko API and saved locally in a CSV file. The dataset includes:
- Cryptocurrency name and ID.
- Current price, market cap, and total volume.
- 24-hour high and low prices.
- Percentage change in price over the last 24 hours.
- Timestamp of data retrieval.

### 2. **Data Analysis**
A dynamically generated Jupyter Notebook performs:
- **Descriptive Analysis**: Provides summary statistics of cryptocurrency prices, volumes, and market caps.
- **Visualizations**: Displays price trends with both static (`matplotlib`) and interactive (`plotly`) plots.
- **Forecasting**: Predicts the price trends for the next 7 days using Facebook Prophet.

### 3. **Email Delivery**
The generated reports are emailed daily. Attachments include:
- The complete dataset as a CSV.
- CSV files highlighting the top gainers and losers.
- The Jupyter Notebook with visualizations and forecasts.


---

## Tech Stack

This project uses the following technologies and tools:

### Programming Languages and Frameworks
- **Python**: Primary programming language for data fetching, processing, and analysis.
- **Facebook Prophet**: Forecasting library for predicting cryptocurrency trends.
- **Matplotlib**: For static data visualization.
- **Plotly**: For interactive data visualizations.
- **Jupyter Notebook**: For detailed daily analysis and reporting.

### Libraries and APIs
- **Pandas**: For data manipulation and analysis.
- **Requests**: To fetch cryptocurrency data from the [CoinGecko API](https://www.coingecko.com/en/api).
- **Schedule**: To automate the daily execution of tasks.
- **smtplib**: For sending emails with attachments.

### Email Delivery
- **SMTP**: Email communication protocol for sending daily reports.

### Environment
- **Python 3.7+**: Ensure compatibility with libraries like `prophet`.
- **Virtual Environment**: Recommended for managing dependencies.


---

## Outputs

This project generates the following outputs daily:

### Email Report
The email contains:
1. **Complete Cryptocurrency Dataset**: Includes all cryptocurrencies with relevant market data.
2. **Top 10 Gainers**: Cryptocurrencies with the highest price increases in the last 24 hours.
3. **Top 10 Losers**: Cryptocurrencies with the highest price decreases in the last 24 hours.
4. **Jupyter Notebook**: A detailed daily analysis and forecasting report.

---

### Example Outputs

#### 1. **Email Screenshot**
> Screenshot of the received email:
<p align="center">
    <img src="https://github.com/user-attachments/assets/3269eaff-a1f9-4cac-9283-f7ac8d016f39" alt="Email Screenshot" width="600">
</p>

#### 2. **Daily Price Trend**
> Example of a static plot showing daily price trends:
<p align="center">
    <img src="https://github.com/user-attachments/assets/afecb66c-2089-49fa-9d1b-e528eaedb44d" alt="Static Plot" width="600">
</p>

#### 3. **Forecasting**
> Example of a static plot showing forecasting:
<p align="center">
    <img src="https://github.com/user-attachments/assets/5f72e017-5762-42fb-b354-e6d5edb53487" alt="Interactive Plot" width="600">
</p>

---

## Future Work

To make this system more insightful and actionable, I plan to:

1. **Develop an automated data analysis system**:
    - Use machine learning to predict trends based on historical data.
    - Generate more interactive visualizations using tools like Plotly or Matplotlib.
2. **Store data in a database**:
    - Integrate a database like MongoDB or PostgreSQL for better data management.
    - Build a dashboard for real-time monitoring of cryptocurrency trends.
3. **Enhance email reports**:
    - Include graphical summaries of top gainers/losers.
    - Add multi-recipient functionality.

---

## Conclusion

This project demonstrates the power of automation in simplifying complex tasks like real-time data analysis and reporting. By combining Python libraries with API integration, email automation, and scheduling, this project serves as a robust tool for staying informed about the volatile cryptocurrency market. In future enhancements, I am planning it to make it even more scalable and insightful.
