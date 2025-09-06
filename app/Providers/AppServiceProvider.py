"""
App Service Provider
Similar to Laravel's app/Providers/AppServiceProvider.php
"""

from larapy.support.service_provider import ServiceProvider

class AppServiceProvider(ServiceProvider):
    """
    The application service provider.
    """
    
    def register(self):
        """
        Register any application services.
        """
        # Register application bindings
        pass
    
    def boot(self):
        """
        Bootstrap any application services.
        """
        # Bootstrap application services
        pass