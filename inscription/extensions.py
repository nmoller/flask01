from flask_mysqldb import MySQL
from flask_debugtoolbar import DebugToolbarExtension


debug_toolbar = DebugToolbarExtension()
db = MySQL()