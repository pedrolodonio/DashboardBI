import sys
import os
import streamlit as st
import plotly as px

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))

if project_root not in sys.path:
    sys.path.append(project_root)

print(f"Project Root: {project_root}")  # Debug para ver o caminho

from scripts.data_loading import load_data
from scripts.data_cleaning import clean_contracts, clean_customers, clean_services
from scripts.kpi_calculations import calculate_kpi

# Limpeza e Carregamento de Dados
contracts, customers, services = load_data()
contracts = clean_contracts(contracts)
customers = clean_customers(customers)
services = clean_services(services)

# Calculando KPIs
kpis = calculate_kpi(contracts, customers, services)

# Streamlit app
st.title("Telecom Churn Analysis Dashboard")

# KPIs
st.write("### Key performance indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", kpis["Total Customers"])
col2.metric("Churn Rate", f"{kpis['Churn Rate']:.2%}")
col3.metric("Total Revenue", f"{kpis['Total Revenue']:.2f}")

# Divider
st.markdown("---")

# Gráfico distribuição de contrato
st.write("### Distribuição de contratos")
if not kpis["Contract Distribution"].empty:
    st.bar_chart(kpis["Contract Distribution"])
else:
    st.write("Dados indisponíveis")