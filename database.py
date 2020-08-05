import sqlite3
import datetime

class Database:

    def __init__(self):
        self.connection = None


    def get_connection(self):
        #self.connection = sqlite3.connect('db/database.db')
        self.connection = sqlite3.connect('db/database.db')
        self.connection.row_factory = sqlite3.Row
        return self.connection


    def disconnect(self):
        if self.connection is not None:
            self.connection.close()



    def get_user_complet(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from user")
        res = [dict(row) for row in cursor.fetchall()]
        return res



    def get_user(self,_email,_password):
        cursor = self.get_connection().cursor()
        cursor.execute(("select * from user where email is ? and password is ?"),(_email,_password))
        res = [dict(row) for row in cursor.fetchall()]
        return res


    def get_user_with_id(self,_id):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from user where id is ?",(_id,))
        res = [dict(row) for row in cursor.fetchall()]
        return res



    def get_user_with_email(self,_email):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from user where email is ?",(_email,))
        res = [dict(row) for row in cursor.fetchall()]
        return res

    def get_groupe_admin(self,_id):
        cursor = self.get_connection().cursor()
        cursor.execute("select admin from groupe where id is ?",(_id,))
        res = [dict(row) for row in cursor.fetchall()]
        return res


     # a revoir --  retirer
    def get_user_groupes(self,_id):
        cursor = self.get_connection().cursor()
        #cursor.execute(("select * from groupe where participant is ?"),(_id))
        cursor.execute("select * from groupe where id is ?",(_id,))
        res = [dict(row) for row in cursor.fetchall()]
        return res


    def get_participant_groupes(self,_id):
        cursor = self.get_connection().cursor()
        #cursor.execute(("select * from groupe where participant is ?"),(_id))
        cursor.execute("select * from participant where id is ?",(_id,))
        res = [dict(row) for row in cursor.fetchall()]
        return res

    #retourne la liste des participants d'un groupe
    def get_participant_du_groupes(self,_id):
        cursor = self.get_connection().cursor()
        #cursor.execute(("select * from groupe where participant is ?"),(_id))
        cursor.execute("select * from participant where groupeId is ?",(_id,))
        res = [dict(row) for row in cursor.fetchall()]
        return res


    def get_user_cadeaux(self,_userId,_groupeId):
        cursor = self.get_connection().cursor()
        #cursor.execute(("select * from groupe where participant is ?"),(_id))
        cursor.execute("select * from cadeaux where userId is ? and groupeId is ?",(_userId,_groupeId,))
        res = [dict(row) for row in cursor.fetchall()]
        return res



    def ajouter_cadeau(self,_groupeId,_userId,_cadeau,_url):
        connection = self.get_connection()
        connection.execute(("insert into cadeaux(groupeId,userId,cadeau,url)"
                            "values(?,?,?,?)"),(_groupeId,_userId,_cadeau,_url))
        connection.commit()



    def enlever_cadeau(self,_groupeId,_userId,_cadeauId):
        connection = self.get_connection()
        connection.execute("delete from cadeaux where cadeauId is ? and groupeId is ? and userId is ?",(_cadeauId,_groupeId,_userId,))
        connection.commit()



    def ajouter_participant(self,_groupeId,_userId):
        connection = self.get_connection()
        connection.execute(("insert into participant(groupeId,id)"
                            "values(?,?)"),(_groupeId,_userId))
        connection.commit()



    def enlever_participant(self,_groupeId,_userId):
        connection = self.get_connection()
        connection.execute("delete from participant where groupeId is ? and id is ?",(_groupeId,_userId,))
        connection.commit()



    def ajouter_groupe(self,_nom,_admin,_montant,_datePige):
        connection = self.get_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute(("insert into groupe(nom,admin,montant,datePige)"
                                "values(?,?,?,?)"),(_nom,_admin,_montant,_datePige))
            #print(cursor.lastrowid)
            #return(cursor.lastrowid)
            last = cursor.lastrowid
        self.disconnect()
        self.ajouter_participant(last,_admin)



    def ajouter_user(self,_nom,_prenom,_email,_password):
        connection = self.get_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute(("insert into user(nom,prenom,email,password)"
                                "values(?,?,?,?)"),(_nom,_prenom,_email,_password))
            print(cursor.lastrowid)
            #return(cursor.lastrowid)
            last = cursor.lastrowid
        #self.disconnect()
        #self.get_user_with_id(last)
        return last






