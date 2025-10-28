# Build and Compile Instructions

This document provides comprehensive instructions for building, compiling, and distributing the LoliCode Generator with GUI.

## Quick Start

### Linux/macOS
```bash
./build.sh
```

### Windows
```cmd
build.bat
```

## What the Build Process Does

The build script performs the following steps:

1. **Clean**: Removes previous build artifacts
2. **Compile**: Validates Python syntax for all source files
3. **Test**: Runs the complete test suite (44 tests)
4. **Package**: Creates distributable packages:
   - Source distribution (`.tar.gz`)
   - Wheel distribution (`.whl`)

## Build Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
Install build dependencies:
```bash
pip install pytest pytest-asyncio setuptools wheel
```

## Build Outputs

After a successful build, you'll find the following in the `dist/` directory:

```
dist/
├── lolicode-generator-1.0.0.tar.gz          # Source distribution
└── lolicode_generator-1.0.0-py3-none-any.whl # Wheel distribution
```

## Installation

### Install from Wheel (Recommended)
```bash
pip install dist/lolicode_generator-1.0.0-py3-none-any.whl
```

After installation, you can run the GUI with:
```bash
lolicode-gui
```

### Install from Source
```bash
pip install dist/lolicode-generator-1.0.0.tar.gz
```

### Install in Development Mode
For active development:
```bash
pip install -e .
```

## Manual Build Steps

If you prefer to build manually without the build script:

### 1. Clean Previous Builds
```bash
rm -rf build/ dist/ *.egg-info
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
```

### 2. Compile Python Files (Syntax Check)
```bash
python -m py_compile gui_app.py
python -m py_compile src/generator/*.py
python -m py_compile src/generator/builders/*.py
python -m py_compile src/generator/validators/*.py
```

### 3. Run Tests
```bash
python -m pytest tests/ -v
```

### 4. Build Distributions
```bash
python setup.py sdist bdist_wheel
```

## Package Contents

The built package includes:

### Python Modules
- `generator/` - Core LoliCode generator library
  - `lolicode_generator.py` - Main generator
  - `types.py` - Type definitions
  - `builders/` - Block builders (Request, Keycheck, Parse)
  - `validators/` - Script validators

### GUI Application
- `gui_app.py` - Complete GUI application

### Documentation
- `README.md` - Main documentation
- `GUI_README.md` - GUI user guide
- `GUI_VISUAL_GUIDE.md` - Visual mockups
- `QUICK_REFERENCE.md` - Quick start guide
- `FEATURES_SUMMARY.md` - Feature analysis
- `IMPLEMENTATION_SUMMARY.md` - Implementation details

### Utilities
- `launch_gui.sh` / `launch_gui.bat` - Platform launchers
- `examples/` - Example usage code
- `tests/` - Complete test suite

## Distribution

### PyPI Upload (for maintainers)
```bash
# Install twine
pip install twine

# Upload to PyPI
python -m twine upload dist/*

# Or test on TestPyPI first
python -m twine upload --repository testpypi dist/*
```

### GitHub Release
1. Tag the release:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. Attach the built distributions to the GitHub release

## Verification

### Verify Package Contents
```bash
# List contents of wheel
unzip -l dist/lolicode_generator-1.0.0-py3-none-any.whl

# List contents of source distribution
tar -tzf dist/lolicode-generator-1.0.0.tar.gz
```

### Test Installation
```bash
# Create a test virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the package
pip install dist/lolicode_generator-1.0.0-py3-none-any.whl

# Test the installation
lolicode-gui

# Clean up
deactivate
rm -rf test_env
```

## Troubleshooting

### Build Fails at Compilation Step
**Issue**: Python syntax errors detected
**Solution**: Fix the syntax errors in the reported files

### Build Fails at Test Step
**Issue**: One or more tests failing
**Solution**: Review test output and fix the failing tests

### Missing Dependencies
**Issue**: `ModuleNotFoundError` during build
**Solution**: Install missing dependencies:
```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio setuptools wheel
```

### Wheel Build Fails
**Issue**: `error: invalid command 'bdist_wheel'`
**Solution**: Install wheel package:
```bash
pip install wheel
```

## Platform-Specific Notes

### Linux
- Requires `python3-dev` for some distributions
- Install: `sudo apt-get install python3-dev` (Debian/Ubuntu)

### macOS
- Use Python 3 from Homebrew for best results
- Install: `brew install python@3.11`

### Windows
- Ensure Python is in PATH
- Use Command Prompt or PowerShell as Administrator if needed

## Continuous Integration

The build process is suitable for CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
steps:
  - name: Install dependencies
    run: pip install pytest pytest-asyncio setuptools wheel
  
  - name: Build package
    run: ./build.sh
  
  - name: Upload artifacts
    uses: actions/upload-artifact@v2
    with:
      name: distributions
      path: dist/
```

## Version Management

To release a new version:

1. Update version in `setup.py`
2. Update version references in documentation
3. Run build script
4. Tag the release in git
5. Upload to PyPI (optional)

## Build Artifacts

The build process creates the following artifacts:

```
python_generator/
├── build/                    # Temporary build files (gitignored)
├── dist/                     # Distribution packages (gitignored)
│   ├── *.tar.gz             # Source distribution
│   └── *.whl                # Wheel distribution
├── *.egg-info/              # Package metadata (gitignored)
└── __pycache__/             # Compiled bytecode (gitignored)
```

All build artifacts are excluded from version control via `.gitignore`.

## Support

For build issues:
1. Check this documentation
2. Review error messages carefully
3. Ensure all dependencies are installed
4. Try cleaning and rebuilding
5. Check Python version compatibility

---

**Last Updated**: 2025-10-28
**Build System Version**: 1.0.0
