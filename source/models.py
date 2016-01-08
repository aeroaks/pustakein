from source import app, db
import re

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author_sort = db.Column(db.Text)

    def __repr__(self):
        # how to print objects of this class
        return '<Title %r, Author %r>' % (self.title, self.author_sort)
        
    @staticmethod
    def make_valid_requests(string):
        return re.sub('[^a-zA-Z]', '', string)

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    sort = db.Column(db.Text)

    def __repr__(self):
        return '<Author %r>' % (self.name)

class Books_Authors_Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.Integer)
    author = db.Column(db.Integer)



