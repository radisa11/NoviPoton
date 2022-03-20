
from flask import Flask, render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = "pssst"


@app.route("/")
def index():
    if "voters" not in session:
        session["voters"] = []
    if "total_votes" not in session:
        session["total_votes"] = 0
        if "votes" not in session:
            session["votes"] = {"Toy Story":0,"The Incredibles":0, "Monsters Inc":0}

    return render_template("index.html")

@app.route("/vote",methods=["POST"])
def vote():
    temp_user = {
        "name": request.form["name"],
        "age": request.form["age"],
        "movie": request.form["movie"]
    }
    session["voters"].append(temp_user)
    session.modified = True
    session["total_votes"] += 1
    session["votes"][temp_user["movie"]] +=1
    return redirect("/results") # dont't render_template on a post route

@app.route("/results")
def results():
    return render_template("results.html",voters=session["voters"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)