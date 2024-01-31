# from app import app
# from models import db, Bird

# db.init_app(app)

# with app.app_context():

#     print('Deleting existing birds...')
#     Bird.query.delete()

#     print('Creating bird objects...')
#     chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
#     grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
#     starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
#     dove = Bird(name='Mourning Dove', species='Zenaida Macroura')

#     print('Adding bird objects to transaction...')
#     db.session.add_all([chickadee, grackle, starling, dove])

#     print('Committing transaction...')
#     db.session.commit()

#     print('Complete.')

from app import app, db
from models import Bird

with app.app_context():
    # Check if db has been initialized
    if not hasattr(app, 'extensions') or 'sqlalchemy' not in app.extensions:
        db.init_app(app)

    print('Deleting existing birds...')
    Bird.query.delete()

    print('Creating bird objects...')
    chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
    grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
    starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
    dove = Bird(name='Mourning Dove', species='Zenaida Macroura')

    print('Adding bird objects to transaction...')
    db.session.add_all([chickadee, grackle, starling, dove])

    print('Committing transaction...')
    db.session.commit()

    print('Complete.')
