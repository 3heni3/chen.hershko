from flask import Blueprint, Response, request, render_template
from interact_with_DB import interact_db
import json
import requests
Assignment11 = Blueprint(
    'Assignment11',
    __name__,
    static_folder='static',
    static_url_path='/Pages/Assignment11',
    template_folder='templates'
)


@Assignment11.route('/assignment11/users')
def index():
    query = f'''
    SELECT * from users
    '''
    # Returns as a JSON because dictionary is True
    users = interact_db(query=query, query_type='fetch', named_tuple=None, dictionary=True)
    return Response(json.dumps(users), mimetype='application/json')

@Assignment11.route('/assignment11/outer_source')
def outer_source():
    args = request.args
    x = args.get('x-py')
    # Second form was filled, python requests
    if x:
        response = requests.get(f'https://reqres.in/api/users/{x}')
        try:
            x = response.json()['data']
        except Exception:
            x = 'Could not retrieve the user data'
    return render_template('Assignment11.html', user_data=x)
