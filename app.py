from flask import Flask, request, render_template, session, url_for, redirect
import random
import string

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
SPORT_HOBBIES = ['football', 'volleyball', 'ballet']
TV_SHOW_HOBBIES = ['pokemon', 'yugi-oh', 'marko', 'sheshtus']
MUSIC_HOBBIES = ['guitar', 'saxophone', 'drums']
CATEGORY_DICT = {'sport': SPORT_HOBBIES, 'tv': TV_SHOW_HOBBIES, 'music': MUSIC_HOBBIES}
CHEN_HOBBIES = SPORT_HOBBIES + TV_SHOW_HOBBIES + MUSIC_HOBBIES

users = {'user1': {'name': 'Roni', 'email': 'Roni@gmail.com'},
         'user2': {'name': 'Ran', 'email': 'Ran@gmail.com'},
         'user3': {'name': 'Tom', 'email': 'Tom@gmail.com'},
         'user4': {'name': 'Chen', 'email': 'Chen@gmail.com'},
         'user5': {'name': 'Mimi', 'email': 'Mimi@gmail.com'}}


@app.route('/assignment9', methods=["POST", "GET"])
def ex9():
    if request.method == "POST":
        session["nickname"] = request.form.get("nickname")
        return redirect(url_for('ex9'))
    else:
        query_parameters = request.args
        nickname = session.get('nickname')
        if 'name' in query_parameters:
            name = query_parameters['name']
            if name == '':
                return render_template('assignment9.html', users=list(users.values()), nickname=nickname)
            else:
                filtered_users = []
                for user_data in users.values():
                    if user_data['name'] == name:
                        filtered_users.append(user_data)
                return render_template('assignment9.html', users=filtered_users, nickname=nickname)
        return render_template('assignment9.html', nickname=nickname)


@app.route('/')
def home():
    nickname = session.get('nickname')
    return render_template('exercise2.html', nickname=nickname)


@app.route('/cv-grid')
def cv_grid():
    nickname = session.get('nickname')
    return render_template('CVgrid.html', nickname=nickname)


@app.route('/cv')
def cv():
    nickname = session.get('nickname')
    return render_template('cv.html', nickname=nickname)


@app.route('/form')
def form():
    nickname = session.get('nickname')
    return render_template('forms.html', nickname=nickname)


@app.route('/assignment8')
def hobbies():
    nickname = session.get('nickname')
    category = request.args.get('category')
    hobbies_list = CATEGORY_DICT.get(category)
    if hobbies_list:
        return render_template('assignment8.html', hobbies_list=hobbies_list, category=category, nickname=nickname)
    else:
        return render_template('assignment8.html', nickname=nickname)


@app.route('/hobbies/compare')
def compare_hobbies():
    nickname = session.get('nickname')
    args = request.args
    user_hobbies = args.get('user-hobbies', []) if args.get('user-hobbies') else []
    if user_hobbies:
        user_hobbies = [hobie.strip().lower() for hobie in user_hobbies.split(',')]
    only_user_hobbies = [hobie for hobie in user_hobbies if hobie not in CHEN_HOBBIES]
    only_chen_hobbies = [hobie for hobie in CHEN_HOBBIES if hobie not in user_hobbies]
    both_hobbies = [hobie for hobie in user_hobbies if hobie in CHEN_HOBBIES]
    last_name = args.get('lname', '')
    first_name = args.get('fname', '')
    if first_name or last_name:
        user = {'last_name': last_name, 'first_name': first_name}
        return render_template('compare-hobbies.html', user=user, only_user_hobbies=only_user_hobbies,
                               only_chen_hobbies=only_chen_hobbies, both_hobbies=both_hobbies, nickname=nickname)
    else:
        return render_template('compare-hobbies.html', only_user_hobbies=only_user_hobbies,
                               only_chen_hobbies=only_chen_hobbies, both_hobbies=both_hobbies, nickname=nickname)


@app.route('/logout')
def logout():
    session['nickname'] = None
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
