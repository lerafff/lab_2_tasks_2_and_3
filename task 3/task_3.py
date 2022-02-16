'''Lab 2.3'''

from geopy.geocoders import Nominatim
from folium import FeatureGroup, Map, Marker, Icon, LayerControl
from flask import Flask, render_template, url_for, request
import requests


def get_info(user_name):
    '''
    Gets info about the user using twitter API and my bearer key
    '''
    key = 'AAAAAAAAAAAAAAAAAAAAAHD2ZAEAAAAAN9Y2q7ytC8NoBO%2BfGm7\
jje6ACS0%3DyYnsbmV1kCC3dLX34tymK4aObVK3mCrIurxcUtZgOrVx4T4drx'
    headers = {'Authorization': f'Bearer {key}'}
    params = {'screen_name': user_name, 'count': 200}

    response = requests.get('https://api.twitter.com/1.1/friends/list.json',
                            headers=headers,
                            params=params)
    return response.json()


def read_file(text_json):
    '''
    Reads a text returned from twitter api and returns a
    dictionary with all necessary information
    '''
    temporary_dict = {}
    all_info = []
    for elem in text_json.get('users'):
        name_of_person = elem.get('screen_name')
        location = elem.get('location')
        temporary_dict.setdefault('user', name_of_person)
        if location != '':
            temporary_dict.setdefault('location', location)
        else:
            continue
        all_info.append(temporary_dict)
        temporary_dict = {}
    return all_info


def find_location(all_info):
    '''
    Finds locations of the places
    '''
    copy_to_add_loc = all_info
    flag = True
    for indexx in range(len(all_info)):
        loc = all_info[indexx].get('location')
        try:
            location = Nominatim(user_agent='app_name').geocode(loc)
            if location is not None:
                coord = (location.latitude, location.longitude)
                copy_to_add_loc[indexx].setdefault('coordinates', coord)
            else:
                if loc.find(',') == -1:
                    continue
                else:
                    while flag:
                        loc_copy = loc
                        indexx = loc_copy.find(',')
                        loc_copy = loc_copy[(indexx + 2):]
                        location1 = Nominatim(
                                    user_agent='app_name').geocode(loc_copy)
                        if location1 is not None:
                            coord_2 = (location1.lattitude,
                                       location1.longtitude)
                            copy_to_add_loc[indexx].setdefault(
                                        'coordinates', coord_2)
                            flag = False
        except:
            continue
    flag = True
    return copy_to_add_loc


def make_map(copy_to_add_loc):
    '''
    Creates a map with final markers
    '''
    main_map = Map(location=[20, 0], zoom_start=2, control_scale=True)
    markers_gr = FeatureGroup(name='Group')

    main_map.add_child(markers_gr)
    for one_dict in range(len(copy_to_add_loc)):
        try:
            lattitude, longtitude =
            copy_to_add_loc[one_dict].get('coordinates')
            name = copy_to_add_loc[one_dict].get('user')
            markers_gr.add_child(Marker(location=[lattitude, longtitude],
                popup=name, icon=Icon(color='darkpurple')))
        except TypeError:
            continue
    main_map.add_child(LayerControl())
    main_map.save('templates/mapp.html')


def all_func(user_name):
    '''
    A function that helps everything to work properly
    '''
    text_json = get_info(user_name)
    all_info = read_file(text_json)
    copy_to_add_loc = find_location(all_info)

    make_map(copy_to_add_loc)

app = Flask(__name__)


@app.route('/')
def display_the_main_page():
    '''
    The function makes a site
    '''
    return render_template('index.html')


@app.route('/result_version_alpha_0.2', methods=['POST'])
def eenter():
    '''
    The function gets user name and makes a map
    '''
    user_name = request.form['username']
    all_func(user_name)
    return render_template('mapp.html')

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
