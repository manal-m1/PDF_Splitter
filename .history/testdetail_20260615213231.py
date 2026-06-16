from playwright.sync_api import sync_playwright


html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">

<style>

@page {
    size: A4 landscape;
    margin: 1cm;
}

body{
    font-family: Arial, sans-serif;
    padding:20px;
    color:#222;
}


.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:3px solid #003366;
    padding-bottom:15px;
    margin-bottom:20px;
}

.logo{
    width:100px;
}

.title{
    text-align:center;
    flex:1;
}

.title h1{
    color:#003366;
    margin:0;
    font-size:28px;
}

.title h2{
    margin-top:5px;
    font-weight:normal;
}

table{
    width:100%;
    border-collapse:collapse;
}

th{
    background: #8A7F75; 
    color: #FFFFFF; 
    border: 1px solid #786E65;
    padding:12px;
    font-size:18px;
}

td{
    border:1px solid #ccc;
    padding:10px;
    text-align:center;
    font-size:22px;
}

tr:nth-child(even){
    background:#f5f7fa;
}
<style>
/* Variables pour unifier la palette nude */
:root {
  --nude-dark: #8A7F75;    /* Remplacement du bleu marine */
  --nude-mid: #D2C6B6;     /* Pour les bordures et accents */
  --nude-light: #FDFBF7;   /* Fond global */
  --nude-bg-row: #F5F2EF;  /* Fond des lignes */
  --ink: #4A4540;          /* Texte principal */
}

@page { size: A4 landscape; margin: 1cm; background-color: var(--nude-light); }

body { font-family: 'Segoe UI', sans-serif; background: var(--nude-light); color: var(--ink); padding: 20px; }

/* Header unifié */
.header {
  display: flex; justify-content: space-between; align-items: center;
  border-bottom: 3px solid var(--nude-dark);
  padding-bottom: 15px; margin-bottom: 20px;
}
.title h1 { color: var(--nude-dark); margin: 0; font-size: 28px; }

/* Tableau */
table { width: 100%; border-collapse: collapse; }

th {
  background: var(--nude-dark); /* Remplace le bleu */
  color: white;
  border: 1px solid var(--nude-mid);
  padding: 12px;
  font-size: 16px;
  text-transform: uppercase;
}

td {
  border: 1px solid var(--nude-mid);
  padding: 10px;
  text-align: center;
  font-size: 14px;
}

/* Lignes alternées neutres */
tr:nth-child(even) { background: var(--nude-bg-row); }

/* Suppression des anciennes classes colorées (ex: .c-d1, .c-welcome) 
   et remplacement par un style épuré */
.session-highlight { 
  background: #FDF9F5; 
  border-left: 4px solid var(--nude-dark) !important; 
}
</style>
</head>

<body>
   
<div class="header">
  <div>
    <div class="conf-title">
      International Summer School on Artificial Intelligence<br>
      of the Franco-Moroccan Research Center 2026
    </div>
    <div class="conf-sub">Rabat, Morocco &nbsp;·&nbsp; ENSIAS · UIR · FLSHR</div>
  </div>
  <div>
    <div class="big-dates">6–10</div>
    <div class="date-sub">July 2026 &nbsp;·&nbsp; Rabat</div>
  </div>
</div>
<table>

<thead>
<tr>
   <th>Speaker</th>
<th>Session Type</th>

<th>Session Title</th>
<th style="width:180px;">Time Slot</th>
<th>Date</th>
</tr>
</thead>

<tbody>

<tr>
    <td> Prof. Fabrice KORDON
 </td>
    <td> Invited Talk
</td>
    <td> Cybersecurity, the massive surge of AI
</td>
    <td> 12:00  - 13:00 
</td>
    <td>Monday, July 6, 2026
</td>
</tr>
<tr>
    <td>Prof. Mohamed ESSAAIDI</td>
    <td>Invited Talk</td>
    <td>Leveraging AI for the acceleration of the 2030 UN Agenda for Sustainable Developement
</td>
    <td>14:00 - 15:00 
</td>
    <td>Monday, July 6, 2026</td>
</tr>
<tr>
    <td>
    Prof. Mohamed BOUTAYEB<br>
    Prof. Youssef GAHI<br>
    Prof. Ahmed DRISSI EL MALIANI<br>
    Dr. Samson LASAULCE

</td>
    <td>Round Table</td>
    <td>When Data Fails the Machine: Industrial AI under Constraints of Scarcity, Incompleteness, and Bias

</td>
    <td>15:00 - 16:00 </td>
    <td>Monday, July 6, 2026</td>
</tr>
<tr>
    <td>Dr. Mohamed IMAM</td>
    <td>Hands on Lab</td>
    <td>Deploying Real-Time Vision Systems for Mining Safety on Edge AI</td>
    <td>16:30 - 18:00 </td>
    <td>Monday, July 6, 2026</td>
</tr>
<tr>
    <td> Prof. Mohamed CHETOUANI</td>
    <td>Invited Talk</td>
    <td>When Robots Get It Wrong: Detecting Ambiguity and Failure Using Vision-Language Models
</td>
    <td>9:00 - 10:30</td>
    <td>Tuesday, July 7, 2026</td>
</tr>
<tr>
    <td>Prof. El Habib BEN LAHMAR</td>
    <td>Invited Talk</td>
    <td>Thinking Ahead: Joint-Embedding Predictive Architecture for Long-Range Coherence in Small Language Models
</td>
    <td>11:00 - 12:00   </td>
    <td>Tuesday, July 7, 2026</td>
</tr>
<tr>
    <td>Prof. Anass NOURI</td>
    <td>Invited Talk</td>
    <td>Analyse multimodale d’images médicales en contexte de faible disponibilité des données
</td>
    <td>12:00 - 13:00</td>
    <td>Tuesday, July 7, 2026</td>
</tr>
<tr>
    <td>Prof. Mohammed KHALIL</td>
    <td>Invited Talk</td>
    <td>The Seven Sophisms of AI
</td>
    <td>14:00 - 15:00</td>
    <td>Tuesday, July 7, 2026</td>
</tr>
<tr>
    <td>Prof. Boutaina HDIOUD</td>
    <td>Invited Talk</td>
    <td>Fondements des architectures Transformer : des LLMs à l’intelligence artificielle multimodale
</td>
    <td>15:00 - 16:00</td>
    <td>Tuesday, July 7, 2026</td>
</tr>
<tr>
    <td>Prof. Jihane GHARIB
</td>
    <td>Hands on Lab
</td>
    <td>Designing and Stress-Testing an AI-Assisted Prioritization System in Real-Time Contexts: Decision Matrix, Data Quality, Human Verification, and Accountability
</td>
    <td>16:30 - 18:00</td>
    <td>Tuesday, July 7, 2026</td>
</tr>
<tr>
    <td>Prof. Kamel SMAÏLI
</td>
    <td>Invited Talk</td>
    <td>From Judge to Mentor: How LLMs Can Guide Small Models to Detect Fake News
</td>
    <td>9:00 - 10:30</td>
    <td> Wednesday, July 08th, 2026
</td>
</tr>
<tr>
    <td>Prof. Mohamed BENDAHAN</td>
    <td>Invited Talk</td>
    <td>Vers une IA enracinée : les SHS à l'épreuve des datas </td>
    <td>11:00 - 12:00</td>
    <td> Wednesday, July 08th, 2026
</td>
</tr>
<tr>
    <td>Prof. Dounia LOTFI
</td>
    <td>Invited Talk</td>
    <td>Graph intelligence for complex networks analysis
</td>
    <td>12:00 - 13:00</td>
    <td> Wednesday, July 08th, 2026
</td>
</tr>
<tr>
    <td> Prof. Soufiane
AZOUAGHE <br> & Mekki EL
AMIRI</td>
    <td>Invited Talk </td>
    <td>Psychologie et intelligence artificielle : acceptabilité, expérience utilisateur et santé mentale</td>
    <td>14:00 - 15:00</td>
    <td> Wednesday, July 08th, 2026
</td>
</tr>
<tr>
    <td>Prof. Ibrahim RAHHAL
</td>
    <td>Invited Talk</td>
    <td>Aligning Education with the Digital Labor Market Using AI: From Labor Market Intelligence to Personalized Learning.
</td>
    <td>15:00 - 16:00</td>
    <td> Wednesday, July 08th, 2026
</td>
</tr>
<tr>
    <td>Dr. Ayoub FARKANE
</td>
    <td>Hands on Lab</td>
    <td>Hands-On Physics-Informed Neural Networks: From Theory to Real-World Applications in Healthcare and Energy
</td>
    <td>16:30 - 18:00</td>
    <td> Wednesday, July 08th, 2026
</td>
</tr>
<tr>
    <td>Prof. Luc DE BRABANDERE
</td>
    <td>Invited Talk</td>
    <td>The Art of Thinking in a Digital World
</td>
    <td>9:00 - 10:00</td>
    <td>Thursday, July 09th, 2026
</td>
</tr>
<tr>
    <td>Prof.  Ouassim KARRAKCHOU
</td>
    <td>Invited Talk</td>
    <td>Dynamic Neural Network Approaches for a Sustainable Edge AI
</td>
    <td>11:00 - 12:00</td>
    <td>Thursday, July 09th, 2026
</td>
</tr>
<tr>
    <td>Prof. Houda BENBRAHIM
</td>
    <td>Invited Talk</td>
    <td>Graphs Are Not Dead: How GNNs and LLMs Together Are Redefining Multilingual Sentiment

</td>
    <td>12:00 - 13:00</td>
    <td>Thursday, July 09th, 2026
</td>
</tr>
<tr>
    <td>Prof. Hakim HAFIDI
</td>
    <td>Invited Talk</td>
    <td>Less Data, More Geometry: 
Symmetry, Inductive Biases, and the Case for Frugal Deep Learning
</td>
    <td>14:00 - 15:00</td>
    <td>Thursday, July 09th, 2026
</td>
</tr>
<tr>
    <td>Prof. Aniss MOUMEN</td>
    <td>Hands on Lab
</td>
    <td>The Augmented Researcher: Transforming Scientific Inquiry through Generative AI, RAG Systems, and Open-Source LLMs

</td>
    <td>15:00 - 16:00</td>
    <td>Thursday, July 09th, 2026
</td>
</tr>
<tr>
    <td>Ms.Tiffany SOUTERRE <br> Mr. Olivier LEPLUS
</td>
    <td>Hands-on Lab: AWS
</td>
    <td>Build Your Own RPG Game Master Using Agentic AI and the Strands Agents SDK


</td>
    <td>16:30 - 18:30</td>
    <td>Thursday, July 09th, 2026
</td>
</tr>
<tr>
    <td> Mr. Mohammed ACHOUR

</td>
    <td>
    Invited Talk
</td>
    <td>

The Cisco AI Story: Scaling and Securing the Intelligent Era

</td>
    <td>9:00 - 10:30</td>
    <td>Friday, July 10th, 2026
</td>
</tr>
<tr>
    <td> Prof. Aissam BERRAHOU

</td>
    <td>
    Hands on Lab
</td>
    <td>

Edge AI for Computer Vision: Fundamentals, Hardware-Aware Optimization, and Experimental Validation on Resource-Constrained Systems

</td>
    <td>11:00 - 12:30</td>
    <td>Friday, July 10th, 2026
</td>
</tr>
<tr>
    <td>
    Dr. Karim BENZIDANE

</td>
    <td> Invited Talk
</td>
    <td>
Cracking the AWS Certification Code: A Trainer's Playbook for Exam Success


</td>
    <td>12:30 - 13:00</td>
    <td>Friday, July 10th, 2026
</td>
</tr>
</tbody>

</table>

</body>
</html>
"""



output_pdf = r"C:\Users\GASMI MANAL\Desktop\Summer_School_Tasks\HTML Program\programme_Intervenant.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(
        viewport={"width": 1920, "height": 1080}
    )

    page.set_content(html_content)
    page.wait_for_timeout(1000)

    # Génération PDF haute qualité
    page.pdf(
        path=output_pdf,
        format="A3",          # ou "A4" selon ton programme
        print_background=True,
        prefer_css_page_size=True,
        margin={
            "top": "10mm",
            "bottom": "10mm",
            "left": "10mm",
            "right": "10mm"
        }
    )

    browser.close()

print(f"PDF généré : {output_pdf}")