# News Highlights:

## Built by; Augustine Ochieng


### Date of Release

15th April, 2019.

## Description

News Highlight is a python built application that displays a list of various news sources.On choosing the news source it displays the top news.One is also able to view news headlines.


## User Stories
These are the behaviours that the  application
implements for use by a user.

As a user i would like to:

* See various news sources
* Select one of thier choice
* See the details of the news
* Read all the details and news

## BDD

| Behaviour                           | Output                                                         |
|-------------------------------------|----------------------------------------------------------------|
| Display news source                 | List of variuos news source in a list                          |
| Display articles from a news source | Redirects to a page with article from source                   |
| Display tabs with news by category  | Onclick links opens based on categories                        |
| To read article                     | Redirects to the news source's site to read the entire article | -->

### SetUp / Installation Requirements

### Prerequisites

* `python3.6`
* `pip`
* `virtualenvironment`

## Cloning
* In your terminal:

       $ git clone:https://gustinews.herokuapp.com/

## Running the Application

* Creating the virtual environment

`$ python3.6 -m venv --without-pip virtual
$ source virtual/bin/env
$ curl https://boostrap.pypa.io/get-pip | python`

* Installing Flask and other required modules

`$ python3.6 -m pip install Flask
$ python3.6 -m pip install Flask-bootstrap
$ python3.6 -m pip install Flask-Script`

* Setting up the API KEY

`To be able to gather article info from the News API you need an API key.`

 * Visit https://newsapi.org/ and register for an API key.
 * In the root directory of the project folder create a file: start.sh
 * Insert the following info into it:

     export NEWS_API_KEY='<Your-Api-Key>'
     python3.6 manage.py server

 * Insert the API key you received from News Api where
    <Your-Api-Key>
 * To run the application, in your terminal:

     $ chmod +x start.sh
     $ ./start.sh


## Testing the Application

*  $ python3.6 manage.py tests

## Technologies Used
* Python3.6
* Flask

## Known Bugs
* Incase of any bug reachout to gusochieng@gmail.com

### License
*License is under MIT 2019*
Copyright (c) 2019 *AugustineOchieng*.