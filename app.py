import random
import os

from flask import Flask, jsonify, request
from images import images


app = Flask(__name__)
app.debug = os.environ.get('DEBUG', False)

# The number of sad-soo's we drop by default.
DEFAULT_BOMB = 3


@app.route('/')
def index():
    d = {
        'resources': {
            '/random': 'A random picture of a sad-soo.',
            '/bomb(?count=5)': 'Bomb sad-soo\'s. Optionally, set how many you\'d like to bomb.',
            '/count': 'The number of sad-soo\'s we have.'
        },
        'source': 'https://github.com/pearkes/sad-soo',
        'thanks': 'https://github.com/bryanveloso',
        'forked': 'https://github.com/bryanveloso/aidoru',
    }
    return jsonify(d)


@app.route('/random')
def random_sad_soo():
    sad_soo = random.choice(images)
    return jsonify({'sad_soo': sad_soo})


@app.route('/bomb')
def bomb_sad_soos():
    count = request.args.get('count', DEFAULT_BOMB)
    sad_soos = random.sample(images, int(count))
    return jsonify({'sad_soos': sad_soos})


@app.route('/count')
def count_sad_soos():
    count = len(images)
    return jsonify({'count': count})


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
