from flask import Blueprint, render_template
from flask import current_app
from inscription.extensions import db


page = Blueprint('page', __name__, template_folder='templates')



@page.route('/')
def home():
  cur = db.connection.cursor()
  cur.execute('''SELECT user, host FROM mysql.user''')
  rv = cur.fetchall()
  result = rv
  #return str(rv)
  return render_template('page/home.html', result = result)