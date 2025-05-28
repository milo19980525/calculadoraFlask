from flask import Flask
from flask import render_template,request,make_response
import requests

app = Flask(__name__)


@app.route('/')
def show_all():
	return render_template('show_all.html')

@app.route('/send', methods = ['POST','GET'])
def send():
	sig = request.form['action']
	numero1 = request.form["numero1"]
	numero2 = request.form["numero2"]
	resultado = requests.get('http://app:5000/'+numero1+'/'+numero2+'/'+sig).text
	return render_template('/show_all.html', string_variable=resultado)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
	