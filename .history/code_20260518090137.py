# Découper un PDF en plusieurs PDFs (1 page par fichier)
# Nécessite : pip install PyPDF2

from PyPDF2 import PdfReader, PdfWriter
import os

# ====== CONFIGURATION ======
input_pdf = "document.pdf"      # Ton PDF de départ
output_folder = "pages_pdf"     # Dossier de sortie
# ===========================

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

# Lire le PDF
reader = PdfReader(input_pdf)

# Nombre total de pages
num_pages = len(reader.pages)

print(f"Nombre de pages : {num_pages}")

# Boucle sur chaque page
for i in range(num_pages):
    writer = PdfWriter()

    # Ajouter la page actuelle
    writer.add_page(reader.pages[i])

    # Nom du fichier de sortie
    output_path = os.path.join(output_folder, f"page_{i+1}.pdf")

    # Sauvegarder le PDF
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Créé : {output_path}")

print("Terminé !")