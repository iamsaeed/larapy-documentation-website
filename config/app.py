"""
Application Configuration
Similar to Laravel's config/app.php

This configuration file defines application settings and uses the env() helper
to pull values from environment variables with sensible defaults.
"""

import sys
import os
from pathlib import Path

# Add the package to the Python path to import helpers
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'package-larapy'))

try:
    from core.helpers import env
except ImportError:
    # Fallback if helpers not available
    def env(key, default=None):
        return os.getenv(key, default)


# Configuration dictionary (Laravel style)
CONFIG = {
    # Application name
    'name': env('APP_NAME', 'Larapy Documentation'),

    # Application environment (local, testing, staging, production)
    'env': env('APP_ENV', 'production'),

    # Application debug mode
    'debug': env('APP_DEBUG', False),

    # Application URL
    'url': env('APP_URL', 'http://localhost:8000'),

    # Application timezone
    'timezone': env('APP_TIMEZONE', 'UTC'),

    # Application locale
    'locale': env('APP_LOCALE', 'en'),

    # Application fallback locale
    'fallback_locale': env('APP_FALLBACK_LOCALE', 'en'),

    # Application key for encryption
    'key': env('APP_KEY', ''),

    # Application cipher
    'cipher': env('APP_CIPHER', 'AES-256-CBC'),

    # Maintenance mode
    'maintenance': env('APP_MAINTENANCE', False),
    
    # Logging configuration
    'log_channel': env('LOG_CHANNEL', 'stack'),
    'log_level': env('LOG_LEVEL', 'debug'),
    'log_deprecations_channel': env('LOG_DEPRECATIONS_CHANNEL', 'null'),
    
    # Application service providers
    'providers': [
        'app.providers.app_service_provider.AppServiceProvider',
        'app.providers.route_service_provider.RouteServiceProvider',
    ],

    # Class aliases
    'aliases': {
        'App': 'larapy.support.facades.App',
        'Auth': 'larapy.support.facades.Auth',
        'Cache': 'larapy.support.facades.Cache',
        'Config': 'larapy.support.facades.Config',
        'DB': 'larapy.support.facades.DB',
        'Hash': 'larapy.support.facades.Hash',
        'Log': 'larapy.support.facades.Log',
        'Route': 'larapy.support.facades.Route',
        'Schema': 'larapy.support.facades.Schema',
        'Session': 'larapy.support.facades.Session',
        'Storage': 'larapy.support.facades.Storage',
        'URL': 'larapy.support.facades.URL',
        'Validator': 'larapy.support.facades.Validator',
        'View': 'larapy.support.facades.View',
    },
}