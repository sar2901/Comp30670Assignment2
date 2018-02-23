# flask_platform/flaskapp/views.py

from flask import render_template
from flaskapp import app
import systeminfo

@app.route('/')
def index():
	returnDict = {}
	returnDict['user'] = 'Sybilla Robertson'
	returnDict['title'] = 'Home'
	returnDict['systeminfo'] = systeminfo.get_platform_info()
	return render_template("index.html", **returnDict)
