# omniparser/gradebook_parser.py

import os
import statistics

import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)  #use panda to read the csv
    #the pandas package gives us the ability to read df (dataFrame)
    


    #rows = df.to_dict("records")  #records is one of the accepted values for this package
#
    #grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
    #avg_grade = statistics.mean(grades)
#
    avg_grade = df["final_grade"].mean()

    return avg_grade #90.64 #"OOPS"


if __name__ == "__main__":   #this will only run script below if ran from command line
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")

    print(gradebook_filepath)

    avg = calculate_average_grade_from_csv(gradebook_filepath)

    print(avg)