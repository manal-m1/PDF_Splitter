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

</style>
</head>

<body>

<div class="header">

    <div>
        <img src="logo_gauche.png" class="logo">
    </div>

    <div class="title">
        <h1>SUMMER SCHOOL 2026</h1>
        <h2>Programme des Interventions</h2>
    </div>

    <div>
        <img src="logo_droite.png" class="logo">
    </div>

</div>

<table>

<thead>
<tr>
    <th>Nom de l'intervenant</th>
    <th>Type d'intervention</th>
    <th>Titre</th>
    <th>Créneau</th>
    <th>Date</th>
</tr>
</thead>

<tbody>

<tr>
    <td>Pr. Ahmed Benali</td>
    <td>Conférence</td>
    <td>Introduction à l'IA</td>
    <td>09h00 - 10h30</td>
    <td>15/07/2026</td>
</tr>

<tr>
    <td>Dr. Sara El Idrissi</td>
    <td>Atelier</td>
    <td>Machine Learning : Cas Pratiques</td>
    <td>11h00 - 12h30</td>
    <td>15/07/2026</td>
</tr>

<tr>
    <td>Pr. Mohamed Alami</td>
    <td>Keynote</td>
    <td>IA et Transformation Numérique</td>
    <td>14h00 - 15h30</td>
    <td>15/07/2026</td>
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