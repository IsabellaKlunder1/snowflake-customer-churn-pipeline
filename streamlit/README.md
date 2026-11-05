# Snowflake Customer Churn Data Engineering Pipeline

## Project Overview

Built an end-to-end customer churn analytics pipeline using Snowflake, SQL, Python, and Streamlit to analyze 7,043 customer records from the IBM Telco Customer Churn dataset.

The project demonstrates cloud data warehousing, SQL transformations, data quality validation, business intelligence reporting, and interactive dashboard development.

## Technologies Used

- **Snowflake:** Cloud data warehouse
- **SQL:** Data cleaning, transformations, aggregations, and validation
- **Python:** Dashboard development and data retrieval
- **Streamlit:** Interactive business intelligence dashboard
- **Snowpark:** Connection between Python and Snowflake
- **GitHub:** Version control and project documentation

## Pipeline Architecture

IBM Telco Customer Churn CSV  
↓  
Snowflake RAW Schema  
↓  
Snowflake STAGING Schema  
↓  
Snowflake ANALYTICS Schema  
↓  
Streamlit Dashboard

## Key Features

- Loaded and analyzed 7,043 customer records.
- Created a three-layer RAW, STAGING, and ANALYTICS architecture.
- Identified and preserved 11 missing TotalCharges values.
- Validated customer ID uniqueness, churn values, and nonnegative monthly charges.
- Developed reusable SQL transformations and a manual pipeline refresh script.
- Built an interactive Streamlit dashboard with contract-type filtering.
- Analyzed customer churn rates and monthly revenue associated with churned customers.

## Business Insights

| Contract Type | Customers | Churn Rate |
|---|---:|---:|
| Month-to-month | 3,875 | 42.71% |
| One year | 1,473 | 11.27% |
| Two year | 1,695 | 2.83% |

**Overall customer churn rate: 26.54%.**

Month-to-month customers experienced the highest observed churn rate, suggesting an opportunity to investigate retention strategies for this segment.

These findings demonstrate associations in a historical sample dataset, not proof that contract length causes customer churn.

## Data Quality

Validation confirmed:

- 7,043 total customer records
- 7,043 unique customer IDs
- Zero missing customer IDs
- Zero invalid churn values
- Zero negative monthly charges
- 11 missing TotalCharges values identified and preserved
- Overall data quality status: PASS

## Project Structure

```text
snowflake-customer-churn-pipeline/
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_clean_customers.sql
│   ├── 03_churn_analytics.sql
│   ├── 04_data_quality_tests.sql
│   └── 05_refresh_pipeline.sql
├── streamlit/
│   └── app.py
└── README.md
```

## Reproducing the Project

1. Obtain the IBM Telco Customer Churn CSV dataset.
2. Create the Snowflake database and schemas using `01_create_database.sql`.
3. Load the CSV into `CUSTOMER_CHURN_DB.RAW.TELCO_CUSTOMERS`, preserving `TotalCharges` as text.
4. Run the cleaning and analytics SQL scripts.
5. Create the data quality validation view.
6. Run the manual refresh script to rebuild downstream tables and verify results.
7. Create a Streamlit app in Snowflake and use the code in `streamlit/app.py`.

A Snowflake warehouse and appropriate database permissions are required. The refresh process is manually executed rather than automatically scheduled.

## Future Improvements

- Schedule pipeline execution using Snowflake Tasks.
- Add automated failure alerts and stronger quality gates.
- Implement incremental loading.
- Expand customer-level analytics and dashboard filtering.

## Dataset

IBM Telco Customer Churn sample dataset, used for educational and portfolio purposes.
