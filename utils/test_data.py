# utils/test_data.py

from faker import Faker

class TestDataGenerator:
    """Generador de datos de prueba usando Faker."""
    
    def __init__(self):
        self.fake = Faker()
    
    def get_invalid_credentials(self):
        """Genera credenciales inválidas aleatorias."""
        return {
            'username': self.fake.user_name(),
            'password': self.fake.password()
        }
    
    def get_user_data(self):
        """Genera datos de usuario completos."""
        return {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
            'phone': self.fake.phone_number(),
            'address': self.fake.address()
        }