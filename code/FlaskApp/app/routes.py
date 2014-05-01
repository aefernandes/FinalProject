from flask import Flask, render_template, request
import helpers
import filters
import csv


################# DATA MINER ####################
#                                               #
#      Makes a dataminer for government data    #
#      that outputs useful CSV files for easy   #
#      data manipulation                        #
#################################################   



app = Flask(__name__, static_url_path='')

# creates a dictionary to store request objects
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
		if request.form['initial'] != '':
			app.vars['initial'] = request.form['initial']
		if request.form['popgreater'] != '':
			app.vars['popgreater'] = request.form['popgreater']
		if request.form['poplesser'] != '':
			app.vars['poplesser'] = request.form['poplesser']
		
	
		if len(app.vars) == 1:
        # checks for errors in the post request
			searchtype = app.vars.keys()[0]
		        
			filters.filter(populationskiplist, app.vars, searchtype, 'NAME', 1)

			# resets the request dictionary
			app.vars = {}
			return render_template('download.html')
		else:
			app.vars = {}
			return render_template('error.html')

@app.route('/orders', methods = ['GET', 'POST'])
def orders():
	if request.method == 'GET':

		return render_template('searchorders.html')
		
	else:


		# build the skiplist
		orderskiplist = helpers.makePresidentialOrderlist()

	
		if request.form['title_cont'] != '':
			app.vars['title_cont'] = request.form['title_cont']
		if request.form['category'] != '':
			app.vars['category'] = request.form['category']
	    
		if len(app.vars) == 1:

			searchtype = app.vars.keys()[0]
			
			filters.filter(orderskiplist, app.vars, searchtype, 'title', 2)

			# resets the request dictionary
			app.vars = {}
			return render_template('download.html')

		else:
			app.vars = {}
			return render_template('error.html')

		

@app.route('/grants', methods = ['GET', 'POST'])
def grants():
	if request.method == 'GET':
		# build the skiplist and pass in as argument
		grantskiplist = helpers.makeGrantlist()

		return render_template('searchgrants.html')
	else:
		# for post request do the searching and redirect

		# build the skiplist
		grantskiplist = helpers.makeGrantlist()

		if request.form['name_cont'] != '':
			app.vars['name_cont'] = request.form['name_cont']
		if request.form['category'] != '':
			app.vars['category'] = request.form['category']

	    
		if len(app.vars) == 1:

			searchtype = app.vars.keys()[0]

			filters.filter(grantskiplist, app.vars, searchtype, 'Awardee', 3)

			# resets the request dictionary
			app.vars = {}
			return render_template('download.html')
		else:
			app.vars = {}
			return render_template('error.html')


# makes the download link for the filtered file
@app.route('/download', methods = ['GET'])
def download():
	return app.send_static_file('filtereddata.csv')



if __name__ == '__main__':
    app.run(debug=True)	
