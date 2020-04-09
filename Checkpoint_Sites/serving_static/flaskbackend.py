

from flask import Flask, request, render_template, Response, redirect, url_for
app = Flask(__name__,static_url_path='')



@app.route('/title')
def indextitle():
    title = "Bex"
    myName = "Bex"
    return render_template('name.html', name=myName, title=title) #remmemmber to list vars when declaring! these objects are used with jinja in name.html

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/inspo')
def inspo():
    
    return render_template("inspiration.html")

@app.route('/page/<string:title>') #whatever is put after page/ will redirect to inspiration.html via /inspo route
def page(title):
    #return 'Title: ' + title
    return redirect(url_for("inspo"))
   


@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/response', methods=['POST'])
def response():
    name = request.form.get("name")
    return render_template("form.html", name=name)

@app.route('/load_data')
def load_data():
    return "Success"

#mongodb stuff    

from mongoengine import *
connect('Checkpoint_DB')

class User(Document):
    email = StringField()
    first_name = StringField()
    last_name = StringField()
#bex = User(first_name='Bex', last_name='S')
#bex.save()

class Countries(Document):
    name = StringField()


#API stuff

@app.route('/addCountry') #hardcode adding to db
def addCountry():
  #  list = db.Countries.find()
  #  return list
    nz1 = Countries(name="New Zealand 1")
    nz1.save()
    return "Success"

@app.route('/addCountry/<name>', methods=['POST']) #hardcode adding to db
def addUser(name):

    country = Checkpoint_DB.Countries.insert({ "name": name })
    country.save()
  #  list = db.Countries.find()
  #  return list
    
    return "Success"

@app.route('/getCountries', methods=['GET'])
def getCountries():
    country = Countries.objects
    return country.to_json()

@app.route('/getCountries/<string:name>', methods=['GET'])
def getCountriesByName(name):
    country = Countries.objects.get(name=name)
    return country.to_json()


@app.route('/users', methods=['GET'])
def users():
    users = User.objects
    return users.to_json()

@app.route('/users/<first_name>', methods=['GET'])
def getUserByFirstName(first_name):
    users = User.objects.get(first_name=first_name)
    return users.to_json()


if __name__ =="__main__":
   # app.run(host='10.25.100.59',debug=True,port=8080) for deployment
    app.run(debug=True,port=8080) #for local





