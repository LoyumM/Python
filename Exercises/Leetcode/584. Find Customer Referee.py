import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer["referee_id"] = customer["referee_id"].fillna(0)
    result = customer[customer['referee_id'] != 2]
    return pd.DataFrame(result['name'])