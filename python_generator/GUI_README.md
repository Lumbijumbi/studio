# LoliCode Generator - GUI Application

## Overview

A comprehensive, professional-grade graphical user interface for the LoliCode Generator. This GUI provides an intuitive, efficient way to create OpenBullet 2 configurations from HAR files or manual input.

## Features

### 🎯 Core Features

- **HAR File Import**: Directly load and parse HAR files from browser developer tools
- **Example Data**: Quick-start with built-in example data
- **Visual Request Selection**: Easy checkbox-based selection of HTTP requests
- **Live Preview**: Real-time generation and preview of LoliCode scripts
- **Export Options**: Save to file or copy to clipboard

### 🔧 Advanced Configuration

- **Custom Headers**: Add API keys, authentication tokens, and custom headers per request
- **Assertions/Keychecks**: Define success/fail conditions with multiple types:
  - Status code checks
  - Contains text searches
  - Regex pattern matching
  - JSON path queries
- **Variable Extractions**: Extract values from responses for use in subsequent requests:
  - Regex extraction
  - JSON path extraction
  - CSS selector extraction
  - XPath extraction
- **Global Settings**: Configure proxy, redirects, timeouts, and retry counts

### 🎨 User Experience Enhancements

- **Tabbed Interface**: Organized workflow with 8 dedicated tabs
- **Bulk Operations**: Select all, deselect all, invert selection
- **Quick Presets**: Fast mode, Secure mode, and Default mode presets
- **Status Bar**: Real-time feedback on operations
- **Visual Feedback**: Comprehensive dialogs and messages
- **Keyboard Shortcuts**: Quick access to common operations

## Installation

### Prerequisites

```bash
# Python 3.8 or higher
# tkinter (usually comes with Python)

# On Ubuntu/Debian, if tkinter is not installed:
sudo apt-get install python3-tk

# On macOS, tkinter comes with Python
# On Windows, tkinter comes with Python
```

### Install Dependencies

```bash
cd python_generator
pip install -r requirements.txt
```

## Usage

### Launch the GUI

```bash
python gui_app.py
```

Or use the launcher script:

```bash
./launch_gui.sh    # Linux/macOS
launch_gui.bat     # Windows
```

### Quick Start Guide

1. **Start the Application**
   - Run `python gui_app.py`
   - The GUI will open with a welcome screen

2. **Load Data**
   - Click "📁 Load HAR File" to import a HAR file, OR
   - Click "📝 Load Example" to try with sample data

3. **Select Requests**
   - Go to the "📋 Select Requests" tab
   - Check the boxes for requests you want in your script
   - Use bulk operation buttons for convenience

4. **Configure (Optional)**
   - **Headers Tab**: Add custom headers like API keys
   - **Assertions Tab**: Define success/fail conditions
   - **Extractions Tab**: Extract variables from responses
   - **Settings Tab**: Configure global script settings

5. **Generate & Export**
   - Click "🔄 Generate Preview" to see your script
   - Review in the "👁 Preview Script" tab
   - Click "💾 Save Script" or "📋 Copy to Clipboard"

## GUI Layout

### Toolbar (Top)
- 📁 Load HAR File
- 📝 Load Example
- 🔄 Generate Preview
- 💾 Save Script
- 📋 Copy to Clipboard
- 🔧 Quick Settings

### Tabs

1. **📥 Import Data**
   - Welcome instructions
   - Data preview in tree view
   - Shows all loaded requests

2. **📋 Select Requests**
   - Checkbox list of all requests
   - Bulk operation buttons
   - Shows URL, method for each request

3. **📄 Custom Headers**
   - Add custom headers per request
   - Supports variables in values
   - Delete unwanted headers

4. **✓ Assertions**
   - Add keychecks/assertions
   - Multiple types: status, contains, regex, json-path
   - Actions: success, fail, retry, ban

5. **🔍 Variable Extractions**
   - Extract values from responses
   - Types: regex, json, css, xpath
   - Global or local scope

6. **⚙️ Settings**
   - Use Proxy toggle
   - Follow Redirects toggle
   - Timeout configuration
   - Retry count
   - Quick presets

7. **👁 Preview Script**
   - Live preview of generated LoliCode
   - Syntax-friendly monospace font
   - Quick export buttons

8. **❓ Help**
   - Comprehensive user guide
   - Tips and tricks
   - Keyboard shortcuts
   - Common patterns reference

### Status Bar (Bottom)
- Shows current operation status
- Timestamp of last action

## Keyboard Shortcuts

- `Ctrl+L`: Load HAR file
- `Ctrl+E`: Load example
- `Ctrl+G`: Generate preview
- `Ctrl+S`: Save script
- `Ctrl+C`: Copy to clipboard (when preview focused)

## Tips & Best Practices

### For Beginners
- Start with the example data to learn the interface
- Use the Help tab as a reference
- Test with simple requests before complex workflows

### For Power Users
- Use keyboard shortcuts for faster workflow
- Leverage quick presets for common configurations
- Use descriptive variable names for maintainability
- Test regex patterns before adding to extractions

### Common Workflows

#### Login Flow with Token Extraction
1. Load HAR with login sequence
2. Select GET login page + POST login + GET protected resource
3. Add extraction for auth token from POST response
4. Add assertion on POST to check for "success"
5. Generate and export

#### API Testing
1. Load HAR with API calls
2. Select relevant API endpoints
3. Add custom headers (API keys)
4. Add status code assertions
5. Add JSON response extractions
6. Generate script

## Examples

### Adding Custom Header
1. Go to "📄 Custom Headers" tab
2. Set Request Index: `0`
3. Header Key: `X-API-Key`
4. Header Value: `your-api-key-123`
5. Click "➕ Add Header"

### Adding Variable Extraction
1. Go to "🔍 Variable Extractions" tab
2. Set Request Index: `1`
3. Type: `json`
4. Pattern: `$.token`
5. Variable Name: `auth_token`
6. Check "Global"
7. Click "➕ Add Extraction"

### Adding Assertion
1. Go to "✓ Assertions" tab
2. Set Request Index: `1`
3. Type: `contains`
4. Value: `success`
5. Action: `success`
6. Click "➕ Add Assertion"

## Troubleshooting

### GUI Won't Launch
- **Issue**: `ModuleNotFoundError: No module named 'tkinter'`
- **Solution**: Install tkinter for your system (see Installation section)

### Can't Load HAR File
- **Issue**: Error loading HAR file
- **Solution**: Ensure the file is valid JSON and follows HAR format

### Generated Script Invalid
- **Issue**: Script validation fails
- **Solution**: Check that selected requests are valid and indices are correct

### Preview Not Updating
- **Issue**: Preview doesn't show new changes
- **Solution**: Click "🔄 Generate Preview" after making changes

## Architecture

The GUI is built with:
- **tkinter**: Python's standard GUI library
- **ttk**: Themed widget set for modern appearance
- **asyncio**: For async script generation
- **Modular Design**: Separate concerns for maintainability

## Development

### Code Structure
```python
class LoliCodeGUI:
    - __init__(): Initialize GUI and data structures
    - _setup_ui(): Create all UI components
    - _create_*_tab(): Create individual tabs
    - Event handlers for user interactions
    - Data processing and validation
    - Script generation and export
```

### Key Components
- Data storage for entries, headers, assertions, extractions
- Integration with LoliCodeGenerator
- Validation and error handling
- User feedback through dialogs and status bar

## Future Enhancements

Potential features for future versions:
- Drag-and-drop request ordering
- Visual dependency graph
- Template system for common patterns
- Import/Export configurations
- Multi-language support
- Dark mode theme
- Syntax highlighting in preview
- Advanced search and filter
- Batch processing multiple HAR files

## Contributing

To contribute to the GUI:
1. Test thoroughly on your platform
2. Follow the existing code style
3. Add comments for complex logic
4. Update this README with new features

## License

Same as the main project.

## Support

For issues, questions, or feature requests:
- Check the Help tab in the application
- Review this README
- Check the main project documentation
- Open an issue on GitHub

---

**Built with ❤️ for the OpenBullet 2 community**
