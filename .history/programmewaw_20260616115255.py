from playwright.sync_api import sync_playwright
import base64

with open(r"D:\Summer School\Codepythondecoupagepdfsenpdf\banniere.png", "rb") as f:
    banner = base64.b64encode(f.read()).decode("utf-8")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ISSAI Franco-Moroccan 2026 — Full Programme</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --ink:        #1C1917;
  --ink-mid:    #44403C;
  --ink-soft:   #78716C;
  --line:       #E7E2DB;
  --page:       #FDFAF6;
  --white:      #FFFFFF;

  --d1: #2D5A8E;   --d1-bg: #EEF4FB;   --d1-border: #C5D9F0;
  --d2: #2A7A5C;   --d2-bg: #EBF7F2;   --d2-border: #B8E4D4;
  --d3: #9B3E1A;   --d3-bg: #FBF0EB;   --d3-border: #F4CCBA;
  --d4: #5B3580;   --d4-bg: #F3EEF9;   --d4-border: #D9C9EE;
  --d5: #1A6E7A;   --d5-bg: #EAF5F7;   --d5-border: #B5DDE3;

  --gold:       #B8860B;
  --gold-pale:  #FBF5E6;

  --amber:      #D97706;
  --amber-bg:   #FFFBEB;
  --aws:        #EA580C;
  --aws-bg:     #FFF7ED;
  --violet:     #7C3AED;
  --violet-bg:  #F5F3FF;
  --teal:       #0891B2;
  --teal-bg:    #ECFEFF;
  --green:      #059669;
  --green-bg:   #F0FDF4;
  --red:        #C13030;
  --red-bg:     #FEF2F2;
}

body {
  font-family: 'Outfit', sans-serif;
  background: var(--page);
  color: var(--ink);
}

/* ══════════════════════════════
   SHARED HEADER
══════════════════════════════ */
.main-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  padding: 36px 44px 20px;
  border-bottom: 2px solid var(--ink);
  position: relative;
  background: var(--page);
}
.main-header::after {
  content: '';
  position: absolute;
  bottom: -5px; left: 0; right: 0;
  height: 1px;
  background: var(--gold);
  opacity: 0.5;
}
.conf-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 36px; font-weight: 700; line-height: 1.15;
  color: var(--ink); letter-spacing: -0.5px;
}
.conf-sub { font-size: 13px; color: var(--ink-soft); margin-top: 6px; font-weight: 300; }
.big-dates {
  font-family: 'Cormorant Garamond', serif;
  font-size: 64px; font-weight: 700; color: var(--ink);
  line-height: 1; letter-spacing: -3px; text-align: right;
}
.date-sub { font-size: 11px; color: var(--ink-soft); text-align: right; font-weight: 300; margin-top: 4px; }

/* ══════════════════════════════
   SECTION DIVIDERS
══════════════════════════════ */
.section-title {
  padding: 18px 44px 14px;
  background: var(--page);
}
.section-title h2 {
  font-family: 'Cormorant Garamond', serif;
  font-size: 28px; font-weight: 700;
  color: var(--ink-mid); letter-spacing: -0.5px;
}
.section-title p { font-size: 12px; color: var(--ink-soft); margin-top: 3px; }

.page-break { page-break-before: always; }

/* ══════════════════════════════
   PROGRAMME 1 — GRID VIEW
══════════════════════════════ */
.grid-wrap {
  padding: 0 44px 44px;
  background: var(--page);
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
  color: #fff;
  font-family: 'Cormorant Garamond', serif;
  font-size: 14px;
  font-weight: 700;
  padding: 14px 10px;
}
.d1h { background: var(--d1); }
.d2h { background: var(--d2); }
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
  width: 68px; min-width: 68px;
}
.tag { font-size: 10px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 3px; opacity: 0.75; display: block; }
.speaker { font-size: 13px; font-weight: 600; color: var(--ink); line-height: 1.3; display: block; }
.affil { font-size: 11px; color: var(--ink-soft); font-weight: 300; margin-top: 2px; font-style: italic; display: block; }

.c-reg     { background: #F5F5F4; }
.c-coffee  { background: #F8F7F5; font-size:10px; color: var(--ink-soft); }
.c-welcome { background: var(--red-bg);    border-left: 3px solid var(--red) !important; }
.c-lunch   { background: var(--green-bg);  border-left: 3px solid var(--green) !important; }
.c-sponsor { background: var(--gold-pale); border-left: 3px solid var(--gold) !important; }
.c-d1      { background: var(--d1-bg);     border-left: 3px solid var(--d1) !important; }
.c-d2      { background: var(--d2-bg);     border-left: 3px solid var(--d2) !important; }
.c-d3      { background: var(--d3-bg);     border-left: 3px solid var(--d3) !important; }
.c-d4      { background: var(--d4-bg);     border-left: 3px solid var(--d4) !important; }
.c-d5      { background: var(--d5-bg);     border-left: 3px solid var(--d5) !important; }
.c-handson { background: var(--amber-bg);  border-left: 3px solid var(--amber) !important; }
.c-aws     { background: var(--aws-bg);    border-left: 3px solid var(--aws) !important; }
.c-parallel{ background: var(--violet-bg); border-left: 3px solid var(--violet) !important; }
.c-roundtable{ background: var(--teal-bg); border-left: 3px solid var(--teal) !important; }
.c-sport   { background: #F0FDFA;          border-left: 3px solid #0D9488 !important; }
.c-closing { background: var(--violet-bg); border-left: 3px solid var(--violet) !important; }
.c-empty   { background: #FAFAF8; }

/* ══════════════════════════════
   PROGRAMME 2 — DETAILED TABLE
══════════════════════════════ */
.detail-wrap {
  padding: 0 44px 44px;
  background: var(--page);
}
table.detail {
  width: 100%;
  border-collapse: collapse;
  background: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 24px rgba(28,25,23,0.07);
}
table.detail th {
  background: #FFFFFF;
  color: var(--ink);
  padding: 12px 14px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  border: 1px solid var(--line);
  text-align: left;
}
table.detail td {
  border: 1px solid var(--line);
  padding: 10px 14px;
  font-size: 12px;
  color: var(--ink);
  vertical-align: middle;
}

/* Day header rows */
.day-row td {
  background: var(--ink-mid);
  color: #fff;
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  font-weight: 700;
  padding: 10px 14px;
  letter-spacing: 0.2px;
}
/* Break rows */
.break-row td {
  background: #F8F7F5;
  color: var(--ink-soft);
  font-size: 11px;
  font-style: italic;
  text-align: center;
  padding: 7px 14px;
  border: 1px solid var(--line);
}
/* Session type badge */
.badge {
  display: inline-block;
  font-size: 9px; font-weight: 700;
  letter-spacing: 1.2px; text-transform: uppercase;
  padding: 2px 8px; border-radius: 20px;
  white-space: nowrap;
}
.badge-talk     { background: var(--d1-bg); color: var(--d1); border: 1px solid var(--d1-border); }
.badge-handson  { background: var(--amber-bg); color: var(--amber); border: 1px solid #FDE68A; }
.badge-aws      { background: var(--aws-bg); color: var(--aws); border: 1px solid #FDBA74; }
.badge-round    { background: var(--teal-bg); color: var(--teal); border: 1px solid #A5F3FC; }
.badge-parallel { background: var(--violet-bg); color: var(--violet); border: 1px solid #DDD6FE; }
.badge-opening  { background: var(--red-bg); color: var(--red); border: 1px solid #FECACA; }
.badge-closing  { background: var(--violet-bg); color: var(--violet); border: 1px solid #DDD6FE; }
.badge-poster   { background: var(--gold-pale); color: var(--gold); border: 1px solid #FDE68A; }

.speaker-name { font-weight: 600; font-size: 13px; color: var(--ink); display: block; }
.speaker-affil { font-size: 11px; color: var(--ink-soft); font-style: italic; margin-top: 1px; display: block; }

.time-slot { font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 12px; color: var(--ink-mid); white-space: nowrap; }

.title-cell { font-size: 12px; color: var(--ink); line-height: 1.5; }
.title-cell em { color: var(--ink-soft); font-size: 11px; }

/* alternate rows */
table.detail tbody tr:not(.day-row):not(.break-row):nth-child(odd) td { background: var(--page); }
table.detail tbody tr:not(.day-row):not(.break-row):nth-child(even) td { background: var(--white); }

/* footer */
.footer {
  display: flex; justify-content: space-between; align-items: center;
  padding: 14px 44px 30px;
  font-size: 10px; color: var(--ink-soft);
  border-top: 1px solid var(--line);
}
.footer strong { color: var(--ink-mid); font-weight: 600; }

/* Legend */
.legend {
  display: flex; flex-wrap: wrap; gap: 10px;
  padding: 14px 44px;
}
.legend-item {
  display: flex; align-items: center; gap: 6px;
  font-size: 10px; color: var(--ink-mid);
}
.legend-dot {
  width: 10px; height: 10px; border-radius: 50%;
  flex-shrink: 0;
}

.banner {
  width: 100%;
  height: auto;
  display: block;
}

.banner-container {
  width: 100%;
  overflow: hidden;
}

.day-row td {
  background: transparent;
  color: var(--ink);
}
</style>
</head>
<body>


<!-- ═══════════════════════════════════════════════
     SHARED HEADER
═══════════════════════════════════════════════ -->
<div class="main-header">
  <div>
    <div class="conf-title">
      International Summer School on Artificial Intelligence<br>
      of the Franco-Moroccan Research Center 2026
    </div>
    <div class="conf-sub">Rabat, Morocco &nbsp;·&nbsp; ENSIAS &nbsp;·&nbsp; UIR &nbsp;·&nbsp; FLSHR</div>
  </div>
  <div>
    <div class="big-dates">6–10</div>
    <div class="date-sub">July 2026 &nbsp;·&nbsp; Rabat</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 1 — OVERVIEW GRID
═══════════════════════════════════════════════ -->
<div class="section-title" style="padding-top:24px;">
  <h2>Overview Programme</h2>
  <p>At-a-glance weekly schedule across all venues</p>
</div>

<div class="legend">
  <div class="legend-item"><div class="legend-dot" style="background:var(--d1);"></div>Invited Talk (Mon)</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--d2);"></div>Invited Talk (Tue)</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--d3);"></div>Invited Talk (Wed)</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--d4);"></div>Invited Talk (Thu)</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--d5);"></div>Invited Talk (Fri)</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--amber);"></div>Hands-on Lab</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--aws);"></div>AWS Session</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--teal);"></div>Round Table</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--violet);"></div>Parallel / Closing</div>
  <div class="legend-item"><div class="legend-dot" style="background:var(--gold);"></div>To Be Confirmed</div>
</div>

<div class="grid-wrap">
<div class="sched-wrap">
<table class="sched">
  <colgroup>
    <col style="width:68px">
    <col style="width:16.66%">
    <col style="width:16.66%">
    <col style="width:16.66%">
    <col style="width:16.66%">
    <col style="width:16.66%">
  </colgroup>
  <thead>
    <tr>
      <th style="background:none;"></th>
      <th class="thead-day d1h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:20px;opacity:.4;">01</div>
        <div style="font-size:18px;font-weight:600;">Monday 6 July 2026</div>
        <div style="font-size:13px;opacity:.6;font-weight:300;">1st day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
      <th class="thead-day d2h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:20px;opacity:.4;">02</div>
        <div style="font-size:18px;font-weight:600;">Tuesday 7 July 2026</div>
        <div style="font-size:13px;opacity:.6;font-weight:300;">2nd day</div>
        <div class="venue-badge">UIR</div>
      </th>
      <th class="thead-day d3h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:20px;opacity:.4;">03</div>
        <div style="font-size:18px;font-weight:600;">Wednesday 8 July 2026</div>
        <div style="font-size:13px;opacity:.6;font-weight:300;">3rd day</div>
        <div class="venue-badge">FLSHR</div>
      </th>
      <th class="thead-day d4h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:20px;opacity:.4;">04</div>
        <div style="font-size:18px;font-weight:600;">Thursday 9 July 2026</div>
        <div style="font-size:13px;opacity:.6;font-weight:300;">4th day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
      <th class="thead-day d5h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:20px;opacity:.4;">05</div>
        <div style="font-size:18px;font-weight:600;">Friday 10 July 2026</div>
        <div style="font-size:13px;opacity:.6;font-weight:300;">Last day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
    </tr>
  </thead>
  <tbody>

    <tr>
      <td class="time-cell">08:30<br>09:00</td>
      <td class="c-reg">
        <span class="tag">Welcome</span>
        <span class="speaker">🎟 Participant Registration</span>
      </td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
    </tr>

    <tr>
      <td class="time-cell"></td>
      <td class="c-coffee" colspan="5" style="text-align:center;">☕ Coffee Break</td>
    </tr>

    <tr>
      <td class="time-cell">09:00<br>10:30</td>
      <td class="c-welcome">
        <span class="tag" style="color:var(--red);">Opening Ceremony</span>
        <span class="affil">Opening Session and Official Speeches<br>Partners' Words</span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 9H00–10H30</span>
        <span class="speaker">Prof. Mohamed CHETOUANI</span>
        <span class="affil">Sorbonne Université (SU), France</span>
      </td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk · 9H00–10H30</span>
        <span class="speaker">Prof. Kamel SMAILI</span>
        <span class="affil">Université de Lorraine (UL), France</span>
      </td>
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 9H00–10H00</span>
        <span class="speaker">Prof. Luc De Brabandere</span>
      </td>
      <td class="c-d5">
        <span class="tag" style="color:var(--d5);">Invited Talk · 9H00–10H30</span>
        <span class="speaker">Mr. Mohammed ACHOUR</span>
        <span class="affil">Cisco, Morocco</span>
      </td>
    </tr>

    <tr>
      <td class="time-cell">10:30<br>11:00</td>
      <td class="c-coffee" colspan="5" style="text-align:center;">
        <span class="tag">☕ Coffee Break &amp; Participant Poster Presentations</span>
      </td>
    </tr>

    <tr>
      <td class="time-cell">11:00<br>12:00</td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">Session to be Confirmed</span>
        <span class="affil">11H00 – 12:00</span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. El Habib BEN LAHMER</span>
        <span class="affil">UHII, Morocco</span>
      </td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. Mohamed BENDAHAN</span>
        <span class="affil">FLSH / UM5R, Morocco</span>
      </td>
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. Ouassim KARRAKCHOU</span>
        <span class="affil">UIR, Morocco</span>
      </td>
      <td class="c-handson">
        <span class="tag" style="color:var(--amber);">Hands-on · 11H00–12H30</span>
        <span class="speaker">Prof. Aissam BERRAHOU</span>
        <span class="affil">ENSIAS / UM5R, Morocco</span>
      </td>
    </tr>

    <tr>
      <td class="time-cell">12:00<br>13:00</td>
      <td class="c-d1">
        <span class="tag" style="color:var(--d1);">Invited Talk · 12H00–13H00</span>
        <span class="speaker">Prof. Fabrice KORDON</span>
        <span class="affil">Sorbonne Université (SU), France</span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 12H00–13H00</span>
        <span class="speaker">Prof. Anass NOURI</span>
        <span class="affil">FSK, UIT, Morocco</span>
      </td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk · 12H00–13H00</span>
        <span class="speaker">Prof. Dounia LOTFI</span>
        <span class="affil">FSR / UM5R, Morocco</span>
      </td>
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 12H00–13H00</span>
        <span class="speaker">Prof. Houda BENBRAHIM</span>
        <span class="affil">ENSIAS / UM5R, Morocco</span>
      </td>
      <td class="c-aws">
        <span class="tag" style="color:var(--aws);">AWS Certifications · 12H30–13H00</span>
        <span class="speaker">Dr. Karim BENZIDANE</span>
        <span class="affil">AWS, France</span>
      </td>
    </tr>

    <tr>
      <td class="time-cell">13:00<br>14:00</td>
      <td class="c-lunch" colspan="4" style="text-align:center;">
        <span class="tag" style="color:var(--green);">🍽 Lunch Break &nbsp;·&nbsp; 13H00 – 14H00</span>
      </td>
      <td class="c-closing">
        <span class="tag" style="color:var(--violet);">Closing Session · 13:00–13:30</span>
        <span class="speaker" style="font-size:11px;">Participant Feedback &amp; Closing Session</span>
      </td>
    </tr>

    <tr>
      <td class="time-cell">13:30<br>15:00</td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-sponsor">
        <span class="speaker">Lunch</span>
        <span class="affil">13H30 – 15H00</span>
      </td>
    </tr>

    <tr>
      <td class="time-cell">14:00<br>15:00</td>
      <td class="c-d1">
        <span class="tag" style="color:var(--d1);">Invited Talk · 14H00–15H00</span>
        <span class="speaker">Prof. Mohamed ESSAAIDI</span>
        <span class="affil">IEEE | ENSIAS / UM5R, Morocco</span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 14H00–15H00</span>
        <span class="speaker">Prof. Mohammed KHALIL</span>
        <span class="affil">FSTM, UH2C, Morocco</span>
        <div style="margin-top:8px;padding-top:6px;border-top:1px solid #D8B4FE;">
          <span style="color:var(--violet);font-size:11px;font-weight:700;">Parallel Session — My Thesis in 180s</span>
        </div>
      </td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk &amp; Demo · 14H00–15H00</span>
        <span class="speaker">Prof. Soufiane AZOUAGHE &amp; Mekki EL AMIRI</span>
        <span class="affil">FLSH / UM5R, Morocco</span>
      </td>
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 14H00–15H00</span>
        <span class="speaker">Prof. Hakim HAFIDI</span>
        <span class="affil">UIR, Morocco</span>
      </td>
      <td class="c-empty"></td>
    </tr>

    <tr>
      <td class="time-cell">15:00<br>16:00</td>
      <td class="c-roundtable">
        <span class="tag" style="color:var(--teal);">Round Table · 15H00–16H00</span>
        <span class="speaker">Prof. Y. GAHI</span>
        <span class="affil">ENSAK / UIT, Morocco</span>
        <span class="speaker">Prof. M. BOUTAYEB</span>
        <span class="affil">University of Lorraine, France</span>
        <span class="speaker">Prof. A. DRISSI EL MALIANI</span>
        <span class="affil">FSR / UM5R, Morocco</span>
        <span class="speaker">Dr. Samson LASAULCE</span>
        <span class="affil">CRAN, France</span>
        <span class="speaker">Prof. Gilles SIMON</span>
        <span class="affil">University of Lorraine, France</span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 15H00–16H00</span>
        <span class="speaker">Prof. Boutaina HDIOUD</span>
        <span class="affil">ENSIAS / UM5R, Morocco</span>
        <div style="margin-top:8px;padding-top:6px;border-top:1px solid #D8B4FE;">
          <span style="color:var(--violet);font-size:11px;font-weight:700;">Parallel Session — My Thesis in 180s</span>
        </div>
      </td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk · 15H00–16H00</span>
        <span class="speaker">Prof. Ibrahim RAHHAL</span>
        <span class="affil">UIR, Morocco</span>
      </td>
      <td class="c-handson">
        <span class="tag" style="color:var(--amber);">Hands-on · 15H00–16H00</span>
        <span class="speaker">Prof. Aniss MOUMEN</span>
        <span class="affil">ENSAK / UIT, Morocco</span>
      </td>
      <td class="c-sport" rowspan="3" style="vertical-align:middle;text-align:center;">
        <span class="tag" style="color:#0D9488;">To Be Confirmed · 15H00–18H30</span>
      </td>
    </tr>

    <tr>
      <td class="time-cell">16:00<br>16:30</td>
      <td class="c-coffee" colspan="4" style="text-align:center;">
        <span class="tag">☕ Coffee Break &amp; Participant Poster Presentations</span>
      </td>
    </tr>

    <tr style="height:110px;">
      <td class="time-cell">16:30<br>18:00</td>
      <td class="c-handson">
        <span class="tag" style="color:var(--amber);">Hands-on · 16H30–18H00</span>
        <span class="speaker">Dr. Mohamed IMAM</span>
        <span class="affil">University of Waterloo &amp; LoopX Canada · ENSIAS, UM5R, Morocco</span>
      </td>
      <td class="c-handson">
        <span class="tag" style="color:var(--amber);">Hands-on · 16H30–18H00</span>
        <span class="speaker">Prof. Jihane GHARIB</span>
        <span class="affil">ENSAK / UIT, Morocco</span>
        <div style="margin-top:8px;padding-top:6px;border-top:1px solid #D8B4FE;">
          <span style="color:var(--violet);font-size:11px;font-weight:700;">Parallel Session — My Thesis in 180s</span>
        </div>
      </td>
      <td class="c-handson" style="vertical-align:middle;text-align:center;">
        <span class="tag" style="color:var(--amber);">Hands-on · 16H30–18H00</span>
        <span class="speaker">Dr. Ayoub FARKANE</span>
        <span class="affil">Université de Lorraine, France · UIR, Morocco</span>
      </td>
      <td class="c-aws" style="vertical-align:middle;text-align:center;">
        <span class="tag" style="color:var(--aws);">Invited Talk &amp; Hands-on AWS · 16:30–18:30</span>
        <span class="speaker">Ms. Tiffany SOUTERRE<br>Mr. Olivier LEPLUS</span>
        <span class="affil">AWS, France</span>
      </td>
    </tr>

    <tr style="height:32px;">
      <td class="time-cell">18:30</td>
      <td class="c-empty" style="font-size:10px;color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:10px;color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:10px;color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:10px;color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:10px;color:var(--ink-soft);">End of day</td>
    </tr>

  </tbody>
</table>
</div>
</div>


<!-- ═══════════════════════════════════════════════
     PAGE BREAK
═══════════════════════════════════════════════ -->
<div class="page-break"></div>

<!-- HEADER repeat on page 2 -->
<div class="main-header">
  <div>
    <div class="conf-title">
      International Summer School on Artificial Intelligence<br>
      of the Franco-Moroccan Research Center 2026
    </div>
    <div class="conf-sub">Rabat, Morocco &nbsp;·&nbsp; ENSIAS &nbsp;·&nbsp; UIR &nbsp;·&nbsp; FLSHR</div>
  </div>
  <div>
    <div class="big-dates">6–10</div>
    <div class="date-sub">July 2026 &nbsp;·&nbsp; Rabat</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     SECTION 2 — DETAILED PROGRAMME
═══════════════════════════════════════════════ -->
<div class="section-title" style="padding-top:24px;">
  <h2>Detailed Programme</h2>
  <p>Full session details — speakers, affiliations, titles, and time slots</p>
</div>

<div class="detail-wrap">
<table class="detail">
  <thead>
    <tr>
      <th style="width:90px;">Date</th>
      <th style="width:100px;">Time Slot</th>
      <th style="width:200px;">Speaker &amp; Affiliation</th>
      <th style="width:110px;">Session Type</th>
      <th>Session Title</th>
    </tr>
  </thead>
  <tbody>

    <!-- ── MONDAY 6 JULY ── -->
    <tr class="day-row">
      <td colspan="5">📅 &nbsp;Monday, 6 July 2026 &nbsp;·&nbsp; ENSIAS</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Mon 6 Jul</td>
      <td class="time-slot">08:30 – 09:00</td>
      <td>
        <span class="speaker-name">—</span>
        <span class="speaker-affil">All participants</span>
      </td>
      <td><span class="badge badge-opening">🎟 Registration</span></td>
      <td class="title-cell">Participant Registration &amp; Welcome</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Mon 6 Jul</td>
      <td class="time-slot">09:00 – 10:30</td>
      <td>
        <span class="speaker-name">—</span>
        <span class="speaker-affil">Organising Committee</span>
      </td>
      <td><span class="badge badge-opening">Opening</span></td>
      <td class="title-cell">Opening Ceremony — Official Speeches &amp; Partners' Words</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 10:30 – 11:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Mon 6 Jul</td>
      <td class="time-slot">11:00 – 12:00</td>
      <td>
        <span class="speaker-name">—</span>
        <span class="speaker-affil">TBC</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell"><em>Session to be confirmed</em></td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Mon 6 Jul</td>
      <td class="time-slot">12:00 – 13:00</td>
      <td>
        <span class="speaker-name">Prof. Fabrice KORDON</span>
        <span class="speaker-affil">Sorbonne Université (SU), France</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Cybersecurity, the massive surge of AI</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🍽 Lunch Break &nbsp;·&nbsp; 13:00 – 14:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Mon 6 Jul</td>
      <td class="time-slot">14:00 – 15:00</td>
      <td>
        <span class="speaker-name">Prof. Mohamed ESSAAIDI</span>
        <span class="speaker-affil">IEEE | ENSIAS / UM5R, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Leveraging AI for the acceleration of the 2030 UN Agenda for Sustainable Development</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Mon 6 Jul</td>
      <td class="time-slot">15:00 – 16:00</td>
      <td>
        <span class="speaker-name">Prof. Y. GAHI &amp; Prof. M. BOUTAYEB<br>Prof. A. DRISSI EL MALIANI &amp; Dr. S. LASAULCE; Prof. G. SIMON</span>
        <span class="speaker-affil">ENSAK/UIT Morocco · Univ. de Lorraine, France · FSR/UM5R Morocco · CRAN, France · Univ. de Lorraine</span>
      </td>
      <td><span class="badge badge-round">Round Table</span></td>
      <td class="title-cell">When Data Fails the Machine: Industrial AI under Constraints of Scarcity, Incompleteness, and Bias</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 16:00 – 16:30</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Mon 6 Jul</td>
      <td class="time-slot">16:30 – 18:00</td>
      <td>
        <span class="speaker-name">Dr. Mohamed IMAM</span>
        <span class="speaker-affil">University of Waterloo &amp; LoopX Canada · ENSIAS, UM5R, Morocco</span>
      </td>
      <td><span class="badge badge-handson">Hands-on Lab</span></td>
      <td class="title-cell">Deploying Real-Time Vision Systems for Mining Safety on Edge AI</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🔚 End of Day &nbsp;·&nbsp; 18:30</td>
    </tr>

    <!-- ── TUESDAY 7 JULY ── -->
    <tr class="day-row">
      <td colspan="5">📅 &nbsp;Tuesday, 7 July 2026 &nbsp;·&nbsp; UIR</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Tue 7 Jul</td>
      <td class="time-slot">09:00 – 10:30</td>
      <td>
        <span class="speaker-name">Prof. Mohamed CHETOUANI</span>
        <span class="speaker-affil">Sorbonne Université (SU), France</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">When Robots Get It Wrong: Detecting Ambiguity and Failure Using Vision-Language Models</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 10:30 – 11:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Tue 7 Jul</td>
      <td class="time-slot">11:00 – 12:00</td>
      <td>
        <span class="speaker-name">Prof. El Habib BEN LAHMER</span>
        <span class="speaker-affil">UHII, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Thinking Ahead: Joint-Embedding Predictive Architecture for Long-Range Coherence in Small Language Models</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Tue 7 Jul</td>
      <td class="time-slot">12:00 – 13:00</td>
      <td>
        <span class="speaker-name">Prof. Anass NOURI</span>
        <span class="speaker-affil">FSK, UIT, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Analyse multimodale d'images médicales en contexte de faible disponibilité des données</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🍽 Lunch Break &nbsp;·&nbsp; 13:00 – 14:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Tue 7 Jul</td>
      <td class="time-slot">14:00 – 15:00</td>
      <td>
        <span class="speaker-name">Prof. Mohammed KHALIL</span>
        <span class="speaker-affil">FSTM, UH2C, Morocco</span>
      </td>
      <td>
        <span class="badge badge-talk">Invited Talk</span><br>
        <span class="badge badge-parallel" style="margin-top:4px;">Parallel — My Thesis 180s</span>
      </td>
      <td class="title-cell">The Seven Sophisms of AI</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Tue 7 Jul</td>
      <td class="time-slot">15:00 – 16:00</td>
      <td>
        <span class="speaker-name">Prof. Boutaina HDIOUD</span>
        <span class="speaker-affil">ENSIAS / UM5R, Morocco</span>
      </td>
      <td>
        <span class="badge badge-talk">Invited Talk</span><br>
        <span class="badge badge-parallel" style="margin-top:4px;">Parallel — My Thesis 180s</span>
      </td>
      <td class="title-cell">Fondements des architectures Transformer : des LLMs à l'intelligence artificielle multimodale</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 16:00 – 16:30</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Tue 7 Jul</td>
      <td class="time-slot">16:30 – 18:00</td>
      <td>
        <span class="speaker-name">Prof. Jihane GHARIB</span>
        <span class="speaker-affil">ENSAK / UIT, Morocco</span>
      </td>
      <td>
        <span class="badge badge-handson">Hands-on Lab</span><br>
        <span class="badge badge-parallel" style="margin-top:4px;">Parallel — My Thesis 180s</span>
      </td>
      <td class="title-cell">Designing and Stress-Testing an AI-Assisted Prioritization System in Real-Time Contexts: Decision Matrix, Data Quality, Human Verification, and Accountability</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🔚 End of Day &nbsp;·&nbsp; 18:30</td>
    </tr>

    <!-- ── WEDNESDAY 8 JULY ── -->
    <tr class="day-row">
      <td colspan="5">📅 &nbsp;Wednesday, 8 July 2026 &nbsp;·&nbsp; FLSHR</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Wed 8 Jul</td>
      <td class="time-slot">09:00 – 10:30</td>
      <td>
        <span class="speaker-name">Prof. Kamel SMAÏLI</span>
        <span class="speaker-affil">Université de Lorraine (UL), France</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">From Judge to Mentor: How LLMs Can Guide Small Models to Detect Fake News</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 10:30 – 11:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Wed 8 Jul</td>
      <td class="time-slot">11:00 – 12:00</td>
      <td>
        <span class="speaker-name">Prof. Mohamed BENDAHAN</span>
        <span class="speaker-affil">FLSH / UM5R, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Vers une IA enracinée : les SHS à l'épreuve des datas</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Wed 8 Jul</td>
      <td class="time-slot">12:00 – 13:00</td>
      <td>
        <span class="speaker-name">Prof. Dounia LOTFI</span>
        <span class="speaker-affil">FSR / UM5R, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Graph intelligence for complex networks analysis</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🍽 Lunch Break &nbsp;·&nbsp; 13:00 – 14:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Wed 8 Jul</td>
      <td class="time-slot">14:00 – 15:00</td>
      <td>
        <span class="speaker-name">Prof. Soufiane AZOUAGHE &amp; Mekki EL AMIRI</span>
        <span class="speaker-affil">FLSH / UM5R, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk &amp; Demo</span></td>
      <td class="title-cell">Psychologie et intelligence artificielle : acceptabilité, expérience utilisateur et santé mentale</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Wed 8 Jul</td>
      <td class="time-slot">15:00 – 16:00</td>
      <td>
        <span class="speaker-name">Prof. Ibrahim RAHHAL</span>
        <span class="speaker-affil">UIR, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Aligning Education with the Digital Labor Market Using AI: From Labor Market Intelligence to Personalized Learning</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 16:00 – 16:30</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Wed 8 Jul</td>
      <td class="time-slot">16:30 – 18:00</td>
      <td>
        <span class="speaker-name">Dr. Ayoub FARKANE</span>
        <span class="speaker-affil">Université de Lorraine, France · UIR, Morocco</span>
      </td>
      <td><span class="badge badge-handson">Hands-on Lab</span></td>
      <td class="title-cell">Hands-On Physics-Informed Neural Networks: From Theory to Real-World Applications in Healthcare and Energy</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🔚 End of Day &nbsp;·&nbsp; 18:30</td>
    </tr>

    <!-- ── THURSDAY 9 JULY ── -->
    <tr class="day-row">
      <td colspan="5">📅 &nbsp;Thursday, 9 July 2026 &nbsp;·&nbsp; ENSIAS</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Thu 9 Jul</td>
      <td class="time-slot">09:00 – 10:00</td>
      <td>
        <span class="speaker-name">Prof. Luc DE BRABANDERE</span>
        <span class="speaker-affil"></span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">The Art of Thinking in a Digital World</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 10:30 – 11:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Thu 9 Jul</td>
      <td class="time-slot">11:00 – 12:00</td>
      <td>
        <span class="speaker-name">Prof. Ouassim KARRAKCHOU</span>
        <span class="speaker-affil">UIR, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Dynamic Neural Network Approaches for a Sustainable Edge AI</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Thu 9 Jul</td>
      <td class="time-slot">12:00 – 13:00</td>
      <td>
        <span class="speaker-name">Prof. Houda BENBRAHIM</span>
        <span class="speaker-affil">ENSIAS / UM5R, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Graphs Are Not Dead: How GNNs and LLMs Together Are Redefining Multilingual Sentiment</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🍽 Lunch Break &nbsp;·&nbsp; 13:00 – 14:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Thu 9 Jul</td>
      <td class="time-slot">14:00 – 15:00</td>
      <td>
        <span class="speaker-name">Prof. Hakim HAFIDI</span>
        <span class="speaker-affil">UIR, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">Less Data, More Geometry: Symmetry, Inductive Biases, and the Case for Frugal Deep Learning</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Thu 9 Jul</td>
      <td class="time-slot">15:00 – 16:00</td>
      <td>
        <span class="speaker-name">Prof. Aniss MOUMEN</span>
        <span class="speaker-affil">ENSAK / UIT, Morocco</span>
      </td>
      <td><span class="badge badge-handson">Hands-on Lab</span></td>
      <td class="title-cell">The Augmented Researcher: Transforming Scientific Inquiry through Generative AI, RAG Systems, and Open-Source LLMs</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 16:00 – 16:30</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Thu 9 Jul</td>
      <td class="time-slot">16:30 – 18:30</td>
      <td>
        <span class="speaker-name">Ms. Tiffany SOUTERRE &amp; Mr. Olivier LEPLUS</span>
        <span class="speaker-affil">AWS, France</span>
      </td>
      <td><span class="badge badge-aws">AWS Hands-on</span></td>
      <td class="title-cell">Build Your Own RPG Game Master Using Agentic AI and the Strands Agents SDK</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🔚 End of Day &nbsp;·&nbsp; 18:30</td>
    </tr>

    <!-- ── FRIDAY 10 JULY ── -->
    <tr class="day-row">
      <td colspan="5">📅 &nbsp;Friday, 10 July 2026 &nbsp;·&nbsp; ENSIAS</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Fri 10 Jul</td>
      <td class="time-slot">09:00 – 10:30</td>
      <td>
        <span class="speaker-name">Mr. Mohammed ACHOUR</span>
        <span class="speaker-affil">Cisco, Morocco</span>
      </td>
      <td><span class="badge badge-talk">Invited Talk</span></td>
      <td class="title-cell">The Cisco AI Story: Scaling and Securing the Intelligent Era</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">☕ Coffee Break &amp; Participant Poster Presentations &nbsp;·&nbsp; 10:30 – 11:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Fri 10 Jul</td>
      <td class="time-slot">11:00 – 12:30</td>
      <td>
        <span class="speaker-name">Prof. Aissam BERRAHOU</span>
        <span class="speaker-affil">ENSIAS / UM5R, Morocco</span>
      </td>
      <td><span class="badge badge-handson">Hands-on Lab</span></td>
      <td class="title-cell">Edge AI for Computer Vision: Fundamentals, Hardware-Aware Optimization, and Experimental Validation on Resource-Constrained Systems</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Fri 10 Jul</td>
      <td class="time-slot">12:30 – 13:00</td>
      <td>
        <span class="speaker-name">Dr. Karim BENZIDANE</span>
        <span class="speaker-affil">AWS, France</span>
      </td>
      <td><span class="badge badge-aws">AWS Session</span></td>
      <td class="title-cell">Cracking the AWS Certification Code: A Trainer's Playbook for Exam Success</td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🍽 Lunch &nbsp;·&nbsp; 13:00 – 13:30 (Closing) → 13:30 – 15:00</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Fri 10 Jul</td>
      <td class="time-slot">13:00 – 13:30</td>
      <td>
        <span class="speaker-name">—</span>
        <span class="speaker-affil">All participants</span>
      </td>
      <td><span class="badge badge-closing">Closing Session</span></td>
      <td class="title-cell">Participant Feedback &amp; Closing Session</td>
    </tr>

    <tr>
      <td style="font-size:11px;color:var(--ink-soft);">Fri 10 Jul</td>
      <td class="time-slot">15:00 – 18:30</td>
      <td>
        <span class="speaker-name">—</span>
        <span class="speaker-affil">All participants</span>
      </td>
      <td><span class="badge badge-poster">TBC</span></td>
      <td class="title-cell"><em>To Be Confirmed</em></td>
    </tr>

    <tr class="break-row">
      <td colspan="5">🔚 End of Summer School &nbsp;·&nbsp; 18:30</td>
    </tr>

  </tbody>
</table>
</div>

<div class="footer">
  <div><strong>ENSIAS &nbsp;·&nbsp; UIR &nbsp;·&nbsp; FLSHR</strong> — Rabat, Morocco</div>
  <div>International Summer School on AI — Franco-Moroccan Research Center 2026</div>
  <div>6 – 10 July 2026</div>
</div>

</body>
</html>"""

output_pdf = r"C:\Users\GASMI MANAL\Desktop\Summer_School_Tasks\HTML Program\programme_Intervenant.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.set_content(html_content, wait_until="networkidle")
    page.wait_for_timeout(2000)
    page.pdf(
    path=output_pdf,
    format="A3",
    landscape=True,
    print_background=True,
    prefer_css_page_size=False,

    display_header_footer=True,

    header_template=f"""
    <div style="width:100%;">
        <img src="data:image/png;base64,{banner}"
             style="width:100%; height:auto;">
    </div>
    """,

    footer_template="""
    <div></div>
    """,

    margin={
        "top": "80mm",      # à ajuster selon la hauteur réelle de ta bannière
        "bottom": "10mm",
        "left": "10mm",
        "right": "10mm"
    }
)
    browser.close()

print(f"PDF generated: {output_pdf}")