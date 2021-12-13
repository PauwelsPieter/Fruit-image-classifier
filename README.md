# Big-Data Scraper

## (required) Installing packages
From the root folder, run `python3 -m pip install -r requirements.txt`

## Running the app
From the `app/` folder, run `python3 main.py`

Required:
- Create a directory named `uploads` in the map `./app`
- Create a directory named `uploads` in the map `./app/static`

## Retraining the model
Run the notebook found in the `model/` folder

## Rescrape the images
- Specify the categories to scrape in `scraper/main.py`
- From the `scraper/` folder, run `python3 main.py` 

Required:
- Create a directory named `out` in the `root` of the project
