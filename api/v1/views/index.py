#!/usr/bin/python3
'''Contains the index view for the API.'''

from api.v1.views import app_views
from models import storage
from flask import jsonify

@app_views.route('/status')
def status():
    '''Gets the status of the API.
    '''
    return jsonify({'status': 'OK'})


@app_views.route('stats', methods=['GET'])
def get_stats():
    '''Gets the number of objects for each type.
    '''
    classes = {
        'Amenity': storage.count('Amenity'),
        'City': storage.count('City'),
        'Place': storage.count('Place'),
        'Review': storage.count('Review'),
        'State': storage.count('State'),
        'User': storage.count('User')
    }
    return jsonify(classes)
