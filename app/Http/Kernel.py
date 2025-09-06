"""
HTTP Kernel
Similar to Laravel's app/Http/Kernel.php
"""

from larapy.http.kernel import HttpKernel as BaseKernel

class Kernel(BaseKernel):
    """
    The application's global HTTP middleware stack.
    """
    
    # Global middleware stack
    middleware = [
        'app.Http.Middleware.TrustProxies.TrustProxies',
        'app.Http.Middleware.EncryptCookies.EncryptCookies',
        'larapy.middleware.AddQueuedCookiesToResponse',
        'larapy.middleware.StartSession',
        'larapy.middleware.ShareErrorsFromSession',
        'app.Http.Middleware.VerifyCsrfToken.VerifyCsrfToken',
        'larapy.middleware.SubstituteBindings',
    ]
    
    # Route middleware groups
    middleware_groups = {
        'web': [
            'app.Http.Middleware.EncryptCookies.EncryptCookies',
            'larapy.middleware.AddQueuedCookiesToResponse',
            'larapy.middleware.StartSession',
            'larapy.middleware.ShareErrorsFromSession',
            'app.Http.Middleware.VerifyCsrfToken.VerifyCsrfToken',
            'larapy.middleware.SubstituteBindings',
        ],
        
        'api': [
            'larapy.middleware.throttle:api',
            'larapy.middleware.SubstituteBindings',
        ],
    }
    
    # Route middleware
    route_middleware = {
        'auth': 'app.Http.Middleware.Authenticate.Authenticate',
        'auth.basic': 'larapy.auth.middleware.AuthenticateWithBasicAuth',
        'auth.session': 'larapy.auth.middleware.AuthenticateSession',
        'cache.headers': 'larapy.http.middleware.SetCacheHeaders',
        'can': 'larapy.auth.middleware.Authorize',
        'guest': 'app.Http.Middleware.RedirectIfAuthenticated.RedirectIfAuthenticated',
        'password.confirm': 'larapy.auth.middleware.RequirePassword',
        'signed': 'larapy.routing.middleware.ValidateSignature',
        'throttle': 'larapy.routing.middleware.ThrottleRequests',
        'verified': 'larapy.auth.middleware.EnsureEmailIsVerified',
    }