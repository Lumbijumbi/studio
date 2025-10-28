# LoliCode Generator GUI - Quick Reference Card

## 🚀 Quick Start

```bash
python gui_app.py
```

## 🎯 Main Features at a Glance

### Toolbar Actions
| Button | Action | Shortcut |
|--------|--------|----------|
| 📁 Load HAR File | Import HAR from browser | Ctrl+L |
| 📝 Load Example | Try with sample data | Ctrl+E |
| 🔄 Generate Preview | Create LoliCode script | Ctrl+G |
| 💾 Save Script | Save to .loli file | Ctrl+S |
| 📋 Copy to Clipboard | Copy script text | Ctrl+C |
| 🔧 Quick Settings | Open settings dialog | - |

### Tab Navigation
| Tab | Purpose | Key Features |
|-----|---------|--------------|
| 📥 Import Data | Load and view data | HAR import, tree view, welcome guide |
| 📋 Select Requests | Choose requests | Checkboxes, bulk operations |
| 📄 Custom Headers | Add headers | Per-request headers, variable support |
| ✓ Assertions | Define checks | Status/contains/regex/json-path |
| 🔍 Variable Extractions | Extract data | Regex/JSON/CSS/XPath patterns |
| ⚙️ Settings | Global config | Proxy, timeout, retry, presets |
| 👁 Preview Script | View output | Live preview, syntax display |
| ❓ Help | Get assistance | Full guide, tips, examples |

## 📋 Common Workflows

### Workflow 1: Basic HAR Import
1. Click "📁 Load HAR File"
2. Select your .har file
3. Go to "📋 Select Requests" tab
4. Check desired requests
5. Click "🔄 Generate Preview"
6. Click "💾 Save Script"

### Workflow 2: Using Example Data
1. Click "📝 Load Example"
2. Explore the pre-configured example
3. Go to "👁 Preview Script"
4. Click "🔄 Refresh Preview"
5. Review generated script

### Workflow 3: Custom Configuration
1. Load data (HAR or example)
2. Select requests in "📋 Select Requests"
3. Add headers in "📄 Custom Headers"
4. Add assertions in "✓ Assertions"
5. Add extractions in "🔍 Variable Extractions"
6. Configure in "⚙️ Settings"
7. Preview and export

## 🔧 Settings Presets

| Preset | Use Case | Configuration |
|--------|----------|---------------|
| 🚀 Fast Mode | Testing, Development | No proxy, 10s timeout |
| 🛡 Secure Mode | Production, Security | Proxy enabled, 60s timeout, 3 retries |
| ⚡ Default Mode | General use | Proxy enabled, 30s timeout |

## 📝 Common Patterns

### Variable Extraction Patterns
```
CSRF Token (regex):    name="csrf" value="([^"]+)"
JSON Token:            $.data.token
Auth Header (regex):   Authorization: Bearer ([^\s]+)
Session Cookie:        Set-Cookie: session=([^;]+)
```

### Assertion Examples
```
Status Check:    Type: status,    Value: 200
Contains Text:   Type: contains,  Value: success
Regex Match:     Type: regex,     Value: "error":\s*false
JSON Path:       Type: json-path, Value: $.success
```

### Variable Syntax
```
<INPUT.USERNAME>          - User input
<csrf_token>              - Extracted variable
<RESPONSE.STATUS>         - Response status
<RESPONSE.BODY>           - Response body
<auth_token>              - Custom variable
```

## 💡 Pro Tips

1. **Start Simple**: Begin with the example data to learn the interface
2. **Use Descriptive Names**: Name variables clearly (e.g., "auth_token" not "t1")
3. **Test Patterns**: Verify regex patterns before adding them
4. **Bulk Operations**: Use "Select All" then deselect unwanted requests
5. **Quick Settings**: Use presets to avoid manual configuration
6. **Status Bar**: Check status bar for operation feedback
7. **Help Tab**: Reference the help tab for detailed information
8. **Save Often**: Export your script regularly during configuration

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| GUI won't start | Install tkinter for your system: |
|                 | Ubuntu/Debian: `sudo apt-get install python3-tk` |
|                 | Fedora/RHEL: `sudo dnf install python3-tkinter` |
|                 | Arch Linux: `sudo pacman -S tk` |
|                 | macOS/Windows: tkinter included with Python |
| Can't load HAR | Ensure valid JSON format |
| Preview empty | Select at least one request first |
| Script invalid | Check indices and patterns are correct |
| Changes not showing | Click "🔄 Generate Preview" to refresh |

## 🎓 Learning Path

### Beginner
1. Load example data
2. Explore each tab
3. Generate preview without changes
4. Try modifying settings

### Intermediate
1. Load your own HAR file
2. Select specific requests
3. Add custom headers
4. Add simple assertions

### Advanced
1. Complex variable extractions
2. Multi-step authentication flows
3. Custom regex patterns
4. Multiple assertions per request

## 📊 GUI Statistics

- **8 Dedicated Tabs** for organized workflow
- **6 Quick-Access Buttons** on toolbar
- **3 Settings Presets** for common scenarios
- **4 Extraction Types** (regex, json, css, xpath)
- **4 Assertion Types** (status, contains, regex, json-path)
- **Unlimited** custom headers per request
- **Real-time** status updates
- **Full** keyboard shortcut support

## 🌟 Key Benefits

✓ **No Command Line Required** - Pure GUI experience
✓ **Visual Feedback** - See everything at a glance
✓ **Error Prevention** - Validation before operations
✓ **Time Saving** - Bulk operations and presets
✓ **Learning Friendly** - Built-in examples and help
✓ **Professional** - Modern, organized interface
✓ **Cross-Platform** - Works on Windows, Linux, macOS
✓ **Zero Dependencies** - Uses built-in tkinter library

## 📚 Documentation

- **GUI_README.md** - Complete user guide
- **GUI_VISUAL_GUIDE.md** - Visual layouts and mockups
- **This file** - Quick reference
- **Help Tab** - In-app comprehensive guide

## 🎯 Next Steps

1. **Launch**: Run `python gui_app.py`
2. **Explore**: Try the example data
3. **Experiment**: Modify settings and configurations
4. **Create**: Generate your first LoliCode script
5. **Share**: Export and use in OpenBullet 2

---

**Happy LoliCode Generation! 🎉**

*For detailed documentation, see GUI_README.md*
