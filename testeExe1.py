from exercice1 import User, Client, Commande, Produit, Lign_cmd
from exercice1DAO import UserDAO, ClientDAO, CommandeDAO, ProduitDAO, Lign_cmdDAO




#teste create

user1 = User(None, "elyahyaouy imane", "elyahyaouyiman9@gmail.com", "password")
user2 = User(None, "imano", "imano@gmail.com", "password2")
user_dao = UserDAO()
user_id_1 = user_dao.create(user1)
user_id_2 = user_dao.create(user2)


client1 = Client(None, "064574", user_id_1)  
client_dao = ClientDAO()
client_id1=client_dao.create(client1)
print(client1)
client1.SetNumClient("0655")


c1 = Commande(None,12364, "28/11/2024",client_id1 )  
c2 = Commande(None,2554, "29/11/2024", client_id1)   
c3 = Commande(None,0, "", client1) 
print(c1)
c3.CopieyReferenceComand(c2)
print(c3)  
commande_dao = CommandeDAO()
c1_id=commande_dao.create(c1)
c2_id=commande_dao.create(c2)
c3_id=commande_dao.create(c3)




produit1 = Produit(None,"car", 6588)
produit2 = Produit(None,"phone", 3000)
produit3 = Produit(None,"pc", 7000)
produit_dao = ProduitDAO()
p2_id=produit_dao.create(produit1)
p3_id=produit_dao.create(produit2)
p4_id=produit_dao.create(produit3)
print(produit1)
print(produit2)
print(produit3)



l1 = Lign_cmd(None,20, p3_id, c1_id)
l2 = Lign_cmd(None,2, p2_id, c2_id)
l3 = Lign_cmd(None,5, p3_id, c2_id)
l4 = Lign_cmd(None,34, p4_id, c1_id)

lign_cmd_dao = Lign_cmdDAO()
lign_cmd_dao.create(l1)
lign_cmd_dao.create(l2)
lign_cmd_dao.create(l3)
lign_cmd_dao.create(l4)
l1.afficher()
l2.afficher()
l3.afficher()
l4.afficher()



client1.link_command(c1)
client1.link_command(c2)

client1.aficheCmd()

prix = produit1 + produit3
print(f"le prix de 2 {prix}")




listPro = [produit1, produit2, produit3]
listProTie = produit3.trieProduit(listPro)
for i in listProTie:
    print(i)







#teste getone
existeclient = 9
client_dao = ClientDAO()
client_1 = client_dao.get_one(existeclient)
if client_1:
    print(client_1)
else:
    print("Clientnot found")


# Testing getALL
all_clients = client_dao.get_all()
print("All Clients:")
for client in all_clients:
    print(client)


#teste Update
clientUP = client_dao.get_one(existeclient)
if clientUP:
    clientUP.SetNumClient("985565")  
    client_dao.update(clientUP)
    updated_client = client_dao.get_one(existeclient)
else:
    print("Client 2 not existe")

#tetset delete
delete = client_dao.get_one(existeclient)
if delete:
    client_dao.delete(delete)
    delete = client_dao.get_one(existeclient)    
else:
    print("Client not found")