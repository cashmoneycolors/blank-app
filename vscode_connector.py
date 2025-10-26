#!/usr/bin/env python3
"""
Visual Studio Code Remote Connection Helper
Helps establish connection to Visual Studio Code for Python development
"""

import os
import sys
import webbrowser
import subprocess
import json
from pathlib import Path

class VisualStudioConnector:
    def __init__(self):
        self.project_path = Path.cwd()
        self.vscode_settings_dir = self.project_path / ".vscode"
        
    def check_environment(self):
        """Check the current development environment"""
        print("🔍 Checking development environment...")
        print(f"📁 Current directory: {self.project_path}")
        print(f"🐍 Python version: {sys.version}")
        print(f"🔧 Python executable: {sys.executable}")
        
        # Check if we're in a Python project
        python_files = list(self.project_path.glob("*.py"))
        requirements_file = self.project_path / "requirements.txt"
        setup_py = self.project_path / "setup.py"
        pyproject_toml = self.project_path / "pyproject.toml"
        
        print(f"📝 Python files found: {len(python_files)}")
        if requirements_file.exists():
            print("✅ requirements.txt found")
        if setup_py.exists():
            print("✅ setup.py found")
        if pyproject_toml.exists():
            print("✅ pyproject.toml found")
            
    def create_vscode_settings(self):
        """Create VS Code settings for Python development"""
        print("⚙️ Creating VS Code configuration...")
        
        self.vscode_settings_dir.mkdir(exist_ok=True)
        
        # Create settings.json
        settings = {
            "python.pythonPath": sys.executable,
            "python.linting.enabled": True,
            "python.linting.pylintEnabled": True,
            "python.formatting.provider": "black",
            "python.linting.flake8Enabled": True,
            "files.autoSave": "onFocusChange",
            "editor.formatOnSave": True,
            "python.terminal.activateEnvironment": True
        }
        
        settings_file = self.vscode_settings_dir / "settings.json"
        with open(settings_file, 'w') as f:
            json.dump(settings, f, indent=2)
        print(f"✅ Created {settings_file}")
        
        # Create launch.json for debugging
        launch_config = {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Python: Current File",
                    "type": "python",
                    "request": "launch",
                    "program": "${file}",
                    "console": "integratedTerminal"
                }
            ]
        }
        
        launch_file = self.vscode_settings_dir / "launch.json"
        with open(launch_file, 'w') as f:
            json.dump(launch_config, f, indent=2)
        print(f"✅ Created {launch_file}")
        
        # Create extensions.json
        extensions = {
            "recommendations": [
                "ms-python.python",
                "ms-python.flake8",
                "ms-python.black-formatter",
                "ms-python.pylint"
            ]
        }
        
        extensions_file = self.vscode_settings_dir / "extensions.json"
        with open(extensions_file, 'w') as f:
            json.dump(extensions, f, indent=2)
        print(f"✅ Created {extensions_file}")
        
    def create_connection_instructions(self):
        """Create instructions for connecting to VS Code"""
        instructions = """# Visual Studio Code Connection Instructions

## Option 1: VS Code Web (Recommended for Remote Development)
1. Open your web browser
2. Go to: https://vscode.dev/
3. Click "Open Folder" and select this project directory
4. Install recommended Python extensions when prompted

## Option 2: Local VS Code Installation
If you have VS Code installed locally:
1. Open terminal/command prompt
2. Navigate to this project directory
3. Run: `code .`

## Option 3: VS Code Remote Development
If working on a remote server:
1. Install "Remote - SSH" extension in VS Code
2. Connect to your remote server
3. Open this project directory

## Python Development Setup
The following VS Code settings have been configured:
- Python interpreter path
- Linting with pylint and flake8
- Formatting with black
- Auto-save and format on save
- Debugging configuration

## Recommended Extensions
- Python (ms-python.python)
- Pylint (ms-python.pylint)
- Black Formatter (ms-python.black-formatter)
- Flake8 (ms-python.flake8)

## Project Structure
```
{project_path}
├── .vscode/
│   ├── settings.json    # Python development settings
│   ├── launch.json      # Debug configuration
│   └── extensions.json  # Recommended extensions
└── ... (your Python files)
```

Happy coding! 🐍✨
""".format(project_path=self.project_path)
        
        instructions_file = self.project_path / "VSCODE_CONNECTION.md"
        with open(instructions_file, 'w') as f:
            f.write(instructions)
        print(f"✅ Created connection instructions: {instructions_file}")
        
    def open_vscode_web(self):
        """Try to open VS Code web interface"""
        try:
            print("🌐 Opening VS Code Web...")
            webbrowser.open("https://vscode.dev/")
            print("✅ VS Code Web should open in your browser")
            print("   Select 'Open Folder' and navigate to this project directory")
        except Exception as e:
            print(f"❌ Could not open browser: {e}")
            
    def run(self):
        """Main connection process"""
        print("🚀 Visual Studio Code Connection Helper")
        print("=" * 50)
        
        self.check_environment()
        print()
        
        self.create_vscode_settings()
        print()
        
        self.create_connection_instructions()
        print()
        
        self.open_vscode_web()
        print()
        
        print("📋 Summary:")
        print("✅ VS Code configuration files created")
        print("✅ Connection instructions generated")
        print("✅ VS Code Web opened (if browser available)")
        print()
        print("📖 Read VSCODE_CONNECTION.md for detailed setup instructions")

if __name__ == "__main__":
    connector = VisualStudioConnector()
    connector.run()
