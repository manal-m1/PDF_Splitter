from playwright.sync_api import sync_playwright

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Official Programme — Conference July 2026</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --ink:       #1C1917;
  --ink-mid:   #44403C;
  --ink-soft:  #78716C;
  --line:      #D6CFC4;
  --page:      #FDFAF6;
  --white:     #FFFFFF;

  --d1: #1A4971;   --d1-bg: #E2EEF8;   --d1-border: #A8C8E8;
  --d2: #1B5E3F;   --d2-bg: #E0F2E9;   --d2-border: #8FCFB0;
  --d3: #7B2D0E;   --d3-bg: #F7E5DC;   --d3-border: #E8A882;
  --d4: #442470;   --d4-bg: #EDE5F6;   --d4-border: #C4A8E5;
  --d5: #0E4F5A;   --d5-bg: #DCF0F4;   --d5-border: #85CAD6;

  --gold:      #8B5E00;
  --gold-pale: #F5E8C8;
  --gold-border: #C49A2A;

  --sponsor-bg:    #F5E8C8;
  --sponsor-border:#C49A2A;

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
.conf-sub { font-size: 13px; color: var(--ink-soft); margin-top: 6px; font-weight: 300; }
.big-dates {
  font-family: 'Cormorant Garamond', serif;
  font-size: 60px; font-weight: 700; color: var(--ink);
  line-height: 1; letter-spacing: -3px;
}
.date-sub { font-size: 12px; color: var(--ink-soft); text-align: right; font-weight: 300; margin-top: 4px; }

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
  padding: 10px 12px;
  vertical-align: middle;
  font-size: 13px;
  text-align: center;
}

.thead-day {
  background: var(--ink);
  color: #fff;
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
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
  font-size: 9px; font-weight: 700; letter-spacing: 2px;
  text-transform: uppercase; padding: 2px 7px;
  border-radius: 4px;
  background: rgba(255,255,255,0.18); color: rgba(255,255,255,0.95);
}

.time-cell {
  background: var(--white);
  font-size: 12px; font-weight: 600;
  color: var(--ink-soft);
  white-space: nowrap;
  width: 68px;
  min-width: 68px;
}

.tag {
  font-size: 10px; font-weight: 700; letter-spacing: 1px;
  text-transform: uppercase; margin-bottom: 4px; opacity: 0.80;
  display: block;
}
.speaker { font-size: 13px; font-weight: 600; color: var(--ink); line-height: 1.4; display: block; }
.affil { font-size: 11px; color: var(--ink-soft); font-weight: 300; margin-top: 3px; font-style: italic; display: block; }

.c-reg     { background: #F0EDE6; }
.c-coffee  { background: #EDE9E0; font-size:12px; color: var(--ink-soft); }
.c-welcome { background: #FDEAEA; border-left: 3px solid #B02020 !important; }
.c-lunch   { background: #E4F5EB; border-left: 3px solid #047857 !important; }
.c-sponsor { background: var(--sponsor-bg); border-left: 3px solid var(--sponsor-border) !important; }
.c-d1      { background: var(--d1-bg); border-left: 3px solid var(--d1) !important; }
.c-d2      { background: var(--d2-bg); border-left: 3px solid var(--d2) !important; }
.c-d3      { background: var(--d3-bg); border-left: 3px solid var(--d3) !important; }
.c-d4      { background: var(--d4-bg); border-left: 3px solid var(--d4) !important; }
.c-d5      { background: var(--d5-bg); border-left: 3px solid var(--d5) !important; }
.c-handson { background: #FFF0D0; border-left: 3px solid #B45309 !important; }
.c-aws     { background: #FDE8D8; border-left: 3px solid #C2440A !important; }
.c-roundtable { background: #D8F5F9; border-left: 3px solid #0369A1 !important; }
.c-sport   { background: #D4F5EE; border-left: 3px solid #0D7A6B !important; }
.c-closing { background: #EAE4F9; border-left: 3px solid #6D28D9 !important; }
.c-empty   { background: #F7F5F0; }

.footer {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 20px; padding-top: 14px; border-top: 1px solid var(--line);
  font-size: 11px; color: var(--ink-soft);
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

<div class="sched-wrap">
<table class="sched">
  <colgroup>
    <col style="width:68px">
    <col style="width:calc((100% - 68px)/6)">
    <col style="width:calc((100% - 68px)/6)">
    <col style="width:calc((100% - 68px)/12)">
    <col style="width:calc((100% - 68px)/6)">
    <col style="width:calc((100% - 68px)/6)">
    <col style="width:calc((100% - 68px)/6)">
  </colgroup>
  <thead>
    <tr>
      <th style="background:var(--ink);"></th>
      <th class="thead-day d1h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:22px;opacity:.4;">01</div>
        Monday 6 July
        <div style="font-size:10px;opacity:.6;font-weight:300;">1st day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
      <th class="thead-day d2h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:22px;opacity:.4;">02</div>
        Tuesday 7 July
        <div style="font-size:10px;opacity:.6;font-weight:300;">2nd day</div>
        <div class="venue-badge">UIR</div>
      </th>
      <th style="background:#5B21B6; color:#fff; font-size:11px; font-weight:700; padding:10px 6px; text-align:center;">
        Parallel<br>
        <span style="font-size:9px; font-weight:400; opacity:.8;">Ma Thèse en 180s</span>
      </th>
      <th class="thead-day d3h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:22px;opacity:.4;">03</div>
        Wednesday 8 July
        <div style="font-size:10px;opacity:.6;font-weight:300;">3rd day</div>
        <div class="venue-badge">FLSHR</div>
      </th>
      <th class="thead-day d4h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:22px;opacity:.4;">04</div>
        Thursday 9 July
        <div style="font-size:10px;opacity:.6;font-weight:300;">4th day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
      <th class="thead-day d5h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:22px;opacity:.4;">05</div>
        Friday 10 July
        <div style="font-size:10px;opacity:.6;font-weight:300;">Last day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
    </tr>
  </thead>
  <tbody>

    <!-- REGISTRATION -->
    <tr>
      <td class="time-cell">08:30<br>09:30</td>
      <td class="c-reg">
        <span class="tag">Welcome</span>
        <span class="speaker">🎟 Participant Registration</span>
      </td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
    </tr>

    <!-- MORNING TALKS -->
    <tr>
      <td class="time-cell">09:00<br>10:30</td>
      <td class="c-welcome">
        <span class="tag" style="color:#B02020;">Opening Ceremony</span>
        <span class="speaker">Welcome Session</span>
        <span class="affil">Opening Remarks and Official Speeches<br>Partners' Words</span>
      </td>
      <!-- Chetouani : mardi uniquement, 1 colonne -->
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 9H00–10H30</span>
        <span class="speaker">Prof. Mohamed CHETOUANI</span>
        <span class="affil">Sorbonne Université (SU), France</span>
      </td>
      <!-- Parallel Session Ma Thèse en 180s : rowspan couvre 11h00 → 18h00 (7 rows) -->
      <td class="c-parallel" rowspan="7" style="vertical-align:middle; text-align:center; background:#F5F3FF; border-left:3px solid #7C3AED !important;">
        <span class="tag" style="color:#7C3AED;">Parallel Session</span>
        <span class="speaker" style="color:#7C3AED; font-size:13px;">My Thesis<br>in 180s</span>
        <span class="affil" style="color:#7C3AED;">11H00 – 18H00</span>
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

    <!-- COFFEE BREAK MATIN -->
    <tr>
      <td class="time-cell">10:30<br>11:00</td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
        <div style="margin-top:4px; font-size:11px; color:var(--ink-soft);">[to be confirmed]</div>
      </td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
        <div style="margin-top:4px; font-size:11px; color:var(--ink-soft);">[to be confirmed]</div>
      </td>
      <!-- parallel col: rowspan from previous row, skip -->
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
        <div style="margin-top:4px; font-size:11px; color:var(--ink-soft);">[to be confirmed]</div>
      </td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
        <div style="margin-top:4px; font-size:11px; color:var(--ink-soft);">[to be confirmed]</div>
      </td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
        <div style="margin-top:4px; font-size:11px; color:var(--ink-soft);">[to be confirmed]</div>
      </td>
    </tr>

    <!-- 11H00 -->
    <tr>
      <td class="time-cell">11:00<br>12:00</td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">Platinum Sponsor Invited Talk</span>
        <span class="affil">11H00 – 12:00</span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. El Habib BEN LAHMER</span>
        <span class="affil">UHII</span>
      </td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. Mohamed BENDAHAN</span>
        <span class="affil">FLSH / UM5R</span>
      </td>
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. Ouassim KARRAKCHOU</span>
        <span class="affil">UIR, Rabat</span>
      </td>
      <td class="c-handson">
        <span class="tag" style="color:#B45309;">Hands-on · 11H00–12H30</span>
        <span class="speaker">Prof. Aissam BERRAHOU</span>
        <span class="affil">ENSIAS / UM5R</span>
      </td>
    </tr>

    <!-- 12H00 -->
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
        <span class="affil">FSR / UM5R</span>
      </td>
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 12H00–13H00</span>
        <span class="speaker">Prof. Houda BENBRAHIM</span>
        <span class="affil">ENSIAS / UM5R</span>
      </td>
      <td class="c-aws">
        <span class="tag" style="color:#C2440A;">AWS Certifications · 12H30–13H00</span>
        <span class="speaker">Dr. Karim BENZIDANE</span>
        <span class="affil">AWS Paris, France</span>
      </td>
    </tr>

    <!-- LUNCH -->
    <tr>
      <td class="time-cell">13:00<br>14:00</td>
      <td class="c-lunch">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:18px;">🍽</span>
      </td>
      <td class="c-lunch">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:18px;">🍽</span>
      </td>
      <td class="c-lunch">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:18px;">🍽</span>
      </td>
      <td class="c-lunch">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:18px;">🍽</span>
      </td>
      <td class="c-closing">
        <span class="tag" style="color:#6D28D9;">Closing · 13H00–13H30</span>
        <span class="speaker" style="font-size:12px;">Participant feedback &amp; Closing session</span>
      </td>
    </tr>

    <!-- 13H30 -->
    <tr>
      <td class="time-cell">13:30<br>15:00</td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-sponsor" style="text-align:center;">
        <span class="tag" style="color:var(--gold);">Déjeuner</span>
        <span class="speaker">en partenariat avec notre Platinum Sponsor</span>
        <span class="affil">13H30 – 15H00</span>
        <div style="margin-top:5px; font-size:11px; color:var(--ink-soft);">[to be confirmed]</div>
      </td>
    </tr>

    <!-- 14H00 -->
    <tr>
      <td class="time-cell">14:00<br>15:00</td>
      <td class="c-d1">
        <span class="tag" style="color:var(--d1);">Invited Talk · 14H00–15H00</span>
        <span class="speaker">Prof. Mohamed ESSAAIDI</span>
        <span class="affil">IEEE | ENSIAS / UM5R</span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 14H00–15H00</span>
        <span class="speaker">Prof. Mohammed KHALIL</span>
        <span class="affil">FSTM, UH2C, Morocco</span>
      </td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk &amp; Demo · 14H00–15H00</span>
        <span class="speaker" style="font-size:12px;">Prof. Soufiane AZOUAGHE<br>&amp; Mekki EL AMIRI</span>
        <span class="affil">FLSH / UM5R</span>
      </td>
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 14H00–15H00</span>
        <span class="speaker">Prof. Hakim HAFIDI</span>
        <span class="affil">UIR, Rabat</span>
      </td>
      <td class="c-empty" style="color:var(--ink-soft); font-size:11px;">
        Platinum Partner Lunch
      </td>
    </tr>

    <!-- ROUND TABLE / 15H00 -->
    <tr>
      <td class="time-cell">15:00<br>16:00</td>
      <td class="c-roundtable">
        <span class="tag" style="color:#0369A1;">Round Table · 15H00–16H00</span>
        <span class="speaker" style="font-size:12px;">
          Prof. Y. GAHI<br>
          Prof. M. BOUTAYEB<br>
          Prof. A. DRISSI EL MALIANI
        </span>
        <span class="affil">
          UIT<br>
          Université de Lorraine<br>
          UM5R
        </span>
      </td>
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 15H00–16H00</span>
        <span class="speaker">Prof. Boutaina HDIOUD</span>
        <span class="affil">ENSIAS / UM5R</span>
      </td>
      <td class="c-empty"></td>
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk · 15H00–16H00</span>
        <span class="speaker">Prof. Ibrahim RAHHAL</span>
        <span class="affil">UIR, Rabat</span>
      </td>
      <td class="c-handson">
        <span class="tag" style="color:#B45309;">Hands-on · 15H00–16H00</span>
        <span class="speaker">Prof. Aniss MOUMEN</span>
        <span class="affil">ENSAK / UIT</span>
      </td>
      <td class="c-sport" rowspan="3" style="vertical-align:middle; text-align:center;">
        <span class="tag" style="color:#0D7A6B;">Activities · 15H00–18H30</span>
        <span class="speaker" style="font-size:14px;">ACTIVITIES</span>
        <div style="margin-top:6px; font-size:11px; color:#0D7A6B; font-style:italic;">[to be confirmed]</div>
      </td>
    </tr>

    <!-- COFFEE BREAK APRES-MIDI -->
    <tr>
      <td class="time-cell">16:00<br>16:30</td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
      </td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
      </td>
      <td class="c-empty"></td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
      </td>
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">☕ Coffee Break</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">&amp; Participants Presentations (POSTERS)</span>
      </td>
      <!-- Friday: covered by sport rowspan -->
    </tr>

    <!-- 16H30 -->
    <tr style="height:120px;">
      <td class="time-cell">16:30<br>18:00</td>
      <td class="c-handson">
        <span class="tag" style="color:#B45309;">Hands-on · 16H30–18H00</span>
        <span class="speaker">Dr. Mohamed IMAM</span>
        <span class="affil">ENSIAS/UM5R &amp; Université de Waterloo</span>
      </td>
      <td class="c-handson">
        <span class="tag" style="color:#B45309;">Hands-on Session · 16H30–18H00</span>
        <span class="speaker">Prof. Jihane GHARIB</span>
        <span class="affil">ENSAK / UIT</span>
      </td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-handson" style="vertical-align:middle; text-align:center;">
        <span class="tag" style="color:#B45309;">Hands-on · 16H30–18H00</span>
        <span class="speaker" style="font-size:14px; font-weight:700; line-height:1.4;">Dr. Ayoub FARKANE</span>
        <span class="affil">Université de Lorraine, France<br>UIR, Morocco</span>
      </td>
      <!-- Friday: covered by sport rowspan -->
    </tr>

    <!-- AWS TALK JEUDI (separate row to avoid overlap) -->
    <tr style="height:80px;">
      <td class="time-cell">16:30<br>18:30</td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-aws" style="vertical-align:middle; text-align:center;">
        <span class="tag" style="color:#C2440A;">Invited Talk &amp; Hands-on AWS · 16H30–18H30</span>
        <span class="speaker" style="font-size:13px; font-weight:700; line-height:1.5;">Ms. Tiffany SOUTERRE<br>Mr. Olivier LEPLUS</span>
        <span class="affil">AWS Paris, France</span>
      </td>
      <td class="c-empty"></td>
    </tr>

    <!-- END OF DAY -->
    <tr style="height:36px;">
      <td class="time-cell">18:30</td>
      <td class="c-empty" style="font-size:11px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:11px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:11px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:11px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty"></td>
    </tr>

    <!-- GALA DINNER -->
    <tr style="height: 80px;">
      <td style="border: none; background: transparent;"></td>
      <td style="border: none; background: transparent;"></td>
      <td style="border: none; background: transparent;"></td>
      <td class="c-sponsor" style="vertical-align: middle; text-align: center; background: var(--sponsor-bg); border-left: 3px solid var(--gold-border) !important; border-radius: 0 0 8px 8px; box-shadow: 0 4px 12px rgba(184,134,11,0.08);">
        <span class="speaker" style="font-size: 14px; font-weight: 700; color: var(--ink); margin-top: 2px;">🍽 GALA DINNER</span>
      </td>
      <td style="border: none; background: transparent;"></td>
      <td style="border: none; background: transparent;"></td>
    </tr>

  </tbody>
</table>
</div>

<div class="footer">
  <div><strong>ENSIAS · UIR · FLSHR</strong> — Rabat, Morocco</div>
</div>

</body>

</html>
"""

output_path = r"C:\Users\GASMI MANAL\Desktop\Summer_School_Tasks\HTML Program\output_hd.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1920, "height": 1080},
        device_scale_factor=2
    )

    page.set_content(html_content)
    page.wait_for_timeout(1000)
    page.screenshot(path=output_path, full_page=True)
    browser.close()

print(f"Image correctement réalignée et générée : {output_path}")