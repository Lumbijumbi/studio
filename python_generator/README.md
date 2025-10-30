# LoliCode Generator - Python Implementation

A Python implementation of the LoliCode script generator for OpenBullet 2.

## 🎉 NEW: Professional GUI Available!

**Now with a comprehensive graphical user interface!** See [GUI_README.md](GUI_README.md) for details.

### Quick Start with GUI

```bash
python gui_app.py
# Or use the launcher scripts: ./launch_gui.sh (Linux/macOS) or launch_gui.bat (Windows)
```

The GUI provides:
- Visual HAR file import and preview
- Interactive request selection with checkboxes
- Easy configuration of headers, assertions, and extractions
- Live script preview
- One-click export and clipboard copy
- Built-in help and examples

## Features

- Generate LoliCode scripts from HAR (HTTP Archive) analysis
- Support for custom headers, assertions, and variable extractions
- Dependency-based request ordering
- Comprehensive validation
- Type hints and modern Python practices
- **Professional GUI for enhanced user experience**

## Installation

### Quick Install (No Build Required)
```bash
pip install -r requirements.txt
```

### Build and Install as Package

To build and install the package with the GUI:

**Linux/macOS:**
```bash
./build.sh
pip install dist/lolicode_generator-1.0.0-py3-none-any.whl
```

**Windows:**
```cmd
build.bat
pip install dist\lolicode_generator-1.0.0-py3-none-any.whl
```

After installation, launch the GUI with:
```bash
lolicode-gui
```

See [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) for detailed build information.

## Usage

### GUI Mode (Recommended)

```bash
python gui_app.py
```

Or use the platform-specific launchers:
- **Linux/macOS**: `./launch_gui.sh`
- **Windows**: `launch_gui.bat`

See [GUI_README.md](GUI_README.md) and [GUI_VISUAL_GUIDE.md](GUI_VISUAL_GUIDE.md) for complete GUI documentation.

### Programmatic Mode

```python
from src.generator.lolicode_generator import LoliCodeGenerator, LoliCodeConfig

# Create configuration
config = LoliCodeConfig(
    selected_indices=[0, 1, 2],
    settings={
        'use_proxy': True,
        'timeout': 30
    }
)

# Generate LoliCode
generator = LoliCodeGenerator()
script = await generator.generate(config, entries, dependency_matrix)
```

## Testing

```bash
pytest tests/
```

## Project Structure

```
python_generator/
├── gui_app.py                 # GUI Application (NEW!)
├── launch_gui.sh             # GUI Launcher for Linux/macOS (NEW!)
├── launch_gui.bat            # GUI Launcher for Windows (NEW!)
├── GUI_README.md             # GUI Documentation (NEW!)
├── GUI_VISUAL_GUIDE.md       # GUI Visual Guide (NEW!)
├── src/
│   └── generator/
│       ├── __init__.py
│       ├── lolicode_generator.py
│       ├── types.py
│       ├── builders/
│       │   ├── __init__.py
│       │   ├── request_block_builder.py
│       │   ├── keycheck_block_builder.py
│       │   └── parse_block_builder.py
│       └── validators/
│           ├── __init__.py
│           └── lolicode_validator.py
├── tests/
│   ├── __init__.py
│   ├── test_lolicode_generator.py
│   ├── test_request_block_builder.py
│   ├── test_keycheck_block_builder.py
│   ├── test_parse_block_builder.py
│   └── test_lolicode_validator.py
└── examples/
    └── example_usage.py
```
