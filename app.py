from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from src.config import test_new_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your-database-uri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# API Routes for JS

# Depending on how we display data and serve data, might need to change the method.
@app.route('/api/product_data/<product_name>', methods=['GET'])
def get_product_data(product_name):
    pass
# Depending on how we display data and serve data, might need to change the method.
@app.route('/api/all_data', methods=['GET'])
def get_all_data():
    pass

# HTML Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/all_data')
def metrics():
    return render_template('templates/dashboard_or_whatevernamewewant.html')

@app.route('/product_specific')
def products():
    return render_template('product_specific.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()