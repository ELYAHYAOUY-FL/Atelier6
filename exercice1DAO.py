import mysql.connector
from exercice1 import User  
from exercice1 import Client 
from exercice1 import Commande  
from exercice1 import Produit  
from exercice1 import Lign_cmd  


class UserDAO:
    _url = "localhost"
    _password = ""
    _username = "root"
    _database = "Atelier6"

    def __init__(self):
        self.mydb = mysql.connector.connect(host=self._url, user=self._username, password=self._password, database=self._database)
        self.mycursor = self.mydb.cursor()

    def create(self, user):
        sql = "INSERT INTO User (nom, login, password) VALUES (%s, %s, %s)"
        val = (user._nom, user._login, user._password)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.lastrowid

    def update(self, user):
        sql = "UPDATE User SET nom = %s, login = %s, password = %s WHERE id = %s"
        val = (user._nom, user._login, user._password, user.id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def delete(self, user):
        sql = "DELETE FROM User WHERE id = %s"
        val = (user.id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def get_one(self, id):
        sql = "SELECT * FROM User WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        result = self.mycursor.fetchone()
        if result:
            return User(*result)  
        return None

    def get_all(self):
        sql = "SELECT * FROM User"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        users = []
        for result in results:
            user = User(*result) 
            users.append(user)
        return users


class ClientDAO:
    _url = "localhost"
    _password = ""
    _username = "root"
    _database = "Atelier6"

    def __init__(self):
        self.mydb = mysql.connector.connect(host=self._url, user=self._username, password=self._password, database=self._database)
        self.mycursor = self.mydb.cursor()

    def create(self, client):
        sql = "INSERT INTO Client (numero, user_id) VALUES (%s, %s)"
        val = (client.getNumero(), client.user_id)  
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.lastrowid

    def update(self, client):
        sql = "UPDATE Client SET numero = %s, user_id = %s WHERE id = %s"
        val = (client.getNumero(), client.user_id, client.id)  
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def delete(self, client):
        sql = "DELETE FROM Client WHERE id = %s"
        val = (client.id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def get_one(self, id):
        sql = "SELECT * FROM Client WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        result = self.mycursor.fetchone()
        if result:
            return Client(*result)  
        return None

    def get_all(self):
        sql = "SELECT * FROM Client"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        clients = []
        for result in results:
            client = Client(*result)  
            clients.append(client)
        return clients



class CommandeDAO:
    _url = "localhost"
    _password = ""
    _username = "root"
    _database = "Atelier6"

    def __init__(self):
        self.mydb = mysql.connector.connect(host=self._url, user=self._username, password=self._password, database=self._database)
        self.mycursor = self.mydb.cursor()

    def create(self, commande):
        sql = "INSERT INTO Commande (reference, date, client_id) VALUES (%s, %s, %s)"
        val = (commande.getReferance(), commande.date, commande.client_id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.lastrowid

    def update(self, commande):
        sql = "UPDATE Commande SET reference = %s, date = %s, client_id = %s WHERE id = %s"
        val = (commande.getReferance(), commande.date, commande.client_id, commande.id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def delete(self, commande):
        sql = "DELETE FROM Commande WHERE id = %s"
        val = (commande.id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def get_one(self, id):
        sql = "SELECT * FROM Commande WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        result = self.mycursor.fetchone()
        if result:
            return Commande(*result)  
        return None

    def get_all(self):
        sql = "SELECT * FROM Commande"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        commandes = []
        for result in results:
            commande = Commande(*result) 
            commandes.append(commande)
        return commandes

    def get_orders_by_client_id(self, client_id):
        sql = "SELECT * FROM Commande WHERE client_id = %s"
        val = (client_id,)
        self.mycursor.execute(sql, val)
        results = self.mycursor.fetchall()
        orders = []
        for result in results:
            order = Commande(*result)
            orders.append(order)
        return orders

class ProduitDAO:
    _url = "localhost"
    _password = ""
    _username = "root"
    _database = "Atelier6"  

    def __init__(self):
        self.mydb = mysql.connector.connect(host=self._url, user=self._username, password=self._password, database=self._database)
        self.mycursor = self.mydb.cursor()
    
    def create(self, produit):
        sql = "INSERT INTO Produit (libelle, prix) VALUES (%s, %s)"
        val = (produit.libelle, produit.prix)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.lastrowid 
     
    def update(self, produit):
        sql = "UPDATE Produit SET libelle = %s, prix = %s WHERE id = %s"
        val = (produit.libelle, produit.prix, produit.id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.rowcount
    
    def delete(self, produit):
        sql = "DELETE FROM Produit WHERE id = %s"
        val = (produit.id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.rowcount
    
    def getOne(self, id):
        sql = "SELECT * FROM Produit WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        result = self.mycursor.fetchone()
        if result:
            return Produit(result[0], result[1], result[2])
        return None
    
    def getAll(self):
        mylist = []
        sql = "SELECT * FROM Produit"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        for res in results:
            mylist.append(Produit(res[0], res[1], res[2]))
        return mylist


class Lign_cmdDAO:
    _url = "localhost"
    _password = ""
    _username = "root"
    _database = "Atelier6"

    def __init__(self):
        self.mydb = mysql.connector.connect(host=self._url, user=self._username, password=self._password, database=self._database)
        self.mycursor = self.mydb.cursor()

    def create(self, lign_cmd):
        sql = "INSERT INTO Lign_cmd (qte, produit_id, commande_id) VALUES (%s, %s, %s)"
        val = (lign_cmd.qte, lign_cmd.produit_id, lign_cmd.commande_id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        return self.mycursor.lastrowid

    def update(self, lign_cmd):
        sql = "UPDATE Lign_cmd SET qte = %s, produit_id = %s, commande_id = %s WHERE id = %s"
        val = (lign_cmd.qte, lign_cmd.produit_id, lign_cmd.commande_id, lign_cmd.id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def delete(self, lign_cmd):
        sql = "DELETE FROM Lign_cmd WHERE id = %s"
        val = (lign_cmd.id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def get_one(self, id):
        sql = "SELECT * FROM Lign_cmd WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        result = self.mycursor.fetchone()
        if result:
            return Lign_cmd(*result)  
        return None

    def get_all(self):
        sql = "SELECT * FROM Lign_cmd"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        lign_cmds = []
        for result in results:
            lign_cmd = Lign_cmd(*result)  
            lign_cmds.append(lign_cmd)
        return lign_cmds





