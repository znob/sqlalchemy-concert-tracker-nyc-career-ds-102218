
# Concert Tracker

We are going to build to help users keep track of all the concerts they have attended.  There will be many models, including both one-to-many and many-to-many relationships.  This will be challenging, but doable given all our practice in the previous sections.  Whenever necessary, refer back to the previous labs to review the syntax for creating one-to-many and many-to-many relationships.

## Objectives

1.  Review mapping objects to a database with the SQLAlchemy ORM
2.  Become comfortable writing different object relationships using SQLAlchemy
3.  Practice pulling data from a database using SQLAlchemy query objects


## Instructions

Our app will have eight models in total.  For this reason, we broke the `models.py` we are used to working with into smaller and easier to understand chunks.  Each of the eight models will have its own file.

#### Note:
Since we broke up the models into their own files, we have also split the declarative base into its own file, `base.py`.  We will need to import the `Base` at the top of each of our model files.

> ```python
from base import Base
```

Start by writing the classes for each of the eight models.  It probably makes more sense to begin with the more conventional models before building out the join tables.  The models, their columns, and their relationships are described below:

* **`User`**
    - id
    - name
    - has many Shows

* **`Band`**
    - id
    - name
    - has many Shows

* **`Show`**
    - id
    - date
    - belongs to a Band
    - belongs to a Venue
    - has many Songs
    - has many Users

* **`City`**
    - id
    - name
    - has many Venues

* **`Venue`**
    - id
    - name
    - capacity
    - belongs to a City
    - has many Shows

* **`Song`**
    - id
    - name
    - has many Shows

* **`UserShow`**
    - sets up the many-to-many between User and Show

* **`ShowSong`**
    - id
    - length (in seconds)
    - notes (recall the datatype for long text?)
    - sets up the many-to-many between Show and Song

### Queries

`count_user_ids`

Query the session and use the count aggregate function to return the total number of users.

`return_band_name_and_total_shows_histogram`

Write a query that will return an object containing a histogram for each band and their total number of shows played.

### Instance methods

We can also write customized instance methods for each class to pull useful information about each instance.  Write two instance methods for the `User` class.

`total_shows`

Write an instance method that returns a User's total shows attended.  When we write, `User.total_shows` we should see this number returned.


#### Challenge
`first_show`

Write an instance method that will return a User's first show in the following format:
> `'Band Name - MM/DD/YYYY - Venue Name, City Name'`

You will need to [sort each concert by its date](https://stackoverflow.com/questions/5055812/sort-python-list-of-objects-by-date) and [convert the date object into a more readable format](https://stackoverflow.com/questions/10624937/convert-datetime-object-to-a-string-of-date-only-in-python).
