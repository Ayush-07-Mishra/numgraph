#!/bin/bash
# Development setup script for numgraph

echo "=================================="
echo "numgraph Development Setup"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
python --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install in development mode
echo ""
echo "Installing numgraph in development mode..."
pip install -e ".[dev]"

# Run tests to verify installation
echo ""
echo "Running tests to verify installation..."
pytest tests/ -v

echo ""
echo "=================================="
echo "✓ Setup complete!"
echo "=================================="
echo ""
echo "To activate the virtual environment, run:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "  venv\\Scripts\\activate"
else
    echo "  source venv/bin/activate"
fi
echo ""
echo "Try the quickstart:"
echo "  python quickstart.py"
echo ""
echo "Run examples:"
echo "  python examples/circle_equation.py"
echo ""
