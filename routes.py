from flask import Flask, render_template, request, url_for
from facebook import get_user_from_cookie, GraphAPI
import datetime, threading, time

app = Flask(__name__)


@app.route('/choose_friends')
def hello():
    access_token = 'access_token_here'
    graph = GraphAPI(access_token)
    friends = graph.get_object('me/friends')
    friendsList = []
    me_picture = graph.get_object('me/picture')['url']
    me_name = graph.get_object('me')['name']
    for friend in friends['data']:
        friend_picture = graph.get_object(friend['id']+'/picture')['url']
        friendsList.append({'name': friend['name'],
                            'id': friend['id'],
                            'profile_thumbnail': friend_picture})
    return render_template('choose_friends.html',
                           me_name=me_name,
                           me_picture=me_picture,
                           friendsList=friendsList)


@app.route('/', methods=['POST', 'GET'])
def index():
    if not request.args.get('access_token'):
        message = 'No access token'
    else:
        message = request.args.get('access_token')
    return render_template('index.html', message=message)


# def periodic_func():
#     print(time.ctime())
#     threading.Timer(1, periodic_func).start()
# periodic_func()

if __name__ == '__main__':

    app.debug = True
    app.run()
