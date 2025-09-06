"""
Web Routes
Similar to Laravel's routes/web.php
"""

from larapy.routing.route import Route

def register_routes(app):
    """
    Register web routes for the application.
    These routes are loaded by the RouteServiceProvider within a group which
    contains the "web" middleware group.
    """
    
    # Home route
    Route.get('/', 'app.http.controllers.home_controller@index').name('home')
    
    # Documentation routes (for future implementation)
    # Route.get('/docs', 'app.http.controllers.docs_controller@index').name('docs')
    # Route.get('/docs/{slug}', 'app.http.controllers.docs_controller@show').name('docs.show')
    
    # API documentation routes
    # Route.get('/api-docs', 'app.http.controllers.api_docs_controller@index').name('api-docs')