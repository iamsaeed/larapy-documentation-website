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
        'larapy.middleware.TrustProxies',
        'larapy.middleware.HandleCors',
        'larapy.middleware.PreventRequestsDuringMaintenance',
        'larapy.middleware.ValidatePostSize',
        'larapy.middleware.TrimStrings',
        'larapy.middleware.ConvertEmptyStringsToNull',
    ]
    
    # Route middleware groups
    middleware_groups = {
        'web': [
            'larapy.middleware.EncryptCookies',
            'larapy.middleware.AddQueuedCookiesToResponse',
            'larapy.middleware.StartSession',
            'larapy.middleware.ShareErrorsFromSession',
            'larapy.middleware.VerifyCsrfToken',
            'larapy.middleware.SubstituteBindings',
        ],
        
        'api': [
            'larapy.middleware.throttle:api',
            'larapy.middleware.SubstituteBindings',
        ],
    }
    
    # Route middleware
    route_middleware = {
        'auth': 'larapy.auth.middleware.Authenticate',
        'auth.basic': 'larapy.auth.middleware.AuthenticateWithBasicAuth',
        'auth.session': 'larapy.auth.middleware.AuthenticateSession',
        'cache.headers': 'larapy.http.middleware.SetCacheHeaders',
        'can': 'larapy.auth.middleware.Authorize',
        'guest': 'larapy.auth.middleware.RedirectIfAuthenticated',
        'password.confirm': 'larapy.auth.middleware.RequirePassword',
        'signed': 'larapy.routing.middleware.ValidateSignature',
        'throttle': 'larapy.routing.middleware.ThrottleRequests',
        'verified': 'larapy.auth.middleware.EnsureEmailIsVerified',
    }