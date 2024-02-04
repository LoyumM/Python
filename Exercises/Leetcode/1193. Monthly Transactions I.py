import pandas as pd
import numpy as np

data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})


def monthly_transactions(transactions: pd.DataFrame):
    transactions['month'] = transactions['trans_date'].dt.strftime("%Y-%m")
    transactions['country'].fillna('null',inplace=True)
    transactions['approved'] = np.where(
        transactions['state'] == 'approved',transactions['amount'],nan
    )
    transactions = transactions.groupby(['month','country'],as_index=False).agg(
        trans_count=('amount','count'),
        approved_count=('approved','count'),
        trans_total_amount=('amount','sum'),
        approved_total_amount=('approved','sum')
    )
    transactions['country'].replace('null',nan,inplace=True)
    return transactions