## Flask_SQL_query_API_and_web_app

This is a simple app using [Flask](http://flask.pocoo.org), [SQLAlchemy](http://www.sqlalchemy.org/) and the connecting [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) library.

Once deployed, you could use url such as http://localhost:5000/api?id={$id} to implement an HTTP REST API and do SQL queries. 
Besides, you could also do SQL query using HTML page. 

### Installing Dependencies

```
pip install -r requirements.txt
```

### Running the App

To run the app, first run the `models.py` file directly to create the database tables:

```
$ python models.py
```

You only need to do this once, unless you change your model definitions (see below).

Then run the app itself:

```
$ python app.py
```

Visit [http://localhost:5000/](http://localhost:5000/) and http://127.0.0.1:5000/api?identifier=foo in your browser to see the results.
