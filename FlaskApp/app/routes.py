from flask import Flask, render_template, request
import helpers

app = Flask(__name__)

app.vars = {}


@app.route('/', methods = ['GET'])
def index():
    numquestions=5
    if request.method == 'GET':
        return render_template('home.html',num=numquestions)
    else:
    	# for post requests
    	app.vars['name'] = request.form['name']
    	app.vars['age'] = request.form['age']

    	f = open('%s_%s.txt'%(app.vars['name'],app.vars['age']),'w')
        f.write('Name: %s\n'%(app.vars['name']))
        f.write('Age: %s\n\n'%(app.vars['age']))
        f.close()

        return 'request.method was not a GET!'

@app.route('/population', methods = ['GET', 'POST'])
def population():
	if request.method == 'GET':
		# build the skiplist and pass in as argument
		populationskiplist = helpers.makePopulationList()

		return render_template('searchpopulation.html')
	else:
		# for post request do the searching and redirect
		# to the download page and pass in file as arg
	    return render_template('searchpopulation.html')

@app.route('/orders', methods = ['GET', 'POST'])
def orders():
	if request.method == 'GET':
		# build the skiplist and pass in as argument
		orderskiplist = helpers.makePresidentialOrderList()

		return render_template('searchorders.html')
	else:
		# for post request do the searching and redirect
		# to the download page and pass in file as arg
		return render_template('searchpopulation.html')

@app.route('/grants', methods = ['GET', 'POST'])
def grants():
	if request.method == 'GET':
		# build the skiplist and pass in as argument
		grantskiplist = helpers.makeGrantList()

		return render_template('searchgrants.html')
	else:
		# for post request do the searching and redirect
		# to the download page and pass in file as ar 
		return render_template('searchpopulation.html')


if __name__ == '__main__':
    app.run(debug=True)	
