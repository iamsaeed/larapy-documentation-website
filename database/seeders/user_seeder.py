"""
UserSeeder for seeding database tables.
"""

from larapy.database.migrations.seeder import Seeder
from app.models.user import User  # Import your models here


class UserSeeder(Seeder):
    """
    UserSeeder for populating database tables with test data.
    """
    
    def run(self):
        """
        Run the database seeds.
        
        @return void
        """
        # Example seeder implementation:
        # 
        # User.create({
        #     'name': 'John Doe',
        #     'email': 'john@example.com',
        #     'password': 'hashed_password'
        # })
        # 
        # for i in range(10):
        #     User.create({
        #         'name': f'User {i}',
        #         'email': f'user{i}@example.com',
        #         'password': 'hashed_password'
        #     })
        
        pass
