#!/bin/sh

set -x

python3 google_graphics_crawler.py -q rose -o images/crawler/rose -n 200
python3 google_graphics_crawler.py -q róża -o images/crawler/roza -n 200

python3 google_graphics_crawler.py -q daisy -o images/crawler/daisy -n 200
python3 google_graphics_crawler.py -q stokrotka -o images/crawler/stokrotka -n 200

python3 google_graphics_crawler.py -q dandelion -o images/crawler/dandelion -n 200
python3 google_graphics_crawler.py -q "mniszek lekarski" -o images/crawler/mniszek_lekarski -n 200

python3 google_graphics_crawler.py -q sunflower -o images/crawler/sunflower -n 200
python3 google_graphics_crawler.py -q słonecznik -o images/crawler/slonecznik -n 200

python3 google_graphics_crawler.py -q tulip -o images/crawler/tulip -n 200
python3 google_graphics_crawler.py -q tulipan -o images/crawler/tulipan -n 200

python3 generate_report.py -d ./images/kaggle/rose/ -o ./reports/kaggle_white_rose_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35
python3 generate_report.py -d ./images/crawler/rose/ -o ./reports/crawler_white_rose_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35
python3 generate_report.py -d ./images/crawler/roza/ -o ./reports/crawler_white_roza_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35

python3 generate_report.py -d ./images/kaggle/rose/ -o ./reports/kaggle_red_rose_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/rose/ -o ./reports/crawler_red_rose_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/roza/ -o ./reports/crawler_red_roza_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25

python3 generate_report.py -d ./images/kaggle/daisy/ -o ./reports/kaggle_daisy_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85
python3 generate_report.py -d ./images/crawler/daisy/ -o ./reports/crawler_daisy_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85
python3 generate_report.py -d ./images/crawler/stokrotka/ -o ./reports/crawler_stokrotka_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85

python3 generate_report.py -d ./images/kaggle/dandelion/ -o ./reports/kaggle_dandelion_150_105_170_85_25_25.csv -r 150 -rt 105 -g 170 -gt 85 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/dandelion/ -o ./reports/crawler_dandelion_150_105_170_85_25_25.csv -r 150 -rt 105 -g 170 -gt 85 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/mniszek_lekarski/ -o ./reports/crawler_mniszek_lekarski_150_105_170_85_25_25.csv -r 150 -rt 105 -g 170 -gt 85 -b 25 -bt 25

python3 generate_report.py -d ./images/kaggle/sunflower/ -o ./reports/kaggle_sunflower_150_105_170_50_25_25.csv -r 150 -rt 105 -g 170 -gt 50 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/sunflower/ -o ./reports/crawler_sunflower_150_105_170_50_25_25.csv -r 150 -rt 105 -g 170 -gt 50 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/slonecznik/ -o ./reports/crawler_slonecznik_150_105_170_50_25_25.csv -r 150 -rt 105 -g 170 -gt 50 -b 25 -bt 25

# Used random color
python3 generate_report.py -d ./images/kaggle/tulip/ -o ./reports/kaggle_tulip_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/tulip/ -o ./reports/crawler_tulip_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_report.py -d ./images/crawler/tulipan/ -o ./reports/crawler_tulipan_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25

python3 analyse_reports.py
