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
   <th>Speaker</th>
<th>Session Type</th>
<th style="width:180px;">Time Slot</th>
<th>Time Slot</th>
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
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
</tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
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