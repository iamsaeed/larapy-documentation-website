"""
View Configuration
Similar to Laravel's config/view.php

This configuration file defines view settings and uses the env() helper
to pull values from environment variables with sensible defaults.
"""

import sys
import os
from pathlib import Path

# Add the package to the Python path to import helpers
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'package-larapy'))

try:
    from core.helpers import env, resource_path, storage_path
except ImportError:
    # Fallback if helpers not available
    def env(key, default=None):
        return os.getenv(key, default)
    
    def resource_path(path=''):
        return str(Path(__file__).parent.parent / 'resources' / path) if path else str(Path(__file__).parent.parent / 'resources')
    
    def storage_path(path=''):
        return str(Path(__file__).parent.parent / 'storage' / path) if path else str(Path(__file__).parent.parent / 'storage')


# Configuration dictionary (Laravel style)
CONFIG = {
    # View file paths - where templates are stored
    'paths': [
        resource_path('views'),
    ],

    # Compiled view cache path
    'compiled': storage_path('framework/views'),

    # Template engine configuration
    'engine': {
        'name': 'jinja2',
        'options': {
            'auto_reload': env('APP_DEBUG', False),
            'cache_size': int(env('VIEW_CACHE_SIZE', '400')),
            'extensions': [
                'jinja2.ext.do',
                'jinja2.ext.loopcontrols',
            ],
        },
    },

    # View file extensions
    'extensions': ['.html', '.jinja2', '.j2', '.blade'],

    # Global view data - available to all templates
    'shared': {
        'app_name': env('APP_NAME', 'Larapy Documentation'),
        'app_url': env('APP_URL', 'http://localhost:8000'),
        'app_env': env('APP_ENV', 'production'),
        'app_debug': env('APP_DEBUG', False),
    },

    # View composers - automatically include data for specific views
    'composers': {
        # 'profile': ['ProfileComposer', 'getProfileData'],
        # '*': ['GlobalComposer', 'getGlobalData'],
    },

    # View creators - run before view is rendered
    'creators': {
        # 'profile': ['ProfileCreator', 'create'],
    },
}