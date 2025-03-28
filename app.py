# from __init__ import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({
#         'message': 'Welcome to Ceylonmine Backend!'
#     })

#     return app

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))  # Use PORT if set, otherwise default to 5000
#     app.run(host="0.0.0.0", port=port)

import os
from flask import Flask, jsonify
from __init__ import create_app

app = create_app()

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Ceylonmine Backend!'
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT if set, otherwise default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)




    