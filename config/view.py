"""
View Configuration
Similar to Laravel's config/view.php
"""

import os
from pathlib import Path

# View template paths
PATHS = [
    str(Path(__file__).parent.parent / 'resources' / 'views'),
]

# Compiled view path
COMPILED = str(Path(__file__).parent.parent / 'storage' / 'framework' / 'views')

# Template engine configuration
ENGINE = {
    'name': 'jinja2',
    'options': {
        'auto_reload': os.getenv('APP_DEBUG', 'false').lower() == 'true',
        'cache_size': int(os.getenv('VIEW_CACHE_SIZE', '400')),
        'extensions': [
            'jinja2.ext.do',
            'jinja2.ext.loopcontrols',
        ],
    },
}