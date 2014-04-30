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
        app.vars['poplesser'] = request.form['poplesser']

        # FIX BUG HERE: should only accept one request
        filters.filter(populationskiplist, app.vars, 'initial', 'NAME', 1)

        return render_template('download.html')

@app.route('/orders', methods = ['GET', 'POST'])
def orders():
	if request.method == 'GET':

		return render_template('searchorders.html')
		
	else:


		# build the skiplist
		orderskiplist = helpers.makePresidentialOrderlist()

		app.vars['title_cont'] = request.form['title_cont']
		app.vars['category'] = request.form['category']

		# FIX BUG HERE: should only accept one request
		filters.filter(orderskiplist, app.vars, 'category', 'title', 2)


		return render_template('download.html')

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

		app.vars['name_cont'] = request.form['name_cont']
		app.vars['category'] = request.form['category']


		# FIX BUG HERE: should only accept one request
		filters.filter(grantskiplist, app.vars, 'category', 'Awardee', 3)


		return render_template('download.html')

@app.route('/download', methods = ['GET'])
def download():
	return app.send_static_file('filtereddata.csv')



if __name__ == '__main__':
    app.run(debug=True)	
