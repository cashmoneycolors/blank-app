# Visual Studio Code Insider Verbindung - Anleitung

## 🚀 Verbindung mit Visual Studio Code Insider herstellen

### Voraussetzungen
1. **VS Code Insider** installiert: [Download hier](https://code.visualstudio.com/insiders/)
2. **Remote Development Extension Pack** installiert
3. **Python Extension** installiert

### Verbindungsmethoden

#### 1. 📁 Lokale Entwicklung
```bash
# Projekt in VS Code Insider öffnen
code-insiders .

# Oder über das Workspace-File
code-insiders workspace.code-workspace
```

#### 2. 🐳 DevContainer verwenden
Das Projekt ist bereits mit DevContainer-Konfiguration ausgestattet:
- Öffne VS Code Insider
- Drücke `Ctrl+Shift+P` (Cmd+Shift+P auf Mac)
- Wähle: "Dev Containers: Open Folder in Container"
- Wähle diesen Projektordner

#### 3. 🌐 Remote Development
Für Remote-Server oder WSL:
```bash
# Über SSH
code-insiders --remote ssh-remote+user@hostname /pfad/zum/projekt

# Über WSL (Windows)
code-insiders --remote wsl+Ubuntu /mnt/c/pfad/zum/projekt
```

### ✨ Konfigurierte Features

#### Python-Entwicklung
- **Linting**: Flake8 aktiviert
- **Formatting**: Black Formatter
- **IntelliSense**: Pylance
- **Debugging**: Launch-Konfigurationen für Python und Streamlit

#### Verfügbare Debug-Konfigurationen
1. **Python: Current File** - Debuggt die aktuell geöffnete Python-Datei
2. **Python: Streamlit App** - Startet die Streamlit-App im Debug-Modus
3. **Python: Debug Current File** - Erweiterte Debug-Optionen
4. **Python: Attach to Running Process** - Anhängen an laufende Prozesse

#### Tasks (Ctrl+Shift+P → "Tasks: Run Task")
- **Install Python Requirements** - Installiert requirements.txt
- **Run Streamlit App** - Startet die Streamlit-Anwendung
- **Python: Lint with Flake8** - Code-Analyse
- **Python: Format with Black** - Code-Formatierung

### 🔧 Empfohlene Extensions
Die folgenden Extensions werden automatisch vorgeschlagen:
- **ms-python.python** - Python-Unterstützung
- **ms-python.vscode-pylance** - Erweiterte Python-IntelliSense
- **ms-python.flake8** - Code-Linting
- **ms-python.black-formatter** - Code-Formatierung
- **github.copilot** - AI-Unterstützung
- **ms-vscode-remote.vscode-remote-extensionpack** - Remote Development

### 📝 Erste Schritte nach der Verbindung

1. **Python Interpreter auswählen**:
   - Drücke `Ctrl+Shift+P`
   - Wähle "Python: Select Interpreter"
   - Wähle Python 3.11 oder höher

2. **Dependencies installieren**:
   ```bash
   pip install -r requirements.txt
   pip install streamlit
   ```

3. **Streamlit App starten**:
   - Drücke `F5` für Debug-Modus
   - Oder verwende Task: "Run Streamlit App"
   - Oder Terminal: `streamlit run streamlit_app.py`

### 🐛 Debugging

#### Streamlit App debuggen:
1. Setze Breakpoints in `streamlit_app.py`
2. Wähle Debug-Konfiguration "Python: Streamlit App"
3. Drücke `F5` zum Starten
4. App öffnet sich automatisch auf Port 8501

#### Python-Code debuggen:
1. Öffne eine Python-Datei
2. Setze Breakpoints mit `F9`
3. Wähle "Python: Current File" Konfiguration
4. Drücke `F5` zum Debuggen

### 📊 Projektstruktur
```
/vercel/sandbox/
├── .vscode/                    # VS Code Konfiguration
│   ├── settings.json          # Workspace-Einstellungen
│   ├── extensions.json        # Empfohlene Extensions
│   ├── launch.json           # Debug-Konfigurationen
│   └── tasks.json            # Build-Tasks
├── .devcontainer/             # DevContainer-Konfiguration
│   └── devcontainer.json
├── streamlit_app.py          # Hauptanwendung
├── requirements.txt          # Python-Dependencies
└── workspace.code-workspace  # VS Code Workspace-Datei
```

### 🔗 Nützliche Shortcuts in VS Code Insider
- `Ctrl+Shift+P` - Command Palette
- `F5` - Debugging starten
- `Ctrl+F5` - Ohne Debugging ausführen
- `F9` - Breakpoint setzen/entfernen
- `F10` - Step Over (Debugging)
- `F11` - Step Into (Debugging)
- `Shift+F5` - Debugging stoppen

### 💡 Tipps für optimale Entwicklung
1. **Nutze die integrierte Terminal**: `Ctrl+` `
2. **Verwende Git-Integration**: Eingebaute Git-Unterstützung
3. **IntelliSense**: Automatische Code-Vervollständigung
4. **Format on Save**: Automatische Code-Formatierung beim Speichern
5. **Extensions**: Installiere empfohlene Extensions für bessere Produktivität

### ❓ Troubleshooting

#### Python Interpreter nicht gefunden:
```bash
# Python-Pfad prüfen
which python3
# Oder
whereis python3
```

#### Streamlit startet nicht:
```bash
# Streamlit installieren
pip install streamlit

# Version prüfen
streamlit version
```

#### Port 8501 bereits verwendet:
```bash
# Anderen Port verwenden
streamlit run streamlit_app.py --server.port 8502
```

### 🎯 Nächste Schritte
1. Verbinde dich mit VS Code Insider
2. Installiere empfohlene Extensions
3. Wähle Python Interpreter
4. Starte das Debugging mit der Streamlit-Konfiguration
5. Beginne mit der Entwicklung!

---

**Viel Erfolg bei der Entwicklung mit Visual Studio Code Insider! 🚀**
