from flask import Flask, redirect, render_template, request, flash, url_for
app=Flask(__name__)
app.secret_key="portfolio_secret_key_2026"
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/skills")
def skills():
    return render_template("skills.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")
@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name=request.form["name"]
        email=request.form["email"]
        message=request.form["message"]
        flash(f"Thank you {name}! Your message been sent.","success")
        return redirect(url_for("home"))
    return render_template("contact.html")
if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)