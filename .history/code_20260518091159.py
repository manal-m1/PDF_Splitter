from PyPDF2 import PdfReader, PdfWriter
import os

# Chemin complet du PDF
input_pdf = r"D:\Summer School\Codepythondecoupagepdfsenpdf\document.pdf"

# Dossier où les PDFs générés seront enregistrés
output_folder = r"D:\Summer School\Codepythondecoupagepdfsenpdf\pages_pdf"

# Création du dossier de sortie
os.makedirs(output_folder, exist_ok=True)

# Lecture du PDF
reader = PdfReader(input_pdf)

# Découpage page par page
for i in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[i])

    output_path = os.path.join(output_folder, f"page_{i+1}.pdf")

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Créé : {output_path}")

print("Terminé !")