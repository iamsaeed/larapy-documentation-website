"""
Database Configuration
Similar to Laravel's config/database.php

This configuration file defines database connections and uses the env() helper
to pull values from environment variables with sensible defaults.
"""

import sys
import os
from pathlib import Path

# Add the package to the Python path to import helpers
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'package-larapy'))

try:
    from core.helpers import env, database_path
except ImportError:
    # Fallback if helpers not available
    def env(key, default=None):
        return os.getenv(key, default)
    
    def database_path(path=''):
        return str(Path(__file__).parent.parent / 'database' / path) if path else str(Path(__file__).parent.parent / 'database')


# Configuration dictionary (Laravel style)
CONFIG = {
    # Default database connection name
    'default': env('DB_CONNECTION', 'sqlite'),
    
    # Database connections configuration
    'connections': {
        'sqlite': {
            'driver': 'sqlite',
            'database': env('DB_DATABASE', database_path('database.sqlite')),
            'prefix': env('DB_PREFIX', ''),
            'foreign_key_constraints': env('DB_FOREIGN_KEYS', True),
        },

        'mysql': {
            'driver': 'mysql',
            'host': env('DB_HOST', '127.0.0.1'),
            'port': int(env('DB_PORT', '3306')),
            'database': env('DB_DATABASE', 'larapy_docs'),
            'username': env('DB_USERNAME', 'root'),
            'password': env('DB_PASSWORD', ''),
            'unix_socket': env('DB_SOCKET', ''),
            'charset': env('DB_CHARSET', 'utf8mb4'),
            'collation': env('DB_COLLATION', 'utf8mb4_unicode_ci'),
            'prefix': env('DB_PREFIX', ''),
            'prefix_indexes': True,
            'strict': True,
            'engine': None,
            'options': {}
        },

        'pgsql': {
            'driver': 'pgsql',
            'host': env('DB_HOST', '127.0.0.1'),
            'port': int(env('DB_PORT', '5432')),
            'database': env('DB_DATABASE', 'larapy_docs'),
            'username': env('DB_USERNAME', 'postgres'),
            'password': env('DB_PASSWORD', ''),
            'charset': env('DB_CHARSET', 'utf8'),
            'prefix': env('DB_PREFIX', ''),
            'prefix_indexes': True,
            'search_path': env('DB_SEARCH_PATH', 'public'),
            'sslmode': env('DB_SSLMODE', 'prefer'),
        },
    },

    # Migration repository table name
    'migrations': env('DB_MIGRATIONS_TABLE', 'migrations'),
    
    # Redis configuration
    'redis': {
        'client': env('REDIS_CLIENT', 'predis'),
        
        'options': {
            'cluster': env('REDIS_CLUSTER', 'redis'),
            'prefix': env('REDIS_PREFIX', f"{env('APP_NAME', 'larapy_docs')}_database_"),
        },
        
        'default': {
            'url': env('REDIS_URL'),
            'host': env('REDIS_HOST', '127.0.0.1'),
            'username': env('REDIS_USERNAME'),
            'password': env('REDIS_PASSWORD'),
            'port': int(env('REDIS_PORT', '6379')),
            'database': int(env('REDIS_DB', '0')),
        },
        
        'cache': {
            'url': env('REDIS_URL'),
            'host': env('REDIS_HOST', '127.0.0.1'),
            'username': env('REDIS_USERNAME'),
            'password': env('REDIS_PASSWORD'),
            'port': int(env('REDIS_PORT', '6379')),
            'database': int(env('REDIS_CACHE_DB', '1')),
        },
        
        'session': {
            'url': env('REDIS_URL'),
            'host': env('REDIS_HOST', '127.0.0.1'),
            'username': env('REDIS_USERNAME'),
            'password': env('REDIS_PASSWORD'),
            'port': int(env('REDIS_PORT', '6379')),
            'database': int(env('REDIS_SESSION_DB', '2')),
        },
    }
}