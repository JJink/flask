from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/home', methods=['GET'])
def index() :
    #return "Hello World"
    return render_template("home.html", data = "HA")

@app.route('/about')
def about() :
    return render_template("about.html", hello = "gary kim")

@app.route('/articles')
def article() :
    return render_template("articles.html", hello = "gary kim")

if __name__ == "__main__" :
    app.run()
