class User:
    def __init__(self,id,nom,login,password):
        self._nom=nom
        self._login=login
        self._password=password
        self.id=id
    def _getPassword(self):
        return self._password
    def __str__(self):
                 return f"user information acount  :  nom:{self._nom} login:{self._login}  password:{self._password}"

         
class Client(User):
        def __init__(self, id,numero,use):
            self.id=id
            self.__numero = numero  
            self.user_id=use       
            self.commandes=[]
        def SetNumClient(self, numero):
           self.__numero = numero  
        def getNumero(self):
           return self.__numero 

        def link_command(self,cmd):
             self.commandes.append(cmd)  
        def __str__(self):
                 return   f" le numero {self.__numero} "
        
        def aficheCmd(self):
              print("la liste de command de cet client est : ")
              for i in self.commandes:
                    print(i)

class Commande:
    def __init__(self,id, reference, date, client_id):
        self.id=id
        self.__reference = reference
        self.date = date
        self.client_id = client_id
        
    def getReferance(self):
        return self.__reference
    
    def CopieyReferenceComand(self, cmd):
        self.__reference = cmd.getReferance()
        self.date = cmd.date
        self.client_id = cmd.client_id
    
    def __str__(self):
        return f"command information: reference:{self.__reference} le date:{self.date}"
   
     
class Produit:
     def __init__(self,id,libelle,prix):
          self.id=id
          self.libelle=libelle
          self.prix=prix
     def trieProduit(self,listt): 
          return sorted(listt , key=lambda produit: produit.prix)
     def __add__(self, produit): 
          return self.prix + produit.prix
     def __str__(self):
           return f"le produit infromation : {self.libelle}  prix ={self.prix}"
     
class Lign_cmd:
          def __init__(self,id,qte,produit,commande):
               self.id=id

               self.qte=qte
               self.produit_id=produit
               self.commande_id=commande
          def afficher(self):
                print(f"pour cet ligne de command on a la quantite {self.qte}" )
                print(self.produit_id)
                print(self.commande_id)

                

