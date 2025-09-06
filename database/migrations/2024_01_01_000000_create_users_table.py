"""
Create Users Table Migration
Similar to Laravel's create_users_table migration
"""

from larapy.database.migrations.migration import Migration
from larapy.database.schema.blueprint import Blueprint
from larapy.database.schema import Schema

class CreateUsersTable(Migration):
    """
    Run the migrations.
    """
    
    def up(self):
        """
        Create the users table
        """
        Schema.create('users', self.build_table)
    
    def build_table(self, table: Blueprint):
        """
        Define the users table structure
        """
        # Primary key
        table.id()
        
        # User information
        table.string('name')
        table.string('email').unique()
        table.timestamp('email_verified_at').nullable()
        table.string('password')
        
        # Remember token for persistent login
        table.remember_token()
        
        # Timestamps
        table.timestamps()
        
        # Indexes
        table.index('email')
    
    def down(self):
        """
        Reverse the migrations.
        """
        Schema.drop_if_exists('users')

# Migration registration
migration = CreateUsersTable()