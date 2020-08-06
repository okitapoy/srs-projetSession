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
import random
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
	#tab = [1,2,3,4,5,6,13,55,432]
	#tt = {"un": 1,"deux": 2,"trois": 3,"quatre":4,"cinq":5}
	#print(tt)
	if len(request.args) > 0:
		return render_template('accueil.html',erreur=request.args['erreur'])
	else:
		return render_template('accueil.html')

	#return render_template('accueil.html',erreur=request.args['erreur'])



@app.route('/profil', methods=['POST','GET'])
def page_profil():
	db = get_db()
	if request.method == 'POST':
		userListe = db.get_user(request.form['email'],request.form['password'])
		listeGroupe = []
		if userListe:
			user = userListe[0]
			#groupes = db.get_participant_groupes(user['id'])

			#for groupe in groupes:
				#le_groupe = db.get_user_groupes(groupe['groupeId'])
				#if le_groupe:
					#listeGroupe.append(le_groupe[0])

			#return render_template('profil.html', profil = user, groupes = listeGroupe)
			#return redirect(url_for('affichier_profil', profil = user['id'], groupes = listeGroupe))
			return redirect(url_for('affichier_profil', userId = user['id'] ))
		else:
			return redirect(url_for('page_acceuil',erreur = 1))
	else:
		user = request.args['profil']
		listeGroupe = request.args['listeGroupe']
		#render_template('profil.html', profil = user, groupes = listeGroupe)
		return redirect(url_for('page_profil', profil = user, groupes = listeGroupe))



@app.route('/affichier_profil')
def affichier_profil():
	db = get_db()

	userListe = db.get_user_with_id(request.args['userId'])
	listeGroupe = []
	if userListe:
		user = userListe[0]
		groupes = db.get_participant_groupes(user['id'])

		for groupe in groupes:
			le_groupe = db.get_user_groupes(groupe['groupeId'])
			if le_groupe:
				listeGroupe.append(le_groupe[0])
	return render_template('profil.html',profil = user, groupes = listeGroupe)



@app.route('/creer_compte', methods=['POST'])
def creer_compte():
	db = get_db()
	#_userId = 1
	_userId = db.ajouter_user(request.form['nom'],request.form['prenom'],request.form['email'],request.form['password'])
	return redirect(url_for('affichier_profil', userId = _userId))



@app.route('/creer_groupe/<adminId>', methods=['POST'])
def creer_groupe(adminId):
	db = get_db()
	db.ajouter_groupe(request.form['nom'],adminId,request.form['montant'],request.form['date'])
	return redirect(url_for('affichier_profil', userId = adminId))




@app.route('/groupe/<id>/<userId>')
def groupe(id,userId):
	db = get_db()

	admin = db.get_groupe_admin(id)[0]['admin']

	participants = db.get_participant_du_groupes(id)
	liste_cadeaux = db.get_user_cadeaux(userId,id)
	liste_participants = []

	for parti in participants:
		le_participant = db.get_user_with_id(parti['id'])
		if le_participant:
			liste_participants.append(le_participant[0])
	return render_template('groupe.html', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = int(userId), adminId = admin)




@app.route('/ajouter_cadeau/<id>/<userId>', methods=['POST','GET'])
def ajouter_cadeau(id,userId):
	db = get_db()

	db.ajouter_cadeau(id,userId,request.form['cadeau'],request.form['url'])
	participants = db.get_participant_du_groupes(id)
	liste_cadeaux = db.get_user_cadeaux(userId,id)
	liste_participants = []

	for parti in participants:
		le_participant = db.get_user_with_id(parti['id'])
		if le_participant:
			liste_participants.append(le_participant[0])
	#return render_template('groupe.html', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId)
	return redirect (url_for('groupe', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId, id =id))



@app.route('/retirer_cadeau/<id>/<userId>/<cadeauId>', methods=['POST','GET'])
def retirer_cadeau(id,userId,cadeauId):
	db = get_db()

	db.enlever_cadeau(id,userId,cadeauId)
	participants = db.get_participant_du_groupes(id)
	liste_cadeaux = db.get_user_cadeaux(userId,id)
	liste_participants = []

	for parti in participants:
		le_participant = db.get_user_with_id(parti['id'])
		if le_participant:
			liste_participants.append(le_participant[0])
	#return render_template('groupe.html', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId)
	return redirect (url_for('groupe', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId, id =id))




@app.route('/ajouter_participant/<id>/<userId>', methods=['POST','GET'])
def ajouter_participant(id,userId):
	db = get_db()
	print(request.form['email'])

	userListe = db.get_user_with_email(request.form['email'])
	if userListe:
		user = userListe[0]
		db.ajouter_participant(id,user['id'])

	participants = db.get_participant_du_groupes(id)
	liste_cadeaux = db.get_user_cadeaux(userId,id)
	liste_participants = []

	for parti in participants:
		le_participant = db.get_user_with_id(parti['id'])
		if le_participant:
			liste_participants.append(le_participant[0])
	#return render_template('groupe.html', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId)
	return redirect (url_for('groupe', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId, id =id))




@app.route('/retirer_participant/<id>/<userId>/<participantId>', methods=['POST','GET'])
def retirer_participant(id,userId,participantId):
	db = get_db()

	db.enlever_participant(id,participantId)
	participants = db.get_participant_du_groupes(id)
	liste_cadeaux = db.get_user_cadeaux(userId,id)
	liste_participants = []

	for parti in participants:
		le_participant = db.get_user_with_id(parti['id'])
		if le_participant:
			liste_participants.append(le_participant[0])
	#return render_template('groupe.html', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId)
	return redirect (url_for('groupe', participants = liste_participants, groupeId = id, cadeaux = liste_cadeaux, userId = userId, id =id))




@app.route('/effectuer_pige/<id>/<userId>')
def effectuer_pige(id,userId):
	db = get_db()
	index = 0;
	tabloId = []
	tabloBrasser = []
	participants = db.get_participant_du_groupes(id)
	print(participants)

	for parti in participants:
		tabloId.append(parti['id'])
		tabloBrasser.append(parti['id'])

	if len(tabloId) > 0:
		#random.shuffle(tabloBrasser)
		max = len(tabloId)
		min = 1
		brasser = 0

		while brasser == 0:
			random.shuffle(tabloBrasser)
			brasser = 1
			for i in range(max):
				if tabloId[i] == tabloBrasser[i]:
					brasser = 0
			print(tabloBrasser)



		#for i in range(max):
			#nbr = random.randint(min,max)
			#while nbr in tabloBrasser or nbr is tabloId[i]:
				#nbr = random.randint(min,max)

			#tabloBrasser.append(nbr)


    #max = len(tabloId) - 1
    #min = 0
	print("original : ")
	print(tabloId)
	#print(tabloBrasser)

	if tabloId == tabloBrasser:
		print("ceeeeeeee egallllllll")


	#return redirect(url_for('affichier_profil', userId = adminId))
	return render_template('accueil.html')







