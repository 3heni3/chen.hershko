from flask import Flask, request, render_template

app = Flask(__name__)
SPORT_HOBBIES = ['football', 'volleyball', 'ballet']
TV_SHOW_HOBBIES = ['pokemon', 'yugi-oh', 'marko', 'sheshtus']
MUSIC_HOBBIES = ['guitar', 'saxophone', 'drums']
CATEGORY_DICT = {'sport': SPORT_HOBBIES, 'tv': TV_SHOW_HOBBIES, 'music': MUSIC_HOBBIES}
CHEN_HOBBIES = SPORT_HOBBIES + TV_SHOW_HOBBIES + MUSIC_HOBBIES


@app.route('/')
def home():
    return render_template('exercise2.html')


@app.route('/cv-grid')
def cv_grid():
    return render_template('CVgrid.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


@app.route('/form')
def form():
    return render_template('forms.html')


@app.route('/assignment8')
def hobbies():
    category = request.args.get('category')
    hobbies_list = CATEGORY_DICT.get(category)
    if hobbies_list:
        return render_template('assignment8.html', hobbies_list=hobbies_list, category=category)
    else:
        return render_template('assignment8.html')


@app.route('/hobbies/compare')
def compare_hobbies():
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
                               only_chen_hobbies=only_chen_hobbies, both_hobbies=both_hobbies)
    else:
        return render_template('compare-hobbies.html', only_user_hobbies=only_user_hobbies,
                               only_chen_hobbies=only_chen_hobbies, both_hobbies=both_hobbies)


if __name__ == '__main__':
    app.run()
