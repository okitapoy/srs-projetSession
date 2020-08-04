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





def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database





@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()








@app.route('/')
def page_acceuil():
	#db = get_db()
	#n = db.get_user_complet()
	#print(n)
	if len(request.args) > 0:
		return render_template('accueil.html',erreur=request.args['erreur'])
	else:
		return render_template('accueil.html')

	#return render_template('accueil.html',erreur=request.args['erreur'])



@app.route('/profil', methods=['POST'])
def page_profil():
	db = get_db()
	userListe = db.get_user(request.form['email'],request.form['password'])
	listeGroupe = []
	#user = userListe[0]
	#groupes = db.get_user_groupes(user['id'])

	if userListe:
		user = userListe[0]
		groupes = db.get_participant_groupes(user['id'])

		for groupe in groupes:
			le_groupe = db.get_user_groupes(groupe['groupeId'])
			if le_groupe:
				listeGroupe.append(le_groupe[0])

		return render_template('profil.html', profil = user, groupes = listeGroupe)
	else:
		return redirect(url_for('page_acceuil',erreur = 1))



@app.route('/inscription')
def page_inscription():
	return render_template('inscription.html')


@app.route('/creer_groupe')
def creer_groupe():
	print(request.args['id'])
	return render_template('creer_groupe.html')


@app.route('/groupe')
def groupe():
	db = get_db()
	participants = db.get_participant_du_groupes(request.args['id'])
	liste_participants = []

	for parti in participants:
		le_participant = db.get_user_with_id(parti['id'])
		if le_participant:
			liste_participants.append(le_participant[0])
	return render_template('groupe.html', participants = liste_participants, groupeId = request.args['id'])













