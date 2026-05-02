import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # This line is the key: It gets the port from Railway
    port = int(os.environ.get('PORT', 5000))
    # host='0.0.0.0' is required for the internet to see your app
    app.run(host='0.0.0.0', port=port)
