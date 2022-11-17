from flask import Flask, request, jsonify, render_template
from utils.twitter import Twitter

app = Flask(__name__)
app.config.from_pyfile('config.py')

# tweepy credentials
tw_apikey = app.config['TW_API_KEY']
tw_apikey_secret = app.config['TW_API_KEY_SECRET']
tw_access_token = app.config['TW_ACCESS_TOKEN']
tw_access_token_secret = app.config['TW_ACCESS_TOKEN_SECRET']


@app.route('/')
def temp_search():
    return render_template('result.html')


@app.route('/get-tweets', methods=['GET', 'POST'])
def temp_sentiment():
    keyword = request.form["search[value]"]
    rows_per_page = int(request.form['length'])
    print(rows_per_page)
    tweets = []
    if len(keyword.strip()) > 0:
        client = Twitter(tw_apikey, tw_apikey_secret, tw_access_token, tw_access_token_secret)
        tweets = client.get_tweets(keyword, rows_per_page)
    return jsonify({"data": tweets})


if __name__ == '__main__':
    try:
        app.run()
    except Exception as err:
        print(str(err))
