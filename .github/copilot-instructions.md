# Streamlit App Template - Copilot Instructions

## Architektur-Übersicht
Vollständig konfiguriertes Streamlit-Entwicklungsprojekt mit VS Code Integration, DevContainer und Debugging-Support.

**Core-Komponenten:**
- `streamlit_app.py`: Haupt-Streamlit-Anwendung (Template)
- `.vscode/`: VS Code Konfiguration (Debug, Tasks, Settings)
- `.devcontainer/`: Docker-basierte Entwicklungsumgebung
- `open-vscode.sh`: Automatisches VS Code/Insider Launcher-Script

## VS Code Integration (Production-Ready)

**Multi-Editor-Support:**
```bash
# Automatischer Launch (erkennt VS Code/Insider)
./open-vscode.sh

# Manuell (Workspace-File verwenden)
code-insiders workspace.code-workspace
code workspace.code-workspace
```

**Debug-Konfigurationen (`.vscode/launch.json`):**
- **"Python: Current File"**: Standard Python-Debugging
- **"Python: Streamlit"**: Startet Streamlit mit `--server.headless true`

**Tasks (`.vscode/tasks.json`):**
- **"streamlit: Run"**: Startet App (`streamlit run streamlit_app.py`)
- **"pip: Install Requirements"**: Installiert Dependencies

**Formatter/Linter-Setup:**
- **Black**: Auto-Formatter (Format-on-Save aktiv)
- **Flake8**: Linting mit relaxierter Line-Length (88 Zeichen)
- **Pylance**: Type-Checking (basic mode)

## Entwickler-Workflows

**Setup (3 Optionen):**

1. **VS Code DevContainer (Empfohlen):**
   - `F1` → "Dev Containers: Reopen in Container"
   - Isolierte Python-Umgebung mit allen Tools

2. **VS Code Lokal:**
   - `./open-vscode.sh` → Auto-Setup
   - Debugging: `F5` → "Python: Streamlit"

3. **Kommandozeile:**
   ```bash
   pip install -r requirements.txt
   streamlit run streamlit_app.py
   ```

**Debug-Workflow:**
1. Breakpoints setzen in `streamlit_app.py`
2. `F5` → "Python: Streamlit" Launch-Config wählen
3. Browser öffnet automatisch auf `localhost:8501`
4. Debugger stoppt an Breakpoints

## Konventionen

**Streamlit-Patterns:**
```python
# Page Config (immer als erstes!)
st.set_page_config(
    page_title='App Title',
    page_icon=':emoji:',
    layout='wide'  # Optional
)

# Caching für Performance
@st.cache_data
def load_data():
    return expensive_operation()

# Sidebar für Navigation
with st.sidebar:
    option = st.selectbox('Wähle Seite', ['Home', 'About'])
```

**VS Code Settings-Überrides:**
- Auto-Save: `afterDelay` (1 Sekunde)
- Format-on-Save: Aktiviert
- Python Linting: Flake8 mit `--max-line-length=88`
- Type-Checking: Pylance Basic Mode

**DevContainer-Features:**
- Base Image: `mcr.microsoft.com/devcontainers/python:1-3.11-bullseye`
- Port-Forwarding: 8501 (Streamlit-Standard)
- Extensions: Python, Pylance, Black Formatter

## Integration Points

**Externe Dependencies:**
```txt
# requirements.txt
streamlit>=1.28.0
pandas
numpy
matplotlib
# Weitere je nach App-Bedarf
```

**VS Code Workspace (`.code-workspace`):**
- Zentrale Konfiguration für Multi-Root-Workspaces
- Synced Settings zwischen Teammitgliedern
- Tasks und Launch-Configs wiederverwendbar

**Deployment:**
- Streamlit Community Cloud Ready
- Docker-Support via DevContainer
- GitHub Actions CI/CD (optional erweiterbar)

## Quick-Reference

**Häufige Kommandos:**
```bash
# App starten
streamlit run streamlit_app.py

# Mit Custom Port
streamlit run streamlit_app.py --server.port 8080

# Headless (ohne Browser)
streamlit run streamlit_app.py --server.headless true

# Debug-Logs aktivieren
streamlit run streamlit_app.py --logger.level=debug
```

**VS Code Shortcuts:**
- `F5`: Debug starten
- `Ctrl+Shift+P`: Command Palette
- `Ctrl+Shift+B`: Run Task
- `Shift+Alt+F`: Format Document (Black)
