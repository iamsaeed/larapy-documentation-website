"""
Route Service Provider
Similar to Laravel's app/Providers/RouteServiceProvider.php
"""

from larapy.support.service_provider import ServiceProvider
from larapy.routing.route import Route

class RouteServiceProvider(ServiceProvider):
    """
    The route service provider.
    """
    
    # The path to the "home" route for your application
    HOME = '/home'
    
    def boot(self):
        """
        Bootstrap any application services.
        """
        self.configure_rate_limiting()
        
        # Load routes
        self.map_routes()
    
    def map_routes(self):
        """
        Define the routes for the application.
        """
        self.map_api_routes()
        self.map_web_routes()
    
    def map_web_routes(self):
        """
        Define the "web" routes for the application.
        """
        from routes import web
        
        Route.middleware('web').group(lambda: web.register_routes(self.app))
    
    def map_api_routes(self):
        """
        Define the "api" routes for the application.
        """
        from routes import api
        
        Route.prefix('api').middleware('api').group(lambda: api.register_routes(self.app))
    
    def configure_rate_limiting(self):
        """
        Configure the rate limiters for the application.
        """
        from larapy.cache.rate_limiting import RateLimiter
        
        RateLimiter.for_('api', lambda request: 60)  # 60 requests per minute
        RateLimiter.for_('global', lambda request: 1000)  # 1000 requests per minute