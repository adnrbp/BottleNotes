"""
API Server
"""

# Bottle
from bottle import run, get

import config

notes = [{'title': 'Example Note1', 'description': 'Just description'},
        {'title': 'Example Note2', 'description': 'Just description2'},
        {'title': 'Example Note3', 'description': 'Just description4'}]

@get('/api/v1/notes')
def getAll():
    return {'notes': notes}

if __name__ == '__main__':  
    run(reloader=True, 
        host=config.HOST, 
        port=config.PORT
    )