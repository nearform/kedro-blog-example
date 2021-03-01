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
    data = data.drop(['UnitCost', 'Margin'], axis=1)
    return data


def transform_json(data: pd.DataFrame) -> pd.DataFrame:
    output_data = data.reset_index()
    output_data = output_data.drop(['index'], axis=1)
    return output_data