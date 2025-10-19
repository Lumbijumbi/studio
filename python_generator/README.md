# LoliCode Generator - Python Implementation

A Python implementation of the LoliCode script generator for OpenBullet 2.

## Features

- Generate LoliCode scripts from HAR (HTTP Archive) analysis
- Support for custom headers, assertions, and variable extractions
- Dependency-based request ordering
- Comprehensive validation
- Type hints and modern Python practices

## Installation

```bash
pip install -r requirements.txt
```

## Usage

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
└── tests/
    ├── __init__.py
    ├── test_lolicode_generator.py
    ├── test_request_block_builder.py
    ├── test_keycheck_block_builder.py
    ├── test_parse_block_builder.py
    └── test_lolicode_validator.py
```
