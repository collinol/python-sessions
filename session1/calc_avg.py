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


def process_csv() -> None:
    """ main function that calculates average from input csv file and writes result to csv

    """

    # get start time
    start_time = datetime.datetime.now()

    # open csv file and do something with contents
    counts = []
    with open(args.input_csv, 'r') as csv_file:
        csv_file.readline()
        for line in csv_file:
            counts.append(int(line.split(',')[1].replace('\n','')))

    with open(args.output_csv, 'w') as output_file:
        output_file.write(f"calculation,result\n")
        output_file.write(f"average,{sum(counts)/len(counts)}")

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


def process_pandas() -> None:
    """ main function that calculates average from input csv file and write to output, using pandas"""
    # get start time
    start_time = datetime.datetime.now()

    # open csv file and do something with contents
    df = pd.read_csv(args.input_csv)
    average = df['read_count'].sum() / len(df)
    with open(args.output_csv, 'w') as output_file:
        output_file.write(f"calculation,result\n")
        output_file.write(f"average,{average}")

    curr_time = datetime.datetime.now()
    diff_time = curr_time - start_time
    hours = (diff_time.days * 24) + (diff_time.seconds // 3600)
    minutes = (diff_time.seconds // 60) % 60
    seconds = diff_time.microseconds / 1000000
    print(diff_time, average)
    print(
        'Run time for pandas: {} hours, {} minutes, {} seconds'.format(
            hours, minutes, seconds
        )
    )

def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-csv', default=None, required=True)
    parser.add_argument('--output-csv', default="default_output.csv", required=False)
    args = parser.parse_args()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-csv', default=None, required=True)
    parser.add_argument('--output-csv', default="default_output.csv", required=False)
    args = parser.parse_args()
    # with open(args.input_csv, 'w') as addto:
    #     for i in range(1000000):
    #         addto.write(f"{random.randrange(1000,2000)},{random.randrange(1000,8000)}\n")
    process_csv()
    process_pandas()


