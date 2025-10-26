# Visual Studio Code Connection Instructions

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
/vercel/sandbox
├── .vscode/
│   ├── settings.json    # Python development settings
│   ├── launch.json      # Debug configuration
│   └── extensions.json  # Recommended extensions
└── ... (your Python files)
```

Happy coding! 🐍✨
