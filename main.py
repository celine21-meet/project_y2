from flask import Flask, jsonify, request, render_template, redirect, url_for
import random
import requests 
import json
app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'super-secret-key'

Username= 'celine'
Password= '123'
@app.route('/', methods = ['GET', 'POST'])
def login():
  if request.method == 'GET' :
    return render_template('login.html')
  if request.method == 'POST' :
    username = request.form['username']
    password = request.form['pass']
    if Username == username:
      if Password == password:
        return redirect(url_for('portal')
        )
    else:
      return render_template('login.html')

@app.route('/portal')
def portal():
  Welcome = 'Welcome, ' + Username
  return render_template ('portal.html', Welcome=Welcome)


@app.route('/display')
def display():
  response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY")
  python_dictionary = json.loads(response.content)
  img_link = python_dictionary["photos"][0]["img_src"]
  print(img_link)
  return render_template('display.html', img_link = img_link)

if __name__ == "__main__":  # Makes sure this is the main process
  app.run( # Starts the site
    host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
    port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
  )