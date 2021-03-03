from typing import Any, Dict

import pandas as pd


def remove_missing_label(data: pd.DataFrame) -> pd.DataFrame:
    data.dropna(subset=['Product'], inplace=True)
    return data


def remove_no_units(data: pd.DataFrame) -> pd.DataFrame:
    return data[data['Units'] > 0]


def capitalize_product_names(data: pd.DataFrame) -> pd.DataFrame:
    data['Product'] = data.Product.apply(lambda x: x.capitalize())
    return data


def calculate_pricing(data: pd.DataFrame) -> pd.DataFrame:
    data['Price'] = data.UnitCost + data.UnitCost * data.Margin
    return data.drop(['UnitCost', 'Margin'], axis=1)


def transform_json(data: pd.DataFrame) -> pd.DataFrame:
    return data.reset_index().drop(['index'], axis=1)
