import os
import unittest

from session1.calculate_avg import process_csv

process_csv()


class TestAvgCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.input_file = "values.csv"

    def test_csv_calculation(self):
        expected_result = ['calculation,result\n', 'average,4498.3872343872345']
        os.system(f"python calc_avg.py --input-csv {self.input_file} --output-csv values_output.csv")
        self.assertEqual(
            expected_result,
            open('values_output.csv', 'r').readlines()
        )


