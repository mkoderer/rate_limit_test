import random
from app import app
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/')
@app.route('/index')
@limiter.limit("45 per second")
def index():
     return "proceed"
