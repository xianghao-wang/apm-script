import csv

def calculate(courses):
    apm = 0.0
    leveled = [[], [], [], [], []]
    for name, mark in courses:
        weight = int(name[4])
        leveled[weight].append(mark)
    for level, marks in enumerate(leveled):
        for mark in marks:
            apm += 0.1 * level * mark / len(marks)

    return apm

filename = input("Please enter csv file path: ")

courses = []
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        courses.append((row['course'], int(row['mark'])))

print("Your APM mark is", calculate(courses))
