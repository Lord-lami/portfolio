from flask import Flask, render_template, send_from_directory, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/<string:page>')
def display(page):
	return render_template(page)

def write_to_csv(data):
	with open('database.csv', 'a') as database:
		email = data['email']
		subject = data['subject']
		messag = data['message']
		csv_writer = csv.writer(database, delimiter=',')
		csv_writer.writerow([email, subject, messag])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('/thankyou.html')
    else:
    	return 'Somethings wrong'



    	

# @app.route('/favicon.ico')
# def favicon():
# 	return send_from_directory('static', 'favicon.ico')
