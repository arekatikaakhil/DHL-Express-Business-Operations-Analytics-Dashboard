
# DHL Express Business Operations Analytics Dashboard

## Project Overview

This project presents an **interactive Power BI dashboard** analyzing DHL Express operational data. The dashboard consolidates information across **orders**, **shipping**, **customers**, **products**, and **departments** into a single, actionable view.

It enables business leaders to monitor key metrics such as **sales**, **orders**, **delivery performance**, and **customer behavior**, and make informed, data-driven decisions to improve efficiency, customer satisfaction, and profitability.

---
![image](https://github.com/user-attachments/assets/badb5b69-e755-4228-b2d7-7877808275bb)

## Features

* Real-time operational KPIs: Total Sales, Total Orders, On-Time Delivery Percentage, Average Shipping Days
* Trend analysis of monthly orders and delivery performance
* Regional and market-level performance comparisons
* Customer segmentation insights: corporate vs. consumer, regions, and discount patterns
* Shipping mode analysis: balancing reliability and speed
* Actionable recommendations for operational and strategic improvements

---

## Tools and Technologies

* **SQL**: Queried relational tables to extract, join, and filter relevant columns, calculated intermediate fields, and ensured referential integrity
* **Python (pandas)**: Additional data cleaning, handling missing values, removing duplicates, standardizing column names/formats, and exporting cleaned datasets
* **Power BI**:

  * Designed data model (star schema)
  * Built interactive dashboards with slicers, filters, DAX measures, and visuals
  * Published for easy access and decision support

---

## Data Model

The dashboard is powered by a **star schema data model**, ensuring efficiency and simplicity.

### Tables

* **Fact Table:**

  * `Orders`: Transactional data, calculated fields, and KPIs

* **Dimension Tables:**

  * `Shipping`: Shipping mode, delivery times, and status
  * `Customers`: Segments, region, city, and geographic details
  * `Products`: Product names, categories, departments, and prices
  * `Department`: Department-level attributes and locations
  * `DateTable`: Calendar table for time-series analysis (month, quarter, year)

This model improves performance and supports robust DAX calculations for KPIs and trends.

### Data Model Diagram

*(Include and link the provided image in your repository, named for example `data_model.png`.)*
![image](https://github.com/user-attachments/assets/3f727969-8091-4ac8-974c-f3745f0c6278)

---

## Dashboard Pages

1. **Main Dashboard**
   Overview of sales, orders, shipping days, and on-time delivery

2. **Orders Page**
   Monthly order trends, regional distribution, and average profit per order

3. **Shipping Page**
   Performance by shipping mode, risk analysis, delivery status funnel, and shipping days

4. **Customers Page**
   Customer segment and regional distribution, shipping preferences, and discount insights

5. **Insights Page**
   Summarized findings, actionable recommendations, and strategic business impact

---

## Strategic Insights and Business Impact

* Highlights underperforming regions, shipping modes, and customer segments for targeted improvements
* Identifies on-time delivery as a key driver of customer satisfaction and operational efficiency
* Supports tailored marketing and pricing strategies based on customer behavior patterns
* Reveals opportunities to align inventory and promotions with high-margin, high-demand products
* Helps balance operational efficiency, customer experience, and profitability through informed decisions

---

## Project Structure

```
data/
    cleaned_data.csv
    raw_data/
visuals/
    dashboard_screenshots/
    data_model.png
DHL_Analytics_Dashboard.pbix
README.md
LICENSE
```

---

## How to Run

1. Open the `.pbix` file (`DHL_Analytics_Dashboard.pbix`) in **Power BI Desktop**.
2. Refresh data or replace with your own updated dataset.
3. Explore interactive dashboard pages and slicers.
4. Optionally publish the dashboard to Power BI Service for online sharing.

---

## License

**Copyright © Akhil Arekatika. All rights reserved.**

This project is intended for **educational and portfolio purposes only**. Redistribution, commercial use, or modification without explicit permission from the author is not permitted.

---

## Repository

The complete project files, including cleaned datasets, SQL and Python scripts, Power BI dashboard file, and screenshots, are available in this repository.

---

## Contact

**Developed by:** Akhil Arekatika
Email: [arekatikaakhil@gmail.com](mailto:arekatikaakhil@gmail.com)

If you have questions, suggestions, or feedback, feel free to contact me.

