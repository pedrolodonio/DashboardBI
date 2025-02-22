import pandas as pd

def load_data():
    contracts = pd.read_csv(r"C:\Users\User\Documents\cursos\python\DashboardBI\data\churn_contracts.csv")
    customers = pd.read_csv(r"C:\Users\User\Documents\cursos\python\DashboardBI\data\churn_customers.csv")
    services = pd.read_csv(r"C:\Users\User\Documents\cursos\python\DashboardBI\data\churn_services.csv")

    return contracts, customers, services
