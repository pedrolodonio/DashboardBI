import pandas as pd

def load_data():
    contracts = pd.read_csv(r"PATH_ARQUIVO_CSV")
    customers = pd.read_csv(r"PATH_ARQUIVO_CSV")
    services = pd.read_csv(r"PATH_ARQUIVO_CSV")

    return contracts, customers, services
