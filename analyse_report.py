import csv

IS_GRAYSCALE = 3
COLOR_COVERAGE = 4


def analyse_report(csv_file_path):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        next(csv_reader)
        for row in csv_reader:
            print("- is grayscale: " + row[IS_GRAYSCALE])
            print(" color coverage: " + row[COLOR_COVERAGE])


analyse_report('/home/michal/PycharmProjects/szum-scripts/reports/crawler_red_rose_150_105_25_25_25_25.csv')
