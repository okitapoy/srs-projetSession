#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask import make_response
from flask import g
from flask import request
from flask import redirect
from flask import Response
from flask import url_for
from flask import jsonify
from flask import send_from_directory, send_file
from .database import Database
#import uuid
from datetime import datetime, timedelta, date
#
#
import csv
import urllib
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import shutil
import xml.etree.ElementTree as ET
#
#
from apscheduler.schedulers.background import BackgroundScheduler
from dicttoxml import dicttoxml
import datetime

app = Flask(__name__)










@app.route('/')
def page_acceuil():
    return render_template('accueil.html')



@app.route('/profil')
def page_profil():
	return render_template('profil.html')



@app.route('/inscription')
def page_inscription():
	return render_template('inscription.html')













