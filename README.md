# Larapy Documentation Website

A documentation website for the Larapy framework, built with Laravel-style folder structure and powered by Python.

## 🚀 Features

- **Laravel-style Architecture**: Familiar folder structure with `app/`, `config/`, `routes/`, `resources/`, etc.
- **Modern Web Framework**: Built on top of Larapy framework with Flask under the hood
- **Beautiful UI**: Bootstrap-based responsive design with modern components
- **Documentation Ready**: Structure prepared for comprehensive documentation
- **Developer Friendly**: Hot reload, debugging, and development tools

## 📁 Project Structure

```
documentation-webiste-larapy/
├── app/
│   ├── console/                       # Console commands
│   │   └── commands/                  # Artisan-like commands
│   ├── events/                        # Event classes
│   ├── exceptions/                    # Exception handlers
│   ├── http/
│   │   ├── controllers/
│   │   │   ├── controller.py          # Base controller
│   │   │   └── home_controller.py     # Home page controller
│   │   ├── middleware/                # HTTP middleware
│   │   ├── requests/                  # Form request classes
│   │   └── kernel.py                  # HTTP kernel with middleware
│   ├── jobs/                          # Queue job classes
│   ├── listeners/                     # Event listeners
│   ├── mail/                          # Mail classes
│   ├── models/                        # Eloquent models
│   ├── notifications/                 # Notification classes
│   ├── policies/                      # Authorization policies
│   ├── providers/
│   │   ├── app_service_provider.py    # Application services
│   │   └── route_service_provider.py  # Route configuration
│   └── rules/                         # Custom validation rules
├── bootstrap/
│   └── app.py                         # Application bootstrap
├── config/
│   ├── app.py                         # Application configuration
│   ├── database.py                    # Database configuration
│   └── view.py                        # View engine configuration
├── public/
│   ├── index.py                       # Application entry point
│   ├── css/                           # Public CSS files
│   └── js/                            # Public JavaScript files
├── resources/
│   ├── css/
│   │   └── app.css                    # Application styles
│   ├── js/
│   │   └── app.js                     # Application JavaScript
│   └── views/
│       ├── layouts/
│       │   └── app.html               # Main layout template
│       └── home.html                  # Home page template
├── routes/
│   ├── web.py                         # Web routes
│   └── api.py                         # API routes
├── storage/                           # Storage directories
├── .env.example                       # Environment template
├── .gitignore                         # Git ignore rules
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## 🛠 Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd documentation-webiste-larapy
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment:**
   ```bash
   cp .env.example .env
   ```

4. **Run the application:**
   ```bash
   python public/index.py
   ```

5. **Visit the application:**
   Open your browser to `http://localhost:8000`

## 🎯 Quick Start

The application follows Laravel conventions with PEP 8 naming:

- **Controllers**: Located in `app/http/controllers/`
- **Routes**: Defined in `routes/web.py` and `routes/api.py`
- **Views**: Jinja2 templates in `resources/views/`
- **Configuration**: Settings in `config/` directory
- **Public Assets**: CSS, JS, images in `public/`

## 🐍 Python Naming Conventions (PEP 8)

This project strictly follows PEP 8 naming conventions to ensure consistency and readability:

### **Naming Standards**
- **Modules/Files**: `snake_case.py` (e.g., `home_controller.py`, `app_service_provider.py`)
- **Directories**: `snake_case/` (e.g., `http/`, `controllers/`, `providers/`)
- **Classes**: `PascalCase` (e.g., `HomeController`, `AppServiceProvider`, `RouteServiceProvider`)
- **Functions/Methods**: `snake_case` (e.g., `register_routes()`, `create_application()`, `configure_flask_app()`)
- **Variables**: `snake_case` (e.g., `flask_app`, `larapy_app`, `base_path`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `APP_NAME`, `APP_DEBUG`, `MAX_CONNECTIONS`)

### **Laravel Compatibility Note**
While Laravel uses PascalCase for directories (e.g., `Http/Controllers/`), we follow Python's PEP 8 convention of snake_case for all module and directory names. This ensures consistency with Python ecosystem standards while maintaining Laravel's familiar structure and functionality.

### **Migration from Laravel-style Naming**
If you're coming from Laravel-style naming, here's the complete mapping:
```
Laravel Style              →  Python PEP 8 Style
app/Console/               →  app/console/
app/Console/Commands/      →  app/console/commands/
app/Events/                →  app/events/
app/Exceptions/            →  app/exceptions/
app/Http/                  →  app/http/
app/Http/Controllers/      →  app/http/controllers/
app/Http/Middleware/       →  app/http/middleware/
app/Http/Requests/         →  app/http/requests/
app/Jobs/                  →  app/jobs/
app/Listeners/             →  app/listeners/
app/Mail/                  →  app/mail/
app/Models/                →  app/models/
app/Notifications/         →  app/notifications/
app/Policies/              →  app/policies/
app/Providers/             →  app/providers/
app/Rules/                 →  app/rules/

# File naming examples
HomeController.php         →  home_controller.py
AppServiceProvider.php     →  app_service_provider.py
UserAuthRequest.php        →  user_auth_request.py
SendEmailJob.php          →  send_email_job.py
```

## 🔧 Development

### Adding New Routes

Edit `routes/web.py`:
```python
# Add to register_routes function
Route.get('/docs', 'app.http.controllers.docs_controller@index').name('docs')
```

### Creating Controllers

Controllers should extend the base `Controller` class:
```python
from .controller import Controller
from larapy.view import View

class DocsController(Controller):
    async def index(self, request):
        return View.render('docs.index', {'title': 'Documentation'})
```

### Adding Views

Create Jinja2 templates in `resources/views/`:
```html
{% extends "layouts/app.html" %}

{% block content %}
<div class="container">
    <h1>{{ title }}</h1>
    <!-- Your content here -->
</div>
{% endblock %}
```

## ⚙️ Configuration System

This project uses a Laravel-like configuration system with proper environment variable handling:

### **Environment Configuration**
- **Environment Variables**: Use `.env` file for environment-specific settings
- **Configuration Files**: Structured config files in `config/` directory
- **Helper Functions**: Laravel-like `env()` and `config()` helpers
- **Caching**: Configuration caching for production performance

### **Configuration Usage**

**Environment Variables (.env):**
```bash
APP_NAME=Larapy Documentation
APP_ENV=production
APP_DEBUG=false
DB_CONNECTION=sqlite
DB_DATABASE=database/database.sqlite
```

**Configuration Files (config/app.py):**
```python
from core.helpers import env

CONFIG = {
    'name': env('APP_NAME', 'Larapy Documentation'),
    'debug': env('APP_DEBUG', False),
    'timezone': env('APP_TIMEZONE', 'UTC'),
}
```

**Using Configuration:**
```python
from core.helpers import config

# Get configuration values
app_name = config('app.name')
debug_mode = config('app.debug')
database_driver = config('database.default')
```

### **Configuration Precedence**
1. System environment variables (highest priority)
2. Environment-specific `.env` files
3. Default `.env` file
4. Default values in configuration files (lowest priority)

### **Configuration Commands**
```bash
# Cache configuration for production
larapy config:cache

# Clear configuration cache
larapy config:clear

# Show current configuration
larapy config:show
```

## 📚 Documentation Structure (Coming Soon)

The website is prepared for comprehensive documentation including:

- **Installation Guide**: Step-by-step setup instructions
- **API Reference**: Complete framework API documentation
- **Examples**: Code samples and tutorials
- **Best Practices**: Recommended patterns and practices

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source. Please check the main Larapy repository for license details.

## 🔗 Links

- [Larapy Framework](https://github.com/larapy/larapy)
- [Documentation](https://docs.larapy.org) (Coming Soon)
- [Examples](https://examples.larapy.org) (Coming Soon)

---

**Built with ❤️ using Larapy - Laravel's elegant syntax meets Python's simplicity**