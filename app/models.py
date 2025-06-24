from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    # Relationship
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    # Serialization rules to prevent recursive loops
    serialize_rules = ('-hero_powers.hero',)

    def __repr__(self):
        return f'<Hero {self.super_name}>'

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Relationship
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

    # Serialization rules
    serialize_rules = ('-hero_powers.power',)

    # Validations
    @db.validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError('Description must be present and at least 20 characters long')
        return value

    def __repr__(self):
        return f'<Power {self.name}>'

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    # Relationships
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    # Serialization rules
    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')

    # Validations
    @db.validates('strength')
    def validate_strength(self, key, value):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if value not in valid_strengths:
            raise ValueError('Strength must be one of: Strong, Weak, Average')
        return value

    def __repr__(self):
        return f'<HeroPower hero_id={self.hero_id} power_id={self.power_id} strength={self.strength}>'