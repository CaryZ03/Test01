from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DDL, text
import json
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/midterm?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)


# 插入数据
@app.route('/api/v1/<table_name>', methods=['POST'])
def insert_data(table_name):
    data = request.json
    rows = data['rows']
    for row in rows:
        keys = ', '.join(row.keys())
        values = ', '.join([f"'{value}'" for value in row.values()])
        db.session.execute(text(f'INSERT INTO {table_name}({keys}) VALUES({values})'))
    db.session.commit()
    return jsonify({'message': 'hihi'}), 201


# 更新数据
@app.route('/api/v1/<table_name>', methods=['PUT'])
def update_data(table_name):
    data = request.json
    update_values = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
    match table_name:
        case 'departments':
            dept_no = data['dept_no']
            where_clause = f'dept_no = "{dept_no}"'
        case 'employees':
            emp_no = data['emp_no']
            where_clause = f'emp_no = "{emp_no}"'
        case 'dept_emp' | 'dept_manager':
            emp_no = data['emp_no']
            dept_no = data['dept_no']
            where_clause = f'emp_no = "{emp_no}" AND dept_no = "{dept_no}"'
        case 'titles':
            emp_no = data['emp_no']
            dept_no = data['dept_no']
            from_date = data['from_date']
            where_clause = f'emp_no = "{emp_no}" AND dept_no = "{dept_no}" AND from_date = "{from_date}"'
    db.session.execute(text(f'UPDATE {table_name} SET {update_values} WHERE {where_clause};'))
    db.session.commit()
    return jsonify({'message': 'hihihi'}), 200


# 删除数据
@app.route('/api/v1/<table_name>/<path:no>', methods=['DELETE'])
def delete_data(table_name, no):
    match table_name:
        case 'departments':
            where_clause = f'dept_no = "{no}"'
        case 'employees':
            where_clause = f'emp_no = "{no}"'
        case 'dept_emp' | 'dept_manager':
            emp_no, dept_no = no.split('/')
            where_clause = f'emp_no = "{emp_no}" AND dept_no = "{dept_no}"'
        case 'titles':
            emp_no, dept_no, from_date = no.split('/')
            where_clause = f'emp_no = "{emp_no}" AND dept_no = "{dept_no}" AND from_date = "{from_date}"'
    db.session.execute(text(f'DELETE FROM {table_name} WHERE {where_clause};'))
    db.session.commit()
    return jsonify({'message': 'hihihihi'}), 204


# 查询数据
@app.route('/api/v1/<table_name>/<path:no>', methods=['GET'])
def select_data_with_pri(table_name, no):
    match table_name:
        case 'departments':
            where_clause = f'dept_no = "{no}"'
        case 'employees':
            where_clause = f'emp_no = "{no}"'
        case 'dept_emp' | 'dept_manager':
            emp_no, dept_no = no.split('/')
            where_clause = f'emp_no = "{emp_no}" AND dept_no = "{dept_no}"'
        case 'titles':
            emp_no, dept_no, from_date = no.split('/')
            where_clause = f'emp_no = "{emp_no}" AND dept_no = "{dept_no}" AND from_date = "{from_date}"'
    result = db.session.execute(text(f'SELECT * FROM {table_name} WHERE {where_clause};'))
    rows = [dict(zip(result.keys(), row)) for row in result.fetchall()]
    return jsonify({'rows': rows}), 200


# 条件查询数据
@app.route('/api/v1/<table_name>', methods=['GET'])
def select_data_with_cond(table_name):
    condition = request.args
    if condition:
        key = list(condition.keys())[0]
        value = condition.get(key)
        query = text(f'SELECT * FROM {table_name} WHERE {key}="{value}";')
    else:
        query = text(f'SELECT * FROM {table_name};')
    result = db.session.execute(query)
    rows = [dict(zip(result.keys(), row)) for row in result.fetchall()]
    return jsonify({'rows': rows}), 200


if __name__ == '__main__':
    app.run(debug=False)