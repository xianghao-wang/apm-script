import csv

def calculate(courses):
    apm = 0.0
    for name, mark in courses:
        weight = int(name[4])
        apm += 0.1 * weight * mark
    return apm

filename = input("Please enter csv file path: ")

courses = []
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        courses.append((row['course'], int(row['mark'])))

print("Your APM mark is", calculate(courses))
