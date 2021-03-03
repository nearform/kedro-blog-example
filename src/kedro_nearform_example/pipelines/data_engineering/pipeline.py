from kedro.pipeline import Pipeline, node

from .nodes import remove_missing_label, remove_no_units, capitalize_product_names, calculate_pricing, transform_json

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                remove_missing_label,
                "example_spreadsheet",
                "remove_missing_label",
            ),
            node(
                remove_no_units,
                "remove_missing_label",
                "remove_no_units",
            ),
            node(
                capitalize_product_names,
                "remove_no_units",
                "capitalize_product_names",
            ),
            node(
                calculate_pricing,
                "capitalize_product_names",
                "calculate_pricing",
            ),
            node(
                transform_json,
                "calculate_pricing",
                "product_data",
            ),
        ]
    )
