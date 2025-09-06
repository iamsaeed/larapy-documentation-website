# My Larapy Project

A Laravel-style Python web application built with the Larapy framework.

## 🚀 Features

- **Laravel-inspired structure** - Familiar directory layout and conventions
- **Larapy ORM** - Eloquent-like database interactions
- **Authentication System** - User authentication and authorization
- **Middleware Support** - Request/response filtering
- **Template Engine** - Jinja2 with Laravel Blade-like helpers
- **Console Commands** - Artisan-equivalent CLI tools
- **Service Container** - Dependency injection system

## 📋 Requirements

- Python 3.8+
- pip (Python package manager)

## 🛠️ Installation

1. **Clone or download this project**

2. **Navigate to the project directory**
   ```bash
   cd my-larapy-project
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the project in development mode (makes `larapy` command available)**
   ```bash
   pip install -e .
   ```

5. **Set up environment**
   ```bash
   cp .env.example .env
   ```

6. **Generate application key**
   ```bash
   larapy key:generate
   ```

7. **Set up database (SQLite for quick start)**
   ```bash
   touch database/database.sqlite
   ```

8. **Run migrations**
   ```bash
   larapy db:migrate
   ```

9. **Seed database (optional)**
   ```bash
   larapy db:seed
   ```

## 🏃‍♂️ Running the Application

### Using the Larapy CLI (Recommended)
```bash
larapy serve
```

### Or run directly
```bash
python public/index.py
```

The application will be available at `http://localhost:8000`

## 🎯 Available Commands

### Server Management
```bash
# Start development server
larapy serve --port 8000 --reload

# Start with custom host and port
larapy serve --host 0.0.0.0 --port 3000
```

### Code Generation
```bash
# Generate a new controller
larapy make:controller UserController --resource

# Generate a new model
larapy make:model Post --migration

# Generate middleware
larapy make:middleware AuthMiddleware

# Generate migration
larapy make:migration create_posts_table
```

### Database Operations
```bash
# Run migrations
larapy db:migrate

# Rollback migrations
larapy db:rollback

# Seed database
larapy db:seed

# Check migration status
larapy db:status
```

### Custom Commands
```bash
# Test command with options
larapy test:command "Your Name" --greeting="Hello"

# Inspirational quotes
larapy inspire

# Greet in different languages
larapy greet "World" --lang=es
```

### Interactive Shell
```bash
# Launch interactive Python shell with app context
larapy tinker
```

## 📁 Project Structure

```
my-larapy-project/
├── app/                    # Application code
│   ├── Console/           # Console commands
│   ├── Http/              # HTTP layer (controllers, middleware, kernel)
│   ├── Models/            # Database models
│   └── Providers/         # Service providers
├── bootstrap/             # Application bootstrap
├── config/                # Configuration files
├── database/              # Database migrations, seeds, factories
├── public/                # Public assets and main entry point
│   └── index.py          # Main application entry point
├── resources/             # Views, CSS, JS, language files
│   └── views/            # Jinja2 templates
├── routes/                # Route definitions
├── storage/               # File storage (logs, cache, uploads)
├── tests/                 # Test files
├── .env.example          # Environment variables template
├── larapy_cli.py         # Global CLI entry point
├── larapy_main.py        # Main CLI application
├── pyproject.toml        # Package configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🧪 Testing

Run tests using pytest:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_example.py

# Run with coverage
pytest --cov=app tests/
```

## 📖 Usage Examples

### Creating Routes
```python
# routes/web.py
from larapy.routing.route import Route

def register_routes(app):
    # Basic route
    Route.get('/', 'app.Http.Controllers.HomeController@index').name('home')
    
    # Route with parameters
    Route.get('/users/{id}', 'app.Http.Controllers.UserController@show')
    
    # Route groups
    Route.group({'prefix': 'api', 'middleware': ['auth']}, lambda: [
        Route.get('/users', 'app.Http.Controllers.Api.UserController@index'),
        Route.post('/users', 'app.Http.Controllers.Api.UserController@store'),
    ])
```

### Using Models
```python
# Interacting with the User model
from app.Models.User import User

# Create a new user
user = User.create({
    'name': 'John Doe',
    'email': 'john@example.com',
    'password': 'secure_password'
})

# Find users
user = User.find(1)
users = User.where('email_verified_at', '!=', None).get()
active_users = User.active().verified().get()
```

### Template Usage
```html
<!-- resources/views/welcome.html -->
{% extends "layouts/app.html" %}

{% block content %}
<div class="container">
    <h1>Welcome, {{ auth.user().name if auth.check() else 'Guest' }}!</h1>
    
    <form method="POST" action="{{ route('users.store') }}">
        {{ csrf_field() }}
        <input type="text" name="name" value="{{ old('name') }}">
        
        {% if errors.has('name') %}
            <div class="error">{{ errors.first('name') }}</div>
        {% endif %}
        
        <button type="submit">Submit</button>
    </form>
</div>
{% endblock %}
```

## 🔧 Configuration

### Database Configuration
Edit `config/database.py` to configure your database connections.

### Application Configuration  
Edit `config/app.py` for application-wide settings.

### Environment Variables
Copy `.env.example` to `.env` and configure your environment-specific settings.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Format code (`black .`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## 📄 License

This project is open-sourced software licensed under the MIT license.

## 🆘 Support

- 📧 Issues: Report bugs and request features via GitHub issues
- 📖 Documentation: Visit the [Larapy documentation](https://github.com/larapy/larapy)
- 💬 Community: Join discussions on GitHub

## 🙏 Acknowledgments

- Inspired by [Laravel](https://laravel.com) - The PHP Framework for Web Artisans
- Built with [Larapy](https://github.com/larapy/larapy) - Laravel's elegance in Python
- Powered by [FastAPI](https://fastapi.tiangolo.com/) and [Starlette](https://starlette.io/)

---

**Made with ❤️ using Larapy - Laravel's elegant syntax meets Python's simplicity**