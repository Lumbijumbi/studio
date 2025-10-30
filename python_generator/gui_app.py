"""
LoliCode Generator GUI Application
A comprehensive graphical user interface for generating LoliCode scripts.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import asyncio
import sys
import os
from datetime import datetime
from typing import List, Dict, Optional, Any

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from generator import (
    LoliCodeGenerator,
    LoliCodeConfig,
    SemanticHarEntry,
    SemanticHarRequest,
    SemanticHarResponse,
    RequestBody,
    DependencyMatrix,
    CustomHeader,
    CustomAssertion,
    VariableExtraction,
)


class LoliCodeGUI:
    """Main GUI application for LoliCode Generator."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("LoliCode Generator - Professional GUI")
        self.root.geometry("1400x900")
        
        # Data storage
        self.har_data: List[Dict[str, Any]] = []
        self.entries: List[SemanticHarEntry] = []
        self.selected_indices: List[int] = []
        self.custom_headers: Dict[int, List[CustomHeader]] = {}
        self.custom_assertions: Dict[int, List[CustomAssertion]] = {}
        self.variable_extractions: Dict[int, List[VariableExtraction]] = {}
        self.settings: Dict[str, Any] = {
            'use_proxy': True,
            'follow_redirects': True,
            'timeout': 30,
            'retry_count': 0
        }
        
        # Generator instance
        self.generator = LoliCodeGenerator()
        
        # Setup UI
        self._setup_ui()
        self._apply_theme()
        
    def _setup_ui(self):
        """Setup the main UI components."""
        # Create main container with padding
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure root grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        main_container.rowconfigure(1, weight=1)
        
        # Top toolbar
        self._create_toolbar(main_container)
        
        # Main notebook (tabbed interface)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Create tabs
        self._create_import_tab()
        self._create_requests_tab()
        self._create_headers_tab()
        self._create_assertions_tab()
        self._create_extractions_tab()
        self._create_settings_tab()
        self._create_preview_tab()
        self._create_help_tab()
        
        # Status bar
        self._create_status_bar(main_container)
        
    def _create_toolbar(self, parent):
        """Create the top toolbar."""
        toolbar = ttk.Frame(parent)
        toolbar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(toolbar, text="📁 Load HAR File", command=self._load_har_file, width=20).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📝 Load Example", command=self._load_example, width=20).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🔄 Generate Preview", command=self._generate_preview, width=20).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="💾 Save Script", command=self._save_script, width=20).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📋 Copy to Clipboard", command=self._copy_to_clipboard, width=20).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🔧 Quick Settings", command=self._show_quick_settings, width=20).pack(side=tk.LEFT, padx=2)
        
    def _create_import_tab(self):
        """Create the import/data tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="📥 Import Data")
        
        # Instructions
        instructions = ttk.LabelFrame(frame, text="Instructions", padding="10")
        instructions.pack(fill=tk.X, pady=5)
        
        instructions_text = """
Welcome to LoliCode Generator!

1. Load a HAR file or use the example data to get started
2. Select the requests you want to include in your script
3. Configure headers, assertions, and variable extractions as needed
4. Adjust settings for your requirements
5. Preview and save your generated LoliCode script

Tip: Use the toolbar buttons for quick access to common actions!
        """
        ttk.Label(instructions, text=instructions_text, justify=tk.LEFT).pack()
        
        # Data preview
        preview_frame = ttk.LabelFrame(frame, text="Loaded Data Preview", padding="10")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.data_tree = ttk.Treeview(preview_frame, columns=("Method", "URL", "Status"), show="tree headings", height=15)
        self.data_tree.heading("#0", text="Index")
        self.data_tree.heading("Method", text="Method")
        self.data_tree.heading("URL", text="URL")
        self.data_tree.heading("Status", text="Status")
        
        self.data_tree.column("#0", width=80)
        self.data_tree.column("Method", width=80)
        self.data_tree.column("URL", width=600)
        self.data_tree.column("Status", width=80)
        
        scrollbar = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL, command=self.data_tree.yview)
        self.data_tree.configure(yscroll=scrollbar.set)
        
        self.data_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def _create_requests_tab(self):
        """Create the requests selection tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="📋 Select Requests")
        
        # Instructions
        ttk.Label(frame, text="Select which requests to include in your LoliCode script:", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        # Control buttons
        controls = ttk.Frame(frame)
        controls.pack(fill=tk.X, pady=5)
        
        ttk.Button(controls, text="✓ Select All", command=self._select_all_requests).pack(side=tk.LEFT, padx=2)
        ttk.Button(controls, text="✗ Deselect All", command=self._deselect_all_requests).pack(side=tk.LEFT, padx=2)
        ttk.Button(controls, text="🔄 Invert Selection", command=self._invert_selection).pack(side=tk.LEFT, padx=2)
        
        # Requests listbox with checkboxes
        list_frame = ttk.LabelFrame(frame, text="Requests", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create canvas for scrollable checkboxes
        canvas = tk.Canvas(list_frame)
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=canvas.yview)
        self.requests_frame = ttk.Frame(canvas)
        
        self.requests_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.requests_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.request_vars: List[tk.BooleanVar] = []
        
    def _create_headers_tab(self):
        """Create the custom headers tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="📄 Custom Headers")
        
        # Instructions
        ttk.Label(frame, text="Add custom headers to specific requests:", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        # Controls
        controls = ttk.Frame(frame)
        controls.pack(fill=tk.X, pady=5)
        
        ttk.Label(controls, text="Request Index:").pack(side=tk.LEFT, padx=2)
        self.header_request_var = tk.StringVar(value="0")
        ttk.Spinbox(controls, from_=0, to=100, textvariable=self.header_request_var, width=10).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Header Key:").pack(side=tk.LEFT, padx=2)
        self.header_key_var = tk.StringVar()
        ttk.Entry(controls, textvariable=self.header_key_var, width=20).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Header Value:").pack(side=tk.LEFT, padx=2)
        self.header_value_var = tk.StringVar()
        ttk.Entry(controls, textvariable=self.header_value_var, width=30).pack(side=tk.LEFT, padx=2)
        
        ttk.Button(controls, text="➕ Add Header", command=self._add_custom_header).pack(side=tk.LEFT, padx=2)
        
        # Headers list
        list_frame = ttk.LabelFrame(frame, text="Configured Headers", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.headers_tree = ttk.Treeview(list_frame, columns=("Request", "Key", "Value"), show="headings", height=15)
        self.headers_tree.heading("Request", text="Request Index")
        self.headers_tree.heading("Key", text="Header Key")
        self.headers_tree.heading("Value", text="Header Value")
        
        self.headers_tree.column("Request", width=120)
        self.headers_tree.column("Key", width=250)
        self.headers_tree.column("Value", width=400)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.headers_tree.yview)
        self.headers_tree.configure(yscroll=scrollbar.set)
        
        self.headers_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Delete button
        ttk.Button(frame, text="🗑 Delete Selected Header", command=self._delete_header).pack(pady=5)
        
    def _create_assertions_tab(self):
        """Create the custom assertions tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="✓ Assertions")
        
        # Instructions
        ttk.Label(frame, text="Add custom assertions/keychecks to validate responses:", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        # Controls
        controls = ttk.Frame(frame)
        controls.pack(fill=tk.X, pady=5)
        
        ttk.Label(controls, text="Request Index:").pack(side=tk.LEFT, padx=2)
        self.assertion_request_var = tk.StringVar(value="0")
        ttk.Spinbox(controls, from_=0, to=100, textvariable=self.assertion_request_var, width=10).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Type:").pack(side=tk.LEFT, padx=2)
        self.assertion_type_var = tk.StringVar(value="contains")
        ttk.Combobox(controls, textvariable=self.assertion_type_var, 
                    values=["status", "contains", "regex", "json-path"], 
                    state="readonly", width=15).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Value:").pack(side=tk.LEFT, padx=2)
        self.assertion_value_var = tk.StringVar()
        ttk.Entry(controls, textvariable=self.assertion_value_var, width=30).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Action:").pack(side=tk.LEFT, padx=2)
        self.assertion_action_var = tk.StringVar(value="success")
        ttk.Combobox(controls, textvariable=self.assertion_action_var, 
                    values=["success", "fail", "retry", "ban"], 
                    state="readonly", width=10).pack(side=tk.LEFT, padx=2)
        
        ttk.Button(controls, text="➕ Add Assertion", command=self._add_assertion).pack(side=tk.LEFT, padx=2)
        
        # Assertions list
        list_frame = ttk.LabelFrame(frame, text="Configured Assertions", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.assertions_tree = ttk.Treeview(list_frame, columns=("Request", "Type", "Value", "Action"), 
                                           show="headings", height=15)
        self.assertions_tree.heading("Request", text="Request Index")
        self.assertions_tree.heading("Type", text="Assertion Type")
        self.assertions_tree.heading("Value", text="Value/Pattern")
        self.assertions_tree.heading("Action", text="Action")
        
        self.assertions_tree.column("Request", width=120)
        self.assertions_tree.column("Type", width=150)
        self.assertions_tree.column("Value", width=400)
        self.assertions_tree.column("Action", width=100)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.assertions_tree.yview)
        self.assertions_tree.configure(yscroll=scrollbar.set)
        
        self.assertions_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Delete button
        ttk.Button(frame, text="🗑 Delete Selected Assertion", command=self._delete_assertion).pack(pady=5)
        
    def _create_extractions_tab(self):
        """Create the variable extractions tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="🔍 Variable Extractions")
        
        # Instructions
        ttk.Label(frame, text="Extract variables from responses for use in subsequent requests:", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        # Controls
        controls = ttk.Frame(frame)
        controls.pack(fill=tk.X, pady=5)
        
        ttk.Label(controls, text="Request Index:").pack(side=tk.LEFT, padx=2)
        self.extraction_request_var = tk.StringVar(value="0")
        ttk.Spinbox(controls, from_=0, to=100, textvariable=self.extraction_request_var, width=10).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Type:").pack(side=tk.LEFT, padx=2)
        self.extraction_type_var = tk.StringVar(value="regex")
        ttk.Combobox(controls, textvariable=self.extraction_type_var, 
                    values=["regex", "json", "css", "xpath"], 
                    state="readonly", width=10).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Pattern:").pack(side=tk.LEFT, padx=2)
        self.extraction_pattern_var = tk.StringVar()
        ttk.Entry(controls, textvariable=self.extraction_pattern_var, width=25).pack(side=tk.LEFT, padx=2)
        
        ttk.Label(controls, text="Variable Name:").pack(side=tk.LEFT, padx=2)
        self.extraction_var_var = tk.StringVar()
        ttk.Entry(controls, textvariable=self.extraction_var_var, width=15).pack(side=tk.LEFT, padx=2)
        
        self.extraction_global_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(controls, text="Global", variable=self.extraction_global_var).pack(side=tk.LEFT, padx=2)
        
        ttk.Button(controls, text="➕ Add Extraction", command=self._add_extraction).pack(side=tk.LEFT, padx=2)
        
        # Extractions list
        list_frame = ttk.LabelFrame(frame, text="Configured Variable Extractions", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.extractions_tree = ttk.Treeview(list_frame, columns=("Request", "Type", "Pattern", "Variable", "Global"), 
                                            show="headings", height=15)
        self.extractions_tree.heading("Request", text="Request Index")
        self.extractions_tree.heading("Type", text="Type")
        self.extractions_tree.heading("Pattern", text="Pattern")
        self.extractions_tree.heading("Variable", text="Variable Name")
        self.extractions_tree.heading("Global", text="Global")
        
        self.extractions_tree.column("Request", width=100)
        self.extractions_tree.column("Type", width=100)
        self.extractions_tree.column("Pattern", width=350)
        self.extractions_tree.column("Variable", width=150)
        self.extractions_tree.column("Global", width=80)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.extractions_tree.yview)
        self.extractions_tree.configure(yscroll=scrollbar.set)
        
        self.extractions_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Delete button
        ttk.Button(frame, text="🗑 Delete Selected Extraction", command=self._delete_extraction).pack(pady=5)
        
    def _create_settings_tab(self):
        """Create the settings tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="⚙️ Settings")
        
        # Instructions
        ttk.Label(frame, text="Configure global script settings:", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(frame, text="Script Settings", padding="20")
        settings_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Use Proxy
        self.use_proxy_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="Use Proxy", variable=self.use_proxy_var).grid(row=0, column=0, sticky=tk.W, pady=5)
        
        # Follow Redirects
        self.follow_redirects_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="Follow Redirects", variable=self.follow_redirects_var).grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Timeout
        ttk.Label(settings_frame, text="Timeout (seconds):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.timeout_var = tk.StringVar(value="30")
        ttk.Spinbox(settings_frame, from_=1, to=300, textvariable=self.timeout_var, width=10).grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Retry Count
        ttk.Label(settings_frame, text="Retry Count:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.retry_count_var = tk.StringVar(value="0")
        ttk.Spinbox(settings_frame, from_=0, to=10, textvariable=self.retry_count_var, width=10).grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Apply button
        ttk.Button(settings_frame, text="✓ Apply Settings", command=self._apply_settings).grid(row=4, column=0, columnspan=2, pady=20)
        
        # Presets
        presets_frame = ttk.LabelFrame(frame, text="Quick Presets", padding="20")
        presets_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(presets_frame, text="🚀 Fast Mode (No Proxy, 10s timeout)", 
                  command=lambda: self._apply_preset("fast")).pack(fill=tk.X, pady=2)
        ttk.Button(presets_frame, text="🛡 Secure Mode (Proxy, 60s timeout, 3 retries)", 
                  command=lambda: self._apply_preset("secure")).pack(fill=tk.X, pady=2)
        ttk.Button(presets_frame, text="⚡ Default Mode", 
                  command=lambda: self._apply_preset("default")).pack(fill=tk.X, pady=2)
        
    def _create_preview_tab(self):
        """Create the preview tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="👁 Preview Script")
        
        # Instructions
        ttk.Label(frame, text="Live preview of your generated LoliCode script:", 
                 font=("Arial", 10, "bold")).pack(pady=5)
        
        # Controls
        controls = ttk.Frame(frame)
        controls.pack(fill=tk.X, pady=5)
        
        ttk.Button(controls, text="🔄 Refresh Preview", command=self._generate_preview).pack(side=tk.LEFT, padx=2)
        ttk.Button(controls, text="💾 Save to File", command=self._save_script).pack(side=tk.LEFT, padx=2)
        ttk.Button(controls, text="📋 Copy to Clipboard", command=self._copy_to_clipboard).pack(side=tk.LEFT, padx=2)
        
        # Preview text area
        preview_frame = ttk.LabelFrame(frame, text="Generated LoliCode Script", padding="10")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.preview_text = scrolledtext.ScrolledText(preview_frame, wrap=tk.WORD, font=("Courier New", 10))
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        
        # Syntax highlighting would be nice, but keeping it simple
        self.preview_text.tag_config("keyword", foreground="#0000FF", font=("Courier New", 10, "bold"))
        self.preview_text.tag_config("comment", foreground="#008000", font=("Courier New", 10, "italic"))
        self.preview_text.tag_config("string", foreground="#A31515")
        
    def _create_help_tab(self):
        """Create the help tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="❓ Help")
        
        # Help content
        help_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=("Arial", 10))
        help_text.pack(fill=tk.BOTH, expand=True)
        
        help_content = """
╔══════════════════════════════════════════════════════════════════════════╗
║                    LoliCode Generator - User Guide                        ║
╚══════════════════════════════════════════════════════════════════════════╝

OVERVIEW:
This application helps you generate LoliCode scripts for OpenBullet 2 from
HAR (HTTP Archive) files or manual configuration.

HOW TO USE:

1. IMPORT DATA
   - Click "Load HAR File" to import a HAR file from your browser
   - Or click "Load Example" to try it with sample data
   - View the loaded requests in the Import Data tab

2. SELECT REQUESTS
   - Go to the "Select Requests" tab
   - Check the boxes for requests you want to include
   - Use "Select All", "Deselect All", or "Invert Selection" for bulk operations

3. CONFIGURE HEADERS (Optional)
   - Add custom headers to specific requests
   - Useful for API keys, authentication tokens, etc.
   - Format: Key: "X-API-Key", Value: "your-key-123"

4. ADD ASSERTIONS (Optional)
   - Define success/fail conditions for your requests
   - Types: status (HTTP code), contains (text search), regex, json-path
   - Actions: success, fail, retry, ban

5. VARIABLE EXTRACTIONS (Optional)
   - Extract values from responses for use in later requests
   - Types: regex, json, css, xpath
   - Mark as "Global" to make variable available throughout the script
   - Examples:
     * Regex: 'token":"([^"]+)"' extracts a token
     * JSON: '$.data.token' extracts from JSON response
     * CSS: 'input[name="csrf"]@value' extracts from HTML

6. SETTINGS
   - Configure global script settings
   - Use presets for common configurations
   - Timeout: How long to wait for responses
   - Retry Count: How many times to retry failed requests

7. PREVIEW & EXPORT
   - Click "Generate Preview" to see your script
   - Review the generated LoliCode
   - Save to file or copy to clipboard
   - Import into OpenBullet 2

TIPS & TRICKS:
• Start with the example data to learn the interface
• Use descriptive variable names for better script readability
• Test your regex patterns before adding them
• Use the status bar to see current operation status
• Custom headers support variables like <csrf_token>
• Variable names should be descriptive: "auth_token" not "t1"

KEYBOARD SHORTCUTS:
• Ctrl+L: Load HAR file
• Ctrl+E: Load example
• Ctrl+G: Generate preview
• Ctrl+S: Save script
• Ctrl+C: Copy to clipboard (when preview is focused)

VARIABLE SYNTAX:
• <INPUT.USERNAME>: User input variable
• <csrf_token>: Custom extracted variable
• <RESPONSE.STATUS>: Response status code
• <RESPONSE.BODY>: Response body content

COMMON PATTERNS:
• CSRF Token: name="csrf" value="([^"]+)"
• JSON Token: $.data.token
• Session Cookie: Set-Cookie: session=([^;]+)
• API Response: "success":\\s*true

For more information, visit the GitHub repository or documentation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated by: LoliCode Generator GUI v1.0
        """
        
        help_text.insert("1.0", help_content)
        help_text.configure(state="disabled")
        
    def _create_status_bar(self, parent):
        """Create the status bar."""
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(parent, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
    def _apply_theme(self):
        """Apply visual theme to the application."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure(".", background="#f0f0f0", foreground="#000000")
        style.configure("TLabel", padding=5)
        style.configure("TButton", padding=5)
        style.configure("TLabelframe", padding=10)
        
    # Event handlers
    
    def _load_har_file(self):
        """Load a HAR file."""
        filename = filedialog.askopenfilename(
            title="Select HAR File",
            filetypes=[("HAR files", "*.har"), ("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if not filename:
            return
            
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                har_data = json.load(f)
            
            # Parse HAR file
            if 'log' in har_data and 'entries' in har_data['log']:
                self.har_data = har_data['log']['entries']
            else:
                self.har_data = har_data if isinstance(har_data, list) else []
            
            self._process_har_data()
            self._update_status(f"Loaded {len(self.entries)} requests from HAR file")
            messagebox.showinfo("Success", f"Successfully loaded {len(self.entries)} requests!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load HAR file: {str(e)}")
            
    def _load_example(self):
        """Load example data."""
        # Create example entries
        self.entries = [
            SemanticHarEntry(
                request=SemanticHarRequest(
                    url='https://example.com/login',
                    method='GET',
                    headers={'accept': 'text/html'},
                    cookies={}
                ),
                response=SemanticHarResponse(status=200)
            ),
            SemanticHarEntry(
                request=SemanticHarRequest(
                    url='https://example.com/api/auth/login',
                    method='POST',
                    headers={'content-type': 'application/json'},
                    cookies={},
                    body=RequestBody(
                        data='{"username":"<INPUT.USERNAME>","password":"<INPUT.PASSWORD>"}',
                        content_type='json'
                    )
                ),
                response=SemanticHarResponse(status=200)
            ),
            SemanticHarEntry(
                request=SemanticHarRequest(
                    url='https://example.com/api/profile',
                    method='GET',
                    headers={'authorization': 'Bearer <auth_token>'},
                    cookies={}
                ),
                response=SemanticHarResponse(status=200)
            )
        ]
        
        # Add some example extractions
        self.variable_extractions = {
            1: [
                VariableExtraction(
                    type='json',
                    pattern='$.token',
                    variable_name='auth_token',
                    is_global=True
                )
            ]
        }
        
        self._update_data_view()
        self._update_requests_list()
        self._update_extractions_tree()
        self._update_status("Loaded example data with 3 requests")
        messagebox.showinfo("Example Loaded", "Example data loaded successfully!\n\nThis shows a typical login flow:\n1. GET login page\n2. POST credentials\n3. GET protected resource")
        
    def _update_extractions_tree(self):
        """Update the extractions tree view."""
        # Clear existing items
        for item in self.extractions_tree.get_children():
            self.extractions_tree.delete(item)
        
        # Add extractions
        for request_idx, extractions in self.variable_extractions.items():
            for extraction in extractions:
                self.extractions_tree.insert("", "end", values=(
                    request_idx,
                    extraction.type,
                    extraction.pattern,
                    extraction.variable_name,
                    "Yes" if extraction.is_global else "No"
                ))
        
    def _process_har_data(self):
        """Process HAR data into entries."""
        self.entries = []
        
        for item in self.har_data:
            try:
                request_data = item.get('request', {})
                response_data = item.get('response', {})
                
                # Parse headers
                headers = {}
                for h in request_data.get('headers', []):
                    headers[h.get('name', '').lower()] = h.get('value', '')
                
                # Parse cookies
                cookies = {}
                for c in request_data.get('cookies', []):
                    cookies[c.get('name', '')] = c.get('value', '')
                
                # Parse body
                body = None
                post_data = request_data.get('postData', {})
                if post_data:
                    content_type = 'json' if 'json' in post_data.get('mimeType', '') else 'form'
                    body = RequestBody(
                        data=post_data.get('text', ''),
                        content_type=content_type
                    )
                
                entry = SemanticHarEntry(
                    request=SemanticHarRequest(
                        url=request_data.get('url', ''),
                        method=request_data.get('method', 'GET'),
                        headers=headers,
                        cookies=cookies,
                        body=body
                    ),
                    response=SemanticHarResponse(
                        status=response_data.get('status', 0)
                    )
                )
                
                self.entries.append(entry)
            except Exception as e:
                print(f"Error processing HAR entry: {e}")
                continue
        
        self._update_data_view()
        self._update_requests_list()
        
    def _update_data_view(self):
        """Update the data tree view."""
        # Clear existing items
        for item in self.data_tree.get_children():
            self.data_tree.delete(item)
        
        # Add entries
        for i, entry in enumerate(self.entries):
            url = entry.request.url
            # Truncate long URLs
            if len(url) > 80:
                url = url[:77] + "..."
            
            self.data_tree.insert("", "end", text=str(i), values=(
                entry.request.method,
                url,
                entry.response.status
            ))
            
    def _update_requests_list(self):
        """Update the requests checkboxes list."""
        # Clear existing checkboxes
        for widget in self.requests_frame.winfo_children():
            widget.destroy()
        
        self.request_vars = []
        
        for i, entry in enumerate(self.entries):
            var = tk.BooleanVar(value=False)
            self.request_vars.append(var)
            
            url = entry.request.url
            if len(url) > 100:
                url = url[:97] + "..."
            
            text = f"[{i}] {entry.request.method} - {url}"
            cb = ttk.Checkbutton(self.requests_frame, text=text, variable=var)
            cb.pack(anchor=tk.W, pady=2, padx=10)
            
    def _select_all_requests(self):
        """Select all requests."""
        for var in self.request_vars:
            var.set(True)
        self._update_status("Selected all requests")
        
    def _deselect_all_requests(self):
        """Deselect all requests."""
        for var in self.request_vars:
            var.set(False)
        self._update_status("Deselected all requests")
        
    def _invert_selection(self):
        """Invert request selection."""
        for var in self.request_vars:
            var.set(not var.get())
        self._update_status("Inverted request selection")
        
    def _add_custom_header(self):
        """Add a custom header."""
        try:
            request_idx = int(self.header_request_var.get())
            key = self.header_key_var.get().strip()
            value = self.header_value_var.get().strip()
            
            if not key or not value:
                messagebox.showwarning("Warning", "Please provide both key and value")
                return
            
            if request_idx < 0 or request_idx >= len(self.entries):
                messagebox.showwarning("Warning", f"Request index must be between 0 and {len(self.entries)-1}")
                return
            
            if request_idx not in self.custom_headers:
                self.custom_headers[request_idx] = []
            
            self.custom_headers[request_idx].append(
                CustomHeader(key=key, value=value, enabled=True)
            )
            
            self.headers_tree.insert("", "end", values=(request_idx, key, value))
            
            # Clear inputs
            self.header_key_var.set("")
            self.header_value_var.set("")
            
            self._update_status(f"Added custom header to request {request_idx}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid request index")
            
    def _delete_header(self):
        """Delete selected header."""
        selection = self.headers_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a header to delete")
            return
        
        for item in selection:
            values = self.headers_tree.item(item)['values']
            request_idx = int(values[0])
            key = values[1]
            
            # Remove from data structure
            if request_idx in self.custom_headers:
                self.custom_headers[request_idx] = [
                    h for h in self.custom_headers[request_idx] if h.key != key
                ]
                if not self.custom_headers[request_idx]:
                    del self.custom_headers[request_idx]
            
            self.headers_tree.delete(item)
        
        self._update_status("Deleted selected header(s)")
        
    def _add_assertion(self):
        """Add a custom assertion."""
        try:
            request_idx = int(self.assertion_request_var.get())
            assertion_type = self.assertion_type_var.get()
            value = self.assertion_value_var.get().strip()
            action = self.assertion_action_var.get()
            
            if not value:
                messagebox.showwarning("Warning", "Please provide a value")
                return
            
            if request_idx < 0 or request_idx >= len(self.entries):
                messagebox.showwarning("Warning", f"Request index must be between 0 and {len(self.entries)-1}")
                return
            
            if request_idx not in self.custom_assertions:
                self.custom_assertions[request_idx] = []
            
            self.custom_assertions[request_idx].append(
                CustomAssertion(type=assertion_type, value=value, action=action)
            )
            
            self.assertions_tree.insert("", "end", values=(request_idx, assertion_type, value, action))
            
            # Clear input
            self.assertion_value_var.set("")
            
            self._update_status(f"Added assertion to request {request_idx}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid request index")
            
    def _delete_assertion(self):
        """Delete selected assertion."""
        selection = self.assertions_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an assertion to delete")
            return
        
        for item in selection:
            values = self.assertions_tree.item(item)['values']
            request_idx = int(values[0])
            value = values[2]
            
            # Remove from data structure
            if request_idx in self.custom_assertions:
                self.custom_assertions[request_idx] = [
                    a for a in self.custom_assertions[request_idx] if a.value != value
                ]
                if not self.custom_assertions[request_idx]:
                    del self.custom_assertions[request_idx]
            
            self.assertions_tree.delete(item)
        
        self._update_status("Deleted selected assertion(s)")
        
    def _add_extraction(self):
        """Add a variable extraction."""
        try:
            request_idx = int(self.extraction_request_var.get())
            extraction_type = self.extraction_type_var.get()
            pattern = self.extraction_pattern_var.get().strip()
            var_name = self.extraction_var_var.get().strip()
            is_global = self.extraction_global_var.get()
            
            if not pattern or not var_name:
                messagebox.showwarning("Warning", "Please provide both pattern and variable name")
                return
            
            if request_idx < 0 or request_idx >= len(self.entries):
                messagebox.showwarning("Warning", f"Request index must be between 0 and {len(self.entries)-1}")
                return
            
            if request_idx not in self.variable_extractions:
                self.variable_extractions[request_idx] = []
            
            self.variable_extractions[request_idx].append(
                VariableExtraction(
                    type=extraction_type,
                    pattern=pattern,
                    variable_name=var_name,
                    is_global=is_global
                )
            )
            
            self.extractions_tree.insert("", "end", values=(
                request_idx, extraction_type, pattern, var_name, "Yes" if is_global else "No"
            ))
            
            # Clear inputs
            self.extraction_pattern_var.set("")
            self.extraction_var_var.set("")
            
            self._update_status(f"Added variable extraction to request {request_idx}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid request index")
            
    def _delete_extraction(self):
        """Delete selected extraction."""
        selection = self.extractions_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an extraction to delete")
            return
        
        for item in selection:
            values = self.extractions_tree.item(item)['values']
            request_idx = int(values[0])
            var_name = values[3]
            
            # Remove from data structure
            if request_idx in self.variable_extractions:
                self.variable_extractions[request_idx] = [
                    e for e in self.variable_extractions[request_idx] if e.variable_name != var_name
                ]
                if not self.variable_extractions[request_idx]:
                    del self.variable_extractions[request_idx]
            
            self.extractions_tree.delete(item)
        
        self._update_status("Deleted selected extraction(s)")
        
    def _apply_settings(self):
        """Apply settings."""
        try:
            self.settings = {
                'use_proxy': self.use_proxy_var.get(),
                'follow_redirects': self.follow_redirects_var.get(),
                'timeout': int(self.timeout_var.get()),
                'retry_count': int(self.retry_count_var.get())
            }
            self._update_status("Settings applied successfully")
            messagebox.showinfo("Success", "Settings have been applied")
        except ValueError:
            messagebox.showerror("Error", "Invalid settings values")
            
    def _apply_preset(self, preset: str):
        """Apply a settings preset."""
        if preset == "fast":
            self.use_proxy_var.set(False)
            self.follow_redirects_var.set(True)
            self.timeout_var.set("10")
            self.retry_count_var.set("0")
        elif preset == "secure":
            self.use_proxy_var.set(True)
            self.follow_redirects_var.set(True)
            self.timeout_var.set("60")
            self.retry_count_var.set("3")
        elif preset == "default":
            self.use_proxy_var.set(True)
            self.follow_redirects_var.set(True)
            self.timeout_var.set("30")
            self.retry_count_var.set("0")
        
        self._apply_settings()
        self._update_status(f"Applied {preset} preset")
        
    def _show_quick_settings(self):
        """Show quick settings dialog."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Quick Settings")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Quick Settings", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Button(frame, text="🚀 Fast Mode", 
                  command=lambda: [self._apply_preset("fast"), dialog.destroy()]).pack(fill=tk.X, pady=5)
        ttk.Button(frame, text="🛡 Secure Mode", 
                  command=lambda: [self._apply_preset("secure"), dialog.destroy()]).pack(fill=tk.X, pady=5)
        ttk.Button(frame, text="⚡ Default Mode", 
                  command=lambda: [self._apply_preset("default"), dialog.destroy()]).pack(fill=tk.X, pady=5)
        
        ttk.Separator(frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        ttk.Button(frame, text="Cancel", command=dialog.destroy).pack(fill=tk.X, pady=5)
        
    def _generate_preview(self):
        """Generate and display preview."""
        if not self.entries:
            messagebox.showwarning("Warning", "Please load data first")
            return
        
        # Get selected indices
        self.selected_indices = [i for i, var in enumerate(self.request_vars) if var.get()]
        
        if not self.selected_indices:
            messagebox.showwarning("Warning", "Please select at least one request")
            return
        
        try:
            # Create configuration
            config = LoliCodeConfig(
                selected_indices=self.selected_indices,
                custom_headers=self.custom_headers if self.custom_headers else None,
                custom_assertions=self.custom_assertions if self.custom_assertions else None,
                variable_extractions=self.variable_extractions if self.variable_extractions else None,
                settings=self.settings
            )
            
            # Create dependency matrix
            dependency_matrix = DependencyMatrix(topological_order=self.selected_indices)
            
            # Generate script
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            script = loop.run_until_complete(
                self.generator.generate(config, self.entries, dependency_matrix)
            )
            loop.close()
            
            # Display in preview
            self.preview_text.delete("1.0", tk.END)
            self.preview_text.insert("1.0", script)
            
            # Switch to preview tab
            self.notebook.select(6)  # Preview tab index
            
            self._update_status(f"Generated script with {len(self.selected_indices)} requests")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate script: {str(e)}")
            
    def _save_script(self):
        """Save script to file."""
        script = self.preview_text.get("1.0", tk.END).strip()
        
        if not script:
            messagebox.showwarning("Warning", "Please generate a preview first")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save LoliCode Script",
            defaultextension=".loli",
            filetypes=[("LoliCode files", "*.loli"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(script)
                self._update_status(f"Script saved to {filename}")
                messagebox.showinfo("Success", f"Script saved successfully to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save script: {str(e)}")
                
    def _copy_to_clipboard(self):
        """Copy script to clipboard."""
        script = self.preview_text.get("1.0", tk.END).strip()
        
        if not script:
            messagebox.showwarning("Warning", "Please generate a preview first")
            return
        
        self.root.clipboard_clear()
        self.root.clipboard_append(script)
        self._update_status("Script copied to clipboard")
        messagebox.showinfo("Success", "Script copied to clipboard!")
        
    def _update_status(self, message: str):
        """Update status bar message."""
        self.status_var.set(f"{datetime.now().strftime('%H:%M:%S')} - {message}")
        

def main():
    """Run the GUI application."""
    root = tk.Tk()
    app = LoliCodeGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
