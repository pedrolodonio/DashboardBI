def calculate_kpi(contracts,costumers,services):
    
    #total de clientes
    total_customers = contracts['customerID'].nunique()

    #taxa de churns
    churn_rate = contracts['Churn'].value_counts(normalize = True).get('Yes',0)

    #Receita Mensal Total
    total_revenue = contracts['MonthlyCharges'].sum()

    #tipo de contrato
    contract_distribution =contracts['Contract'].value_counts()

    kpis ={
        "Total Customers":total_customers,
        "Churn Rate":churn_rate,
        "Total Revenue":total_revenue,
        "Contract Distribution":contract_distribution,
    }

    return kpis

