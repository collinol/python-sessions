"""
Script that takes cli args for a csv file to parse
calculates averages
writes to new csv

also does same ^ in pandas

resources
https://docs.python.org/3/library/argparse.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
https://docs.python.org/3/library/csv.html
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
https://stackoverflow.com/questions/24807434/imports-in-init-py-and-import-as-statement
"""
from typing import Dict, List, Tuple


def process_csv(
    xyz: str,
    dictionary_arg: Dict[str, int]
) -> Tuple[str, str, str]:
    """ short one line description here

    Args:
        xyz: some value about a thing
        dictionary_arg: some mapping

    Returns:
        calculation results
    """
    # csv_file = open('values.csv', 'r')
    read_counts = []
    with open('values.csv', 'r') as csv_file:
        headers = csv_file.readline()
        for line in csv_file.readlines():
            read_counts.append(int(line.split(',')[1]))

    avg = sum(read_counts)/len(read_counts)

    print("average count", sum(read_counts)/len(read_counts))
    print("Format String ", f"this was avg = {avg}")

    with open("avg_output.csv", 'w') as output_file:
        output_file.write("calculation_type,result\n")
        output_file.write(f"average,{avg}")


if __name__ == '__main__':
    process_csv(12, 12)