# Phony targets are targets that don't represent files
.PHONY: build create-test-db clean install-dist build-install

# Default target (runs when you just type 'make')
all: build

# Build the package using Poetry
build:
	@echo "🔨 Building package..."
	poetry build

# Create the test database
create-test-db:
	@echo "💾 Creating test database..."
	poetry run python tests/create_test_db.py

# Clean up build artifacts
clean:
	@echo "🧹 Cleaning up..."
	rm -rf dist build *.egg-info
	# Add other cleanup patterns if needed, e.g.:
	# find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

# install dist package
install-dist:
	@echo "🔧 Installing dist package..."
	# find and install the latest version of the package
	pipx install --force $(shell ls dist/mcp_sqlite_manager-*.whl | tail -1)

# Build and install the package in the current environment
build-install:
	@echo "building and installing package..."
	poetry build
	# find and install the latest version of the package
	pipx install --force $(shell ls dist/mcp_sqlite_manager-*.whl | tail -1)

# Publish the package to PyPI
publish:
	@echo "Publishing package to PyPI..."
	poetry publish --build
