from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/ex0/')
def index():
    return app.send_static_file('index.html')

app.run(port=8080, debug=True)
