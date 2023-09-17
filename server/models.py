from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Must enter a name")
        return name

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number)!= 10:
            raise ValueError("must be 10 digits")
        return phone_number
    
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, content):
        if (len(content)<250):
            raise ValueError("Must have >=250 characters")
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if (len(summary)>=250):
            raise ValueError("Must have >=250 characters")
        return summary

    @validates('category')
    def validate_category(self, key, category):
        allowed = ['Fiction', 'Non-Fiction']
        if category not in allowed:
            raise ValueError("Invalid category")
        return category
    
    @validates('title')
    def validate_title(self, key, title):
        allowed = ["Won't Believe", "Secret", "Top", "Guess"]
        if title not in allowed:
            raise ValueError("Title not clickbait-y")
        return title

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
