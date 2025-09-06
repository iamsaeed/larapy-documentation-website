"""
Application Configuration
Similar to Laravel's config/app.php
"""

import os
from pathlib import Path

# Application Name
APP_NAME = os.getenv('APP_NAME', 'Larapy')

# Application Environment
APP_ENV = os.getenv('APP_ENV', 'production')

# Application Debug Mode
APP_DEBUG = os.getenv('APP_DEBUG', 'false').lower() == 'true'

# Application URL
APP_URL = os.getenv('APP_URL', 'http://localhost:8000')

# Application Timezone
APP_TIMEZONE = 'UTC'

# Application Locale
APP_LOCALE = 'en'

# Application Fallback Locale
APP_FALLBACK_LOCALE = 'en'

# Encryption Key
APP_KEY = os.getenv('APP_KEY', '')

# Application Service Providers
PROVIDERS = [
    'app.Providers.AppServiceProvider.AppServiceProvider',
    'app.Providers.AuthServiceProvider.AuthServiceProvider',
    'app.Providers.BroadcastServiceProvider.BroadcastServiceProvider',
    'app.Providers.EventServiceProvider.EventServiceProvider',
    'app.Providers.RouteServiceProvider.RouteServiceProvider',
]

# Class Aliases
ALIASES = {
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
}