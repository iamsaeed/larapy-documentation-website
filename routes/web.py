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
    Route.get('/', 'app.Http.Controllers.HomeController@index').name('home')
    
    # Documentation routes (for future implementation)
    # Route.get('/docs', 'app.Http.Controllers.DocsController@index').name('docs')
    # Route.get('/docs/{slug}', 'app.Http.Controllers.DocsController@show').name('docs.show')
    
    # API documentation routes
    # Route.get('/api-docs', 'app.Http.Controllers.ApiDocsController@index').name('api-docs')