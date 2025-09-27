#!/bin/bash

# 🎮 GIT MASTER QUEST - Versione Semplificata
# Tutorial interattivo per imparare Git

clear
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    🎮 GIT MASTER QUEST 🎮                    ║"
echo "║                                                              ║"
echo "║          Impara Git attraverso sfide pratiche!              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo
echo "🎯 BENVENUTO! Iniziamo con i fondamentali di Git!"
echo
echo "📚 LIVELLO 1: Il tuo primo repository Git"
echo
echo "QUIZ 1: Quale comando inizializza un nuovo repository Git?"
echo "a) git start"
echo "b) git init"
echo "c) git begin"
echo
read -p "Risposta (a/b/c): " answer

if [ "$answer" = "b" ] || [ "$answer" = "B" ]; then
    echo "✅ Corretto! git init crea un nuovo repository Git."
    echo
    echo "🛠️ PRATICA: Ora inizializziamo davvero un repository!"
    echo "Digita: git init"
    read -p "$ " command

    if [ "$command" = "git init" ]; then
        echo "✅ Perfetto! Eseguiamo il comando..."
        git init
        echo
        echo "🎉 Repository Git inizializzato con successo!"
    else
        echo "❌ Il comando corretto era: git init"
        echo "Eseguiamo comunque il comando corretto:"
        git init
    fi
else
    echo "❌ Sbagliato! La risposta corretta è 'b' - git init"
    echo "Eseguiamo comunque il comando:"
    git init
fi

echo
echo "📝 Ora creiamo il nostro primo file..."
echo "# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!" > README.md

echo "✅ File README.md creato!"
echo
echo "QUIZ 2: Quale comando mostra lo stato del repository?"
read -p "$ " command

if [[ "$command" == *"git status"* ]]; then
    echo "✅ Perfetto!"
    git status
else
    echo "❌ Il comando corretto è: git status"
    git status
fi

echo
echo "🎯 Il file è 'untracked' (non tracciato)."
echo "QUIZ 3: Come aggiungiamo README.md al staging area?"
read -p "$ " command

if [[ "$command" == *"git add"* ]]; then
    echo "✅ Ottimo!"
    eval "$command"
    echo "File aggiunto al staging area!"
else
    echo "❌ Il comando corretto è: git add README.md"
    git add README.md
fi

echo
echo "QUIZ 4: Ora facciamo il commit! Usa un messaggio descrittivo:"
read -p "$ " command

if [[ "$command" == *"git commit -m"* ]]; then
    echo "✅ Perfetto!"
    eval "$command"
    echo "🎉 Primo commit creato con successo!"
else
    echo "❌ Il comando corretto è: git commit -m \"tuo messaggio\""
    git commit -m "Primo commit: aggiunto README"
fi

echo
echo "🏆 LIVELLO 1 COMPLETATO!"
echo
echo "📚 Ora impariamo i branch e i conflitti..."
echo "Premi INVIO per continuare al Livello 2..."
read

echo "🌳 LIVELLO 2: BRANCHING E CONFLITTI"
echo
echo "QUIZ: Come si crea un nuovo branch chiamato 'feature'?"
read -p "$ " command

if [[ "$command" == *"git branch feature"* ]] || [[ "$command" == *"git checkout -b feature"* ]]; then
    echo "✅ Corretto!"
    if [[ "$command" == *"-b"* ]]; then
        eval "$command"
        echo "Branch creato e attivato!"
    else
        git branch feature
        echo "Branch creato. Ora attiviamolo:"
        read -p "$ git checkout " branch
        git checkout $branch
    fi
else
    echo "❌ Modi corretti: git branch feature, git checkout -b feature"
    git checkout -b feature
fi

echo
echo "📝 Modifichiamo README.md nel branch 'feature'..."
echo "# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Nuova Feature
Questa è una nuova funzionalità aggiunta nel branch feature!" > README.md

echo "✅ File modificato!"
echo "Ora fai commit delle modifiche (git add + git commit):"
read -p "$ " command1
eval "$command1"
read -p "$ " command2
eval "$command2"

echo
echo "⚠️ ORA CREIAMO UN CONFLITTO!"
echo "Torniamo al branch main:"
read -p "$ git checkout " branch
git checkout $branch

echo
echo "💥 Modifichiamo lo stesso file anche in main..."
echo "# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Aggiornamento Importante
Questo è un aggiornamento fatto direttamente nel branch main!" > README.md

git add README.md
git commit -m "Aggiornamento in main"

echo
echo "✅ Ora abbiamo due branch con modifiche conflittuali!"
echo "💥 Proviamo a fare il merge del branch feature:"
read -p "$ " command

echo "Eseguiamo: git merge feature"
git merge feature

echo
echo "💥 CONFLITTO RILEVATO!"
echo "📖 Vediamo il contenuto del file:"
echo
cat README.md

echo
echo "🎓 LEZIONE SUI CONFLITTI:"
echo "I marker di conflitto sono:"
echo "<<<<<<< HEAD          (versione corrente - main)"
echo "======="
echo ">>>>>>> feature      (versione in arrivo)"
echo
echo "Per risolvere:"
echo "1. Modifica il file rimuovendo i marker"
echo "2. Mantieni solo il contenuto che vuoi"
echo "3. git add del file risolto"
echo "4. git commit per completare il merge"

echo
echo "🎉 CONGRATULAZIONI!"
echo "Hai completato Git Master Quest - Versione Introduttiva!"
echo
echo "🚀 PROSSIMI PASSI:"
echo "• Installa Python per la versione completa del gioco"
echo "• Pratica con repository GitHub"
echo "• Impara git rebase, cherry-pick, stash"
echo "• Contribuisci a progetti open source"
echo
echo "📚 Risorse utili:"
echo "• https://git-scm.com/book (Pro Git book gratuito)"
echo "• https://learngitbranching.js.org/ (tutorial interattivo)"
echo "• https://github.com/skills (GitHub Skills)"