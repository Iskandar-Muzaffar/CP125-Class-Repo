import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)
    
    critical_mask = df['StockLevel'] <= df['ReorderThreshold']
    
    critical_df = df[critical_mask]
    
    result = {
        "total_products": len(df),
        "critical_count": len(critical_df),
        "critical_products": set(critical_df['ProductName'])
    }
    
    return result