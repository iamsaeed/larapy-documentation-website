"""
Database Configuration
Similar to Laravel's config/database.php
"""

import os
from pathlib import Path

# Default database connection name
DEFAULT = os.getenv('DB_CONNECTION', 'sqlite')

# Database connections configuration
CONNECTIONS = {
    'sqlite': {
        'driver': 'sqlite',
        'database': os.getenv('DB_DATABASE', str(Path(__file__).parent.parent / 'database' / 'database.sqlite')),
        'prefix': '',
        'foreign_key_constraints': True,
    },

    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'port': os.getenv('DB_PORT', 3306),
        'database': os.getenv('DB_DATABASE', 'larapy_docs'),
        'username': os.getenv('DB_USERNAME', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'charset': 'utf8mb4',
        'collation': 'utf8mb4_unicode_ci',
        'prefix': '',
        'strict': True,
        'engine': None,
    },

    'pgsql': {
        'driver': 'pgsql',
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'port': os.getenv('DB_PORT', 5432),
        'database': os.getenv('DB_DATABASE', 'larapy_docs'),
        'username': os.getenv('DB_USERNAME', 'postgres'),
        'password': os.getenv('DB_PASSWORD', ''),
        'charset': 'utf8',
        'prefix': '',
        'schema': 'public',
        'sslmode': 'prefer',
    },
}

# Migration repository table
MIGRATIONS = 'migrations'

# Redis configuration
REDIS = {
    'client': os.getenv('REDIS_CLIENT', 'predis'),
    
    'options': {
        'cluster': os.getenv('REDIS_CLUSTER', 'redis'),
        'prefix': os.getenv('REDIS_PREFIX', f"{os.getenv('APP_NAME', 'larapy_docs')}_database_"),
    },
    
    'default': {
        'url': os.getenv('REDIS_URL'),
        'host': os.getenv('REDIS_HOST', '127.0.0.1'),
        'password': os.getenv('REDIS_PASSWORD'),
        'port': os.getenv('REDIS_PORT', 6379),
        'database': os.getenv('REDIS_DB', 0),
    },
    
    'cache': {
        'url': os.getenv('REDIS_URL'),
        'host': os.getenv('REDIS_HOST', '127.0.0.1'),
        'password': os.getenv('REDIS_PASSWORD'),
        'port': os.getenv('REDIS_PORT', 6379),
        'database': os.getenv('REDIS_CACHE_DB', 1),
    },
}