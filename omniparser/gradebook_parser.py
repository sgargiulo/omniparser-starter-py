# omniparser/gradebook_parser.py

import os
import statistics
import json
import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)  #use panda to read the csv
    #the pandas package gives us the ability to read df (dataFrame)
    


    #rows = df.to_dict("records")  #records is one of the accepted values for this package
#
    #grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
    #avg_grade = statistics.mean(grades)
#
    #avg_grade = df["final_grade"].mean()

    #return avg_grade #90.64 #"OOPS"

def calculate_average_grade_from_json(x):
    

    with open(x, "r") as f:
        #print(type(f))
        file_contents = f.read()
        #print(type(file_contents))

    gradebook = json.loads(file_contents)
    #print(type(gradebook))
    #print(gradebook)
    students = gradebook["students"]
    grades = [s["finalGrade"] for s in students]
    avg_grade = statistics.mean(grades)
    
    return avg_grade

if __name__ == "__main__":   #this will only run script below if ran from command line
    #print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    #gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    #print(gradebook_filepath)
    #avg = calculate_average_grade_from_csv(gradebook_filepath)
    #print(avg)

    print("PARSING SOME JSON GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
    print(gradebook_filepath)
    print(os.path.isfile(gradebook_filepath))
    avg = calculate_average_grade_from_json(gradebook_filepath)
    print(avg)