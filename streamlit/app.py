import streamlit as st
from snowflake.snowpark.context import get_active_session

st.set_page_config(
    page_title="Customer Churn Analytics",
    layout="wide"
)

st.title("Customer Churn Analytics Dashboard")
st.caption("Snowflake | SQL | Python | Streamlit")

session = get_active_session()

# Load data from our analytics table
query = """
SELECT
    CONTRACT_TYPE,
    TOTAL_CUSTOMERS,
    CHURNED_CUSTOMERS,
    CHURN_RATE_PERCENTAGE
FROM CUSTOMER_CHURN_DB.ANALYTICS.CHURN_BY_CONTRACT
ORDER BY CHURN_RATE_PERCENTAGE DESC
"""

df = session.sql(query).to_pandas()

# Calculate overall metrics
total_customers = int(df["TOTAL_CUSTOMERS"].sum())
churned_customers = int(df["CHURNED_CUSTOMERS"].sum())

churn_rate = (
    churned_customers / total_customers * 100
    if total_customers > 0 else 0
)

# Dashboard KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", total_customers)
col2.metric("Churned Customers", churned_customers)
col3.metric("Churn Rate", f"{churn_rate:.1f}%")

st.divider()

st.subheader("Churn Rate by Contract Type")

chart_data = df.set_index("CONTRACT_TYPE")[
    "CHURN_RATE_PERCENTAGE"
]

st.bar_chart(chart_data)

st.subheader("Customer Churn Details")
st.dataframe(df, use_container_width=True)

st.info(
    "Sample data only. Month-to-month customers "
    "show the highest churn rate in this dataset."
)
