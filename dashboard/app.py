#imports
import sys
import os
import streamlit as st
from scripts.data_loading import load_data
from scripts.data_cleaning import clean_contracts, clean_customers,clean_services
from scripts.kpi_calculations import calculate_kpi

#adicionando diretórios do projeto
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir,".."))
if project_root not in sys.path:
    sys.path.insert(0,project_root)

#Limpeza e Carregamento de Dados

contracts,customers,services = load_data()
contracts = clean_contracts(contracts)
customers = clean_customers(customers)
services = clean_services (services)

#calculando kpis
kpis = calculate_kpi(contracts,customers,services)

#streamlit app
st.title("Telecom Churn Analysis Dashboard")

#Kpis
st.write("### Key performance indicators")
col1,col2,col3 = st.columns(3)
col1.metric("Total Customers",kpis["Total Customers"])
col2.metric("Churn Rate",f"{kpis['Churn Rate']:.2%}")
col3.metric("Total Revenue",f"{kpis['Total Revenue']:.2f}")

#Divider
st.markdown ("---")

#gráfico distribuição de contrato
st.write("### Distribuição de contatos")
if not kpis ["Contract Distribution"].empty:
    st.bar_chart(kpis["Contract Distribution"])
else:
    st.write("Dados indisponíveis")
