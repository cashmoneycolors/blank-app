#!/bin/bash

# VS Code / VS Code Insider Verbindungs-Script
# Dieses Script öffnet das Projekt in VS Code oder VS Code Insider

echo "🚀 VS Code Verbindungs-Script"
echo "=============================="
echo ""

# Prüfe ob VS Code Insider installiert ist
if command -v code-insiders &> /dev/null; then
    echo "✅ VS Code Insider gefunden"
    HAS_INSIDER=true
else
    echo "❌ VS Code Insider nicht gefunden"
    HAS_INSIDER=false
fi

# Prüfe ob VS Code installiert ist
if command -v code &> /dev/null; then
    echo "✅ VS Code gefunden"
    HAS_CODE=true
else
    echo "❌ VS Code nicht gefunden"
    HAS_CODE=false
fi

echo ""

# Wenn keines installiert ist
if [ "$HAS_INSIDER" = false ] && [ "$HAS_CODE" = false ]; then
    echo "❌ Weder VS Code noch VS Code Insider sind installiert!"
    echo ""
    echo "Bitte installiere eine der folgenden Versionen:"
    echo "  - VS Code: https://code.visualstudio.com/"
    echo "  - VS Code Insider: https://code.visualstudio.com/insiders/"
    exit 1
fi

# Frage Benutzer welche Version verwendet werden soll
echo "Welche Version möchtest du verwenden?"
echo ""

if [ "$HAS_INSIDER" = true ]; then
    echo "  1) VS Code Insider (empfohlen)"
fi

if [ "$HAS_CODE" = true ]; then
    echo "  2) VS Code"
fi

echo "  3) Abbrechen"
echo ""

read -p "Deine Wahl (1-3): " choice

case $choice in
    1)
        if [ "$HAS_INSIDER" = true ]; then
            echo ""
            echo "📂 Öffne Projekt in VS Code Insider..."
            code-insiders workspace.code-workspace
            echo "✅ Fertig! VS Code Insider sollte sich jetzt öffnen."
        else
            echo "❌ VS Code Insider ist nicht installiert!"
            exit 1
        fi
        ;;
    2)
        if [ "$HAS_CODE" = true ]; then
            echo ""
            echo "📂 Öffne Projekt in VS Code..."
            code workspace.code-workspace
            echo "✅ Fertig! VS Code sollte sich jetzt öffnen."
        else
            echo "❌ VS Code ist nicht installiert!"
            exit 1
        fi
        ;;
    3)
        echo "Abgebrochen."
        exit 0
        ;;
    *)
        echo "❌ Ungültige Auswahl!"
        exit 1
        ;;
esac

echo ""
echo "💡 Tipps:"
echo "  - Installiere die empfohlenen Extensions (Popup erscheint automatisch)"
echo "  - Wähle einen Python Interpreter: Ctrl+Shift+P → 'Python: Select Interpreter'"
echo "  - Starte die App mit F5 oder über Tasks"
echo ""
echo "📖 Weitere Infos: Siehe VS_CODE_INSIDER_VERBINDUNG.md"
