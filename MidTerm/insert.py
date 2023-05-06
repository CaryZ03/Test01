from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DDL, text
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/midterm?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)


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


trigger_create_update_dmt = DDL(
    """
    CREATE TRIGGER trigger_UPDATE_dmt
    AFTER UPDATE ON dept_manager
    FOR EACH ROW 
    BEGIN 
        UPDATE dept_manager_title SET from_date=NEW.from_date, to_date=NEW.to_date WHERE emp_no=NEW.emp_no; 
    END
    """
)


with app.app_context():
    db.create_all()
    db.session.execute(trigger_create_insert_dmt)
    db.session.execute(trigger_create_delete_dmt)
    db.session.execute(trigger_create_update_dmt)


def upload(table_name):
    with app.app_context():
        path = 'dataset/' + table_name + '.csv'
        with open(path, 'r') as file:
            # 使用csv模块解析上传的CSV文件
            reader = csv.reader(file)
            headers = ', '.join(next(reader))  # 跳过第一行表头
            for row in reader:
                values = ', '.join([f"'{value}'" for value in row])
                # print(values)
                db.session.execute(text(f'INSERT INTO {table_name} ({headers}) VALUES ({values});'))
            db.session.commit()


if __name__ == '__main__':
    upload('departments')
    upload('employees')
    upload('dept_emp')
    upload('dept_manager')
    upload('titles')
