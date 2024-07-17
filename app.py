from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from src.config.private_info import test_new_db
from src.app.db_operations import query_metrics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = test_new_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# API Routes for JS

# # Depending on how we display data and serve data, might need to change the method.
# @app.route('/butcher/product_data/<product_name>', methods=['GET'])
# def get_product_data(product_name):
#     pass
# # Depending on how we display data and serve data, might need to change the method.
# @app.route('/butcher/all_data', methods=['GET'])
# def get_all_data():
#     pass

# HTML Routes
@app.route('/') # Can we put /butcher? 
def home():
    spec_df = query_metrics(db.engine, "10 oz  Sirloin A" )
    return jsonify(spec_df.to_dict(orient='records'))
    # return render_template('index.html') #Home

# @app.route('butcher/overview')
# def metrics():
#     return render_template('josh.html') #overview

# @app.route('butcher/product')
# def products():
#     return render_template('product_specific.html') #height

if __name__ == '__main__':
    app.run()