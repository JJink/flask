from flask import Flask, render_template
from data import Articles

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index() :
    #return "Hello World"
    return render_template("home.html")

@app.route('/about')
def about() :
    return render_template("about.html")

@app.route('/artcles')
def articles():
    articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles = articles)

if __name__ == "__main__" :
    app.run()
