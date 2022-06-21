from flask import Flask, render_template, url_for
import folium
from folium.plugins import MarkerCluster
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import pymongo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class AutoM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    data_craated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

"""" Trying to create a map centered to Pula - Folium

# Define coordinates of where we want to center our map
pula = [44.86833, 13.84806]

# Create the map
my_map = folium.Map(location=pula, zoom_start=13)

# Display the map
my_map

"""

client = pymongo.MongoClient(
    "mongodb+srv://maliZeus:<password>@backenddatabase.cxfv0qt.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
