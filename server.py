"""
API Server
"""

# Bottle
from bottle import run, get

import config
from bottle_notes import app

if __name__ == '__main__':  
    run(app,
        reloader=True, 
        host=config.HOST, 
        port=config.PORT
    )