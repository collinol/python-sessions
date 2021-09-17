import os
from unittest import TestCase, mock

from pandas import DataFrame
from pandas._testing import assert_frame_equal

from program_with_functions import function_doubles, TestableClass


def test_function_double():
    assert function_doubles(3) == 6


class TestClass(TestCase):
    def setUp(self) -> None:
        self.test_class = TestableClass()
        self.test_class.some_attribute = 1

    def test_doubler(self):
        self.assertEqual(self.test_class.double_attribute(), 40)

    def test_bigquery_client(self):
        with mock.patch.object(self.test_class, "client") as mock_client:
            self.test_class.use_client_to_create_dataset(5)
            mock_client.create_dataset.assert_called_once_with("projectid", "dataset_4")

    @mock.patch.dict(
        os.environ,
        {
            "BIG_VAR": "something_secret"
        }
    )
    def test_pandas_converter(self):
        payload = {"first": [1, 2, 3], "second": [3, 2, 1]}
        response = self.test_class.convert_dict_to_DF(payload)
        expected = DataFrame({"first": [1, 2, 3], "second": [3, 2, 1], "something_secret": [5, 5, 5]})
        assert_frame_equal(response, expected)

    def test_pandas_converter_2(self):
        payload = {"first": [1, 2, 3], "second": [3, 2, 1]}
        response = self.test_class.convert_dict_to_DF(payload)
        expected = DataFrame({"first": [1, 2, 3], "second": [3, 2, 1], "something_secret": [5, 5, 5]})
        assert_frame_equal(response, expected)

    def test_bigquery_response_handling(self):
        with mock.patch.object(self.test_class, "client") as mock_client:
            mock_client.query.return_value = ['initial response']
            data_handled_response = self.test_class.use_client_values()
            self.assertEqual(data_handled_response, ['initial response', "some more data"])