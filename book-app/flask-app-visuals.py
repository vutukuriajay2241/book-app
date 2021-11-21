# Importing Required Libraries
import os
# Loading Google Big Query API Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="bigdatafinalproject-332802-3d5e0d6e4c0e.json"
from flask import Flask, render_template

from google.cloud import bigquery


app = Flask(__name__)
# Loading BigQuery client
client = bigquery.Client(project='bigdatafinalproject-332802')


# Getting data Tables from Big Query of Top 10 Authors
rows = client.list_rows(
    "Book_Crossing_Dataset.Top10AuthorsTable"
)
Top10Authors = rows.to_dataframe(
    create_bqstorage_client=True,
)

# Getting data Tables from Big Query of Top 10 Books which are most published
rows = client.list_rows(
    "Book_Crossing_Dataset.Top10BooksByMostPublishersTable"
)
Top10BooksByMostPublishers = rows.to_dataframe(
    create_bqstorage_client=True,
)

# Getting data Tables from Big Query of Top 10 Books with most ratings by users
rows = client.list_rows(
    "Book_Crossing_Dataset.Top10BooksByMostRatingTable"
)
Top10BooksByMostRating = rows.to_dataframe(
    create_bqstorage_client=True,
)

# Getting data Tables from Big Query of Top 10 Books by region in US
rows = client.list_rows(
    "Book_Crossing_Dataset.Top10BooksByRegionsInUSATable"
)
Top10BooksByRegionsInUSA = rows.to_dataframe(
    create_bqstorage_client=True,
)

# Getting data Tables from Big Query of Top 10 Countries with most books
rows = client.list_rows(
    "Book_Crossing_Dataset.Top10CountriesByMostBooksWithRatingsTable"
)
Top10CountriesByMostBooksWithRatings = rows.to_dataframe(
    create_bqstorage_client=True,
)

# Getting data Tables from Big Query of Top 15 Publishers
rows = client.list_rows(
    "Book_Crossing_Dataset.Top15PublishersTable"
)
Top15Publishers = rows.to_dataframe(
    create_bqstorage_client=True,
)

# Getting data Tables from Big Query of Top 25 Years with most books published
rows = client.list_rows(
    "Book_Crossing_Dataset.Top25YearsMostBooksPublishedTable"
)
Top25YearsMostBooksPublished = rows.to_dataframe(
    create_bqstorage_client=True,
)

# Creating bar chart for Top 10 Authors
fig = Top10Authors.plot.bar(x='BookAuthor',y='NumBooksPublishedByAuthor',color='blue')

# Creating bar chart for Top 10 Books by Most Publishers
fig = Top10BooksByMostPublishers.plot.bar(x='BookTitle',y='NumBooksPublishedByPublisher',color='blue')


# Creating bar chart for Top 10 Books by Most Rating
Top10BooksByMostRating['NumBooksPublishedByPublisher'] = Top10BooksByMostRating['NumBooksPublishedByPublisher'].astype(int)
fig = Top10BooksByMostRating.plot.bar(x='BookTitle',y='NumBooksPublishedByPublisher',color='blue')
fig.set_ylabel("NumBooksWithMostRating")

# Creating bar chart for Top 10 Books by Regions in USA
fig = Top10BooksByRegionsInUSA.plot.bar(x='State',y='MostBooks',color='blue')


# Creating bar chart for Top 10 Countries by Most Books with Ratings
fig = Top10CountriesByMostBooksWithRatings.plot.bar(x='Country',y='MostBooks',color='blue')

# Creating bar chart for Top 15 Publishers
fig = Top25YearsMostBooksPublished.plot.bar(x='YearOfPublication',y='NumBooksPublished',color='blue')

# Creating bar chart for Top 25 Years Most Books Published
fig = Top25YearsMostBooksPublished.plot.bar(x='YearOfPublication',y='NumBooksPublished',color='blue')

# Flask routing components

@app.route("/")
def hello_world():
    return render_template('index.html')


# Routing for Top 10 Authors
@app.route('/Top10Authors')
def top10Authors():
    return render_template('images.html', name = 'Top10Authors', url ='static/images/Top10Authors.png')

# Routing for Top 10 Books by Most Publishers
@app.route('/Top10BooksByMostPublishers')
def top10BooksByMostPublishers():
    
    return render_template('images.html', name = 'Top10BooksByMostPublishers', url ='static/images/Top10BooksByMostPublishers.png')


# Routing for Top 10 Books by Most Rating
@app.route('/Top10BooksByMostRating')
def top10BooksByMostRating():
    return render_template('images.html', name = 'Top10BooksByMostRating', url ='static/images/Top10BooksByMostRating.png')

# Routing for Top 10 Books by Regions in USA
@app.route('/Top10BooksByRegionsInUSA')
def top10BooksByRegionsInUSA():
    return render_template('images.html', name = 'Top10BooksByRegionsInUSA', url ='static/images/Top10BooksByRegionsInUSA.png')

# Routing for Top 15 Publishers
@app.route('/Top15Publishers')
def top15Publishers():
    fig = Top15Publishers.plot.bar(x='Publisher',y='NumBooksPublishedByPublisher',color='blue').get_figure()
    fig.savefig('images/Top15Publishers.png')
    return render_template('images.html', name = 'Top15Publishers', url ='static/images/Top15Publishers.png')

# Routing for Top 10 Countries by Most Books with Ratings
@app.route('/Top10CountriesByMostBooksWithRatings')
def top10CountriesByMostBooksWithRatings():
    return render_template('images.html', name = 'Top10CountriesByMostBooksWithRatings', url ='static/images/Top10CountriesByMostBooksWithRatings.png')

# Routing for Top 25 Years Most Books Published
@app.route('/Top25YearsMostBooksPublished')
def top25YearsMostBooksPublished():
    
    return render_template('images.html', name = 'Top25YearsMostBooksPublished', url ='static/images/Top25YearsMostBooksPublished.png')

