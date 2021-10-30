import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/items/<item_id>', methods=['GET', 'POST'])
def items(item_id):
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        return jsonify(create_order(item_id))
    else:
        raise Exception('Unsupported HTTP request type.')

if __name__ == '__main__':
    app.run()
