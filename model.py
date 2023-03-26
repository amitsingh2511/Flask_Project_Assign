from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class SchoolModel(db.Model):
    __tablename__ = 'TA'
    id = db.Column(db.Integer, primary_key=True)
    native_english_speaker = db.Column(db.String(250), nullable=False)
    course_instructor = db.Column(db.String(250))
    course = db.Column(db.String(250))
    semester = db.Column(db.Integer)
    class_size = db.Column(db.Integer)
    performance_score = db.Column(db.Float)

    def __init__(self, native_english_speaker, course_instructor, course, semester, class_size, performance_score):
        self.native_english_speaker = native_english_speaker
        self.course_instructor = course_instructor
        self.course = course
        self.semester = semester
        self.class_size = class_size
        self.performance_score = performance_score

    
class SchoolSchema(ma.Schema):
    native_english_speaker = fields.String()
    course_instructor = fields.String()
    course = fields.String()
    semester = fields.Integer()
    class_size = fields.Integer()
    performance_score = fields.Float()