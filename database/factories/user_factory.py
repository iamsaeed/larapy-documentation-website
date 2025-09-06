"""
UserFactory for generating User test data.
"""

from larapy.database.migrations.factory import Factory
from app.models.user import User
import random
import string


class UserFactory(Factory):
    """
    UserFactory for generating User model instances.
    """
    
    model = User
    
    def definition(self):
        """
        Define the model's default state.
        
        @return dict
        """
        return {
            # Example factory definition:
            'name': self.faker.name(),
            'email': self.faker.email(),
            'password': 'password',  # Default password
            'created_at': self.faker.date_time(),
            'updated_at': self.faker.date_time(),
        }
    
    def configure(self):
        """
        Configure the model factory.
        """
        return self

