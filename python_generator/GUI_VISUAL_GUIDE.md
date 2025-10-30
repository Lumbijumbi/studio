# LoliCode Generator GUI - Visual Guide

## GUI Screenshots and Layout

Since tkinter may not be available in all environments, this document provides a visual representation of the GUI layout.

## Main Window

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LoliCode Generator - Professional GUI                                      [_][□][X]│
├─────────────────────────────────────────────────────────────────────────────────┤
│ Toolbar:                                                                         │
│ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐  │
│ │📁 Load HAR File│ │📝 Load Example │ │🔄 Generate     │ │💾 Save Script  │  │
│ └────────────────┘ └────────────────┘ │   Preview      │ └────────────────┘  │
│                                        └────────────────┘                       │
│ ┌────────────────┐ ┌────────────────┐                                          │
│ │📋 Copy to      │ │🔧 Quick        │                                          │
│ │   Clipboard    │ │   Settings     │                                          │
│ └────────────────┘ └────────────────┘                                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Tabs:                                                                            │
│ ┌───────────────────────────────────────────────────────────────────────────┐  │
│ │ [📥 Import Data] [📋 Select Requests] [📄 Custom Headers] [✓ Assertions] │  │
│ │ [🔍 Variable Extractions] [⚙️ Settings] [👁 Preview Script] [❓ Help]     │  │
│ ├───────────────────────────────────────────────────────────────────────────┤  │
│ │                                                                           │  │
│ │  TAB CONTENT AREA (See individual tab layouts below)                     │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ │                                                                           │  │
│ └───────────────────────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Status: 14:23:45 - Ready                                                         │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Tab 1: Import Data

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📥 Import Data                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│ ┌─ Instructions ───────────────────────────────────────────────────────────┐│
│ │ Welcome to LoliCode Generator!                                           ││
│ │                                                                           ││
│ │ 1. Load a HAR file or use the example data to get started               ││
│ │ 2. Select the requests you want to include in your script               ││
│ │ 3. Configure headers, assertions, and variable extractions              ││
│ │ 4. Adjust settings for your requirements                                ││
│ │ 5. Preview and save your generated LoliCode script                      ││
│ │                                                                           ││
│ │ Tip: Use the toolbar buttons for quick access to common actions!        ││
│ └───────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│ ┌─ Loaded Data Preview ────────────────────────────────────────────────────┐│
│ │ Index │ Method │ URL                                      │ Status      │││
│ │───────┼────────┼──────────────────────────────────────────┼─────────────│││
│ │  0    │ GET    │ https://example.com/login                │ 200         │││
│ │  1    │ POST   │ https://example.com/api/auth/login       │ 200         │││
│ │  2    │ GET    │ https://example.com/api/profile          │ 200         │││
│ │       │        │                                          │             │││
│ │       │        │                                          │             │││
│ │       │        │                                          │             │││
│ └───────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tab 2: Select Requests

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📋 Select Requests                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ Select which requests to include in your LoliCode script:                   │
│                                                                              │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                           │
│ │✓ Select All │ │✗ Deselect   │ │🔄 Invert    │                           │
│ └─────────────┘ │  All        │ │  Selection  │                           │
│                 └─────────────┘ └─────────────┘                           │
│ ┌─ Requests ──────────────────────────────────────────────────────────────┐│
│ │ ☑ [0] GET - https://example.com/login                                   ││
│ │ ☑ [1] POST - https://example.com/api/auth/login                         ││
│ │ ☑ [2] GET - https://example.com/api/profile                             ││
│ │ ☐ [3] GET - https://example.com/api/settings                            ││
│ │ ☐ [4] POST - https://example.com/api/update                             ││
│ │                                                                          ││
│ │                                                                          ││
│ │                                                                          ││
│ │                                                                          ││
│ │                                                                          ││
│ │                                                                          ││
│ └──────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tab 3: Custom Headers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📄 Custom Headers                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ Add custom headers to specific requests:                                    │
│                                                                              │
│ Request Index: [0▼] Header Key: [X-API-Key     ] Header Value:             │
│ [your-api-key-123                    ] ┌────────────┐                      │
│                                        │➕ Add      │                      │
│                                        │  Header    │                      │
│                                        └────────────┘                      │
│ ┌─ Configured Headers ────────────────────────────────────────────────────┐│
│ │ Request Index │ Header Key      │ Header Value                         │││
│ │───────────────┼─────────────────┼──────────────────────────────────────│││
│ │ 0             │ X-API-Key       │ your-api-key-123                     │││
│ │ 1             │ Authorization   │ Bearer <auth_token>                  │││
│ │               │                 │                                      │││
│ │               │                 │                                      │││
│ │               │                 │                                      │││
│ └──────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│                    ┌────────────────────────────┐                           │
│                    │🗑 Delete Selected Header   │                           │
│                    └────────────────────────────┘                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tab 4: Assertions

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ✓ Assertions                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ Add custom assertions/keychecks to validate responses:                      │
│                                                                              │
│ Request Index: [1▼] Type: [contains ▼] Value: [success              ]     │
│ Action: [success▼] ┌────────────┐                                          │
│                    │➕ Add      │                                          │
│                    │  Assertion │                                          │
│                    └────────────┘                                          │
│ ┌─ Configured Assertions ─────────────────────────────────────────────────┐│
│ │ Request Index │ Assertion Type │ Value/Pattern    │ Action            │││
│ │───────────────┼────────────────┼──────────────────┼───────────────────│││
│ │ 1             │ contains       │ success          │ success           │││
│ │ 2             │ status         │ 200              │ success           │││
│ │               │                │                  │                   │││
│ │               │                │                  │                   │││
│ │               │                │                  │                   │││
│ └──────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│                    ┌────────────────────────────┐                           │
│                    │🗑 Delete Selected Assertion│                           │
│                    └────────────────────────────┘                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tab 5: Variable Extractions

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🔍 Variable Extractions                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ Extract variables from responses for use in subsequent requests:            │
│                                                                              │
│ Request Index: [1▼] Type: [json▼] Pattern: [$.token              ]         │
│ Variable Name: [auth_token  ] ☑ Global  ┌────────────┐                    │
│                                          │➕ Add      │                    │
│                                          │  Extraction│                    │
│                                          └────────────┘                    │
│ ┌─ Configured Variable Extractions ───────────────────────────────────────┐│
│ │ Request │ Type  │ Pattern              │ Variable Name │ Global        │││
│ │─────────┼───────┼──────────────────────┼───────────────┼───────────────│││
│ │ 1       │ json  │ $.token              │ auth_token    │ Yes           │││
│ │ 0       │ regex │ csrf="([^"]+)"       │ csrf_token    │ Yes           │││
│ │         │       │                      │               │               │││
│ │         │       │                      │               │               │││
│ │         │       │                      │               │               │││
│ └──────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│                    ┌────────────────────────────┐                           │
│                    │🗑 Delete Selected Extraction│                          │
│                    └────────────────────────────┘                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tab 6: Settings

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ Settings                                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ Configure global script settings:                                           │
│                                                                              │
│ ┌─ Script Settings ───────────────────────────────────────────────────────┐│
│ │                                                                          ││
│ │  ☑ Use Proxy                                                            ││
│ │                                                                          ││
│ │  ☑ Follow Redirects                                                     ││
│ │                                                                          ││
│ │  Timeout (seconds):        [30▼]                                        ││
│ │                                                                          ││
│ │  Retry Count:              [0▼]                                         ││
│ │                                                                          ││
│ │                     ┌────────────────┐                                  ││
│ │                     │✓ Apply Settings│                                  ││
│ │                     └────────────────┘                                  ││
│ │                                                                          ││
│ └──────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│ ┌─ Quick Presets ─────────────────────────────────────────────────────────┐│
│ │ ┌──────────────────────────────────────────────────────────────────┐   ││
│ │ │🚀 Fast Mode (No Proxy, 10s timeout)                              │   ││
│ │ └──────────────────────────────────────────────────────────────────┘   ││
│ │ ┌──────────────────────────────────────────────────────────────────┐   ││
│ │ │🛡 Secure Mode (Proxy, 60s timeout, 3 retries)                    │   ││
│ │ └──────────────────────────────────────────────────────────────────┘   ││
│ │ ┌──────────────────────────────────────────────────────────────────┐   ││
│ │ │⚡ Default Mode                                                    │   ││
│ │ └──────────────────────────────────────────────────────────────────┘   ││
│ └──────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tab 7: Preview Script

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 👁 Preview Script                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ Live preview of your generated LoliCode script:                             │
│                                                                              │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                        │
│ │🔄 Refresh    │ │💾 Save to    │ │📋 Copy to    │                        │
│ │  Preview     │ │  File        │ │  Clipboard   │                        │
│ └──────────────┘ └──────────────┘ └──────────────┘                        │
│                                                                              │
│ ┌─ Generated LoliCode Script ─────────────────────────────────────────────┐│
│ │# ═══════════════════════════════════════════════════════════════        │││
│ │# Generated by HAR2LoliCode (Python)                                     │││
│ │# Date: 2025-10-28T21:29:06.663370+00:00                                │││
│ │# Description: Automated script from HAR analysis                        │││
│ │# ═══════════════════════════════════════════════════════════════        │││
│ │                                                                          │││
│ │SETTINGS                                                                  │││
│ │  UseProxy: true                                                          │││
│ │  FollowRedirects: true                                                   │││
│ │  Timeout: 30                                                             │││
│ │                                                                          │││
│ │# ─────────────────────────────────────────────────────────────          │││
│ │# Request 1: GET /login                                                   │││
│ │# ─────────────────────────────────────────────────────────────          │││
│ │REQUEST "https://example.com/login"                                       │││
│ │  "accept: text/html"                                                     │││
│ │KEYCHECK SUCCESS                                                          │││
│ │  KEY "<RESPONSE.STATUS>" Equal "200"                                     │││
│ └──────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tab 8: Help

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ❓ Help                                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ ╔══════════════════════════════════════════════════════════════════════╗  │
│ ║              LoliCode Generator - User Guide                         ║  │
│ ╚══════════════════════════════════════════════════════════════════════╝  │
│                                                                              │
│ OVERVIEW:                                                                    │
│ This application helps you generate LoliCode scripts for OpenBullet 2       │
│ from HAR (HTTP Archive) files or manual configuration.                      │
│                                                                              │
│ HOW TO USE:                                                                  │
│                                                                              │
│ 1. IMPORT DATA                                                               │
│    - Click "Load HAR File" to import a HAR file from your browser          │
│    - Or click "Load Example" to try it with sample data                    │
│    - View the loaded requests in the Import Data tab                       │
│                                                                              │
│ 2. SELECT REQUESTS                                                           │
│    - Go to the "Select Requests" tab                                        │
│    - Check the boxes for requests you want to include                      │
│    - Use "Select All", "Deselect All", or "Invert Selection"              │
│                                                                              │
│ [... more help content scrolls here ...]                                    │
│                                                                              │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│ Generated by: LoliCode Generator GUI v1.0                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Quick Settings Dialog

```
┌────────────────────────────────┐
│ Quick Settings            [X]   │
├────────────────────────────────┤
│                                │
│    Quick Settings              │
│                                │
│  ┌────────────────────────────┐│
│  │🚀 Fast Mode                ││
│  └────────────────────────────┘│
│  ┌────────────────────────────┐│
│  │🛡 Secure Mode              ││
│  └────────────────────────────┘│
│  ┌────────────────────────────┐│
│  │⚡ Default Mode             ││
│  └────────────────────────────┘│
│  ──────────────────────────────│
│  ┌────────────────────────────┐│
│  │Cancel                      ││
│  └────────────────────────────┘│
│                                │
└────────────────────────────────┘
```

## Key Visual Features

### Color Scheme
- **Background**: Light gray (#f0f0f0)
- **Foreground**: Black (#000000)
- **Buttons**: Standard themed buttons with padding
- **Labels**: Padding for better spacing
- **Tree views**: Alternating row colors for readability

### Layout Principles
- **Consistent Spacing**: 10px padding on frames
- **Clear Hierarchy**: Labeled frames for grouping
- **Responsive Design**: Components resize with window
- **Visual Feedback**: Status bar with timestamps
- **Emoji Icons**: Clear, universal icons for functions

### User Experience
- **Progressive Disclosure**: Complex features hidden in tabs
- **Bulk Operations**: Convenient buttons for common tasks
- **Real-time Feedback**: Status updates on all actions
- **Error Prevention**: Validation before operations
- **Help Always Available**: Dedicated help tab with full guide

## Window Sizes

- **Default**: 1400x900 pixels
- **Minimum**: Recommended 1024x768
- **Resizable**: Yes, components adjust automatically

## Theme

The GUI uses the 'clam' theme from ttk, which provides:
- Modern, flat design
- Cross-platform consistency
- Professional appearance
- Good contrast and readability

---

This visual guide provides a complete overview of the GUI layout and features without needing to run the application.
