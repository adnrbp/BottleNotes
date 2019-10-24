# -*- coding: utf-8 -*-

# bottle
import json
from bottle import request

from bottle_notes import app
from bottle_notes.notes.models import Note

@app.route('/api/v1/notes', method='GET')
def getAll():
    """List all created notes."""
    notes = []
    for note in Note.select():
        notes.append({
            "title":note.title,
            "description":note.description
            })
    return {'data': notes}

@app.route('/api/v1/notes', method='POST')
def addNote():
    """Create a new note."""
    result = {}
    data =request.json
    created_note = Note.create(**data)
    if created_note.save() :
        result = {
            'result': "OK",
            'data': data 
        }
    else:
        result = {
            'result': "error"
        }
    return result

