from flask import Flask, request, Response
import json 

app = Flask(__name__)

#KEY : VALUE

books_db = {
    "1": {"name": "Stargate", "release_date": "1994" },
    "2": {"name": "Sunshine", "release_date": "2007" },
    "3": {"name": "The Holidays", "release_date": "2006" }
}

@app.route("/") #This tells the application to create a endpoint(route)
def hi(): 
    return "Hello World"

@app.route("/books") 
def list_books():
    return books_db


if __name__ == "__main__": 
    app.run(host="127.0.0.1") #ip address of my machine



