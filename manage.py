import os
import unittest
import coverage
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project import app, db
from project.models import User

app.config.from_object('config.DevelopmentConfig')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def adduser(email, username, admin=False):
    """Registra nuevo usuario."""
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt="Confirm: ")
    if password != password2:
        import sys
        sys.exit("Error: passwords no concuerdan")
    db.create_all()
    user = User(email=email, username=username, password=password, is_admin=admin)
    db.session.add(user)
    db.session.commit()
    print("Usuario {0} se registro con exito.".format(username))


@manager.command
def test():
    """Ejecuta tests sin coverage."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def uni():
    """Ejecuta 1 test."""
    tests = unittest.TestLoader().discover('tests/test_users')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(
        branch=True, include='project/*', omit='*/__init__.py')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()


if __name__ == '__main__':
    manager.run()