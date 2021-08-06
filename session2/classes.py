"""
Goals:
    how to create a class (when you need init)
    usage of self
    subclassing/inheritance
    static methods


"""
import datetime
import pandas as pd

class Squarer:

    def __init__(self):
        self.squared_x = None

    def get_square(self, x: int) -> None:
        """Squares a number

        Args:
            x: integer to square

        Returns:
            value of x squared
        """
        self.squared_x = x**2

class ProcessCsv:

    def process_pandas(self, input_csv, output_csv) -> None:
        """ main function that calculates average from input csv file and write to output, using pandas"""
        # get start time
        start_time = datetime.datetime.now()

        # open csv file and do something with contents
        df = pd.read_csv(input_csv)
        average = df['read_count'].sum() / len(df)
        with open(output_csv, 'w') as output_file:
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


demo = ProcessCsv()
demo.process_pandas('values.csv')

print(demo.squared_x)
