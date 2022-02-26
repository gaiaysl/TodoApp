#flask-SQLalchemy minimall-aplicatiın kodları alyoruz.
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Ramazan/Desktop/todo app/todo.db'
db = SQLAlchemy(app)
#aradaki köprüyü  kurduk class yazacağız.exit
@app.route("/")
def index():

   todos=Todo.query.all() #LİSTE DÖNECEK HTML GİDİP FOR DÖNGÜSÜ YARDIMIYLA İÇERİK GETİRECEĞİZ
                        #herbiri sözlük yapısı şeklinde gelecek
   return render_template("index.html",todos = todos)
"""tamamla butonunun durumunu kontrol ediyoruz
    DİNAMİK URL """
#GÜNCELLE
@app.route("/copmlete/<string:id>")
def completeTodo(id):
    todo=Todo.query.filter_by(id = id).first() #id bu olan objeler
   #içindeki değeri değiştirmek için;
    """if todo.complete==True:
        todo.cmplete=False
        else:
            todo.complete=True"""
    todo.complate=not todo.complate

    db.session.commit()
    return redirect(url_for("index"))
#SİL
@app.route("/Delete/<string:id>")
def deleteTodo(id):
    todo=Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/add",methods=["POST"]) #kullanıcı veri gönderdiğinde,
def addTodo():

    title=request.form.get("title") #fomdan alıyoruz
    newTodo=Todo(title = title,complate = False) #
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    complate=db.Column(db.Boolean)

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)

