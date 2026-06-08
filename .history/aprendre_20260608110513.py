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
  --line:      #C8BDB0;
  --page:      #FDFAF6;
  --white:     #FFFFFF;

  /* Day header colours — kept */
  --d1: #1A4971;   --d1-bg: #D4E8F5;   --d1-border: #6AADD6;
  --d2: #1B5E3F;   --d2-bg: #CEEADB;   --d2-border: #5DB88E;
  --d3: #7B2D0E;   --d3-bg: #F2D8CC;   --d3-border: #D98A60;
  --d4: #442470;   --d4-bg: #E4D8F2;   --d4-border: #A87DD4;
  --d5: #0E4F5A;   --d5-bg: #C8E8EE;   --d5-border: #5BB8C8;

  /* Warm amber for sponsor / coffee */
  --gold:        #7A4A00;
  --gold-pale:   #F0D890;
  --gold-mid:    #C88A1A;
  --gold-border: #AA6C00;
  --sponsor-bg:  #F5DCA0;
  --sponsor-text:#6B3E00;

  /* Other slot colours — warmer/darker */
  --handson-bg:  #FFDFA8;
  --handson-bd:  #A05000;
  --handson-txt: #7A3300;

  --aws-bg:  #FCCBA8;
  --aws-bd:  #AA3A06;
  --aws-txt: #881800;

  --rt-bg:  #C8E8F8;
  --rt-bd:  #0560A0;
  --rt-txt: #024080;

  --closing-bg: #DDD0F8;
  --closing-bd: #5A1EC8;
  --closing-txt:#3A0A9A;

  --welcome-bg: #FAD4D4;
  --welcome-bd: #A01818;

  --lunch-bg: #C8EED8;
  --lunch-bd: #047857;

  --reg-bg: #EDE8E0;
}

body {
  font-family: 'Outfit', sans-serif;
  background: var(--page);
  color: var(--ink);
  padding: 36px 44px;
  min-width: 1400px;
  font-size: 15px; /* base size up for readability */
}

/* ── HEADER ─────────────────────────────────────────── */
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
  background: var(--gold-mid);
  opacity: 0.6;
}
.conf-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 46px; font-weight: 700; line-height: 1.1;
  color: var(--ink); letter-spacing: -1px;
}
.conf-sub { font-size: 15px; color: var(--ink-soft); margin-top: 6px; font-weight: 300; }
.big-dates {
  font-family: 'Cormorant Garamond', serif;
  font-size: 64px; font-weight: 700; color: var(--ink);
  line-height: 1; letter-spacing: -3px;
}
.date-sub { font-size: 13px; color: var(--ink-soft); text-align: right; font-weight: 300; margin-top: 4px; }

/* ── SCHEDULE WRAPPER ────────────────────────────────── */
.sched-wrap {
  border: 1px solid var(--line);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 24px rgba(28,25,23,0.09);
}

table.sched {
  width: 100%;
  border-collapse: collapse;
}

table.sched th,
table.sched td {
  border: 1px solid var(--line);
  padding: 11px 13px;
  vertical-align: middle;
  font-size: 14px;   /* up from 13 */
  text-align: center;
}

/* ── DAY HEADERS ─────────────────────────────────────── */
.thead-day {
  background: var(--ink);
  color: #fff;
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
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
  font-size: 10px; font-weight: 700; letter-spacing: 2px;
  text-transform: uppercase; padding: 2px 8px;
  border-radius: 4px;
  background: rgba(255,255,255,0.20); color: rgba(255,255,255,0.95);
}

/* ── TIME CELL ───────────────────────────────────────── */
.time-cell {
  background: var(--white);
  font-size: 13px; font-weight: 700;
  color: var(--ink-mid);
  white-space: nowrap;
  width: 72px; min-width: 72px;
}

/* ── SHARED SLOT TYPOGRAPHY ──────────────────────────── */
.tag {
  font-size: 11px; font-weight: 700; letter-spacing: 1px;
  text-transform: uppercase; margin-bottom: 5px; opacity: 0.85;
  display: block;
}
.speaker {
  font-size: 14px; font-weight: 600; color: var(--ink);
  line-height: 1.45; display: block;
}
.affil {
  font-size: 12px; color: var(--ink-soft); font-weight: 300;
  margin-top: 3px; font-style: italic; display: block;
}

/* ── SLOT COLOURS (warm, readable) ───────────────────── */
.c-reg     { background: var(--reg-bg); }
.c-empty   { background: #F5F2EC; }
.c-welcome { background: var(--welcome-bg); border-left: 3px solid var(--welcome-bd) !important; }
.c-lunch   { background: var(--lunch-bg);   border-left: 3px solid var(--lunch-bd)   !important; }

.c-sponsor {
  background: var(--sponsor-bg);
  border-left: 3px solid var(--gold-border) !important;
}
.c-sponsor .tag    { color: var(--gold); }
.c-sponsor .speaker{ color: var(--sponsor-text); }
.c-sponsor .affil  { color: var(--gold-border); }

.c-d1 { background: var(--d1-bg); border-left: 3px solid var(--d1) !important; }
.c-d2 { background: var(--d2-bg); border-left: 3px solid var(--d2) !important; }
.c-d3 { background: var(--d3-bg); border-left: 3px solid var(--d3) !important; }
.c-d4 { background: var(--d4-bg); border-left: 3px solid var(--d4) !important; }
.c-d5 { background: var(--d5-bg); border-left: 3px solid var(--d5) !important; }

.c-handson {
  background: var(--handson-bg);
  border-left: 3px solid var(--handson-bd) !important;
}
.c-handson .tag    { color: var(--handson-txt); }
.c-handson .speaker{ color: var(--ink); }

.c-aws {
  background: var(--aws-bg);
  border-left: 3px solid var(--aws-bd) !important;
}
.c-aws .tag { color: var(--aws-txt); }

.c-roundtable {
  background: var(--rt-bg);
  border-left: 3px solid var(--rt-bd) !important;
}
.c-roundtable .tag    { color: var(--rt-txt); }
.c-roundtable .speaker{ color: var(--ink); }
.c-roundtable .affil  { color: var(--rt-txt); }

.c-sport {
  background: #B8EDDA;
  border-left: 3px solid #0B6A58 !important;
}
.c-closing {
  background: var(--closing-bg);
  border-left: 3px solid var(--closing-bd) !important;
}
.c-closing .tag    { color: var(--closing-txt); }
.c-closing .speaker{ color: var(--ink); }

/* ── COFFEE BREAK shared helper ──────────────────────── */
.coffee-content .tag    { color: var(--gold); }
.coffee-content .speaker{ color: var(--sponsor-text); font-weight: 600; }
.coffee-content .affil  { color: var(--gold-border); }

/* ── FOOTER ──────────────────────────────────────────── */
.footer {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 20px; padding-top: 14px; border-top: 1px solid var(--line);
  font-size: 12px; color: var(--ink-soft);
}
.footer strong { color: var(--ink-mid); font-weight: 600; }
</style>
</head>
<body>

<!-- ════════════════ HEADER ════════════════ -->
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

<!-- ════════════════ TABLE ════════════════ -->
<div class="sched-wrap">
<table class="sched">
  <colgroup>
    <col style="width:72px">
    <!-- Mon–Tue: 2 equal columns -->
    <col style="width:calc((100% - 72px)/5)">
    <col style="width:calc((100% - 72px)/5)">
    <!-- Wed / Thu / Fri -->
    <col style="width:calc((100% - 72px)/5)">
    <col style="width:calc((100% - 72px)/5)">
    <col style="width:calc((100% - 72px)/5)">
  </colgroup>

  <!-- ── DAY HEADERS ── -->
  <thead>
    <tr>
      <th style="background:var(--ink);"></th>
      <th class="thead-day d1h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:24px;opacity:.4;">01</div>
        Monday 6 July
        <div style="font-size:11px;opacity:.6;font-weight:300;">1st day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
      <th class="thead-day d2h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:24px;opacity:.4;">02</div>
        Tuesday 7 July
        <div style="font-size:11px;opacity:.6;font-weight:300;">2nd day</div>
        <div class="venue-badge">UIR</div>
      </th>
      <th class="thead-day d3h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:24px;opacity:.4;">03</div>
        Wednesday 8 July
        <div style="font-size:11px;opacity:.6;font-weight:300;">3rd day</div>
        <div class="venue-badge">FLSHR</div>
      </th>
      <th class="thead-day d4h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:24px;opacity:.4;">04</div>
        Thursday 9 July
        <div style="font-size:11px;opacity:.6;font-weight:300;">4th day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
      <th class="thead-day d5h">
        <div style="font-family:'Cormorant Garamond',serif;font-size:24px;opacity:.4;">05</div>
        Friday 10 July
        <div style="font-size:11px;opacity:.6;font-weight:300;">Last day</div>
        <div class="venue-badge">ENSIAS</div>
      </th>
    </tr>
  </thead>

  <tbody>

    <!-- ══ REGISTRATION 08:30–09:30 ══ -->
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
    </tr>

    <!-- ══ MORNING TALKS 09:00–10:30 ══ -->
    <tr>
      <td class="time-cell">09:00<br>10:30</td>

      <!-- Monday: Opening Ceremony -->
      <td class="c-welcome">
        <span class="tag" style="color:#A01818;">Opening Ceremony</span>
        <span class="speaker">Welcome Session</span>
        <span class="affil">Opening Remarks &amp; Official Speeches<br>Partners' Words</span>
      </td>

      <!-- Tuesday: Chetouani spans 2 columns (no parallel session on Tue) -->
      <td class="c-d2" colspan="2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 9H00–10H30</span>
        <span class="speaker">Prof. Mohamed CHETOUANI</span>
        <span class="affil">Sorbonne Université (SU), France</span>
      </td>

      <!-- Thursday -->
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 9H00–10H00</span>
        <span class="speaker">Prof. Luc De Brabandere</span>
      </td>

      <!-- Friday -->
      <td class="c-d5">
        <span class="tag" style="color:var(--d5);">Invited Talk · 9H00–10H30</span>
        <span class="speaker">Mr. Mohammed ACHOUR</span>
        <span class="affil">Cisco, Morocco</span>
      </td>
    </tr>

    <!-- ══ COFFEE BREAK MATIN 10:30–11:00 ══ -->
    <!-- Single reusable snippet via a helper div, repeated per column -->
    <tr>
      <td class="time-cell">10:30<br>11:00</td>
      <!-- Monday -->
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)<br>[to be confirmed]</span>
      </td>
      <!-- Tuesday -->
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)<br>[to be confirmed]</span>
      </td>
      <!-- Wednesday -->
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)<br>[to be confirmed]</span>
      </td>
      <!-- Thursday -->
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)<br>[to be confirmed]</span>
      </td>
      <!-- Friday -->
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)<br>[to be confirmed]</span>
      </td>
    </tr>

    <!-- ══ 11:00–12:00 ══ -->
    <tr>
      <td class="time-cell">11:00<br>12:00</td>

      <!-- Monday: Platinum Sponsor Talk -->
      <td class="c-sponsor">
        <span class="tag" style="color:var(--gold);">Platinum Sponsor Invited Talk</span>
        <span class="affil" style="color:var(--gold-border);">11H00 – 12H00</span>
      </td>

      <!-- Tuesday -->
      <td class="c-d2">
        <span class="tag" style="color:var(--d2);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. El Habib BEN LAHMER</span>
        <span class="affil">UHII</span>
      </td>

      <!-- Wednesday -->
      <td class="c-d3">
        <span class="tag" style="color:var(--d3);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. Mohamed BENDAHAN</span>
        <span class="affil">FLSH / UM5R</span>
      </td>

      <!-- Thursday -->
      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 11H00–12H00</span>
        <span class="speaker">Prof. Ouassim KARRAKCHOU</span>
        <span class="affil">UIR, Rabat</span>
      </td>

      <!-- Friday: Hands-on starts at 11h -->
      <td class="c-handson">
        <span class="tag">Hands-on · 11H00–12H30</span>
        <span class="speaker">Prof. Aissam BERRAHOU</span>
        <span class="affil">ENSIAS / UM5R</span>
      </td>
    </tr>

    <!-- ══ 12:00–13:00 ══ -->
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
        <span class="tag" style="color:var(--aws-txt);">AWS Certifications · 12H30–13H00</span>
        <span class="speaker">Dr. Karim BENZIDANE</span>
        <span class="affil">AWS Paris, France</span>
      </td>
    </tr>

    <!-- ══ LUNCH 13:00–14:00 ══ -->
    <tr>
      <td class="time-cell">13:00<br>14:00</td>
      <td class="c-lunch" style="text-align:center;">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:20px;">🍽</span>
      </td>
      <td class="c-lunch" style="text-align:center;">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:20px;">🍽</span>
      </td>
      <td class="c-lunch" style="text-align:center;">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:20px;">🍽</span>
      </td>
      <td class="c-lunch" style="text-align:center;">
        <span class="tag" style="color:#047857;">Déjeuner</span>
        <span style="font-size:20px;">🍽</span>
      </td>
      <!-- Friday: Closing -->
      <td class="c-closing" style="text-align:center;">
        <span class="tag" style="color:var(--closing-txt);">Closing · 13H00–13H30</span>
        <span class="speaker" style="font-size:13px;">Participant feedback &amp; Closing session</span>
      </td>
    </tr>

    <!-- ══ 13:30–15:00 (Friday: Platinum Partner Lunch) ══ -->
    <tr>
      <td class="time-cell">13:30<br>15:00</td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-sponsor" style="text-align:center; vertical-align:middle;">
        <span class="tag" style="color:var(--gold);">Déjeuner</span>
        <span class="speaker" style="color:var(--sponsor-text);">en partenariat avec notre Platinum Sponsor</span>
        <span class="affil" style="color:var(--gold-border);">13H30 – 15H00</span>
        <div style="margin-top:5px; font-size:12px; color:var(--gold-border);">[to be confirmed]</div>
      </td>
    </tr>

    <!-- ══ 14:00–15:00 ══ -->
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
        <span class="speaker" style="font-size:13px;">Prof. Soufiane AZOUAGHE<br>&amp; Mekki EL AMIRI</span>
        <span class="affil">FLSH / UM5R</span>
      </td>

      <td class="c-d4">
        <span class="tag" style="color:var(--d4);">Invited Talk · 14H00–15H00</span>
        <span class="speaker">Prof. Hakim HAFIDI</span>
        <span class="affil">UIR, Rabat</span>
      </td>

      <!-- Friday: still in Platinum lunch window -->
      <td class="c-empty" style="font-size:12px; color:var(--ink-soft); text-align:center; vertical-align:middle;">
        Platinum Partner Lunch
      </td>
    </tr>

    <!-- ══ ROUND TABLE / 15:00–16:00 ══ -->
    <tr>
      <td class="time-cell">15:00<br>16:00</td>

      <!-- Monday: Round Table -->
      <td class="c-roundtable">
        <span class="tag" style="color:var(--rt-txt);">Round Table · 15H00–16H00</span>
        <span class="speaker" style="font-size:13px; line-height:1.7;">
          Prof. Y. GAHI<br>
          Prof. M. BOUTAYEB<br>
          Prof. A. DRISSI EL MALIANI
        </span>
        <span class="affil" style="line-height:1.7;">
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
        <span class="tag">Hands-on · 15H00–16H00</span>
        <span class="speaker">Prof. Aniss MOUMEN</span>
        <span class="affil">ENSAK / UIT</span>
      </td>

      <!-- Friday: Activities rowspan=3 -->
      <td class="c-sport" rowspan="3" style="vertical-align:middle; text-align:center;">
        <span class="tag" style="color:#0B6A58;">Activities · 15H00–18H30</span>
        <span class="speaker" style="font-size:15px; font-weight:700; color:#0B6A58;">ACTIVITIES</span>
        <div style="margin-top:6px; font-size:12px; color:#0B6A58; font-style:italic;">[to be confirmed]</div>
      </td>
    </tr>

    <!-- ══ COFFEE BREAK APRÈS-MIDI 16:00–16:30 ══ -->
    <tr>
      <td class="time-cell">16:00<br>16:30</td>
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)</span>
      </td>
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)</span>
      </td>
      <td class="c-empty"></td>
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)</span>
      </td>
      <td class="c-sponsor coffee-content">
        <span class="tag">☕ Pause Café</span>
        <span class="speaker">Platinum Sponsor Show Stand</span>
        <span class="affil">Participants Presentations (POSTERS)</span>
      </td>
      <!-- Friday: sport rowspan -->
    </tr>

    <!-- ══ 16:30–18:00 ══ -->
    <tr style="height:120px;">
      <td class="time-cell">16:30<br>18:00</td>

      <td class="c-handson">
        <span class="tag">Hands-on · 16H30–18H00</span>
        <span class="speaker">Dr. Mohamed IMAM</span>
        <span class="affil">ENSIAS/UM5R &amp; Université de Waterloo</span>
      </td>

      <td class="c-handson">
        <span class="tag">Hands-on · 16H30–18H00</span>
        <span class="speaker">Prof. Jihane GHARIB</span>
        <span class="affil">ENSAK / UIT</span>
      </td>

      <td class="c-empty"></td>

      <td class="c-empty"></td>

      <td class="c-handson" style="vertical-align:middle; text-align:center;">
        <span class="tag">Hands-on · 16H30–18H00</span>
        <span class="speaker" style="font-size:15px; font-weight:700;">Dr. Ayoub FARKANE</span>
        <span class="affil">Université de Lorraine, France<br>UIR, Morocco</span>
      </td>
      <!-- Friday: sport rowspan -->
    </tr>

    <!-- ══ AWS JEUDI 16:30–18:30 ══ -->
    <tr style="height:80px;">
      <td class="time-cell">16:30<br>18:30</td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-empty"></td>
      <td class="c-aws" style="vertical-align:middle; text-align:center;">
        <span class="tag" style="color:var(--aws-txt);">Invited Talk &amp; Hands-on AWS · 16H30–18H30</span>
        <span class="speaker" style="font-size:14px; line-height:1.6;">Ms. Tiffany SOUTERRE<br>Mr. Olivier LEPLUS</span>
        <span class="affil">AWS Paris, France</span>
      </td>
      <td class="c-empty"></td>
    </tr>

    <!-- ══ END OF DAY ══ -->
    <tr style="height:36px;">
      <td class="time-cell">18:30</td>
      <td class="c-empty" style="font-size:12px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:12px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:12px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty" style="font-size:12px; color:var(--ink-soft);">End of day</td>
      <td class="c-empty"></td>
    </tr>

    <!-- ══ GALA DINNER (Wednesday only) ══ -->
    <tr style="height:80px;">
      <td style="border:none; background:transparent;"></td>
      <td style="border:none; background:transparent;"></td>
      <td style="border:none; background:transparent;"></td>
      <!-- Wednesday column (index 3 = col 4 counting from time) -->
      <td style="border:none; background:transparent;"></td>
      <td class="c-sponsor" style="vertical-align:middle; text-align:center;
          border-radius:0 0 8px 8px; box-shadow:0 4px 12px rgba(170,108,0,0.12);">
        <span class="speaker" style="font-size:15px; font-weight:700; color:var(--ink);">🍽 GALA DINNER</span>
      </td>
      <td style="border:none; background:transparent;"></td>
    </tr>

  </tbody>
</table>
</div>

<div class="footer">
  <div><strong>ENSIAS · UIR · FLSHR</strong> — Rabat, Morocco</div>
</div>

</body>
</html>