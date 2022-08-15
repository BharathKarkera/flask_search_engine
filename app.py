import flask

import subprocess


app=flask.Flask(__name__)

app.config["DEBUG"]=True

app.secret_key="bharath"


@app.route('/',methods=["GET"])

def index_fun():

    flask.flash("Search for a site...")

    return flask.render_template("index.html")



@app.route("/search", methods=["POST","GET"])

def greet():

    args ='unset GREP_OPTIONS ; unset GREP_COLOR ; cat URL_list.txt |grep -i ' + flask.request.form['search_parameter'] + ' |sed G > raw_result.txt'

    result=subprocess.run(args,capture_output=True, shell=True)	

    

    args ='/bin/bash html_former.sh'

    result=subprocess.run(args,capture_output=True, shell=True)

	

    flask.flash("Showing results for : "+str(flask.request.form['search_parameter'])+" ")

    return  flask.render_template("test.html"),{"Refresh":"5; url=https://localhost:5000"}


app.run(host="0.0.0.0",ssl_context=('cert.pem', 'key.pem'))
