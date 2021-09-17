"""Python file with multiple types of functions to be tested """
import os
from typing import Dict, List

from google.cloud import bigquery
from pandas import DataFrame


def function_doubles(x: int) -> int:
    return x*2


class TestableClass:
    def __init__(self):
        self.some_attribute = 20
        self.client = bigquery.Client('project-id')

    def double_attribute(self) -> int:
        return self.some_attribute*2

    def use_client_to_create_dataset(self, x: int) -> None:
        x -= 1
        self.client.create_dataset("projectid", f"dataset_{x}")

    def use_client_values(self):
        bigquery_response = self.client.query('some query')
        return bigquery_response + ["some more data"]

    @staticmethod
    def convert_dict_to_DF(payload: Dict[str, List[int]]) -> DataFrame:
        payload[os.environ.get("BIG_VAR", "default")] = [5,5,5]
        return DataFrame(payload)


aclass = TestableClass()
print(aclass.double_attribute())
