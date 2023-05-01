from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DDL, text
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/midterm?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(db)


# 定义模型
class Department(db.Model):
    __tablename__ = 'departments'
    dept_no = db.Column(db.String(4), primary_key=True)
    dept_name = db.Column(db.String(40), nullable=False, unique=True)

    def to_dict(self):
        return {
            'dept_no': self.dept_no,
            'dept_name': self.dept_name
        }


class Employee(db.Model):
    __tablename__ = 'employees'
    emp_no = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.String(14), nullable=False, index=True)
    last_name = db.Column(db.String(16), nullable=False)
    gender = db.Column(db.Enum('M', 'F'), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'birth_date': self.birth_date,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'hire_date': self.hire_date
        }


class DeptEmp(db.Model):
    __tablename__ = 'dept_emp'
    emp_no = db.Column(db.Integer, db.ForeignKey("employees.emp_no", ondelete='CASCADE'),
                       primary_key=True)
    dept_no = db.Column(db.String(4), db.ForeignKey("departments.dept_no", ondelete='CASCADE'),
                        primary_key=True, index=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'dept_no': self.dept_no,
            'from_date': self.from_date,
            'to_date': self.to_date
        }


class DeptManager(db.Model):
    __tablename__ = 'dept_manager'
    emp_no = db.Column(db.Integer, db.ForeignKey("employees.emp_no", ondelete='CASCADE'), primary_key=True)
    dept_no = db.Column(db.String(4), db.ForeignKey("departments.dept_no", ondelete='CASCADE'),
                        primary_key=True, index=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'dept_no': self.dept_no,
            'from_date': self.from_date,
            'to_date': self.to_date
        }


class Title(db.Model):
    __tablename__ = 'titles'
    emp_no = db.Column(db.Integer, db.ForeignKey("employees.emp_no", ondelete='CASCADE'), primary_key=True)
    title = db.Column(db.String(50), primary_key=True)
    from_date = db.Column(db.Date, primary_key=True)
    to_date = db.Column(db.Date, nullable=True)

    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'title': self.title,
            'from_date': self.from_date,
            'to_date': self.to_date
        }


class DMT(db.Model):
    __tablename__ = 'dept_manager_title'
    emp_no = db.Column(db.Integer, primary_key=True)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=True)

    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'from_date': self.from_date,
            'to_date': self.to_date
        }


trigger_create_insert_dmt = DDL(
    """
    CREATE TRIGGER trigger_insert_dmt
    AFTER INSERT ON dept_manager
    FOR EACH ROW 
    BEGIN 
        INSERT INTO dept_manager_title(emp_no, from_date, to_date) VALUES (NEW.emp_no, NEW.from_date, NEW.to_date); 
    END
    """
)

trigger_create_delete_dmt = DDL(
    """
    CREATE TRIGGER trigger_delete_dmt
    AFTER DELETE ON dept_manager
    FOR EACH ROW 
    BEGIN 
        DELETE FROM dept_manager_title WHERE (emp_no, from_date, to_date)=(OLD.emp_no, OLD.from_date, OLD.to_date); 
    END
    """
)

with app.app_context():
    db.create_all()
    # db.session.execute(trigger_create_insert_dmt)
    # db.session.execute(trigger_create_delete_dmt)


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
    p_key = []
    for key in data:
        if key.endswith('_no'):
            p_key.append(key)
    update_values = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
    where_clause = "WHERE " + " AND ".join([f"{key} = '{value}'" for key, value in data.items() if key in p_key])
    db.session.execute(text(f'UPDATE {table_name} SET {update_values} {where_clause}'))
    db.session.commit()
    return jsonify({'message': 'hihihi'}), 200


# 删除数据
@app.route('/api/v1/<table_name>/<path:no>', methods=['DELETE'])
def delete_data(table_name, no):
    if table_name == 'dept_emp':
        emp_no, dept_no = no.split('/')
        print(emp_no, dept_no)
        db.session.execute(text(f'DELETE FROM {table_name} WHERE emp_no={emp_no} AND dept_no={dept_no}'))
    elif table_name == 'departments':
        db.session.execute(text(f'DELETE FROM {table_name} WHERE dept_no={no};'))
    else:
        db.session.execute(text(f'DELETE FROM {table_name} WHERE emp_no={no};'))
    db.session.commit()
    return jsonify({'message': 'hihihihi'}), 204


# 查询数据
@app.route('/api/v1/<path:loc>', methods=['GET'])
def select_data(loc):
    lenl = len(loc.split('/'))
    if lenl == 3:
        table_name, emp_no, dept_no = loc.split('/')
        print(emp_no, dept_no)
        query = text(f'SELECT * FROM {table_name} WHERE emp_no={emp_no} AND dept_no={dept_no}')
    elif lenl == 2:
        table_name, no = loc.split('/')
        if table_name == 'departments':
            query = text(f'SELECT * FROM {table_name} WHERE dept_no={no};')
        else:
            query = text(f'SELECT * FROM {table_name} WHERE emp_no={no};')
    else:
        # print(request)
        condition = request.args
        key = list(condition.keys())[0]
        value = condition.get(key)
        table_name = loc
        query = text(f'SELECT * FROM {table_name} WHERE {key}={value};')
    result = db.session.execute(query)
    rows = [dict(row) for row in result]
    return jsonify({'rows': 1}), 200


if __name__ == '__main__':
    app.run(debug=True)
# f'{len(rows)} rows inserted into {table_name} successfully'