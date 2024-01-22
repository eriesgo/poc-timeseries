import os
from flask import Flask, abort, jsonify

from hexagonal import get_symbols_use_case, get_symbol_details_use_case
from infrastructure import get_symbols_repository, get_symbol_details_repository


app = Flask(__name__)

# Retrieve environment variables
flask_run_host = os.environ.get("FLASK_RUN_HOST", "localhost")
flask_run_port = int(os.environ.get("FLASK_RUN_PORT", 5001))

# Endpoint to retrieve symbols from the "company" table
@app.route('/symbols', methods=['GET'])
def get_symbols():
    try:
        symbols = get_symbols_use_case(get_symbols_repository)
        return jsonify(symbols)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/symbols/<string:symbol>', methods=['GET'])
def get_symbol_details(symbol: str):
    try:
        details = get_symbol_details_use_case(symbol, get_symbol_details_repository)
        if details:
            return jsonify(details)
        else:
            abort(404)  # Symbol not found, return HTTP 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(host=flask_run_host, port=flask_run_port)
