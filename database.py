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
