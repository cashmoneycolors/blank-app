# 🚀 VS Code & VS Code Insider - Komplette Setup-Anleitung

## ✅ Was wurde konfiguriert?

Dein Projekt ist jetzt vollständig für VS Code und VS Code Insider eingerichtet:

### 📁 Konfigurationsdateien
- ✅ `.vscode/settings.json` - Workspace-Einstellungen
- ✅ `.vscode/extensions.json` - Empfohlene Extensions
- ✅ `.vscode/launch.json` - Debug-Konfigurationen
- ✅ `.vscode/tasks.json` - Build- und Run-Tasks
- ✅ `workspace.code-workspace` - Workspace-Datei
- ✅ `.devcontainer/devcontainer.json` - DevContainer-Konfiguration
- ✅ `open-vscode.sh` - Automatisches Verbindungs-Script

## 🎯 Verbindungsmethoden

### Methode 1: Automatisches Script (Einfachste Methode) ⭐
```bash
./open-vscode.sh
```
Das Script erkennt automatisch, welche VS Code Version installiert ist und öffnet das Projekt.

### Methode 2: Workspace-Datei öffnen (Empfohlen)
```bash
# Mit VS Code Insider
code-insiders workspace.code-workspace

# Mit VS Code
code workspace.code-workspace
```

### Methode 3: Ordner direkt öffnen
```bash
# Mit VS Code Insider
code-insiders .

# Mit VS Code
code .
```

### Methode 4: DevContainer (Für isolierte Umgebung)
1. Öffne VS Code/VS Code Insider
2. Drücke `Ctrl+Shift+P` (oder `Cmd+Shift+P` auf Mac)
3. Wähle: **"Dev Containers: Open Folder in Container"**
4. Wähle diesen Projektordner
5. Warte, bis der Container gebaut ist

### Methode 5: Remote Development (SSH/WSL)
```bash
# Über SSH
code-insiders --remote ssh-remote+user@hostname /vercel/sandbox

# Über WSL (Windows)
code-insiders --remote wsl+Ubuntu /vercel/sandbox
```

## 🔧 Erste Schritte nach dem Öffnen

### 1. Extensions installieren
VS Code zeigt automatisch eine Benachrichtigung mit empfohlenen Extensions:
- **ms-python.python** - Python-Unterstützung
- **ms-python.vscode-pylance** - IntelliSense
- **ms-python.flake8** - Linting
- **ms-python.black-formatter** - Code-Formatierung
- **github.copilot** - AI-Unterstützung (optional)
- **ms-vscode-remote.vscode-remote-extensionpack** - Remote Development

**Klicke auf "Install All"** oder installiere sie manuell über `Ctrl+Shift+X`.

### 2. Python Interpreter auswählen
1. Drücke `Ctrl+Shift+P`
2. Tippe: **"Python: Select Interpreter"**
3. Wähle Python 3.11 oder höher

### 3. Dependencies installieren
**Option A: Über Task (Empfohlen)**
1. Drücke `Ctrl+Shift+P`
2. Wähle: **"Tasks: Run Task"**
3. Wähle: **"Install Python Requirements"**

**Option B: Über Terminal**
```bash
pip3 install -r requirements.txt
pip3 install streamlit
```

### 4. Streamlit App starten
**Option A: Debug-Modus (F5)**
1. Drücke `F5`
2. Wähle: **"Python: Streamlit App"**
3. App öffnet sich auf http://localhost:8501

**Option B: Über Task**
1. Drücke `Ctrl+Shift+P`
2. Wähle: **"Tasks: Run Task"**
3. Wähle: **"Run Streamlit App"**

**Option C: Über Terminal**
```bash
streamlit run streamlit_app.py
```

## 🎨 Verfügbare Features

### 🐛 Debug-Konfigurationen (F5)
1. **Python: Current File** - Debuggt die aktuell geöffnete Datei
2. **Python: Streamlit App** - Startet Streamlit im Debug-Modus
3. **Python: Debug Current File** - Erweiterte Debug-Optionen
4. **Python: Attach to Running Process** - An laufenden Prozess anhängen

### ⚙️ Tasks (Ctrl+Shift+P → "Tasks: Run Task")
1. **Install Python Requirements** - Installiert alle Dependencies
2. **Run Streamlit App** - Startet die Streamlit-Anwendung
3. **Python: Lint with Flake8** - Führt Code-Analyse durch
4. **Python: Format with Black** - Formatiert den Code

### ✨ Automatische Features
- ✅ **Format on Save** - Code wird beim Speichern automatisch formatiert (Black)
- ✅ **Linting** - Echtzeit-Code-Analyse mit Flake8
- ✅ **IntelliSense** - Intelligente Code-Vervollständigung (Pylance)
- ✅ **Auto-Import** - Automatische Import-Organisation
- ✅ **Type Checking** - Basis-Typ-Überprüfung
- ✅ **Trailing Whitespace Removal** - Entfernt überflüssige Leerzeichen
- ✅ **Final Newline** - Fügt automatisch Zeilenumbruch am Dateiende ein

## ⌨️ Wichtige Shortcuts

### Allgemein
- `Ctrl+Shift+P` - Command Palette öffnen
- `Ctrl+P` - Datei schnell öffnen
- `Ctrl+` ` - Terminal öffnen/schließen
- `Ctrl+B` - Sidebar ein-/ausblenden
- `Ctrl+Shift+E` - Explorer anzeigen
- `Ctrl+Shift+X` - Extensions anzeigen

### Debugging
- `F5` - Debugging starten
- `Ctrl+F5` - Ohne Debugging ausführen
- `F9` - Breakpoint setzen/entfernen
- `F10` - Step Over (nächste Zeile)
- `F11` - Step Into (in Funktion springen)
- `Shift+F11` - Step Out (aus Funktion springen)
- `Shift+F5` - Debugging stoppen

### Code-Bearbeitung
- `Ctrl+Space` - IntelliSense auslösen
- `Ctrl+.` - Quick Fix anzeigen
- `Alt+Shift+F` - Code formatieren
- `Ctrl+/` - Zeile kommentieren/auskommentieren
- `Ctrl+D` - Nächstes Vorkommen auswählen
- `Ctrl+Shift+L` - Alle Vorkommen auswählen

### Navigation
- `Ctrl+G` - Zu Zeile springen
- `F12` - Zur Definition springen
- `Alt+F12` - Definition anzeigen (Peek)
- `Shift+F12` - Alle Referenzen anzeigen
- `Ctrl+Tab` - Zwischen offenen Dateien wechseln

## 📊 Projektstruktur

```
/vercel/sandbox/
├── .vscode/                      # VS Code Konfiguration
│   ├── settings.json            # Workspace-Einstellungen
│   ├── extensions.json          # Empfohlene Extensions
│   ├── launch.json              # Debug-Konfigurationen
│   ├── tasks.json               # Build-Tasks
│   └── README.md                # VS Code Dokumentation
├── .devcontainer/               # DevContainer-Konfiguration
│   └── devcontainer.json        # Container-Setup
├── .github/                     # GitHub-Konfiguration
│   └── CODEOWNERS              # Code-Besitzer
├── streamlit_app.py            # Hauptanwendung
├── requirements.txt            # Python-Dependencies
├── workspace.code-workspace    # VS Code Workspace-Datei
├── open-vscode.sh              # Automatisches Verbindungs-Script
├── VS_CODE_INSIDER_VERBINDUNG.md  # Detaillierte Anleitung
├── VSCODE_SETUP.md             # Diese Datei
└── README.md                   # Projekt-Dokumentation
```

## 🐛 Troubleshooting

### Problem: Python Interpreter nicht gefunden
**Lösung:**
```bash
# Python-Pfad finden
which python3
whereis python3

# In VS Code: Ctrl+Shift+P → "Python: Select Interpreter"
# Oder manuell in .vscode/settings.json eintragen
```

### Problem: Extensions werden nicht vorgeschlagen
**Lösung:**
1. Öffne Extensions-Panel: `Ctrl+Shift+X`
2. Suche nach: `@recommended`
3. Installiere alle empfohlenen Extensions manuell

### Problem: Streamlit startet nicht
**Lösung:**
```bash
# Streamlit installieren
pip3 install streamlit

# Version prüfen
streamlit version

# Manuell starten
streamlit run streamlit_app.py
```

### Problem: Port 8501 bereits verwendet
**Lösung:**
```bash
# Anderen Port verwenden
streamlit run streamlit_app.py --server.port 8502

# Oder laufenden Prozess beenden
lsof -ti:8501 | xargs kill -9
```

### Problem: Linting funktioniert nicht
**Lösung:**
```bash
# Flake8 installieren
pip3 install flake8

# In VS Code: Ctrl+Shift+P → "Python: Select Linter" → "flake8"
```

### Problem: Formatting funktioniert nicht
**Lösung:**
```bash
# Black installieren
pip3 install black

# In VS Code: Ctrl+Shift+P → "Format Document"
```

### Problem: DevContainer baut nicht
**Lösung:**
1. Docker muss installiert und gestartet sein
2. Docker Extension für VS Code installieren
3. Prüfe Docker-Status: `docker ps`
4. Rebuild Container: `Ctrl+Shift+P` → "Dev Containers: Rebuild Container"

## 💡 Best Practices

### 1. Verwende Virtual Environment
```bash
# Virtual Environment erstellen
python3 -m venv .venv

# Aktivieren (Linux/Mac)
source .venv/bin/activate

# Aktivieren (Windows)
.venv\Scripts\activate

# In VS Code: Interpreter auf .venv setzen
```

### 2. Nutze Git-Integration
- VS Code hat eingebaute Git-Unterstützung
- Source Control Panel: `Ctrl+Shift+G`
- GitLens Extension für erweiterte Features

### 3. Verwende Workspace-Einstellungen
- Projekt-spezifische Einstellungen in `.vscode/settings.json`
- Globale Einstellungen in User Settings
- Workspace-Einstellungen überschreiben User Settings

### 4. Nutze Tasks für wiederkehrende Aufgaben
- `Ctrl+Shift+P` → "Tasks: Run Task"
- Eigene Tasks in `.vscode/tasks.json` definieren

### 5. Debugging effektiv nutzen
- Setze Breakpoints mit `F9`
- Nutze Conditional Breakpoints (Rechtsklick auf Breakpoint)
- Watch-Expressions für Variablen
- Debug Console für Experimente

## 🎓 Weiterführende Ressourcen

### Offizielle Dokumentation
- [VS Code Docs](https://code.visualstudio.com/docs)
- [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Debugging in VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)

### Streamlit
- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)

### Python Tools
- [Black Formatter](https://black.readthedocs.io/)
- [Flake8 Linter](https://flake8.pycqa.org/)
- [Pylance](https://github.com/microsoft/pylance-release)

## 🎯 Nächste Schritte

1. ✅ **Verbinde dich mit VS Code/VS Code Insider** (siehe Verbindungsmethoden oben)
2. ✅ **Installiere empfohlene Extensions**
3. ✅ **Wähle Python Interpreter**
4. ✅ **Installiere Dependencies**
5. ✅ **Starte die Streamlit App**
6. ✅ **Beginne mit der Entwicklung!**

---

## 📞 Support

Bei Problemen oder Fragen:
1. Prüfe diese Dokumentation
2. Siehe `VS_CODE_INSIDER_VERBINDUNG.md` für Details
3. Siehe `.vscode/README.md` für Konfigurationsdetails

---

**Viel Erfolg mit VS Code und VS Code Insider! 🚀**

*Erstellt am: 29. Oktober 2025*
