import json
from datetime import datetime

from flask import render_template, jsonify
from flask import request, Response

from app import app
from models import Identifier, create_dessert
from sqlalchemy import create_engine

import pandas as pd

# return Response(json.dumps(t), mimetype='application/json')

@app.route('/', methods=['GET', 'POST'])
def index():

    desserts = Identifier.query.all()

    if request.method == 'POST':
        dessert_name = request.form.get('identifier')
        desserts = Identifier.query.filter_by(identifier=dessert_name)

    return render_template('index.html', desserts=desserts)


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'GET':
        return render_template('add.html')

    # Because we 'returned' for a 'GET', if we get to this next bit, we must
    # have received a POST

    # Get the incoming data from the request.form dictionary.
    # The values on the right, inside get(), correspond to the 'name'
    # values in the HTML form that was submitted.

    dessert_name = request.form.get('name_field')
    dessert_price = request.form.get('price_field')
    dessert_cals = request.form.get('cals_field')
    dessert_website = request.form.get('website_field')
    dessert_status = request.form.get('status_field')
    dessert_introduce = request.form.get('introduce_field')
    dessert_time = request.form.get('time_field')
    dessert_create_time = str(datetime.now())
    dessert_industry = request.form.get('industry_field')

    dessert_info = '{"website": %s, "status": %s}' % (dessert_website, dessert_status)

    dessert = create_dessert(dessert_name, dessert_price, dessert_info)
    return render_template('add.html', dessert=dessert)


@app.route('/api', methods=['GET', "POST"])
def api():
    # http://127.0.0.1:5000/api?identifier=NA.0/199
    # sql = 'select * from identifier where '

    # identifiers = Identifier.query.all()
    result_id = []
    result_identifier = []
    result_price = []
    result_info= []

    result = {'data': []}
    if request.method == 'GET':
        identifier_query = request.args.get('identifier')
        # engine = create_engine('sqlite:///D:\\Users\\HP\\Documents\\repo\\flask-sqlalchemy-example\\identifiers.db')
        # sql = "select * from identifier where identifier='%s'" % identifier_query
        # query_df = pd.read_sql_query(sql, engine)
        # identifiers = Identifier.query.filter_by(identifier=identifier_query)
        identifiers = Identifier.query.filter_by(identifier=identifier_query).all()

    for identifier in identifiers:
        result_id.append(identifier.id)
        result_identifier.append(identifier.identifier)
        result_price.append(identifier.price)
        result_info.append(identifier.info)

    for i in range(len(result_id)):
        result_t = {
            'status_code': 0,
            'identifier': result_identifier[i],
            'price': result_price[i],
            'info': result_info[i],
        }
        result['data'].append(result_t)

    # query_result = {
    #     'status_code': 0,
    #     'data': json.loads(query_df.to_json(orient='index'))
    # }

    # result = identifiers
    # for identifier in identifiers:
        # print "identifier="
        # print identifier
        # result.append(identifier.to_json)
        # temp = identifier.to_json
        # print temp
        # result.append(temp)
        # print "12"
        # print "result="

        # return jsonify(result, id=g.user.id)

    # return jsonify(identifiers)
    # return json.dumps(identifiers, ensure_ascii=False)
        # return result
    # identifiers = []
    # return jsonify(query_result) ############## OK
    return jsonify(result)
    # return Response(json.dumps(identifiers), mimetype='application/json')