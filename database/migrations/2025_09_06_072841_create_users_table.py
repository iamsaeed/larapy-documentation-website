"""
Create users table migration.
"""

from larapy.database.migrations.migration import Migration
from larapy.database.migrations.schema import Schema, Blueprint


class CreateUsersTable(Migration):
    """
    Run the migrations.
    
    @return void
    """
    
    def up(self):
        """
        Run the migrations.
        
        @return void
        """
        def create_users_table(table: Blueprint):
            table.id()
            table.string('name')
            table.string('email').unique()
            table.string('password')
            table.string('remember_token', 100).nullable()
            table.timestamps()
        
        Schema.create('users', create_users_table)
    
    def down(self):
        """
        Reverse the migrations.
        
        @return void
        """
        Schema.drop_if_exists('users')
