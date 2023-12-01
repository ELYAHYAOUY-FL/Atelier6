import mysql.connector

mydb = mysql.connector.connect( host="localhost", user="root", password="")
Atelier6 = mydb.cursor()

Atelier6.execute("CREATE DATABASE Atelier6")

mydb = mysql.connector.connect( host="localhost", user="root", password="", database="Atelier6")

Atelier6 = mydb.cursor()


Atelier6.execute("CREATE TABLE User (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), login VARCHAR(255), password VARCHAR(255))")
Atelier6.execute("CREATE TABLE Client(id INT AUTO_INCREMENT PRIMARY KEY, numero VARCHAR(255), user_id INT, FOREIGN KEY (user_id) REFERENCES User(id))")
Atelier6.execute("CREATE TABLE Commande(id INT AUTO_INCREMENT PRIMARY KEY, reference VARCHAR(255), date VARCHAR(255), client_id INT, FOREIGN KEY (client_id) REFERENCES Client(id))")
Atelier6.execute("CREATE TABLE Produit(id INT AUTO_INCREMENT PRIMARY KEY, libelle VARCHAR(255), prix INT)")
Atelier6.execute("CREATE TABLE Lign_cmd (id INT AUTO_INCREMENT PRIMARY KEY, qte INT, produit_id INT, commande_id INT, FOREIGN KEY (produit_id) REFERENCES Produit(id), FOREIGN KEY (commande_id) REFERENCES Commande(id))")
