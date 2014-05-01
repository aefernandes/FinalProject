
  GovDataMiner by: Anjali Fernandes, Camille Rekhson, Raul Jordan
*******************************************************************

--Version 1.0, Release 1.0.0--

------------------------------
|      Overview of Code      |
------------------------------

We have created a simple website running on our localhost server
in order to run our algorithm. We are using Flask as a microframework
to generate our project in a way that integrates our code and using
some bootstrap css and jquery to style the user interface. We use three 
existing data sets to build and filter our data based on our
algorithms. The backend code is divided into several parts: 

1. The abstract interface for Skip Lists, which we defined as a
python class that implements all major skiplist functions

2. The build and filter modules, which are the two main workhorses of 
our backend. Instead of making 3 different modules for all 3 of our data sets for building,
we decided to create a single build function as an abstraction that takes in 
several arguments and builds a specific skiplist based on the arguments
it is passed in.
The filter module takes in user input from POST requests managed by Flask,
and filterscreates a filtered CSV 

3. Helper functions that assist with building csv's easily from lists of 
dictionaries and other auxiliary features. 

The routes.py of our Flask app brings all these things together and
renders things nicely through the html user interface

For any more in-depth facts about our code, all the main functions are
thoroughly documented and explained in the main files

	* skiplistclass.py
	* builder.py
	* helpers.py
	* routes.py
	* filters.py

--------------------------------------------
|    Dependencies and Running our Code     |
--------------------------------------------

To run our code, a python version of at least 2.7 must be running on 
the machine, and pip should be installed in order to install Flask.

run the command 

	pip install Flask

and navigate to the FlaskApp/app directory and run
	
	python routes.py

if port 5000 is not in use, navigate to localhost:5000
and the main page of our project should show up and should work accordingly

--------------------------------------------
|      User Interface and Navigation       |
--------------------------------------------

The website is based on home page in which a user chooses
what kind of data to mine:

1. All population data per state in the United States
2. All presidential document data signed by Obama
3. All research grant information awarded in the United States
in 2013

Once the user clicks on one, he/she is redirected to
a search form page in which he/she can choose what to filter the
data by. For example, population can be filtered by state initial
or by population numbers. After the filter is performed, the user is
redirected to a page with a download link that contains the filtered 
and formatted data that is easy to open in excel and work with,
entirely based on skiplists and builder algorithms.

-------------------------------
|      Testing *Important*    |
-------------------------------

At first, we used a testing suite known as nosetests
which worked as a standalone testing file that worked
easily for small python projects. However, since we transitioned
to using flask, we decided to change the way we do tests.

To make things easy and simple, we made standalone tests using python's

if __name =='__main__' method to run the tests if each file is run
as a standalone module. We set tests for the main and most important functions in the relevant files of our projects.
We used a combination of assert statements and ran our tests comprehensively.
Every file can that has a __name__=='__main__' in our project runs the tests
and runs correctly with no assertion failures.






