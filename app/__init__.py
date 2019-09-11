from flask import Flask


app = Flask(__name__)

# workaround to circular imports, a common problem with Flask applications
from app import routes
