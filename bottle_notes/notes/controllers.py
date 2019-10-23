# -*- coding: utf-8 -*-
from bottle_notes import app
from bottle import request


notes = [{'title': 'Example Note5', 'description': 'Just description'},
        {'title': 'Example Note2', 'description': 'Just description2'},
        {'title': 'Example Note3', 'description': 'Just description4'}]

@app.route('/api/v1/notes', method='GET')
def getAll():
    return {'notes': notes}