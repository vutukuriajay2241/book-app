#!/usr/bin/env python
# coding: utf-8

# In[165]:



import pandas as pd 
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="bigdatafinalproject-332802-3d5e0d6e4c0e.json"
from flask import Flask, render_template

# In[166]:





# In[167]:


app = Flask(__name__)



# # Imports

# In[168]:


from google.cloud import bigquery

client = bigquery.Client(project='bigdatafinalproject-332802')


# # Reading csv files

# In[112]:


#Users
u_cols = ['user_id', 'location', 'age']
users = pd.read_csv('./BX-CSV-Dump/BX-Users.csv', sep=';', names=u_cols, encoding='latin-1',low_memory=False, skiprows =1)

#Books
i_cols = ['isbn', 'book_title' ,'book_author','year_of_publication', 'publisher', 'img_s', 'img_m', 'img_l']
items = pd.read_csv('./BX-CSV-Dump/BX-Books.csv', sep=';', names=i_cols, encoding='latin-1',low_memory=False, skiprows =1)

#Ratings
r_cols = ['user_id', 'isbn', 'rating']
ratings = pd.read_csv('./BX-CSV-Dump/BX-Book-Ratings.csv', sep=';', names=r_cols, encoding='latin-1',low_memory=False, skiprows =1)


# In[114]:


users.columns = ['UserID', 'Location', 'Age']


# In[115]:


items.columns = ['ISBN', 'BookTitle', 'BookAuthor', 'YearOfPublication', 'Publisher',
       'ImgSURL', 'ImgMURL', 'ImgLURL']


# In[116]:


ratings.columns = ['UserID', 'ISBN', 'Rating']
ratings['UserID'] =ratings['UserID'].astype(str)
ratings['Rating'] =ratings['Rating'].astype(str)
ratings['ISBN'] =ratings['ISBN'].astype(str)


# In[45]:


from google.cloud import bigquery

client = bigquery.Client(project='bigdatafinalproject-332802')
table_id = 'Book_Crossing_Dataset.Users'


job = client.load_table_from_dataframe(
    users, table_id
)


# In[61]:


table_id2 = 'Book_Crossing_Dataset.Books'

job2 = client.load_table_from_dataframe(items, table_id2)


# In[111]:


table_id3 = 'Book_Crossing_Dataset.Ratings'

job2 = client.load_table_from_dataframe(ratings, table_id3)


# # What does the data look like?

# In[118]:


users.head(5)


# In[127]:





# In[129]:


rows = client.list_rows(
    "Book_Crossing_Dataset.Top10AuthorsTable"
)
Top10Authors = rows.to_dataframe(
    create_bqstorage_client=True,
)
Top10Authors


# In[138]:



rows = client.list_rows(
    "Book_Crossing_Dataset.Top10BooksByMostPublishersTable"
)
Top10BooksByMostPublishers = rows.to_dataframe(
    create_bqstorage_client=True,
)
Top10BooksByMostPublishers


# In[139]:



rows = client.list_rows(
    "Book_Crossing_Dataset.Top10BooksByMostRatingTable"
)
Top10BooksByMostRating = rows.to_dataframe(
    create_bqstorage_client=True,
)
Top10BooksByMostRating


# In[140]:


rows = client.list_rows(
    "Book_Crossing_Dataset.Top10BooksByRegionsInUSATable"
)
Top10BooksByRegionsInUSA = rows.to_dataframe(
    create_bqstorage_client=True,
)
Top10BooksByRegionsInUSA


# In[143]:


rows = client.list_rows(
    "Book_Crossing_Dataset.Top10CountriesByMostBooksWithRatingsTable"
)
Top10CountriesByMostBooksWithRatings = rows.to_dataframe(
    create_bqstorage_client=True,
)
Top10CountriesByMostBooksWithRatings


# In[142]:


rows = client.list_rows(
    "Book_Crossing_Dataset.Top15PublishersTable"
)
Top15Publishers = rows.to_dataframe(
    create_bqstorage_client=True,
)
Top15Publishers


# In[141]:


rows = client.list_rows(
    "Book_Crossing_Dataset.Top25YearsMostBooksPublishedTable"
)
Top25YearsMostBooksPublished = rows.to_dataframe(
    create_bqstorage_client=True,
)
Top25YearsMostBooksPublished


# In[ ]:


@app.route("/")
def hello_world():
    return render_template('index.html')


# In[ ]:


@app.route('/Top10Authors')
def top10Authors():
    return render_template('images.html', name = 'Top10Authors', url ='images/Top10Authors.png')


# In[153]:


@app.route('/Top10BooksByMostPublishers')
def top10Authors():
    
    return render_template('images.html', name = 'Top10BooksByMostPublishers', url ='images/Top10BooksByMostPublishers.png')


# In[152]:


@app.route('/Top10BooksByMostRating')
def top10Authors():
    return render_template('images.html', name = 'Top10BooksByMostRating', url ='images/Top10BooksByMostRating.png')


# In[ ]:


@app.route('/Top10BooksByRegionsInUSA')
def top10BooksByRegionsInUSA():
    
    return render_template('images.html', name = 'Top10BooksByRegionsInUSA', url ='images/Top10BooksByRegionsInUSA.png')


# In[ ]:


@app.route('/Top15Publishers')
def top15Publishers():
    fig = Top15Publishers.plot.bar(x='Publisher',y='NumBooksPublishedByPublisher',color='blue').get_figure()
    fig.savefig('images/Top15Publishers.png')
    return render_template('images.html', name = 'Top15Publishers', url ='images/Top15Publishers.png')


# In[ ]:


@app.route('/Top10CountriesByMostBooksWithRatings')
def top10CountriesByMostBooksWithRatings():
    return render_template('images.html', name = 'Top10CountriesByMostBooksWithRatings', url ='images/Top10CountriesByMostBooksWithRatings.png')


# In[ ]:


@app.route('/Top25YearsMostBooksPublished')
def top25YearsMostBooksPublished():
    
    return render_template('images.html', name = 'Top25YearsMostBooksPublished', url ='images/Top25YearsMostBooksPublished.png')


# In[179]:


Top15Publishers.plot.bar(x='Publisher',y='NumBooksPublishedByPublisher',color='blue').get_figure().savefig('Top15Publishers.png')


# In[178]:


fig.savefig('Top15Publishers.png')


# In[181]:



fig = Top10Authors.plot.bar(x='BookAuthor',y='NumBooksPublishedByAuthor',color='blue').get_figure()
fig.savefig('Top10Authors.png')


# In[183]:


fig = Top10BooksByMostPublishers.plot.bar(x='BookTitle',y='NumBooksPublishedByPublisher',color='blue').get_figure()
fig.savefig('Top10BooksByMostPublishers.png')


# In[184]:


Top10BooksByMostRating['NumBooksPublishedByPublisher'] = Top10BooksByMostRating['NumBooksPublishedByPublisher'].astype(int)
fig = Top10BooksByMostRating.plot.bar(x='BookTitle',y='NumBooksPublishedByPublisher',color='blue')
fig.set_ylabel("NumBooksWithMostRating")
fig.get_figure().savefig('Top10BooksByMostRating.png')


# In[185]:


fig = Top10BooksByRegionsInUSA.plot.bar(x='State',y='MostBooks',color='blue').get_figure()
fig.savefig('Top10BooksByRegionsInUSA.png')


# In[186]:


fig = Top10CountriesByMostBooksWithRatings.plot.bar(x='Country',y='MostBooks',color='blue').get_figure()
fig.savefig('Top10CountriesByMostBooksWithRatings.png')


# In[187]:


fig = Top25YearsMostBooksPublished.plot.bar(x='YearOfPublication',y='NumBooksPublished',color='blue').get_figure()
fig.savefig('Top25YearsMostBooksPublished.png')


# In[ ]:




