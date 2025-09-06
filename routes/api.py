"""
API Routes
Similar to Laravel's routes/api.php
"""

from larapy.routing.route import Route

def register_routes(app):
    """
    Register API routes for the application.
    These routes are loaded by the RouteServiceProvider within a group which
    is assigned the "api" middleware group.
    """
    
    # API routes will be prefixed with '/api'
    with Route.group(prefix='/api', middleware=['api']):
        # Documentation API endpoints (for future implementation)
        # Route.get('/docs', 'app.http.controllers.api.docs_controller@index')
        # Route.get('/docs/{slug}', 'app.http.controllers.api.docs_controller@show')
        # Route.get('/search', 'app.http.controllers.api.search_controller@index')
        pass