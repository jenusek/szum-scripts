import csv
import matplotlib.pyplot as plt
import os

# consts for analysis
ALL_DATA_ANALYSIS_INDEX = 18
IS_GRAYSCALE_INDEX = 3
COLOR_COVERAGE_INDEX = 4
RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2
REPORTS_PATHS = [
    './reports/kaggle_white_rose_220_35_230_25_220_35.csv',
    './reports/crawler_white_rose_220_35_230_25_220_35.csv',
    './reports/crawler_white_roza_220_35_230_25_220_35.csv',
    './reports/kaggle_red_rose_150_105_25_25_25_25.csv',
    './reports/crawler_red_rose_150_105_25_25_25_25.csv',
    './reports/crawler_red_roza_150_105_25_25_25_25.csv',
    './reports/kaggle_daisy_150_105_25_25_25_25.csv',
    './reports/crawler_daisy_150_105_25_25_25_25.csv',
    './reports/crawler_stokrotka_150_105_25_25_25_25.csv',
    './reports/kaggle_dandelion_150_105_170_85_25_25.csv',
    './reports/crawler_dandelion_150_105_170_85_25_25.csv',
    './reports/crawler_mniszek_lekarski_150_105_170_85_25_25.csv',
    './reports/kaggle_sunflower_150_105_170_50_25_25.csv',
    './reports/crawler_sunflower_150_105_170_50_25_25.csv',
    './reports/crawler_slonecznik_150_105_170_50_25_25.csv',
    './reports/kaggle_tulip_150_105_25_25_25_25.csv',
    './reports/crawler_tulip_150_105_25_25_25_25.csv',
    './reports/crawler_tulipan_150_105_25_25_25_25.csv'
]
ANALYSIS_PATHS = [
    './analysis/kaggle_white_rose.csv',
    './analysis/crawler_white_rose.csv',
    './analysis/crawler_white_roza.csv',
    './analysis/kaggle_red_rose.csv',
    './analysis/crawler_red_rose.csv',
    './analysis/crawler_red_roza.csv',
    './analysis/kaggle_daisy.csv',
    './analysis/crawler_daisy.csv',
    './analysis/crawler_stokrotka.csv',
    './analysis/kaggle_dandelion.csv',
    './analysis/crawler_dandelion.csv',
    './analysis/crawler_mniszek_lekarski.csv',
    './analysis/kaggle_sunflower.csv',
    './analysis/crawler_sunflower.csv',
    './analysis/crawler_slonecznik.csv',
    './analysis/kaggle_tulip.csv',
    './analysis/crawler_tulip.csv',
    './analysis/crawler_tulipan.csv',
]


class ReportAnalysis:
    data_path = ''
    file_path = ''
    plot_path = ''
    pictures_amount = 0
    black_white_amount = 0
    colorful_amount = 0
    color_coverage_sum = 0.0
    min_color_coverage = 100.0
    max_color_coverage = 0.0
    average_color_coverage = 0.0
    colors = [0, 0, 0]
    colors_tolerance = [0, 0, 0]

    def __init__(self, file_path, data_path=''):
        self.data_path = data_path
        self.file_path = file_path

        self.set_plot_path()
        if 'reports' in self.data_path:
            self.assign_tolerance()

    def increase_pictures_amount(self):
        self.pictures_amount += 1

    def increase_black_white_amount(self):
        self.black_white_amount += 1

    def increase_colorful_amount(self):
        self.colorful_amount += 1

    def add_to_color_coverage(self, color_coverage):
        self.color_coverage_sum += color_coverage

        if color_coverage > self.max_color_coverage:
            self.max_color_coverage = color_coverage
        elif color_coverage < self.min_color_coverage:
            self.min_color_coverage = color_coverage

    def calculate_average_color_coverage(self):
        self.average_color_coverage = self.color_coverage_sum / self.pictures_amount

    def set_plot_path(self):
        splitted_path = self.file_path.split('.')
        self.plot_path = '.' + splitted_path[1] + '_plot.png'

    def assign_tolerance(self):
        colors_part_index = 1
        splitted_data_path = self.data_path.split('.')[colors_part_index].split('_')
        values_amount = 6
        first_value_index = len(splitted_data_path) - values_amount
        self.colors[RED_INDEX] = int(splitted_data_path[first_value_index])
        self.colors_tolerance[RED_INDEX] = int(splitted_data_path[first_value_index + 1])
        self.colors[GREEN_INDEX] = int(splitted_data_path[first_value_index + 2])
        self.colors_tolerance[GREEN_INDEX] = int(splitted_data_path[first_value_index + 3])
        self.colors[BLUE_INDEX] = int(splitted_data_path[first_value_index + 4])
        self.colors_tolerance[BLUE_INDEX] = int(splitted_data_path[first_value_index + 5])

    def save_as_csv(self):
        if not os.path.exists('./analysis'):
            os.makedirs('./analysis')

        with open(self.file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([
                'pictures_amount',
                'black_white_pictures_amount',
                'colorful_pictures_amount',
                'min_color_coverage',
                'max_color_coverage',
                'average_color_coverage',
                'red',
                'red_tolerance',
                'green',
                'green_tolerance',
                'blue',
                'blue_tolerance'
            ])
            csv_writer.writerow([
                self.pictures_amount,
                self.black_white_amount,
                self.colorful_amount,
                self.min_color_coverage,
                self.max_color_coverage,
                self.average_color_coverage,
                self.colors[RED_INDEX],
                self.colors_tolerance[RED_INDEX],
                self.colors[GREEN_INDEX],
                self.colors_tolerance[GREEN_INDEX],
                self.colors[BLUE_INDEX],
                self.colors_tolerance[BLUE_INDEX]
            ])

    def save_plot(self):
        labels = ['min color coverage', 'max color coverage', 'average color coverage']
        values = [self.min_color_coverage, self.max_color_coverage, self.average_color_coverage]
        plt.figure(figsize=(9, 3))
        plt.bar(labels, values)
        plt.savefig(self.plot_path)

    def to_string(self):
        print('\n' + self.data_path +
              '\n' + self.file_path +
              '\npictures amount: ' + str(self.pictures_amount) +
              '\nbw amount: ' + str(self.black_white_amount) +
              '\ncolorful amount: ' + str(self.colorful_amount) +
              '\naverage coverage: ' + str(self.average_color_coverage) +
              '\nred: ' + str(self.colors[RED_INDEX]) +
              '\nred tolerance: ' + str(self.colors_tolerance[RED_INDEX]) +
              '\ngreen: ' + str(self.colors[GREEN_INDEX]) +
              '\ngreen tolerance: ' + str(self.colors_tolerance[GREEN_INDEX]) +
              '\nblue: ' + str(self.colors[BLUE_INDEX]) +
              '\nblue tolerance: ' + str(self.colors_tolerance[BLUE_INDEX]))


def analyse_report():
    analysis_index = 0
    analysis_of_all_data = ReportAnalysis('./analysis/all_data.csv', 'no_source')
    print('Analysis Started')
    for csv_file_path in REPORTS_PATHS:
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            analysis_of_current_csv = ReportAnalysis(ANALYSIS_PATHS[analysis_index], csv_file_path)
            next(csv_reader)
            for row in csv_reader:
                analysis_of_current_csv.increase_pictures_amount()
                analysis_of_all_data.increase_pictures_amount()
                if row[IS_GRAYSCALE_INDEX] == 'True':
                    analysis_of_current_csv.increase_black_white_amount()
                    analysis_of_all_data.increase_black_white_amount()
                else:
                    analysis_of_current_csv.increase_colorful_amount()
                    analysis_of_all_data.increase_colorful_amount()
                analysis_of_current_csv.add_to_color_coverage(float(row[COLOR_COVERAGE_INDEX]))
                analysis_of_all_data.add_to_color_coverage(float(row[COLOR_COVERAGE_INDEX]))
            analysis_of_current_csv.calculate_average_color_coverage()
            analysis_of_current_csv.save_as_csv()
            analysis_of_current_csv.save_plot()
            print('.')
        analysis_index += 1
    analysis_of_all_data.calculate_average_color_coverage()
    analysis_of_all_data.save_as_csv()
    analysis_of_all_data.save_plot()
    print('Analysis done!')


analyse_report()
