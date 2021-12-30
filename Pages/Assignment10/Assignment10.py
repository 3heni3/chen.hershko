from flask import Blueprint, render_template, request, url_for, redirect, flash
from interact_with_DB import interact_db

Assignment10 = Blueprint(
    'Assignment10',
    __name__,
    static_folder='static',
    static_url_path='/Pages/Assignment10',
    template_folder='templates'
)


@Assignment10.route('/assignment10')
def index():
    query = f'''
    SELECT * from users
    '''
    users = interact_db(query=query, query_type='fetch')
    return render_template('Assignment10.html', users=users)


@Assignment10.route('/assignment10/update_user', methods=['POST'])
def update_user():
    parameters = request.form
    email = parameters['email']
    new_name = parameters['new_name']
    new_email = parameters.get('new_email') or email
    query = f'''
    UPDATE users
    SET 
        email = '{new_email}',
        name = '{new_name}'
    WHERE
        email = '{email}';
    '''
    flash('User was updated!', 'info')
    interact_db(query=query, query_type='commit')


@Assignment10.route('/assignment10/delete_user', methods=['POST'])
def delete_user():
    parameters = request.form
    username = parameters['username']
    query = f'''
    DELETE FROM users WHERE name='{username}';
    '''
    interact_db(query=query, query_type='commit')
    flash('User was deleted!', 'info')
    return redirect(url_for('Assignment10.index'))


@Assignment10.route('/assignment10/insert_user', methods=['POST'])
def insert_user():
    parameters = request.form
    new_name = parameters['new_name']
    new_email = parameters['new_email']
    query = f'''
    INSERT INTO users
    VALUES ('{new_name}', '{new_email}');
    '''
    interact_db(query=query, query_type='commit')
    flash('User was inserted!', 'info')
    return redirect(url_for('Assignment10.index'))
