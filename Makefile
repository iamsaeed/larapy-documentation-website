# Larapy Documentation Website Makefile
# Quick commands for development workflow

.PHONY: help install update update-force test migrate serve clean check

# Default target
help:
	@echo "🚀 Larapy Documentation Website Development Commands"
	@echo "=================================================="
	@echo ""
	@echo "Package Management:"
	@echo "  install       - Install all dependencies"
	@echo "  update        - Update larapy package from local source"
	@echo "  update-force  - Force update even if no changes detected"
	@echo "  check         - Check package status"
	@echo ""
	@echo "Development:"
	@echo "  serve         - Start development server"
	@echo "  test          - Run tests"
	@echo "  migrate       - Run database migrations"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean         - Clean cache and temporary files"
	@echo ""
	@echo "Examples:"
	@echo "  make update && make serve"
	@echo "  make update-force test"

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

update:
	@echo "🔄 Updating larapy package..."
	./dev_update.sh

update-force:
	@echo "🔄 Force updating larapy package..."
	./dev_update.sh --force

update-quick:
	@echo "⚡ Quick package update..."
	python simple_update.py

check:
	@echo "📋 Checking package status..."
	python simple_update.py --check

test:
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v

migrate:
	@echo "🗄️ Running migrations..."
	larapy migrate

migrate-fresh:
	@echo "🗄️ Fresh migration..."
	larapy migrate fresh --seed

serve:
	@echo "🌐 Starting development server..."
	python public/index.py

serve-debug:
	@echo "🐛 Starting development server in debug mode..."
	FLASK_ENV=development FLASK_DEBUG=1 python public/index.py

clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	rm -rf .pytest_cache/ htmlcov/ .backup_requirements.txt .last_package_update

lint:
	@echo "🔍 Running linting..."
	flake8 app/ tests/
	black --check app/ tests/

format:
	@echo "✨ Formatting code..."
	black app/ tests/

# Combo commands
dev: update serve
	@echo "🚀 Development environment ready!"

fresh: clean install update migrate-fresh
	@echo "🆕 Fresh environment setup complete!"

ci: install update test lint
	@echo "🔄 CI pipeline complete!"
