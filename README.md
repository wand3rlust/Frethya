# Frethya (Hide)
The name (`Frethya`) is an homage to Christopher Paolini's Inheritance Cycle.

## Intro
Frethya is a python script which performs image stegnography by hiding data in an EXIF tag.
This script is useful for passing messages hidden under the hood (EXIF data).
It encodes the user input in `Base64` and hides it in `UserComment` EXIF tag.


[NOTE:`Base64` is an encoding and not encryption method, hence these messages can be decoded easily.

## Usage

Step 1: Download this repo and `cd` into it.

Step 2: Run `pip install -r requirements.txt`

Step 3: Finally run `python3 frethya.py`



## Contributing

To contribute simply fork this repo, make changes and create a pull request.

## Support

If you like this tool please consider giving a :star:.
