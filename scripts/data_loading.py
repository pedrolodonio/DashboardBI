import pandas as pd

def load_data():
    contracts = pd.read_csv("data\churn_contracts.csv")
    costumers = pd.read_csv("data\churn_customers.csv")
    services = pd.read_csv("data\churn_services.csv")

    return contracts,costumers,services