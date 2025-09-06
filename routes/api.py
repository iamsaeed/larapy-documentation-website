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
        # Example API routes (commented out)
        # Route.get('/users', 'app.Http.Controllers.Api.UserController@index')
        # Route.post('/users', 'app.Http.Controllers.Api.UserController@store')
        # Route.get('/users/{id}', 'app.Http.Controllers.Api.UserController@show')
        # Route.put('/users/{id}', 'app.Http.Controllers.Api.UserController@update')
        # Route.delete('/users/{id}', 'app.Http.Controllers.Api.UserController@destroy')
        pass