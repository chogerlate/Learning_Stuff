import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders, how="left", left_on = "id", right_on = "customerId")
    merged_df = merged_df.fillna(0)
    merged_df = merged_df[merged_df["id_y"] ==0][["name"]]
    merged_df.columns = ['Customers']
    return merged_df