from flask import Flask , render_template, request, redirect
from data import Articles
from passlib.hash import sha256_crypt
import pymysql

app = Flask(__name__)

app.debug = True

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='1234',
    db='busan'
)

@app.route('/', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("index.html", data="KIM")

@app.route('/about')
def about():
  return render_template("about.html", hello = "Gary Kim")

@app.route('/articles')
def articles():
  cursor = db.cursor()
  sql = 'SELECT * FROM topic;'
  cursor.execute(sql)
  topics = cursor.fetchall()
  # print(topics)
  #articles = Articles()
  # print(articles[0]['title'])
  return render_template("articles.html", articles = topics)

@app.route('/article/<int:id>')
def article(id):
  cursor = db.cursor()
  sql = 'SELECT * FROM topic WHERE id = {}'.format(id)
  cursor.execute(sql)
  topic = cursor.fetchone()
  # print(topic)
  # articles = Articles()
  # article = articles[id-1]
  #print(articles[id-1])
  return render_template("article.html" , article = topic)

@app.route('/add_articles', methods = ["GET", "POST"])
def add_articles():
  cursor = db.cursor()
  if request.method == "POST":
    author = request.form['author']
    title = request.form['title']
    desc = request.form['desc']

    sql = "INSERT INTO `busan`.`topic` (`author`, `title`, `desc`) VALUES (%s, %s, %s);"
    input_data = [author, title, desc]
    #print(request.form['desc'])

    cursor.execute(sql, input_data)
    db.commit()
    print(cursor.rowcount)
    # db.close()
    return redirect("/articles")

  else :
    return render_template("add_articles.html")

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
  cursor = db.cursor()
  sql = 'DELETE FROM topic WHERE id = {};'.format(id)
  cursor.execute(sql)
  db.commit()
  return redirect("/articles")

@app.route('/<int:id>/edit', methods =['GET', 'POST'])
def edit(id):
  cursor = db.cursor()
  if request.method == "POST":
    title = request.form['title']
    desc = request.form['desc']
    author = request.form['author']
    sql = "UPDATE topic SET title = %s , desc = %s , author = %s  WHERE id = {};".format(id)
    print(sql)
    input_data = [title, desc, author]
    cursor.execute(sql, input_data)
    db.commit()
    return redirect('/articles')

  else:
    sql = "SELECT * FROM topic WHERE id = {}".format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    # print(topic)
    return render_template("edit_articles.html", article = topic)

@app.route('/register', methods = ['GET', 'POST'])
def register():
  cursor = db.cursor()
  if request.method == "POST" :
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    password = sha256_crypt.encrypt(request.form['password'])
    sql = "INSERT INTO users (name, email, username, password) VALUES (%s,%s,%s,%s)"
    input_data = [name, email, username, password]
    cursor.execute(sql, input_data)
    db.commit()

    return redirect('/articles')

  else:
    return render_template("register.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
  cursor = db.cursor
  if request.method == 'POST':
    username = request.form['username']
    userpw_1 = request.form[password]
    sql = 'SELECT passord FROM users WHERE email = %s;'
    input_data = [username]
    cursor.execute(sql, input_data)
    password = cursor.fetchone()
    print(password[0])
    if sha256_crypt.verify("userpw_1", "password[0]"):
      return "success"

  else:
    return password[0]

if __name__ == '__main__':
  app.run()