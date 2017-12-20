# this renders the home page which is start.html
from allImports import *


@app.route("/", methods = ["GET"])
def start():
  return render_template("index.html")


@app.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method == 'POST':
      username=request.form["username"]
      password=request.form["password"]
      status=request.form['options']
      if status=="Refugee":
          user = Refugees.get(Refugees.username==username)
          return render_template("refugee/profile.html", user=user)
      elif status=="Employer":
          user=Employers.get(Employers.username==username)
          return render_template("employer/profile.html", user=user)
      else:
          user=Asylums.get(Asylums.username==username)
          return render_template("index.html", user=user)
    else:
      return render_template("sign.html")

# Refugee routes
@app.route("/info", methods=["GET"])
def info():
    return render_template("profile.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("profile.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("profile.html")

@app.route("/profile", methods=["GET"])
def settings():
    return render_template("profile.html")

@app.route("/out", methods=["GET"])
def out():
    return render_template("index.html")
#Employer Routes

@app.route("/profile", methods=["GET"])
def info():
    return render_template("profile.html")

@app.route("/postjob", methods=["GET"])
def postjob():
    return render_template("profile.html")

@app.route("/dash", methods=["GET"])
def dash():
    return render_template("profile.html")

@app.route("/setting", methods=["GET"])
def setting():
    return render_template("profile.html")

@app.route("/logout", methods=["GET"])
def logout():
    return render_template("index.html")
