# # from __init__ import create_app

# # app = create_app()

# # if __name__ == '__main__':
# #     app.run(debug=True)


# # render
# # app.py (main file)
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello from Flask on Render!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=10000)

# from __init__ import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT if set, otherwise default to 5000
    app.run(host="0.0.0.0", port=port)