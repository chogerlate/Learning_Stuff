import pandas as pd


# good memory management beating 94% but low speed beating 47% of people
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'),:]
    return products[["product_id"]]
    