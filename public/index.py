#!/usr/bin/env python3
"""
Larapy Application Entry Point
This file serves as the entry point for all requests, similar to Laravel's public/index.php
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import the bootstrap application
from bootstrap.app import create_application

# Create the application instance
app = create_application()

if __name__ == "__main__":
    # Run Flask development server
    app.run(
        host="127.0.0.1", 
        port=8000, 
        debug=True,
        use_reloader=True
    )