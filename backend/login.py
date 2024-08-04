from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pymysql.cursors

app = Flask(__name__)
CORS(app)

# Configure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://madedech_marketing:Wacha00fala@serv3.shujaahost.co.ke/madedech_marketing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Database Connection Test</title>
          </head>
          <body>
            <div class="container">
              <h1>Database Connection Test</h1>
              <button onclick="testConnection()">Test Database Connection</button>
              <p id="result"></p>
            </div>
            <script>
              async function testConnection() {
                const response = await fetch('/test-connection');
                const data = await response.json();
                document.getElementById('result').innerText = data.message;
              }
            </script>
          </body>
        </html>
    ''')

@app.route('/test-connection', methods=['GET'])
def test_connection():
    try:
        # Test PyMySQL connection
        connection = pymysql.connect(host='serv3.shujaahost.co.ke',
                                     user='madedech_marketing',
                                     password='Wacha00fala',
                                     db='madedech_marketing',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        connection.close()

        # If connection is successful
        return jsonify({'message': 'Connection successful!'}), 200
    except Exception as e:
        # If connection fails
        return jsonify({'message': f'Connection failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
