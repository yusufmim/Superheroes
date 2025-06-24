from flask import request
from flask_restful import Resource, Api
from app.models import db, Hero, Power, HeroPower
from app.email import send_email

def init_routes(app):
    api = Api(app)

    class HeroList(Resource):
        def get(self):
            heroes = Hero.query.all()
            return [hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes], 200

    class HeroDetail(Resource):
        def get(self, id):
            hero = Hero.query.get(id)
            if not hero:
                return {'error': 'Hero not found'}, 404
            return hero.to_dict(only=('id', 'name', 'super_name', 'hero_powers')), 200

    class PowerList(Resource):
        def get(self):
            powers = Power.query.all()
            return [power.to_dict(only=('id', 'name', 'description')) for power in powers], 200

    class PowerDetail(Resource):
        def get(self, id):
            power = Power.query.get(id)
            if not power:
                return {'error': 'Power not found'}, 404
            return power.to_dict(only=('id', 'name', 'description')), 200

        def patch(self, id):
            power = Power.query.get(id)
            if not power:
                return {'error': 'Power not found'}, 404

            data = request.get_json()
            try:
                power.description = data.get('description', power.description)
                db.session.commit()
                return power.to_dict(only=('id', 'name', 'description')), 200
            except ValueError as e:
                return {'errors': [str(e)]}, 400

    class HeroPowerCreate(Resource):
        def post(self):
            data = request.get_json()
            try:
                hero_power = HeroPower(
                    strength=data['strength'],
                    hero_id=data['hero_id'],
                    power_id=data['power_id']
                )
                # Verify hero and power exist
                hero = Hero.query.get(data['hero_id'])
                power = Power.query.get(data['power_id'])
                if not hero or not power:
                    return {'errors': ['Hero or Power not found']}, 404

                db.session.add(hero_power)
                db.session.commit()

                # Send email notification 
                send_email(
                    'yusufmim2001@gmail.com',  
                    'New HeroPower Created',
                    f'Hero {hero.super_name} assigned power {power.name} with strength {hero_power.strength}'
                )

                return hero_power.to_dict(only=('id', 'hero_id', 'power_id', 'strength', 'hero', 'power')), 201
            except ValueError as e:
                return {'errors': [str(e)]}, 400

    # Register routes
    api.add_resource(HeroList, '/heroes')
    api.add_resource(HeroDetail, '/heroes/<int:id>')
    api.add_resource(PowerList, '/powers')
    api.add_resource(PowerDetail, '/powers/<int:id>')
    api.add_resource(HeroPowerCreate, '/hero_powers')