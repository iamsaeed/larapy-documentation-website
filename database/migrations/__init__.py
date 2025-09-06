# Migrations module
"""
Database migrations for the application.
Similar to Laravel's database/migrations directory.
"""

# Import all migrations here for auto-discovery
from .create_users_table import CreateUsersTable

# Register migrations
MIGRATIONS = [
    CreateUsersTable,
]