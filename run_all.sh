#!/bin/sh

set -x

python3 google_graphics_clawler.py -q rose -o images/clawler/rose -n 200
python3 google_graphics_clawler.py -q róża -o images/clawler/roza -n 200

python3 google_graphics_clawler.py -q daisy -o images/clawler/daisy -n 200
python3 google_graphics_clawler.py -q stokrotka -o images/clawler/stokrotka -n 200

python3 google_graphics_clawler.py -q dandelion -o images/clawler/dandelion -n 200
python3 google_graphics_clawler.py -q "mniszek lekarski" -o images/clawler/mniszek_lekarski -n 200

python3 google_graphics_clawler.py -q sunflower -o images/clawler/sunflower -n 200
python3 google_graphics_clawler.py -q słonecznik -o images/clawler/slonecznik -n 200

python3 google_graphics_clawler.py -q tulip -o images/clawler/tulip -n 200
python3 google_graphics_clawler.py -q tulipan -o images/clawler/tulipan -n 200

python3 generate_raport.py -d ./images/kaggle/rose/ -o ./raports/kaggle_white_rose_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35
python3 generate_raport.py -d ./images/clawler/rose/ -o ./raports/clawler_white_rose_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35
python3 generate_raport.py -d ./images/clawler/roza/ -o ./raports/clawler_white_roza_220_35_230_25_220_35.csv -r 220 -rt 35 -g 230 -gt 25  -b 220 -bt 35

python3 generate_raport.py -d ./images/kaggle/rose/ -o ./raports/kaggle_red_rose_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/rose/ -o ./raports/clawler_red_rose_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/roza/ -o ./raports/clawler_red_roza_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25

python3 generate_raport.py -d ./images/kaggle/daisy/ -o ./raports/kaggle_daisy_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85
python3 generate_raport.py -d ./images/clawler/daisy/ -o ./raports/clawler_daisy_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85
python3 generate_raport.py -d ./images/clawler/stokrotka/ -o ./raports/clawler_stokrotka_150_105_25_25_25_25.csv -r 170 -rt 85 -g 170 -gt 85 -b 170 -bt 85

python3 generate_raport.py -d ./images/kaggle/dandelion/ -o ./raports/kaggle_dandelion_150_105_170_85_25_25.csv -r 150 -rt 105 -g 170 -gt 85 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/dandelion/ -o ./raports/clawler_dandelion_150_105_170_85_25_25.csv -r 150 -rt 105 -g 170 -gt 85 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/mniszek_lekarski/ -o ./raports/clawler_mniszek_lekarski_150_105_170_85_25_25.csv -r 150 -rt 105 -g 170 -gt 85 -b 25 -bt 25

python3 generate_raport.py -d ./images/kaggle/sunflower/ -o ./raports/kaggle_sunflower_150_105_170_50_25_25.csv -r 150 -rt 105 -g 170 -gt 50 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/sunflower/ -o ./raports/clawler_sunflower_150_105_170_50_25_25.csv -r 150 -rt 105 -g 170 -gt 50 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/slonecznik/ -o ./raports/clawler_slonecznik_150_105_170_50_25_25.csv -r 150 -rt 105 -g 170 -gt 50 -b 25 -bt 25

# Used random color
python3 generate_raport.py -d ./images/kaggle/tulip/ -o ./raports/kaggle_tulip_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/tulip/ -o ./raports/clawler_tulip_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25
python3 generate_raport.py -d ./images/clawler/tulipan/ -o ./raports/clawler_tulip_150_105_25_25_25_25.csv -r 150 -rt 105 -g 25 -gt 25 -b 25 -bt 25

