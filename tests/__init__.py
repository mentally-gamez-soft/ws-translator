"""Declare the base test classfor the tests suit."""

import unittest

from core import create_app  # , db


class BaseTestClass(unittest.TestCase):
    """Define the base test class."""

    def setUp(self):
        """Define the data set create before each test."""
        self.app = create_app(settings_module="config.testing")

        # Crea un contexto de aplicación
        with self.app.app_context():
            pass
            # # Crea las tablas de la base de datos
            # db.create_all()
            # # Creamos un usuario administrador
            # BaseTestClass.create_user("admin", "admin@xyz.com", "1111", True)
            # # Creamos un usuario invitado
            # BaseTestClass.create_user("guest", "guest@xyz.com", "1111", False)

    def tearDown(self):
        """Destroy the data set after each test."""
        with self.app.app_context():
            pass
            # # Elimina todas las tablas de la base de datos
            # db.session.remove()
            # db.drop_all()
