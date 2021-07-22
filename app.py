from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/booklist')
def homepage():
    #books=db.execute("SELECT * FROM booklist order by bookid")
    books='books'
    return render_template("BookList.html", books=books)




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)