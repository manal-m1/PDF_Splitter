from PyPDF2 import PdfReader, PdfWriter
import os
import re

# ==============================
# CONFIGURATION
# ==============================

# PDF source
input_pdf = r"D:\Summer School\Codepythondecoupagepdfsenpdf\Certifs.pdf"

# Dossier de sortie
output_folder = r"D:\Summer School\Codepythondecoupagepdfsenpdf\pages_pdf"

# Création du dossier
os.makedirs(output_folder, exist_ok=True)

# ==============================
# FONCTION POUR NETTOYER LE NOM
# ==============================

def clean_filename(text):

    # Supprimer caractères interdits Windows
    text = re.sub(r'[<>:"/\\|?*]', '', text)

    # Supprimer les tirets seuls entourés d'espaces
    text = re.sub(r'\s+-\s+', ' ', text)

    # Remplacer tous les espaces par _
    text = re.sub(r'\s+', '_', text)

    # Supprimer caractères spéciaux inutiles
    text = re.sub(r'[^\w_]', '', text)

    # Supprimer doubles ou triples underscores
    text = re.sub(r'_+', '_', text)

    return text.strip("_")


# ==============================
# EXTRACTION NOM DEPUIS LE TEXTE
# ==============================

def extract_name(page_text, page_number):

    subject = "UnknownSubject"
    professor = "UnknownProfessor"

    # --------------------------
    # Chercher ligne Subject
    # Exemple :
    # Subject - Deep Learning
    # --------------------------
    subject_match = re.search(
        r"Subject\s*[-:]\s*(.+)",
        page_text,
        re.IGNORECASE
    )

    if subject_match:
        subject = subject_match.group(1).split("\n")[0].strip()

    # --------------------------
    # Chercher Prof. ou Dr.
    # Exemple :
    # Prof. Ahmed Benali
    # Dr. Sara Smith
    # --------------------------
    prof_match = re.search(
        r"(Prof\.?|Dr\.?)\s+([A-Za-zÀ-ÿ\s\-]+)",
        page_text
    )

    if prof_match:
        professor = prof_match.group(2).strip()

    # Nettoyage
    subject = clean_filename(subject)
    professor = clean_filename(professor)

    # Nom final
    filename = f"{subject}_{professor}"

    return filename


# ==============================
# LECTURE PDF
# ==============================

reader = PdfReader(input_pdf)

print(f"Nombre de pages : {len(reader.pages)}")

# ==============================
# DÉCOUPAGE
# ==============================

for i, page in enumerate(reader.pages):

    writer = PdfWriter()

    # Ajouter page
    writer.add_page(page)

    # Extraire texte
    text = page.extract_text()

    if text:
        filename = extract_name(text, i + 1)
    else:
        filename = f"page_{i+1}"

    # Chemin final
    output_path = os.path.join(output_folder, f"{filename}.pdf")

    # Sauvegarde
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Créé : {output_path}")

print("Terminé !")