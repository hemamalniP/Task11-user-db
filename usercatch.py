from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:user10@localhost:5432/empdb'
app.debug=True
db = SQLAlchemy(app)
class usr(db.Model):
    __tablename__='user'
    user_id = db.Column('id', db.Integer, primary_key=True)
    user_name = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(50),nullable=False)
    company_name = db.Column(db.String(200),nullable=False)
    phone_number = db.Column(db.Integer,nullable=False)
    status = db.Column(db.Boolean,default=1)
    def __init__(self,user_id,user_name,password,company_name,phone_number,status):
        self.user_id=user_id
        self.user_name=user_name
        self.password=password
        self.company_name=company_name
        self.phone_number=phone_number
        self.status=status
@app.route('/us',methods=['POST'])
def emrec():
    user_id = request.args.get('user_id')
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    company_name = request.args.get('company_name')
    phone_number = request.args.get('phone_number')
    status = request.args.get('status')
    ipt = request.get_json()
    print(ipt)
    det = usr(user_id=ipt['user_id'],user_name=ipt['user_name'],password=ipt['password'],company_name=ipt['company_name'],phone_number=ipt['phone_number'],status=ipt['status'])
    db.session.add(det)

    try:
        db.session.add(det)
        db.session.commit()
    except IntegrityError:
        return ("invalid input")
    else:
        return ("successfully inserted")

if __name__ == '__main__':
    app.run(debug=True)