from flask import Flask, render_template, request , url_for,redirect
from flask_wtf.csrf import CSRFProtect
from formulaire import OrderForm
from exercice1DAO import ClientDAO, CommandeDAO,UserDAO
from exercice1 import Commande
import secrets
secret_key = secrets.token_hex(16)  
app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = secret_key

csrf = CSRFProtect(app)
client_dao = ClientDAO()
userDao= UserDAO()
commande_dao = CommandeDAO()


@app.route('/add_order/<int:client_id>', methods=['GET', 'POST'])
def add_order(client_id):
    form = OrderForm()
    client = client_dao.get_one(client_id)
    if client and form.validate_on_submit():
        reference = form.reference.data
        date = form.date.data
        new_order = Commande(None, reference, date, client_id)
        commande_dao.create(new_order)

        return redirect(url_for('display_client_orders', client_id=client_id))

    return render_template('form.html', form=form, client=client)





@app.route('/client_orders/<int:client_id>')
def display_client_orders(client_id):
    client = client_dao.get_one(client_id)
    user=userDao.get_one(client.user_id)
    if client:
        client_orders = commande_dao.get_orders_by_client_id(client_id)
        return render_template('view.html', client=client, orders=client_orders,user=user)
    else:
        return "Client not found"

if __name__ == '__main__':
    app.run(debug=True)
