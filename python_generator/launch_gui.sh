#!/bin/bash
# LoliCode Generator GUI Launcher Script for Linux/macOS

echo "======================================"
echo "LoliCode Generator GUI Launcher"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo ""
    echo "Warning: tkinter is not installed!"
    echo ""
    echo "To install tkinter:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "  Fedora: sudo dnf install python3-tkinter"
    echo "  Arch: sudo pacman -S tk"
    echo ""
    read -p "Press Enter to continue anyway (will fail if tkinter is missing)..."
fi

# Check if requirements are installed
echo ""
echo "Checking dependencies..."
if ! python3 -c "import pytest" 2>/dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

echo ""
echo "Launching LoliCode Generator GUI..."
echo ""
python3 gui_app.py

echo ""
echo "GUI closed."
