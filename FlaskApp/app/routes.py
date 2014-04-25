from flask import Flask, render_template, request
import helpers
import filters
import csv

app = Flask(__name__)

app.vars = {}


@app.route('/', methods = ['GET'])
def index():
    return render_template('home.html')
    
@app.route('/population', methods = ['GET', 'POST'])
def population():
	if request.method == 'GET':
		
		return render_template('searchpopulation.html')
	else:
		# build the skiplist and pass in as argument
		populationskiplist = helpers.makePopulationlist()
	
		# for post request do the searching and redirect
		# to the download page and pass in file as arg
	     #request was a POST
        app.vars['initial'] = request.form['initial']
        app.vars['popgreater'] = request.form['popgreater']
        app.vars['poplesser'] = request.form['popgreater']

        filters.makeFilteredPop(populationskiplist, app.vars)

        return render_template('download.html')

@app.route('/orders', methods = ['GET', 'POST'])
def orders():
	if request.method == 'GET':
		# build the skiplist and pass in as argument
		orderskiplist = helpers.makePresidentialOrderlist()

		return render_template('searchorders.html', ord = orderskiplist)
	else:
		# for post request do the searching and redirect
		# to the download page and pass in file as arg
		return render_template('searchpopulation.html')

@app.route('/grants', methods = ['GET', 'POST'])
def grants():
	if request.method == 'GET':
		# build the skiplist and pass in as argument
		grantskiplist = helpers.makeGrantlist()

		return render_template('searchgrants.html', grnt = grantskiplist)
	else:
		# for post request do the searching and redirect
		# to the download page and pass in file as ar 
		return render_template('searchpopulation.html')


if __name__ == '__main__':
    app.run(debug=True)	
