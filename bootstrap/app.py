"""
Application Bootstrap
This file bootstraps the Larapy application similar to Laravel's bootstrap/app.php
"""

from pathlib import Path
from larapy import Application
from larapy.http.kernel import HttpKernel

def create_application():
    """
    Create and configure the Larapy application instance
    """
    # Create application instance
    app = Application(base_path=str(Path(__file__).parent.parent))
    
    # Register configuration
    app.register_config_files()
    
    # Register service providers
    register_service_providers(app)
    
    # Register middleware
    register_middleware(app)
    
    # Register routes
    register_routes(app)
    
    return app

def register_service_providers(app):
    """Register application service providers"""
    from app.Providers.AppServiceProvider import AppServiceProvider
    from app.Providers.AuthServiceProvider import AuthServiceProvider
    from app.Providers.RouteServiceProvider import RouteServiceProvider
    
    app.register(AppServiceProvider)
    app.register(AuthServiceProvider)
    app.register(RouteServiceProvider)

def register_middleware(app):
    """Register application middleware"""
    from app.Http.Kernel import Kernel
    
    kernel = Kernel(app)
    app.singleton('http.kernel', lambda: kernel)

def register_routes(app):
    """Register application routes"""
    # Web routes
    from routes import web
    web.register_routes(app)
    
    # API routes
    from routes import api
    api.register_routes(app)