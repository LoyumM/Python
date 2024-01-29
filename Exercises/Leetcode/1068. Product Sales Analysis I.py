import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(sales, product, on = 'product_id', how = 'left')[['product_name','year','price']]
    return pd.DataFrame(res)