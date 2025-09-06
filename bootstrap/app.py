"""
Application Bootstrap
This file bootstraps the Larapy application similar to Laravel's bootstrap/app.php
"""

from pathlib import Path
from flask import Flask, render_template, jsonify
from larapy.core.application import Application

def create_application():
    """
    Create and configure the Flask application instance integrated with Larapy
    """
    # Set up base path
    base_path = str(Path(__file__).parent.parent)
    
    # Create Larapy application instance
    larapy_app = Application(base_path=base_path)
    
    # Load environment variables
    larapy_app.load_environment_variables()
    
    # Load configuration
    larapy_app.load_config()
    
    # Create Flask application
    flask_app = Flask(
        __name__,
        template_folder=str(Path(base_path) / 'resources' / 'views'),
        static_folder=str(Path(base_path) / 'public')
    )
    
    # Configure Flask app
    configure_flask_app(flask_app, larapy_app)
    
    # Register routes
    register_routes(flask_app, larapy_app)
    
    # Register service providers (if needed)
    register_service_providers(larapy_app)
    
    # Boot the Larapy application
    larapy_app.boot()
    
    # Store Larapy app reference in Flask app
    flask_app.larapy = larapy_app
    
    return flask_app

def configure_flask_app(flask_app, larapy_app):
    """Configure Flask application settings"""
    flask_app.config.update({
        'SECRET_KEY': larapy_app.get_config('app.APP_KEY', 'larapy-default-secret-key'),
        'DEBUG': larapy_app.get_config('app.APP_DEBUG', larapy_app.is_local()),
        'ENV': larapy_app.environment,
    })

def register_routes(flask_app, larapy_app):
    """Register Flask routes"""
    
    @flask_app.route('/')
    def home():
        """Home page route"""
        try:
            # Get data for the home page
            data = {
                'title': 'Welcome to Larapy Documentation Website',
                'message': 'Laravel\'s elegant syntax meets Python\'s simplicity',
                'version': larapy_app.version(),
                'features': [
                    'Larapy ORM',
                    'Authentication System', 
                    'Middleware Support',
                    'Caching System',
                    'Queue System',
                    'Event System'
                ]
            }
            return render_template('home.html', **data)
        except Exception:
            # Fallback if template rendering fails
            return f"""
            <html>
            <head>
                <title>Welcome to Larapy Documentation</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="container mt-5">
                    <div class="jumbotron text-center">
                        <h1 class="display-4">Welcome to Larapy Documentation!</h1>
                        <p class="lead">Laravel's elegant syntax meets Python's simplicity</p>
                        <p class="text-muted">Version {larapy_app.version()}</p>
                        <p class="text-info">Flask integration successful!</p>
                    </div>
                </div>
            </body>
            </html>
            """
    
    @flask_app.route('/health')
    def health():
        """Health check endpoint"""
        return jsonify({
            'status': 'healthy',
            'version': larapy_app.version(),
            'environment': larapy_app.environment,
            'framework': 'Larapy with Flask',
            'debug': larapy_app.is_local()
        })
    
    @flask_app.route('/api/info')
    def api_info():
        """API information endpoint"""
        return jsonify({
            'name': 'Larapy Documentation API',
            'version': larapy_app.version(),
            'framework': 'Larapy with Flask',
            'environment': larapy_app.environment
        })

def register_service_providers(larapy_app):
    """Register Larapy service providers"""
    try:
        from app.providers.app_service_provider import AppServiceProvider
        from app.providers.route_service_provider import RouteServiceProvider
        
        larapy_app.register(AppServiceProvider)
        larapy_app.register(RouteServiceProvider)
    except ImportError:
        # Service providers not yet implemented, skip for now
        pass

def register_middleware(larapy_app):
    """Register application middleware"""
    try:
        from app.http.kernel import Kernel
        
        kernel = Kernel(larapy_app)
        larapy_app.instance('http.kernel', kernel)
    except ImportError:
        # HTTP Kernel not yet implemented, skip for now
        pass