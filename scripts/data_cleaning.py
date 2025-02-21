import pandas as pd

def clean_contracts(contracts):

    #verifica valores ausentes
    contracts.dropna(subset=['customerID'],inplace=True)

    #verifica e remove dados duplicados
    contracts.drop_duplicates(inplace=True)

    #Coverte coluna Total Charges para numérico
    contracts['TotalCharges'] = pd.to_numeric(contracts['TotalCharges'], errors='coerce')
    contracts['TotalCharges'].fillna(0,inplace = True)

    return contracts

def clean_customers(customers):
    customers.drops_duplicates(inplace = True)
    return customers

def clean_services(services):
    services.drops_duplicates(inplace = True)
    return services
