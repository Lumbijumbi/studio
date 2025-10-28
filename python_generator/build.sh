#!/bin/bash
# Build and compile script for LoliCode Generator

set -e

echo "════════════════════════════════════════════════════════════"
echo "  LoliCode Generator - Build & Compile Script"
echo "════════════════════════════════════════════════════════════"
echo ""

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📁 Working directory: $SCRIPT_DIR"
echo ""

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info __pycache__ src/**/__pycache__ 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.pyo" -delete 2>/dev/null || true
echo "   ✓ Cleaned"
echo ""

# Compile Python files (syntax check)
echo "🔨 Compiling Python files..."
python3 -m py_compile gui_app.py
python3 -m py_compile src/generator/*.py
python3 -m py_compile src/generator/builders/*.py
python3 -m py_compile src/generator/validators/*.py
echo "   ✓ All Python files compiled successfully"
echo ""

# Run tests
echo "🧪 Running tests..."
python3 -m pytest tests/ -v --tb=short
if [ $? -eq 0 ]; then
    echo "   ✓ All tests passed"
else
    echo "   ✗ Tests failed!"
    exit 1
fi
echo ""

# Build source distribution
echo "📦 Building source distribution..."
python3 setup.py sdist
echo "   ✓ Source distribution created"
echo ""

# Build wheel distribution
echo "📦 Building wheel distribution..."
python3 setup.py bdist_wheel 2>/dev/null || python3 -m pip install wheel && python3 setup.py bdist_wheel
echo "   ✓ Wheel distribution created"
echo ""

# List built files
echo "📋 Built files:"
ls -lh dist/
echo ""

# Installation instructions
echo "════════════════════════════════════════════════════════════"
echo "  Build Complete! ✓"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "To install the package:"
echo "  pip install dist/lolicode_generator-1.0.0-py3-none-any.whl"
echo ""
echo "To run the GUI after installation:"
echo "  lolicode-gui"
echo ""
echo "Or run directly:"
echo "  python3 gui_app.py"
echo ""
