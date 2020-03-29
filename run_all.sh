#!/bin/sh

python3 generate_raport.py -d ./out/kaggle/rose/ -o ./raports/kaggle_white_rose_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35
python3 generate_raport.py -d ./out/crawler/rose/ -o ./raports/crawler_white_rose_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35

python3 generate_raport.py -d ./out/kaggle/rose/ -o ./raports/kaggle_red_rose_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_raport.py -d ./out/crawler/rose/ -o ./raports/crawler_red_rose_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25

python3 generate_raport.py -d ./out/kaggle/daisy/ -o ./raports/kaggle_daisy_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85
python3 generate_raport.py -d ./out/crawler/daisy/ -o ./raports/crawler_daisy_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85


