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
    
    # Example additional routes (commented out)
    # Route.get('/about', 'app.Http.Controllers.HomeController@about').name('about')
    # Route.get('/contact', 'app.Http.Controllers.HomeController@contact').name('contact')
    
    # Authentication routes (when implemented)
    # Route.group(prefix='/auth', routes=[
    #     Route.get('/login', 'app.Http.Controllers.Auth.LoginController@showLoginForm').name('login'),
    #     Route.post('/login', 'app.Http.Controllers.Auth.LoginController@login'),
    #     Route.post('/logout', 'app.Http.Controllers.Auth.LoginController@logout').name('logout'),
    # ])