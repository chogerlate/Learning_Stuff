import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    v_id = sorted(views[ (views['author_id'] == views['viewer_id']) ]['viewer_id'].unique())
    v_id = pd.DataFrame({
        "id": v_id
    })
    return v_id
