About the Project

Pull the latest version of the project from [GitHub](https://github.com/vutukuriajay2241/book-app.git).

There are many Book recomendation applications. However, this is project is a unique one. Where I was creating a end-to-end application for a book recommendation system. This project is a web application that uses a RESTful API to retrieve data from a database. The application is built using [Flask](https://flask.palletsprojects.com/en/1.1.x/), [BIGQuery](https://bigquery.cloud.google.com/), [JETSTREAM](https://use.jetstream-cloud.org/application/projects) and [Docker](https://www.docker.com/).

Getting Started

Prerequisites

    * Python 3.6 or above
    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * [BIGQuery](https://bigquery.cloud.google.com/), A service account needs to be created for the project.
    * [JETSTREAM](https://use.jetstream-cloud.org/application/projects) 
    * [Docker](https://www.docker.com/)

The files are stored in the following directory structure:

Book-app
├── Dockerfile # Dockerfile for the project
├── requirements.txt # Python requirements
├── BX-CSV-Dump # Contains the data (Note: This is a large file not included in the repository)
    ├── BX-Books.csv # Contains the books
    ├── BX-Users.csv # Contains the users
    ├── BX-Book-Ratings.csv # Contains the ratings
├── static # Static files
│   └── images # Images
├── bigdatafinalproject-332802-3d5e0d6e4c0e.json # Service account credentials (I will not be sharing this file)) 
├── templates # Templates
│   │── index.htmi # Index page
│   └── images.html # Image page which is used to display the images from index page
├── Readme.md # Brief description of the project
│── flask-app-visuals.py # Web application that uses Flask to display the images in web browser
└── sendingDataIntoBigQuery.py # Script that sends CSV data into BigQuery

Data Source

    * [Book - Crossing Data set](https://www.kaggle.com/ruchi798/bookcrossing-dataset)
    * The data set contains three csv files:
        * ratings.csv
            * Contains the following columns:
                * User ID # User ID of the user who rated the book
                * ISBN # ISBN id of the book
                * Rating # Rating of the book
        * books.csv
            * Contains the following columns:
                * ISBN # ISBN id of the book
                * BookTitle # Title of the book
                * BookAuthor # Author of the book
                * BookPublisher # Publisher of the book
                * YearOfPublication # Year of publication
                * Image small #  Small Image of the book
                * Image large # Large Image of the book
                * Image medium # Medium Image of the book
        * users.csv
            * Contains the following columns:
                * User ID # User ID of the user
                * Location # Location of the user
                * Age # Age of the user
    
