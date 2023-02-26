# movies-api
This is a movies API. You can view data on all movies in the API or you can searched by movie type(rom-com and action are the only two categories currently added).

This API also has the functionality to add new movies to it!

###How to Use
This is a Django project so in order to view the API, you should do the following:
1. Make sure Django is installed on your computer
2. Run `pipenv install` to create the virtual environment and install dependencies
3. Run `pipenv shell` to enter the new virtual environment
4. Run `python manage.py migrate` to make migrations
5. Run `python manage.py runserver` and follow on the http link in the terminal or type in **localhost:8000/movies/** in the search bar of your preferred search engine.
