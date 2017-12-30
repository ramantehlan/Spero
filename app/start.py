# this renders the home page which is start.html
from allImports import *


@app.route("/", methods = ["GET"])
def start():
  return render_template("index.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
  return render_template("register.html")

@app.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method == 'POST':
      username=request.form["username"]
      password=request.form["password"]
      status=request.form['options']
      if status=="Refugee":
          user = Refugees.get(Refugees.username==username)
          return render_template("refugee/profile.html", user=user, cfg=cfg)
      elif status=="Employer":
          user=Employers.get(Employers.username==username)
          return render_template("employer/profil.html", user=user, cfg=cfg)
      else:
          user=Asylums.get(Asylums.username==username)
          return render_template("index.html", user=user)
    else:
      return render_template("sign.html")

# Refugee routes
@app.route("/info/<username>", methods=["GET"])
def info(username):
    user = Refugees.get(Refugees.username==username)
    return render_template("refugee/profile.html", cfg=cfg, user=user)

@app.route("/search/<username>", methods=["GET", "POST"])
def search(username):
    user = Refugees.get(Refugees.username==username)
    jobs=[]
    for job in Jobs.select():
        jobs.append(job)
    return render_template("refugee/search.html", cfg=cfg, user=user, jobs=jobs)

@app.route("/dashboard/<username>", methods=["GET"])
def dashboard(username):
    user = Refugees.get(Refugees.username==username)
    return render_template("refugee/dashboard.html", cfg=cfg, user=user)

@app.route("/settings", methods=["GET"])
def settings():
    return render_template("refugee/settings.html", cfg=cfg)

@app.route("/out", methods=["GET"])
def out():
    return render_template("index.html")



#Employer Routes
@app.route("/profil/<username>", methods=["GET"])
def profil(username):
    user=Employers.get(Employers.username==username)
    return render_template("employer/profil.html", cfg=cfg, user=user)

@app.route("/postjob/<username>", methods=["GET", "POST"])
def postjob(username):
    if request.method == 'POST':
      user=Employers.get(Employers.username==username)
      title=request.form["title"]
      extra=request.form["descript"]
      salary=request.form['salary']
      location=request.form['location']
      job={}
      job["title"]= title
      job["description"]=extra
      job["salary"]=salary
      job["location"]=location
      ipfs=api.add_json(job).encode("utf-8")
      print "This job is stored in IPFS file system", ipfs

      job = Jobs(employer=user.uid,
                title=title,
                address=location,
                salary=salary,
                description= job["description"]
                ).save()
      return render_template("employer/jobpost.html", user=user, cfg=cfg)
    user=Employers.get(Employers.username==username)
    return render_template("employer/jobpost.html", user=user, cfg=cfg)

@app.route("/dash/<username>", methods=["GET"])
def dash(username):
    user=Employers.get(Employers.username==username)
    return render_template("employer/dashboard.html", cfg=cfg, user=user)

@app.route("/setting", methods=["GET"])
def setting():
    return render_template("employer/setting.html", cfg=cfg)

@app.route("/logout", methods=["GET"])
def logout():
    return render_template("index.html")
