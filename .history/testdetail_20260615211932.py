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
    background:#003366;
    color:white;
    border:1px solid #ccc;
    padding:12px;
    font-size:14px;
}

td{
    border:1px solid #ccc;
    padding:10px;
    text-align:center;
    font-size:13px;
}

tr:nth-child(even){
    background:#f5f7fa;
}
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --ink:       #1C1917;
  --ink-mid:   #44403C;
  --ink-soft:  #78716C;
  --line:      #E7E2DB;
  --page:      #FDFAF6;
  --white:     #FFFFFF;

  --d1: #2D5A8E;   --d1-bg: #EEF4FB;   --d1-border: #C5D9F0;
  --d2: #2A7A5C;   --d2-bg: #EBF7F2;   --d2-border: #B8E4D4;
  --d3: #9B3E1A;   --d3-bg: #FBF0EB;   --d3-border: #F4CCBA;
  --d4: #5B3580;   --d4-bg: #F3EEF9;   --d4-border: #D9C9EE;
  --d5: #1A6E7A;   --d5-bg: #EAF5F7;   --d5-border: #B5DDE3;

  --gold:      #B8860B;
  --gold-pale: #FBF5E6;

  --col-width: 200px;
  --time-width: 68px;
}

body {
  font-family: 'Outfit', sans-serif;
  background: var(--page);
  color: var(--ink);
  padding: 36px 44px;
  min-width: 1400px;
}

.header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  padding-bottom: 18px;
  margin-bottom: 28px;
  border-bottom: 2px solid var(--ink);
  position: relative;
}
.header::after {
  content: '';
  position: absolute;
  bottom: -5px; left: 0; right: 0;
  height: 1px;
  background: var(--gold);
  opacity: 0.5;
}
.conf-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 44px; font-weight: 700; line-height: 1;
  color: var(--ink); letter-spacing: -1px;
}

.date-sub { font-size: 12px; color: var(--ink-soft); text-align: right; font-weight: 300; margin-top: 4px; }
.conf-sub {
  font-size: 14px; /* 13 → 14 */
  color: var(--ink-soft);
  margin-top: 6px;
  font-weight: 300;
}

.big-dates {
  font-family: 'Cormorant Garamond', serif;
  font-size: 66px; /* 60 → 66 */
  font-weight: 700;
  color: var(--ink);
  line-height: 1;
  letter-spacing: -3px;
}

.sched-wrap {
  border: 1px solid var(--line);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 24px rgba(28,25,23,0.07);
}

table.sched {
  width: 100%;
  border-collapse: collapse;
}

table.sched th, table.sched td {
  border: 1px solid var(--line);
  padding: 8px 10px;
  vertical-align: middle;
  font-size: 11px;
  text-align: center;
}

.thead-day {
  background: var(--ink);
  color: #fff;
  font-family: 'Cormorant Garamond', serif;
  font-size: 14px;
  font-weight: 700;
  padding: 14px 10px;
}
.d1h { background: var(--d1); }
.d2h { background: var(--d2); }
.d2h-parallel { background: #5B21B6; }
.d3h { background: var(--d3); }
.d4h { background: var(--d4); }
.d5h { background: var(--d5); }

.venue-badge {
  display: inline-block; margin-top: 5px;
  font-size: 8px; font-weight: 700; letter-spacing: 2px;
  text-transform: uppercase; padding: 2px 7px;
  border-radius: 4px;
  background: rgba(255,255,255,0.18); color: rgba(255,255,255,0.95);
}

.time-cell {
  background: var(--white);
  font-size: 10px; font-weight: 600;
  color: var(--ink-soft);
  white-space: nowrap;
  width: 68px;
  min-width: 68px;
}

.tag {
  font-size: 11px; font-weight: 700; letter-spacing: 1px;
  text-transform: uppercase; margin-bottom: 3px; opacity: 0.75;
  display: block;
}
.speaker { font-size: 16px; font-weight: 600; color: var(--ink); line-height: 1.3; display: block; }
.affil { font-size: 14px; color: var(--ink-soft); font-weight: 300; margin-top: 2px; font-style: italic; display: block; }

.c-reg     { background: #F5F5F4; }
.c-coffee { background: #F8F7F5; font-size:10px; color: var(--ink-soft); }
.c-welcome{ background: #FEF2F2; border-left: 3px solid #C13030 !important; }
.c-lunch  { background: #F0FDF4; border-left: 3px solid #059669 !important; }
.c-sponsor{ background: var(--gold-pale); border-left: 3px solid var(--gold) !important; }
.c-d1     { background: var(--d1-bg); border-left: 3px solid var(--d1) !important; }
.c-d2     { background: var(--d2-bg); border-left: 3px solid var(--d2) !important; }
.c-d3     { background: var(--d3-bg); border-left: 3px solid var(--d3) !important; }
.c-d4     { background: var(--d4-bg); border-left: 3px solid var(--d4) !important; }
.c-d5     { background: var(--d5-bg); border-left: 3px solid var(--d5) !important; }
.c-handson {
    background: #FFFBEB;
    border-left: 3px solid #D97706 !important;
    font-size: 16px;
}
.c-aws    { background: #FFF7ED; border-left: 3px solid #EA580C !important; }
.c-parallel{ background: #F5F3FF; border-left: 3px solid #7C3AED !important; }
.c-roundtable{ background: #ECFEFF; border-left: 3px solid #0891B2 !important; }
.c-sport  { background: #F0FDFA; border-left: 3px solid #0D9488 !important; }
.c-closing{ background: #F5F3FF; border-left: 3px solid #7C3AED !important; }
.c-empty  { background: #FAFAF8; }

.footer {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 20px; padding-top: 14px; border-top: 1px solid var(--line);
  font-size: 10px; color: var(--ink-soft);
}
.footer strong { color: var(--ink-mid); font-weight: 600; }


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