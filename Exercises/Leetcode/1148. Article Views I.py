import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']]
    result = sorted(views['author_id'].unique())
    return pd.DataFrame({'id':result})