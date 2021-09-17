"""
Script that takes cli args for a csv file to parse
calculates averages
writes to new csv

also does same ^ in pandas

resources
https://docs.python.org/3/library/argparse.html


"""
import argparse
import datetime
import pandas as pd


def process_csv(csv_file) -> None:
    """ main function that calculates average from input csv file and writes result to csv

    """

    # get start time
    start_time = datetime.datetime.now()

    # open csv file and do something with contents
    counts = []
    with open(csv_file, 'r') as csv_file:
        csv_file.readline()
        for line in csv_file:
            counts.append(int(line.split(',')[1].replace('\n','')))

    curr_time = datetime.datetime.now()
    diff_time = curr_time - start_time
    hours = (diff_time.days * 24) + (diff_time.seconds // 3600)
    minutes = (diff_time.seconds // 60) % 60
    seconds = diff_time.microseconds / 1000000
    print(diff_time, sum(counts)/len(counts))
    print(
        'Run time for csv: {} hours, {} minutes, {} seconds'.format(
            hours, minutes, seconds
        )
    )


def process_pandas(csv_file: str, output: str) -> None:
    """ main function that calculates average from input csv file and write to output, using pandas"""
    # open csv file and do something with contents
    start_time = datetime.datetime.now()
    df = pd.read_csv(csv_file)
    average = df['read_count'].sum() / len(df)

    curr_time = datetime.datetime.now()

    diff_time = curr_time - start_time
    hours = (diff_time.days * 24) + (diff_time.seconds // 3600)
    minutes = (diff_time.seconds // 60) % 60
    seconds = diff_time.microseconds / 1000000
    print(diff_time, average)
    print(
        'Run time for csv: {} hours, {} minutes, {} seconds'.format(
            hours, minutes, seconds
        )
    )


if __name__ == '__main__':
    process_csv('values.csv')
    process_pandas("values.csv", 'output2.csv')

