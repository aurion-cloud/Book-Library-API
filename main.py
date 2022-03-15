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

@app.route("/book/<books_id>")
def get_book(books_id):
    return books_db[books_id]

@app.route("/book/add", methods=['POST'])
def add_book():
    #Collect the new book from the user/url
    req_data = request.get_json()
    
    # Extract the book data from the request
    new_book = req_data['book']

    # Get the last position in the database
    new_id = len(books_db) + 1

    # Create a new entry for my book 
    new_book_data = { str(new_id) : new_book }

    #Update the new database with the new entry 
    books_db.update(new_book_data)

    return "The book was added successfully"

@app.route("/book/<books_id>", methods=["PUT"])
def update_book(books_id):
    # Update or create the new book 
    req_date = request.get_json()


    if books_id in book:
        book[books_id] = req
        res = make_response(jsonify({"message": "Book replaced"}), 200)
        return res

        book[books_id] = req
        res = make_response(jsonify({"message": "Book created"}), 201)
        return res

if __name__ == "__main__": 
    app.run(host="127.0.0.1") #ip address of my machine



