# How I run it?
*First 3 steps are optional, but thanks to them you can easly delete all requirements with project*  
*You can achive similar effect using conda, but i'm not expert in that technology*
1. Install virtualenv
```
On macOS and Linux:
python3 -m pip install --user virtualenv

On Windows:
py -m pip install --user virtualenv
``` 

2. Create virtual environment
```
On macOS and Linux:
python3 -m venv env

On Windows:
py -m venv env
```
3. Activate
```
On macOS and Linux:
source env/bin/activate

On Windows:
.\env\Scripts\activate
```

4. Install requirements
```
pip3 install -r requirements.txt
```
5. Download kaggle dataset from
```
https://www.kaggle.com/alxmamaev/flowers-recognition
```

6. Move files from **[download_path]/flowers** to **images/kaggle**
```
Should look like this:
.
+-- images
    +-- kaggle
        +-- daisy
        +-- dandelion
        +-- rose
        +-- sunflower
        +-- tulip
```

7. A. Run all scripts
```
On macOS and Linux:
./run_all

On Windows:
Someone with windows have to chceck, maybe the same
```

7. B. Or run python scripts separately
```
On macOS and Linux:
python3 google_graphics_crawler.py -q <query> -o <output-dir> -n <min-photos>

On Windows:
py google_graphics_crawler.py -q <query> -o <output-dir> -n <min-photos>
```

8. Decativate python environment
```
deactivate
```