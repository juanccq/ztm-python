import os
from flask import Flask, render_template, send_from_directory, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template( 'index.html' )

@app.route('/works')
def my_works():
    return render_template( 'works.html' )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory( os.path.join( app.root_path, 'static' ), 'favicon.ico', mimetype='image/vnd.microsoft.icon' )

@app.route('/about')
def about_me():
    return render_template('about.html')

@app.route('/contact')
def my_contact():
    return render_template('contact.html')

@app.route('/components')
def my_components():
    return render_template('components.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
		
			write_to_csv( data )

			return redirect( 'thankyou' )
		except:
			return 'did not save to database'
	else:
		return 'something is wrong'


def write_database( data ):
	with open( 'database.txt', 'a' ) as my_file:
		text = my_file.write( f"\nemail: {data['email']}, subject: {data['subject']}, message: {data['message']}" )


def write_to_csv( data ):
	with open( 'database.csv', mode='a', newline='' ) as database2:
		email = data[ 'email' ]
		subject = data[ 'subject' ]
		message = data[ 'message' ]

		csv_writter = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writter.writerow([email, subject, message])