import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df1=employee.groupby('managerId')['id'].count().reset_index()
    df=pd.merge(employee,df1,left_on='id',right_on='managerId')
    df=df[df['id_y']>=5]
    return df[['name']]