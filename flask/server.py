from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("index.html")

@app.route("/monsters/<string:monster>")
def monster_page(monster):
    return render_template("monster.html",monster_name=monster.capitalize())



if __name__=="__main__":
    app.run(debug=True)