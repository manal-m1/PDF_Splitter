<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Programme Summer School</title>

<style>

@page {
    size: A4 landscape;
    margin: 1cm;
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family: Arial, Helvetica, sans-serif;
    background:#ffffff;
    color:#222;
    padding:20px;
    line-height:1.5;
}

/* ===== HEADER ===== */

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:4px solid #003366;
    padding-bottom:15px;
    margin-bottom:25px;
}

.logo{
    width:120px;
    height:auto;
}

.title{
    flex:1;
    text-align:center;
}

.title h1{
    color:#003366;
    font-size:2.2rem;
    margin-bottom:8px;
}

.title h2{
    color:#555;
    font-size:1.3rem;
    font-weight:normal;
}

/* ===== TABLE ===== */

.table-container{
    overflow-x:auto;
}

table{
    width:100%;
    border-collapse:collapse;
    background:white;
}

thead th{
    background:#003366;
    color:white;
    padding:16px;
    font-size:1.1rem;
    border:1px solid #ddd;
    text-align:center;
}

tbody td{
    padding:14px;
    border:1px solid #ddd;
    text-align:center;
    font-size:1.05rem;
}

tbody tr:nth-child(even){
    background:#f4f7fb;
}

tbody tr:hover{
    background:#e8f0ff;
}

/* ===== FOOTER ===== */

.footer{
    margin-top:25px;
    text-align:center;
    color:#666;
    font-size:1rem;
}

/* ===== MOBILE ===== */

@media screen and (max-width:768px){

    body{
        padding:10px;
    }

    .header{
        flex-direction:column;
        gap:10px;
    }

    .logo{
        width:90px;
    }

    .title h1{
        font-size:1.8rem;
    }

    .title h2{
        font-size:1.2rem;
    }

    table{
        min-width:900px;
    }

    thead th{
        font-size:1rem;
    }

    tbody td{
        font-size:1rem;
    }
}

/* ===== PRINT PDF ===== */

@media print{

    body{
        padding:0;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }

    .footer{
        position:fixed;
        bottom:0;
        width:100%;
    }

    tr{
        page-break-inside:avoid;
    }

    thead{
        display:table-header-group;
    }
}

</style>
</head>

<body>

<div class="header">

    <!-- Remplacer par votre logo -->
    <img src="logo_gauche.png" alt="Logo gauche" class="logo">

    <div class="title">
        <h1>SUMMER SCHOOL 2026</h1>
        <h2>Programme des Interventions</h2>
    </div>

    <!-- Remplacer par votre logo -->
    <img src="logo_droite.png" alt="Logo droite" class="logo">

</div>

<div class="table-container">

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
            <td>Introduction à l'Intelligence Artificielle</td>
            <td>09h00 – 10h30</td>
            <td>15/07/2026</td>
        </tr>

        <tr>
            <td>Dr. Sara El Idrissi</td>
            <td>Atelier</td>
            <td>Machine Learning : Cas Pratiques</td>
            <td>11h00 – 12h30</td>
            <td>15/07/2026</td>
        </tr>

        <tr>
            <td>Pr. Mohamed Alami</td>
            <td>Keynote</td>
            <td>IA et Transformation Numérique</td>
            <td>14h00 – 15h30</td>
            <td>15/07/2026</td>
        </tr>

        <tr>
            <td>Dr. Fatima Zahra</td>
            <td>Conférence</td>
            <td>Éthique et IA Responsable</td>
            <td>09h00 – 10h30</td>
            <td>16/07/2026</td>
        </tr>

        <tr>
            <td>Pr. Youssef El Mansouri</td>
            <td>Atelier</td>
            <td>Deep Learning et Vision par Ordinateur</td>
            <td>11h00 – 12h30</td>
            <td>16/07/2026</td>
        </tr>

        <!-- Ajouter d'autres lignes ici -->

    </tbody>

</table>

</div>

<div class="footer">
    Summer School 2026 • Programme Officiel
</div>

</body>
</html>

