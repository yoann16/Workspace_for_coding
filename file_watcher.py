import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MonGestionnaire(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return  # On ignore les dossiers
        
        fichier = event.src_path
        print(f"Fichier détecté : {fichier}")
        
        # Vérifie si c'est un .h ou .cpp
        if fichier.endswith('.h'):
            self.deplacer_fichier(fichier, "Game/include/")
        elif fichier.endswith('.cpp'):
            self.deplacer_fichier(fichier, "Game/src/")
        else:
            print(f"Fichier ignoré (pas .h ou .cpp) : {fichier}")
    
    def deplacer_fichier(self, source, destination_dossier):
        print(f"Attente de 3 secondes pour stabilité...")
        time.sleep(3)
        
        nom_fichier = os.path.basename(source)
        destination = os.path.join(destination_dossier, nom_fichier)
        
        print(f"Déplacement : {source} → {destination}")
        
        try:
            shutil.move(source, destination)
            print(f"✓ Fichier déplacé avec succès !")
        except Exception as e:
            print(f"✗ Erreur lors du déplacement : {e}")

print("=== Démarrage de la surveillance avancée ===")
print("Je surveille build/Game/ et déplace les .h et .cpp")
print("Appuie sur Ctrl+C pour arrêter")

gestionnaire = MonGestionnaire()
observer = Observer()
observer.schedule(gestionnaire, "build/Game", recursive=False)

observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("\nArrêt de la surveillance")

observer.join()
