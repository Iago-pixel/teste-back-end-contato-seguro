from app.configs.database import db

users_companies = db.Table('users_companies',
                           db.Column('id', db.Integer, primary_key=True),
                           db.Column('user_id', db.Integer,
                                     db.ForeignKey('users.id')),
                           db.Column('company_id', db.Integer,
                                     db.ForeignKey('companies.id'))
                           )
