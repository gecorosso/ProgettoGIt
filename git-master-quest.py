#!/usr/bin/env python3
"""
🎮 GIT MASTER QUEST - Il Gioco Didattico per Git
Un gioco interattivo per imparare Git attraverso sfide pratiche e simulazioni di conflitti
"""

import os
import subprocess
import sys
from pathlib import Path

class GitMasterQuest:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.current_repo = None
        self.colors = {
            'GREEN': '\033[92m',
            'RED': '\033[91m',
            'YELLOW': '\033[93m',
            'BLUE': '\033[94m',
            'PURPLE': '\033[95m',
            'CYAN': '\033[96m',
            'BOLD': '\033[1m',
            'END': '\033[0m'
        }

    def print_colored(self, text, color='END'):
        print(f"{self.colors[color]}{text}{self.colors['END']}")

    def print_banner(self):
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    🎮 GIT MASTER QUEST 🎮                    ║
║                                                              ║
║          Impara Git attraverso sfide pratiche!              ║
║                                                              ║
║    Livello: {level:<2}                              Punteggio: {score:<6} ║
╚══════════════════════════════════════════════════════════════╝
        """.format(level=self.level, score=self.score)
        self.print_colored(banner, 'CYAN')

    def wait_for_input(self, prompt="Premi INVIO per continuare..."):
        input(f"\n{self.colors['YELLOW']}{prompt}{self.colors['END']}")

    def run_command(self, command, capture_output=True):
        """Esegue un comando e restituisce il risultato"""
        try:
            if capture_output:
                result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd="/mnt/c/ProgettoGit")
                return result.returncode == 0, result.stdout, result.stderr
            else:
                result = subprocess.run(command, shell=True, cwd="/mnt/c/ProgettoGit")
                return result.returncode == 0, "", ""
        except Exception as e:
            return False, "", str(e)

    def check_git_installed(self):
        """Verifica se Git è installato"""
        success, _, _ = self.run_command("git --version")
        if not success:
            self.print_colored("❌ Git non è installato! Installa Git prima di continuare.", 'RED')
            return False
        return True

    def start_game(self):
        """Avvia il gioco"""
        self.print_banner()

        if not self.check_git_installed():
            return

        self.print_colored("""
🎯 BENVENUTO IN GIT MASTER QUEST! 🎯

Questo è un gioco didattico per imparare Git attraverso sfide pratiche.
Imparerai:
• Comandi base di Git
• Gestione dei branch
• Risoluzione dei conflitti
• Tecniche avanzate
• Come uscire da situazioni "catastrofiche"

Ogni livello ti insegnerà qualcosa di nuovo e ti sfiderà con problemi reali!
        """, 'GREEN')

        self.wait_for_input()
        self.level_1_basics()

    def level_1_basics(self):
        """Livello 1: Comandi base di Git"""
        self.level = 1
        self.print_banner()

        self.print_colored("🏁 LIVELLO 1: I FONDAMENTALI DI GIT", 'BOLD')
        self.print_colored("""
In questo livello imparerai:
• git init (inizializzare un repository)
• git add (aggiungere file al staging)
• git commit (creare un commit)
• git status (controllare lo stato)
• git log (vedere la storia)
        """, 'BLUE')

        self.wait_for_input("Iniziamo! Premi INVIO...")

        # Quiz 1: git init
        self.print_colored("\n📚 QUIZ 1: Come si inizializza un nuovo repository Git?", 'YELLOW')
        self.print_colored("a) git start", 'WHITE')
        self.print_colored("b) git init", 'WHITE')
        self.print_colored("c) git begin", 'WHITE')

        answer = input("\nRisposta (a/b/c): ").lower().strip()
        if answer == 'b':
            self.print_colored("✅ Corretto! git init crea un nuovo repository Git.", 'GREEN')
            self.score += 10
        else:
            self.print_colored("❌ Sbagliato! La risposta corretta è 'b' - git init", 'RED')

        # Pratica: Inizializzare repo
        self.print_colored("\n🛠️ PRATICA: Ora inizializziamo un repository!", 'CYAN')
        self.print_colored("Scrivi il comando per inizializzare un repository Git:", 'YELLOW')

        user_command = input("$ ").strip()
        if user_command == "git init":
            success, output, error = self.run_command("git init")
            if success:
                self.print_colored("✅ Perfetto! Repository inizializzato!", 'GREEN')
                self.print_colored(f"Output: {output}", 'BLUE')
                self.score += 20
            else:
                self.print_colored(f"❌ Errore: {error}", 'RED')
        else:
            self.print_colored("❌ Comando errato! Il comando corretto è: git init", 'RED')
            self.run_command("git init")

        self.wait_for_input()
        self.level_1_continued()

    def level_1_continued(self):
        """Continua il livello 1 con file e commit"""
        # Creiamo un file di esempio
        self.print_colored("\n📝 Creiamo il nostro primo file:", 'CYAN')

        with open("/mnt/c/ProgettoGit/README.md", "w") as f:
            f.write("# Il Mio Primo Progetto Git\n\nQuesto è un file di esempio per imparare Git!")

        self.print_colored("Ho creato README.md per te. Ora vediamo lo stato del repository:", 'BLUE')

        # Quiz 2: git status
        self.print_colored("\n📚 QUIZ 2: Quale comando mostra lo stato del repository?", 'YELLOW')
        user_command = input("$ ").strip()

        if user_command == "git status":
            success, output, error = self.run_command("git status")
            self.print_colored("✅ Perfetto!", 'GREEN')
            self.print_colored(f"Output:\n{output}", 'BLUE')
            self.score += 15
        else:
            self.print_colored("❌ Il comando corretto è: git status", 'RED')
            self.run_command("git status", False)

        # Quiz 3: git add
        self.print_colored("\n📚 QUIZ 3: Come aggiungiamo README.md al staging area?", 'YELLOW')
        user_command = input("$ ").strip()

        if user_command in ["git add README.md", "git add ."]:
            success, output, error = self.run_command(user_command)
            self.print_colored("✅ Ottimo! File aggiunto al staging area!", 'GREEN')
            self.score += 15
        else:
            self.print_colored("❌ Il comando corretto è: git add README.md (o git add .)", 'RED')
            self.run_command("git add README.md")

        # Quiz 4: git commit
        self.print_colored("\n📚 QUIZ 4: Ora facciamo il commit! Usa un messaggio descrittivo:", 'YELLOW')
        user_command = input("$ ").strip()

        if user_command.startswith("git commit -m"):
            success, output, error = self.run_command(user_command)
            if success:
                self.print_colored("✅ Perfetto! Primo commit creato!", 'GREEN')
                self.print_colored(f"Output: {output}", 'BLUE')
                self.score += 25
            else:
                self.print_colored(f"❌ Errore: {error}", 'RED')
        else:
            self.print_colored("❌ Il comando corretto è: git commit -m \"tuo messaggio\"", 'RED')
            self.run_command('git commit -m "Primo commit: aggiunto README"')

        # Completamento livello 1
        self.print_colored(f"\n🎉 LIVELLO 1 COMPLETATO! Punteggio: {self.score}", 'GREEN')
        self.wait_for_input("Pronto per il Livello 2? (Branching e Merging)")
        self.level_2_branching()

    def level_2_branching(self):
        """Livello 2: Branching e primi conflitti"""
        self.level = 2
        self.print_banner()

        self.print_colored("🌳 LIVELLO 2: BRANCHING E PRIMI CONFLITTI", 'BOLD')
        self.print_colored("""
In questo livello imparerai:
• git branch (creare e gestire branch)
• git checkout / git switch (cambiare branch)
• git merge (unire branch)
• Risolvere conflitti semplici
        """, 'BLUE')

        self.wait_for_input()

        # Creiamo un nuovo branch
        self.print_colored("\n📚 QUIZ: Come si crea un nuovo branch chiamato 'feature'?", 'YELLOW')
        user_command = input("$ ").strip()

        if user_command in ["git branch feature", "git checkout -b feature", "git switch -c feature"]:
            if "checkout -b" in user_command or "switch -c" in user_command:
                self.run_command(user_command)
                self.print_colored("✅ Perfetto! Branch creato e attivato!", 'GREEN')
            else:
                self.run_command("git branch feature")
                self.print_colored("✅ Corretto! Branch creato. Ora attiviamolo:", 'GREEN')
                user_command2 = input("$ ").strip()
                if "checkout feature" in user_command2 or "switch feature" in user_command2:
                    self.run_command(user_command2)
                    self.print_colored("✅ Branch attivato!", 'GREEN')
                else:
                    self.print_colored("❌ Usa: git checkout feature o git switch feature", 'RED')
                    self.run_command("git checkout feature")
            self.score += 20
        else:
            self.print_colored("❌ Modi corretti: git branch feature, git checkout -b feature, git switch -c feature", 'RED')
            self.run_command("git checkout -b feature")

        self.continue_to_conflict_simulation()

    def continue_to_conflict_simulation(self):
        """Continua con la simulazione di conflitti"""
        # Modifichiamo il file nel branch feature
        self.print_colored("\n📝 Modifichiamo README.md nel branch 'feature':", 'CYAN')

        with open("/mnt/c/ProgettoGit/README.md", "w") as f:
            f.write("""# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Nuova Feature
Questa è una nuova funzionalità aggiunta nel branch feature!
""")

        self.print_colored("File modificato! Ora fai commit delle modifiche:", 'YELLOW')
        user_command = input("$ ").strip()

        if "git add" in user_command:
            self.run_command(user_command)
            self.print_colored("Ora fai il commit:", 'YELLOW')
            user_command = input("$ ").strip()

        if "git commit" in user_command:
            self.run_command(user_command)
            self.print_colored("✅ Commit nel branch feature completato!", 'GREEN')
            self.score += 15
        else:
            self.print_colored("❌ Devi fare git add e git commit", 'RED')
            self.run_command("git add README.md")
            self.run_command('git commit -m "Aggiunta nuova feature"')

        # Torniamo al main e creiamo un conflitto
        self.print_colored("\n⚠️ ORA CREIAMO UN CONFLITTO! ⚠️", 'RED')
        self.print_colored("Torniamo al branch main:", 'YELLOW')

        user_command = input("$ ").strip()
        if "main" in user_command or "master" in user_command:
            self.run_command(user_command)
        else:
            self.print_colored("❌ Usa: git checkout main (o master)", 'RED')
            self.run_command("git checkout main")

        # Modifichiamo lo stesso file in main
        self.print_colored("\n💥 Modifichiamo lo stesso file anche in main (questo creerà un conflitto!):", 'CYAN')

        with open("/mnt/c/ProgettoGit/README.md", "w") as f:
            f.write("""# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Aggiornamento Importante
Questo è un aggiornamento fatto direttamente nel branch main!
""")

        self.run_command("git add README.md")
        self.run_command('git commit -m "Aggiornamento in main"')

        self.print_colored("✅ Ora abbiamo due branch con modifiche conflittuali!", 'GREEN')
        self.wait_for_input("Pronto per imparare a risolvere i conflitti?")
        self.simulate_merge_conflict()

    def simulate_merge_conflict(self):
        """Simula e risolve un conflitto di merge"""
        self.print_colored("\n💥 SIMULAZIONE CONFLITTO DI MERGE", 'RED')
        self.print_colored("""
Situazione:
• Branch main: ha modificato README.md con "Aggiornamento Importante"
• Branch feature: ha modificato README.md con "Nuova Feature"
• Stesso file, stesse righe = CONFLITTO!
        """, 'YELLOW')

        self.print_colored("Proviamo a fare il merge del branch feature:", 'CYAN')
        user_command = input("$ ").strip()

        if "git merge feature" in user_command:
            success, output, error = self.run_command("git merge feature")
            if not success:
                self.print_colored("💥 CONFLITTO RILEVATO!", 'RED')
                self.print_colored(f"Output:\n{output}\n{error}", 'YELLOW')
            else:
                self.print_colored("⚠️ Nessun conflitto? Riproviamo...", 'YELLOW')
        else:
            self.print_colored("❌ Il comando corretto è: git merge feature", 'RED')
            self.run_command("git merge feature")

        # Mostriamo il contenuto del file con conflitto
        self.print_colored("\n📖 Vediamo il contenuto del file in conflitto:", 'CYAN')

        try:
            with open("/mnt/c/ProgettoGit/README.md", "r") as f:
                content = f.read()
                self.print_colored(f"Contenuto di README.md:\n{content}", 'BLUE')
        except:
            pass

        self.print_colored("""
🎓 LEZIONE SUI CONFLITTI:

I marker di conflitto sono:
<<<<<<< HEAD          (versione corrente - main)
contenuto del main
=======              (separatore)
contenuto del feature
>>>>>>> feature      (versione in arrivo)

Per risolvere:
1. Modifica il file rimuovendo i marker <<<, ===, >>>
2. Mantieni solo il contenuto che vuoi
3. git add del file risolto
4. git commit per completare il merge
        """, 'GREEN')

        self.wait_for_input("Ora risolviamo insieme il conflitto!")
        self.guide_conflict_resolution()

    def guide_conflict_resolution(self):
        """Guida l'utente nella risoluzione del conflitto"""
        self.print_colored("\n🔧 RISOLUZIONE GUIDATA DEL CONFLITTO", 'CYAN')

        # Creiamo manualmente un file con conflitto per essere sicuri
        conflict_content = """# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

<<<<<<< HEAD
## Aggiornamento Importante
Questo è un aggiornamento fatto direttamente nel branch main!
=======
## Nuova Feature
Questa è una nuova funzionalità aggiunta nel branch feature!
>>>>>>> feature
"""

        with open("/mnt/c/ProgettoGit/README.md", "w") as f:
            f.write(conflict_content)

        self.print_colored("Ho ricreato il conflitto per te. Ecco cosa devi fare:", 'YELLOW')
        self.print_colored("""
OPZIONI PER RISOLVERE:
1. Tenere solo la versione di main
2. Tenere solo la versione di feature
3. Combinare entrambe le versioni
4. Scrivere qualcosa di completamente nuovo

Quale scegli? (1/2/3/4):""", 'BLUE')

        choice = input().strip()

        if choice == "1":
            resolved_content = """# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Aggiornamento Importante
Questo è un aggiornamento fatto direttamente nel branch main!
"""
        elif choice == "2":
            resolved_content = """# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Nuova Feature
Questa è una nuova funzionalità aggiunta nel branch feature!
"""
        elif choice == "3":
            resolved_content = """# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Aggiornamento Importante
Questo è un aggiornamento fatto direttamente nel branch main!

## Nuova Feature
Questa è una nuova funzionalità aggiunta nel branch feature!
"""
        else:
            resolved_content = """# Il Mio Primo Progetto Git

Questo è un file di esempio per imparare Git!

## Versione Unificata
Ho combinato le migliori parti di entrambe le versioni!
"""

        with open("/mnt/c/ProgettoGit/README.md", "w") as f:
            f.write(resolved_content)

        self.print_colored("✅ Conflitto risolto! Ora aggiungi il file risolto:", 'GREEN')
        user_command = input("$ ").strip()

        if "git add" in user_command:
            self.run_command(user_command)
            self.print_colored("Ora completa il merge con un commit:", 'YELLOW')
            user_command = input("$ ").strip()
            if "git commit" in user_command:
                self.run_command(user_command)
                self.print_colored("🎉 CONFLITTO RISOLTO CON SUCCESSO!", 'GREEN')
                self.score += 50
            else:
                self.print_colored("❌ Devi fare git commit per completare il merge", 'RED')
                self.run_command('git commit -m "Risolto conflitto merge"')
        else:
            self.print_colored("❌ Prima devi fare git add per aggiungere il file risolto", 'RED')
            self.run_command("git add README.md")
            self.run_command('git commit -m "Risolto conflitto merge"')

        self.print_colored(f"\n🏆 LIVELLO 2 COMPLETATO! Punteggio totale: {self.score}", 'GREEN')
        self.wait_for_input("Pronto per gli scenari avanzati e le situazioni di emergenza?")
        self.emergency_scenarios_menu()

    def emergency_scenarios_menu(self):
        """Menu degli scenari di emergenza"""
        self.print_colored("\n🚨 SCENARI DI EMERGENZA E RECOVERY", 'RED')
        self.print_colored("""
Scegli uno scenario da imparare:

1. 😱 "Help! Ho fatto commit al branch sbagliato!"
2. 🔥 "Ho fatto push di qualcosa che non dovevo!"
3. 💀 "Ho cancellato file importanti!"
4. 🌪️ "Il mio repository è un disastro totale!"
5. ⚡ "Come annullo l'ultimo commit?"
6. 🎯 "Voglio solo alcune modifiche da un altro branch"
7. 📚 Vedere tutti i comandi pericolosi da evitare
8. 🏁 Finire il gioco

Scegli (1-8):""", 'YELLOW')

        choice = input().strip()

        scenarios = {
            '1': self.wrong_branch_scenario,
            '2': self.wrong_push_scenario,
            '3': self.deleted_files_scenario,
            '4': self.total_disaster_scenario,
            '5': self.undo_commit_scenario,
            '6': self.cherry_pick_scenario,
            '7': self.dangerous_commands_lesson,
            '8': self.finish_game
        }

        if choice in scenarios:
            scenarios[choice]()
        else:
            self.print_colored("❌ Scelta non valida!", 'RED')
            self.emergency_scenarios_menu()

    def wrong_branch_scenario(self):
        """Scenario: commit nel branch sbagliato"""
        self.print_colored("\n😱 SCENARIO: COMMIT NEL BRANCH SBAGLIATO", 'RED')
        self.print_colored("""
Situazione: Hai fatto un commit nel branch main ma doveva andare in feature!

Cosa è successo:
• Eri su main
• Hai modificato dei file
• Hai fatto commit
• Ti sei accorto che doveva essere su feature!

SOLUZIONI POSSIBILI:
""", 'YELLOW')

        # Simuliamo la situazione
        self.run_command("git checkout main")

        with open("/mnt/c/ProgettoGit/wrong_commit.txt", "w") as f:
            f.write("Questo commit doveva essere nel branch feature!")

        self.run_command("git add wrong_commit.txt")
        self.run_command('git commit -m "Commit sbagliato - doveva essere in feature"')

        self.print_colored("""
🔧 SOLUZIONE 1: git reset (il più comune)
Rimuove il commit dal branch corrente mantenendo le modifiche

Quale comando useresti per rimuovere l'ultimo commit ma mantenere i file?
a) git reset --soft HEAD~1
b) git reset --hard HEAD~1
c) git reset HEAD~1

Scegli (a/b/c):""", 'CYAN')

        choice = input().strip().lower()

        if choice == 'a':
            self.print_colored("✅ PERFETTO! git reset --soft mantiene i file e li lascia in staging", 'GREEN')
            self.run_command("git reset --soft HEAD~1")
            self.score += 30
        elif choice == 'c':
            self.print_colored("✅ BUONO! git reset mantiene i file ma li toglie dallo staging", 'GREEN')
            self.run_command("git reset HEAD~1")
            self.score += 25
        else:
            self.print_colored("❌ PERICOLOSO! --hard cancellerebbe anche le modifiche!", 'RED')
            self.print_colored("Useremo --soft per sicurezza:", 'YELLOW')
            self.run_command("git reset --soft HEAD~1")

        self.print_colored("\nOra i tuoi file sono pronti. Passiamo al branch corretto:", 'CYAN')
        user_command = input("$ git checkout ").strip()

        if "feature" in user_command:
            self.run_command(f"git checkout {user_command}")
            self.print_colored("Ora rifai il commit nel branch giusto!", 'YELLOW')
            user_command = input("$ ").strip()
            if "git commit" in user_command:
                self.run_command(user_command)
                self.print_colored("🎉 PROBLEMA RISOLTO! Commit spostato nel branch corretto!", 'GREEN')
                self.score += 20
            else:
                self.run_command('git commit -m "Commit nel branch corretto"')

        self.print_colored("""
📚 COSA HAI IMPARATO:
• git reset --soft: rimuove commit, mantiene file in staging
• git reset: rimuove commit, mantiene file non staged
• git reset --hard: PERICOLOSO - cancella tutto!
• Sempre controllare il branch prima di fare commit!
        """, 'GREEN')

        self.wait_for_input()
        self.emergency_scenarios_menu()

    def wrong_push_scenario(self):
        """Scenario: push sbagliato"""
        self.print_colored("\n🔥 SCENARIO: HO FATTO PUSH DI QUALCOSA CHE NON DOVEVO!", 'RED')
        self.print_colored("""
😰 OH NO! Hai fatto push di:
• Credenziali/password
• File temporanei
• Codice non finito
• Informazioni sensibili

COSA FARE:
        """, 'YELLOW')

        self.print_colored("""
⚠️ IMPORTANTE: Se hai fatto push di CREDENZIALI, cambiale SUBITO!
Git mantiene la storia, quindi anche se rimuovi il file, le credenziali
restano accessibili nella cronologia!

📋 PIANO DI RECOVERY:

1. 🚨 URGENTE: Cambia le credenziali compromesse
2. 🔄 Rimuovi il commit problematico
3. 🔐 Forza il push per sovrascrivere la storia
4. 📢 Avvisa il team (se necessario)

Scenari:

A) 🕐 ULTIMO COMMIT: git reset HEAD~1 && git push --force
B) 🕑 COMMIT PIÙ VECCHIO: git revert <commit> o git rebase -i
C) 💀 DISASTRO TOTALE: considera l'eliminazione del repo

⚠️ ATTENZIONE: --force è PERICOLOSO nei progetti condivisi!
Può cancellare il lavoro degli altri sviluppatori!
        """, 'CYAN')

        self.print_colored("""
🛡️ ALTERNATIVE PIÙ SICURE:

1. git revert: crea un nuovo commit che annulla quello sbagliato
2. git push --force-with-lease: più sicuro di --force
3. Coordinare con il team prima di modificare la storia

QUIZ: Cosa faresti se hai fatto push di una password nell'ultimo commit?

a) git reset HEAD~1 && git push --force
b) Cambiare la password, poi git revert
c) Prima cambiare la password, poi git reset e force push
d) Ignorare, tanto nessuno se ne accorge

Risposta:""", 'YELLOW')

        choice = input().strip().lower()

        if choice == 'c':
            self.print_colored("✅ PERFETTO! Prima la sicurezza, poi la pulizia!", 'GREEN')
            self.score += 40
        elif choice == 'b':
            self.print_colored("✅ BUONO! Sicuro e preserva la storia", 'GREEN')
            self.score += 30
        elif choice == 'a':
            self.print_colored("⚠️ PERICOLOSO! Prima cambia la password!", 'YELLOW')
            self.score += 10
        else:
            self.print_colored("❌ MAI ignorare problemi di sicurezza!", 'RED')

        self.print_colored("""
📚 COMANDI UTILI PER RECOVERY:

• git log --oneline: vedere gli ultimi commit
• git show <commit>: vedere cosa c'è in un commit
• git revert <commit>: annullare un commit specifico
• git reset --hard HEAD~n: tornare indietro di n commit (PERICOLOSO!)
• git reflog: vedere TUTTO quello che hai fatto (salvavita!)
• git push --force-with-lease: force push più sicuro
        """, 'GREEN')

        self.wait_for_input()
        self.emergency_scenarios_menu()

    def deleted_files_scenario(self):
        """Scenario: file cancellati"""
        self.print_colored("\n💀 SCENARIO: HO CANCELLATO FILE IMPORTANTI!", 'RED')

        # Simuliamo la cancellazione
        self.print_colored("Simuliamo la cancellazione di un file importante...", 'YELLOW')

        with open("/mnt/c/ProgettoGit/important_file.txt", "w") as f:
            f.write("Questo è un file molto importante che non doveva essere cancellato!")

        self.run_command("git add important_file.txt")
        self.run_command('git commit -m "Aggiunto file importante"')

        # Cancelliamo il file
        os.remove("/mnt/c/ProgettoGit/important_file.txt")

        self.print_colored("\n😱 OH NO! Il file important_file.txt è stato cancellato!", 'RED')
        self.print_colored("Come lo recuperiamo?", 'YELLOW')

        self.print_colored("""
🔍 DIAGNOSI: Vediamo cosa è successo

git status ci dirà se il file è:
• Solo cancellato dal filesystem (recuperabile)
• Cancellato e staged per commit (ancora recuperabile)
• Già committato come cancellato (recuperabile da storia)
        """, 'CYAN')

        success, output, _ = self.run_command("git status")
        self.print_colored(f"Git status output:\n{output}", 'BLUE')

        self.print_colored("""
🛠️ SOLUZIONI:

1. 📁 CANCELLATO SOLO DAL FILESYSTEM:
   git checkout -- nome_file
   (ripristina dalla staging area o ultimo commit)

2. 🗑️ CANCELLATO E IN STAGING:
   git reset HEAD nome_file  (toglie dalla staging)
   git checkout -- nome_file  (ripristina il file)

3. 💾 CANCELLATO DA UN COMMIT SPECIFICO:
   git checkout <commit_hash> -- nome_file

4. 🔍 NON SAI DOVE ERA:
   git log --follow -- nome_file  (trova la storia del file)

Quale comando usi per ripristinare important_file.txt?""", 'GREEN')

        user_command = input("$ ").strip()

        if "git checkout" in user_command and "important_file.txt" in user_command:
            self.run_command(user_command)
            if os.path.exists("/mnt/c/ProgettoGit/important_file.txt"):
                self.print_colored("🎉 FILE RECUPERATO CON SUCCESSO!", 'GREEN')
                self.score += 35
            else:
                self.print_colored("Riproviamo con il comando corretto:", 'YELLOW')
                self.run_command("git checkout -- important_file.txt")
        else:
            self.print_colored("Il comando corretto è: git checkout -- important_file.txt", 'YELLOW')
            self.run_command("git checkout -- important_file.txt")

        self.print_colored("""
🎓 LEZIONE AVANZATA: IL REFLOG (il tuo salvavita!)

git reflog mostra TUTTO quello che hai fatto, anche commit "persi".
È come una cronologia completa delle tue azioni Git.

Utile quando:
• Hai fatto reset --hard per sbaglio
• Hai cancellato un branch
• Hai perso commit dopo un rebase
• Hai bisogno di tornare a uno stato precedente

Comando: git reflog
Poi: git checkout <hash> per recuperare qualsiasi stato!
        """, 'PURPLE')

        self.run_command("git reflog")

        self.wait_for_input()
        self.emergency_scenarios_menu()

    def dangerous_commands_lesson(self):
        """Lezione sui comandi pericolosi"""
        self.print_colored("\n⚠️ COMANDI PERICOLOSI CHE POSSONO ROVINARE LA TUA CARRIERA", 'RED')

        self.print_colored("""
🚨 LIVELLO DI PERICOLO: 💀💀💀 MORTALE

git reset --hard
• Cancella TUTTO: modifiche non committate, staging area
• Non c'è modo di recuperare le modifiche perse
• Usa solo se sei SICURO al 100%

git push --force
• Sovrascrive la storia del repository remoto
• Può cancellare il lavoro di altri sviluppatori
• Può causare perdita permanente di dati
• MAI usare in progetti condivisi senza coordinamento

git rebase -i (interactive rebase)
• Riscrive la storia dei commit
• Può creare conflitti complessi
• Se fatto male, può perdere commit
• Pericoloso su branch condivisi

git branch -D
• Cancella un branch forzatamente
• Non controlla se ci sono commit non merged
• Perdita potenziale di lavoro
        """, 'RED')

        self.print_colored("""
🚨 LIVELLO DI PERICOLO: ⚡⚡ MOLTO PERICOLOSO

git clean -fd
• Cancella tutti i file non tracciati
• Include directory intere
• Non è reversibile

git checkout -- .
• Annulla TUTTE le modifiche non committate
• Perde tutto il lavoro non salvato

git reset HEAD~n
• Rimuove gli ultimi n commit
• Può perdere lavoro se non fatto con attenzione
        """, 'YELLOW')

        self.print_colored("""
🛡️ ALTERNATIVE SICURE:

Invece di reset --hard:
• git stash (salva le modifiche)
• git checkout -- file_specifico (solo un file)

Invece di push --force:
• git push --force-with-lease (verifica prima)
• git revert (annulla con nuovo commit)

Invece di branch -D:
• git branch -d (cancella solo se merged)
• git merge --no-ff prima di cancellare

🔍 COMANDI PER VERIFICARE PRIMA:
• git status (cosa cambierà)
• git diff (vedere le differenze)
• git log --oneline (vedere i commit)
• git branch -a (vedere tutti i branch)
        """, 'GREEN')

        self.print_colored("""
📋 QUIZ FINALE: Cosa fai in queste situazioni?

1. Vuoi annullare le modifiche di UN file:
   a) git reset --hard
   b) git checkout -- file.txt  ✅
   c) git clean -fd

2. Vuoi rimuovere l'ultimo commit ma tenere le modifiche:
   a) git reset --hard HEAD~1
   b) git reset --soft HEAD~1  ✅
   c) git revert HEAD

3. Vuoi aggiornare il repository remoto con una modifica:
   a) git push --force
   b) git push --force-with-lease  ✅ (se necessario)
   c) git push (normale)  ✅ (preferibile)

4. Hai modifiche non salvate e vuoi cambiarle branch:
   a) git reset --hard && git checkout altro_branch
   b) git stash && git checkout altro_branch  ✅
   c) git clean -fd && git checkout altro_branch
        """, 'CYAN')

        self.print_colored("""
💡 REGOLA D'ORO:
PRIMA DI USARE COMANDI DISTRUTTIVI:
1. 💾 Fai sempre un backup (git stash o git branch backup)
2. 🔍 Controlla cosa stai per fare (git status, git diff)
3. 🤔 Chiedi a te stesso: "Posso recuperare se va male?"
4. 👥 Se lavori in team, coordina sempre!

La prudenza non è codardia, è professionalità! 🎯
        """, 'PURPLE')

        self.score += 50  # Bonus per aver studiato la sicurezza

        self.wait_for_input()
        self.emergency_scenarios_menu()

    def finish_game(self):
        """Termina il gioco con riassunto"""
        self.print_colored(f"""
🏆 CONGRATULAZIONI! HAI COMPLETATO GIT MASTER QUEST! 🏆

PUNTEGGIO FINALE: {self.score}

🎯 COSA HAI IMPARATO:
✅ Comandi base di Git (init, add, commit, status)
✅ Branching e merging
✅ Risoluzione di conflitti
✅ Scenari di emergenza e recovery
✅ Comandi pericolosi da evitare
✅ Best practices per la sicurezza

🏅 LIVELLO RAGGIUNTO:
""", 'GREEN')

        if self.score >= 200:
            level = "🏆 GIT MASTER - Sei pronto per qualsiasi sfida!"
        elif self.score >= 150:
            level = "🥈 GIT EXPERT - Ottime competenze, continua così!"
        elif self.score >= 100:
            level = "🥉 GIT INTERMEDIATE - Buone basi, pratica ancora!"
        else:
            level = "📚 GIT BEGINNER - Ripassa i fondamentali!"

        self.print_colored(level, 'CYAN')

        self.print_colored("""
📚 PROSSIMI PASSI PER DIVENTARE UN VERO ESPERTO:

1. 🔄 Pratica il workflow Git Flow o GitHub Flow
2. 🏷️ Impara i Git tags per le release
3. 🔍 Studia git bisect per trovare bug
4. 🎯 Pratica git cherry-pick per commit selettivi
5. 🛠️ Configura Git hooks per automatizzazioni
6. 📖 Leggi "Pro Git" book (gratuito online)
7. 💼 Contribuisci a progetti open source su GitHub

🎮 VUOI RIGIOCARE? Rilanciare lo script per nuove sfide!

Grazie per aver giocato a Git Master Quest! 🚀
        """, 'BLUE')

        sys.exit(0)

    def cherry_pick_scenario(self):
        """Scenario: cherry-pick per commit selettivi"""
        self.print_colored("\n🎯 SCENARIO: VOGLIO SOLO ALCUNE MODIFICHE DA UN ALTRO BRANCH", 'CYAN')

        self.print_colored("""
Situazione: Il branch 'experimental' ha 5 commit, ma ne vuoi solo 2 specifici.

Cherry-pick ti permette di "copiare" commit specifici in altro branch!
        """, 'YELLOW')

        # Setup scenario
        self.run_command("git checkout -b experimental")

        for i in range(3):
            with open(f"/mnt/c/ProgettoGit/feature_{i}.txt", "w") as f:
                f.write(f"Feature numero {i}")
            self.run_command(f"git add feature_{i}.txt")
            self.run_command(f'git commit -m "Aggiunta feature {i}"')

        self.run_command("git checkout main")

        self.print_colored("Setup completato! Ora abbiamo 3 commit nel branch experimental.", 'GREEN')

        # Mostra i commit
        success, output, _ = self.run_command("git log --oneline experimental -3")
        self.print_colored(f"Commit nel branch experimental:\n{output}", 'BLUE')

        self.print_colored("""
🎯 CHERRY-PICK CHALLENGE:
Vuoi solo il commit del "feature 1" nel branch main.

Come fai?
1. Trova l'hash del commit che vuoi
2. git cherry-pick <hash>

Quale hash vuoi cherry-pick?""", 'YELLOW')

        user_input = input("Hash del commit: ").strip()

        if user_input:
            success, output, error = self.run_command(f"git cherry-pick {user_input}")
            if success:
                self.print_colored("🎉 Cherry-pick riuscito!", 'GREEN')
                self.score += 30
            else:
                self.print_colored(f"Errore: {error}", 'RED')
                self.print_colored("Riproviamo con il comando automatico...", 'YELLOW')
                # Trova automaticamente l'hash
                success, log_output, _ = self.run_command("git log --oneline experimental -3")
                lines = log_output.strip().split('\n')
                if len(lines) >= 2:
                    hash_to_pick = lines[1].split()[0]  # Secondo commit (feature 1)
                    self.run_command(f"git cherry-pick {hash_to_pick}")

        self.print_colored("""
📚 CHERRY-PICK ADVANCED:

• git cherry-pick <hash1> <hash2>: multipli commit
• git cherry-pick <hash1>..<hash2>: range di commit
• git cherry-pick --no-commit <hash>: applica senza commit
• git cherry-pick --abort: annulla se ci sono conflitti
        """, 'GREEN')

        self.wait_for_input()
        self.emergency_scenarios_menu()

    def undo_commit_scenario(self):
        """Scenario: annullare l'ultimo commit"""
        self.print_colored("\n⚡ SCENARIO: COME ANNULLO L'ULTIMO COMMIT?", 'YELLOW')

        self.print_colored("""
Hai appena fatto un commit ma ti sei accorto di un errore!
Ci sono diversi modi per annullarlo, a seconda di cosa vuoi fare:

📋 OPZIONI:

1. 🔄 ANNULLA MA MANTIENI LE MODIFICHE (più comune)
   git reset --soft HEAD~1
   • Rimuove il commit
   • Mantiene i file modificati in staging
   • Puoi rifare il commit corretto

2. 📝 ANNULLA E RIMUOVI DALLO STAGING
   git reset HEAD~1 (o git reset --mixed HEAD~1)
   • Rimuove il commit
   • Mantiene i file modificati ma non in staging
   • Devi rifare git add

3. 💀 ANNULLA E CANCELLA TUTTO (PERICOLOSO!)
   git reset --hard HEAD~1
   • Rimuove il commit
   • Cancella tutte le modifiche
   • NON RECUPERABILE!

4. 🔀 CREA UN NUOVO COMMIT CHE ANNULLA
   git revert HEAD
   • Mantiene la storia
   • Crea un nuovo commit di "undo"
   • Sicuro per repository condivisi
        """, 'CYAN')

        # Simuliamo un commit sbagliato
        with open("/mnt/c/ProgettoGit/mistake.txt", "w") as f:
            f.write("Questo commit ha un errore!")

        self.run_command("git add mistake.txt")
        self.run_command('git commit -m "Commit con errore - da annullare"')

        self.print_colored("""
🎯 QUIZ: Hai appena fatto il commit sopra, ma c'è un errore nel messaggio.
Vuoi annullarlo per rifare il commit con messaggio corretto.

Quale comando usi?
a) git reset --soft HEAD~1
b) git reset --hard HEAD~1
c) git revert HEAD
d) git commit --amend

Risposta:""", 'YELLOW')

        choice = input().strip().lower()

        if choice == 'a':
            self.print_colored("✅ PERFETTO! Mantieni le modifiche per rifare il commit!", 'GREEN')
            self.run_command("git reset --soft HEAD~1")
            self.score += 25
        elif choice == 'd':
            self.print_colored("✅ OTTIMO! --amend modifica l'ultimo commit!", 'GREEN')
            self.run_command('git commit --amend -m "Commit corretto - errore sistemato"')
            self.score += 30
        elif choice == 'c':
            self.print_colored("✅ BUONO! Sicuro per repository condivisi!", 'GREEN')
            self.run_command("git revert HEAD")
            self.score += 20
        else:
            self.print_colored("❌ PERICOLOSO! --hard cancella tutto!", 'RED')
            self.print_colored("Usiamo --soft per sicurezza:", 'YELLOW')
            self.run_command("git reset --soft HEAD~1")

        self.print_colored("""
🎓 BONUS: git commit --amend

Se vuoi solo modificare l'ultimo commit (messaggio o aggiungere file):
• git commit --amend -m "nuovo messaggio"
• git add file_dimenticato && git commit --amend --no-edit

⚠️ ATTENZIONE: --amend modifica la storia!
Non usare su commit già pushati in repository condivisi!
        """, 'PURPLE')

        self.wait_for_input()
        self.emergency_scenarios_menu()

    def total_disaster_scenario(self):
        """Scenario: disastro totale"""
        self.print_colored("\n🌪️ SCENARIO: IL MIO REPOSITORY È UN DISASTRO TOTALE!", 'RED')

        self.print_colored("""
😱 PANICO TOTALE! Situazioni di completo disastro:

• Branch multipli confusi
• Conflitti ovunque
• Historia corrotta
• Non sai più dove sei
• Merge falliti a metà
• Rebase interrotto
        """, 'YELLOW')

        self.print_colored("""
🚨 PROTOCOLLO DI EMERGENZA "SALVAVITA":

1. 🛑 STOP - Non fare altri comandi Git!

2. 🔍 DIAGNOSI - Capire la situazione:
   git status          (stato attuale)
   git branch -a       (tutti i branch)
   git log --oneline   (ultimi commit)
   git reflog          (cronologia completa)

3. 💾 BACKUP - Salva tutto quello che puoi:
   git stash           (salva modifiche correnti)
   git branch backup-$(date +%Y%m%d) (crea branch backup)

4. 🔄 RESET ALL'ULTIMO STATO BUONO:
   git reflog          (trova un commit buono)
   git reset --hard <hash_buono>

5. 🆘 OPZIONE NUCLEARE - Ricomincia da capo:
   Clona di nuovo il repository remoto
   Applica le tue modifiche manualmente
        """, 'CYAN')

        self.print_colored("""
🛠️ SIMULAZIONE DISASTRO:

Immagina di essere nel mezzo di un merge fallito,
con conflitti irrisolti e in uno stato confuso.

Comandi di EMERGENCY RECOVERY:

1. 🔍 VALUTAZIONE:""", 'RED')

        # Simuliamo uno stato confuso
        success, output, _ = self.run_command("git status")
        self.print_colored(f"git status:\n{output}", 'BLUE')

        success, output, _ = self.run_command("git branch")
        self.print_colored(f"git branch:\n{output}", 'BLUE')

        self.print_colored("""
2. 💾 BACKUP IMMEDIATO:
   Quale comando crea un backup dello stato attuale?""", 'YELLOW')

        user_command = input("$ ").strip()

        if "git stash" in user_command or "git branch" in user_command:
            self.print_colored("✅ Ottimo! Sempre salvare prima di fare recovery!", 'GREEN')
            self.run_command("git stash")
            self.run_command("git branch emergency-backup")
            self.score += 20
        else:
            self.print_colored("💡 Suggerimento: git stash && git branch emergency-backup", 'CYAN')
            self.run_command("git stash")
            self.run_command("git branch emergency-backup")

        self.print_colored("""
3. 🔄 RECOVERY AL PUNTO SICURO:

git reflog ti mostra tutto quello che hai fatto.
Cerca un commit con un messaggio che riconosci come "buono".
        """, 'YELLOW')

        success, output, _ = self.run_command("git reflog --oneline -10")
        self.print_colored(f"git reflog:\n{output}", 'BLUE')

        self.print_colored("""
📚 PREVENZIONE DISASTRI:

1. 🔄 Commit frequenti con messaggi chiari
2. 💾 Push regolari (backup automatico)
3. 🌿 Un branch = una feature (isolamento)
4. 🧪 Testa su branch separati prima di mergare
5. 📖 Usa git status SEMPRE prima di comandi rischiosi
6. 🤝 Comunica con il team prima di operazioni su repository condivisi

🎯 REMEMBER: Git è progettato per essere sicuro.
È quasi impossibile perdere definitivamente il lavoro committato!
        """, 'GREEN')

        self.score += 25
        self.wait_for_input()
        self.emergency_scenarios_menu()

if __name__ == "__main__":
    game = GitMasterQuest()
    game.start_game()