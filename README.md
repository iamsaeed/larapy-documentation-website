# Larapy Documentation Website

A documentation website for the Larapy framework, built with Laravel-style folder structure and powered by Python.

## 🚀 Features

- **Laravel-style Architecture**: Familiar folder structure with `app/`, `config/`, `routes/`, `resources/`, etc.
- **Modern Web Framework**: Built on top of Larapy framework with FastAPI under the hood
- **Beautiful UI**: Bootstrap-based responsive design with modern components
- **Documentation Ready**: Structure prepared for comprehensive documentation
- **Developer Friendly**: Hot reload, debugging, and development tools

## 📁 Project Structure

```
documentation-webiste-larapy/
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   ├── Controller.py          # Base controller
│   │   │   └── HomeController.py      # Home page controller
│   │   └── Kernel.py                  # HTTP kernel with middleware
│   └── Providers/
│       ├── AppServiceProvider.py      # Application services
│       └── RouteServiceProvider.py    # Route configuration
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

The application follows Laravel conventions:

- **Controllers**: Located in `app/Http/Controllers/`
- **Routes**: Defined in `routes/web.py` and `routes/api.py`
- **Views**: Jinja2 templates in `resources/views/`
- **Configuration**: Settings in `config/` directory
- **Public Assets**: CSS, JS, images in `public/`

## 🔧 Development

### Adding New Routes

Edit `routes/web.py`:
```python
# Add to register_routes function
Route.get('/docs', 'app.Http.Controllers.DocsController@index').name('docs')
```

### Creating Controllers

Controllers should extend the base `Controller` class:
```python
from .Controller import Controller
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