from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import csv, math, os

ROOT = Path('datapass_v4_showcase_gpt56sol')
ROOT.mkdir(parents=True, exist_ok=True)
REGULAR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def font(size, bold=False):
    path = BOLD if bold else REGULAR
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def rgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def rr(d, xy, r, fill, outline=None, width=1): d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def wrap(d, text, x, y, f, fill, maxw, max_lines=4, spacing=3):
    words, lines, line = text.split(), [], ''
    for w in words:
        t = (line + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw: line = t
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        s = lines[-1]
        while s and d.textlength(s + '…', font=f) > maxw: s = s[:-1]
        lines[-1] = s + '…'
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += f.size + spacing
    return y

PROJECTS = {
'01_formation': {
'name':'Formation','subtitle':'SQL + Python + Data Engineering learning workspace','repo':'https://github.com/julian-passebecq/Fluent2_J_Formation','site':'No public deployment claimed in repository','tech':'React · TypeScript · Vite · Fluent UI · Datapass V4 notebook/content/figure/progress','colors':('#f7f5f1','#fffdfa','#16252d','#15384b','#0f6f69','#e9f4f1','#ddd9d1'),
'now':['SQL Foundations 0.A–0.C + chapters 1–8','39 SQL Applied Labs','Think in SQL reasoning layer','Gated corrections/solutions','Local progress & review'],'next':['Publish portable V4 packages','First-class sectioned notebook primitive','Stable shared visual registry','Reusable SQL window-frame semantic treatment'],
'scenarios':[('Learning home',['Choose a curriculum','See corpus metrics','Open Foundations or Applied Labs','Resume local progress']),('Foundation lesson',['Read imported notebook section','Keep source language intact','Navigate with section picker','Reveal correction only on demand']),('Think in SQL',['Start from grain/cardinality','Step through grouped/window logic','Use selective semantic figures','Check reasoning checkpoints']),('Practice & review',['Open source-backed exercises','Work without a fake judge','Reveal supplied solutions','Mark progress locally']),('Source fidelity',['Import source notebooks deterministically','Preserve original files','Resolve supplied media safely','Flag missing illustrations instead of inventing them'])]},
'02_code_lab': {
'name':'Data Engineering Code Lab','subtitle':'LeetCode-style practice for deterministic DE challenges','repo':'https://github.com/julian-passebecq/Fluent2_J_CodeLab','site':'Related deployed practice site: https://leetodedataeng.netlify.app/','tech':'React · TypeScript · Vite · Fluent UI · @datapass/code/learning/progress · lazy shared Monaco','colors':('#f7f8fa','#ffffff','#15243b','#15243b','#0f6cbd','#eef5fb','#e1e4ea'),
'now':['323 deterministic items','500 language/engine variants','Code / Solution / Compare','Hints, notes, review, mastery','Visualize only for canonical mappings'],'next':['Portable practice-catalog package','Mapped-only Visualize tab mode','Cleaner cross-repo bootstrap','Full release gate in provisioned environment'],
'scenarios':[('Challenge catalog',['Filter 323 items','Switch language / engine variants','See review and mastery state','Open a challenge']),('Code workbench',['Edit in lazy shared Monaco','Read prompt and constraints','Use hints progressively','No fake Run/Submit runtime']),('Solution compare',['Open Solution tab','Compare approach side by side','Keep notes','Mark for review later']),('Selective visualization',['Show CTA only for real mapping','Reuse canonical Figure','Explain state changes','Avoid bespoke drawings']),('Progress loop',['Track local mastery','Review flagged items','Use compact cheat sheets','Retain browser-local state'])]},
'03_visual_algorithms': {
'name':'Visual Algorithms & Cheat Sheets','subtitle':'ConceptMotion stress test for algorithms and DE/SQL patterns','repo':'https://github.com/julian-passebecq/Fluent2_J_VisualAlgo','site':'https://fluent2jvisualalgo.netlify.app/','tech':'Semantic LoopSceneSpec / WorkflowSpec / ExplanationTrack · responsive web UI','colors':('#faf9f6','#ffffff','#102b40','#102b40','#087985','#e9f4f2','#dde3e1'),
'now':['33 concept pages','Step / Play / Previous / Next / Reset','Synchronized explanation + code focus','4 cheat sheets','Local mastery + practice review'],'next':['External canonical Figure registry package','Traversal-state vocabulary for WorkflowSpec','Vertical stack presentation hint','Shared accessibility harness'],
'scenarios':[('Concept catalog',['Browse algorithms, SQL and DE patterns','Filter by topic','Open one concept','See complexity and mental model']),('Step-through animation',['Use Previous / Next / Play / Reset','Highlight active entities','Synchronize caption and code','Respect reduced motion']),('Binary search',['Track low / mid / high','Eliminate half the range','Advance with keyboard arrows','See state and code move together']),('DFS & recursion',['Reuse WorkflowSpec for traversal','Reuse LoopSceneSpec for stack depth','Show worklist / return state','Avoid a new graph engine']),('Practice + cheat sheets',['Use static reference when enough','Try 1–3 minute prompts','Reveal answer','Mark mastery locally'])]},
'04_cloud_architecture': {
'name':'Pipeline & Cloud Architecture Lab','subtitle':'Workflow behavior + architecture topology for modern data platforms','repo':'https://github.com/julian-passebecq/Fluent2_J_CloudArchi','site':'https://f2jcloudarchi.netlify.app/','tech':'React · TypeScript · Fluent UI · WorkflowSpec · DiagramSpec · ConceptMotion SVG','colors':('#f6f7f5','#ffffff','#102a43','#102a43','#006f75','#e5f3f2','#d9e1e4'),
'now':['DAGs, retries, backfills, CDC','Source→Move→Store→Process→Model→Serve','Fabric / Databricks / GCP / Azure lenses','Lakehouse-to-KPI lessons','Responsive diagrams + exports'],'next':['Keep provider terminology snapshots current','Further tighten cross-repo package closure','Reusable responsive wide-diagram guidance','Continue evidence-led hardening'],
'scenarios':[('Responsibility model',['Start from Source → Serve','Keep Operate/Govern cross-cutting','Select a stage','Connect behavior to responsibility']),('Pipeline pattern lab',['Choose fan-out / fan-in / retry','Run deterministic workflow frames','Inspect risk and design notes','Reset and compare patterns']),('Cloud architecture lens',['Pick conceptual or provider lens','Map the same responsibility model','Pan wide diagrams locally','Animate behavior, not static topology']),('Lakehouse → KPI',['Trace Bronze / Silver / Gold','Inspect star-schema grain and keys','Follow field → measure → KPI','Connect lineage to backfill topology']),('Troubleshooting & QA',['Use failure scenarios','Inspect quality-gate blocking','Export static SVG','Verify desktop + 390px flows'])]},
'05_norsk_vocab': {
'name':'Norsk Tech & Work Vocabulary','subtitle':'Compact Bokmål / English / French professional vocabulary atlas','repo':'https://github.com/julian-passebecq/Fluent2_J_Norsk','site':'No public deployment found in current Netlify project list','tech':'React · TypeScript · Fluent UI · Datapass content/knowledge/progress · local storage','colors':('#f8f8f5','#ffffff','#102d43','#102d43','#0b6870','#eff8f2','#dce3e5'),
'now':['215 terms / 5 themes','NB + EN + FR search','Theme & learning-state filters','Hide/reveal translations','New/Learning/Review/Mastered'],'next':['Locale-keyed lexical translation map','Entity-neutral mastery/review primitive','Optional compact multilingual table primitive','Portable package/bootstrap path'],
'scenarios':[('Browse vocabulary',['Search across three languages','Filter by theme','See current learning state','Open a word']),('Hide / reveal',['Hide translations globally','Reveal a single row','Keep Bokmål visible','Use keyboard controls']),('Learning state',['Move New → Learning → Review','Persist state locally','Filter Review queue','Finish as Mastered']),('Theme cheat sheet',['Open printable-style sheet','Scan NB / EN / FR columns','Jump to word detail','Use compact dense layout']),('Work-focused taxonomy',['Browse IT & Data','Switch to Project / Business','Use Job & Workplace','Prepare Interview & Recruitment'])]},
'06_portfolio_consumer': {
'name':'Portfolio Consumer Lab','subtitle':'Independent preview testing portfolio-hub + Project Galaxy','repo':'https://github.com/julian-passebecq/Fluent2_J_Portfolio','site':'Separate preview design; repository explicitly avoids datapassj.com production binding','tech':'React · TypeScript · Fluent UI · ProjectRegistry · DiagramSpec · shared radial Project Galaxy','colors':('#f5f3ee','#fffdf9','#17242b','#17313c','#28776c','#eef4f1','#d7ddd9'),
'now':['Career axis','Experience timeline','ProjectRegistry grid','Skills & certifications','Semantic Project Galaxy','Links/documents'],'next':['Portable public ProjectRegistry export','Shared ProjectRegistry → DiagramSpec helper','Cross-repo portfolio scaffold mode','Wide Figure phone presentation guidance'],
'scenarios':[('Home positioning',['Present Analyst → BI/SQL → Cloud/DE','Show concise facts','Keep neutral interview design','Navigate six sections']),('Experience timeline',['Scan roles chronologically','Open outcome-focused cards','Keep styling consumer-specific','Avoid a universal timeline renderer']),('Projects',['Read canonical public ProjectRegistry','Sort projects deterministically','Open HTTPS destinations','Keep runtime registry canonical']),('Project Galaxy',['Map registry → DiagramSpec','Use shared radial renderer','Select project nodes','Pan/contain wide view on phone']),('Skills & links',['Show certifications and skills','Keep documents separate','Use compact static layout','Remain isolated from production site'])]}}

def preview(d, box, p, mode, active):
    x0,y0,x1,y1=box; bg,surface,ink,navy,accent,soft,line=p['colors']
    rr(d,box,9,surface,line,1); d.rectangle((x0,y0,x1,y0+28),fill='#ffffff'); d.line((x0,y0+28,x1,y0+28),fill=line)
    rr(d,(x0+7,y0+6,x0+23,y0+22),4,navy); d.text((x0+12,y0+8),'D',font=font(7,True),fill='white'); d.text((x0+28,y0+7),p['name'],font=font(7,True),fill=ink)
    sw=72; d.rectangle((x0,y0+29,x0+sw,y1),fill=bg); d.line((x0+sw,y0+29,x0+sw,y1),fill=line)
    nav=['Home','Learn','Practice','Progress']
    if 'Code Lab' in p['name']: nav=['Practice','Cheat sheets','Review','Progress']
    if 'Visual Algorithms' in p['name']: nav=['Catalog','Concepts','Cheat sheets','Practice']
    if 'Cloud Architecture' in p['name']: nav=['Start','Patterns','Architecture','Practice']
    if 'Norsk' in p['name']: nav=['Browse','Cheat sheets','Review','Progress']
    if 'Portfolio' in p['name']: nav=['Home','Experience','Projects','Galaxy']
    for i,n in enumerate(nav):
        yy=y0+39+i*22
        if i==active%4: rr(d,(x0+5,yy-1,x0+sw-5,yy+15),3,soft)
        d.text((x0+10,yy+3),n,font=font(5,i==active%4),fill=ink)
    mx=x0+sw+8; my=y0+39; mw=x1-mx-7; sy=my+24; d.text((mx,my),mode,font=font(9,True),fill=navy)
    if any(k in mode for k in ['Step-through','Binary search','DFS & recursion']):
        rr(d,(mx,sy,mx+mw,y1-7),5,'#fff',line)
        for i,b in enumerate(['<','>','Play','Reset']):
            bx=mx+5+i*29; rr(d,(bx,sy+5,bx+25,sy+19),3,soft,line); d.text((bx+5,sy+8),b,font=font(4,True),fill=accent)
        vals=[2,5,7,11,14,19]
        for i,v in enumerate(vals):
            bx=mx+7+i*29; rr(d,(bx,sy+32,bx+23,sy+55),3,soft if i==2 else '#fafbfa',accent if i==2 else line); d.text((bx+7,sy+40),str(v),font=font(6,True),fill=ink)
        d.text((mx+6,sy+64),'Semantic state + code focus',font=font(5),fill='#596875')
    elif any(k in mode for k in ['Responsibility','Pipeline pattern','Cloud architecture','Lakehouse','Troubleshooting']):
        rr(d,(mx,sy,mx+mw,y1-7),5,'#fff',line); labs=['Src','Move','Store','Proc','Model','Serve']
        for i,l in enumerate(labs):
            bx=mx+5+i*(mw-10)/6; rr(d,(bx,sy+13,bx+(mw-30)/6,sy+34),3,soft if i==active else '#fff',accent if i==active else line); d.text((bx+3,sy+20),l,font=font(4,True),fill=ink)
        d.line((mx+6,sy+48,mx+mw-6,sy+48),fill=accent,width=1); d.text((mx+6,sy+53),'Operate + Govern',font=font(5,True),fill=accent)
    elif 'Norsk' in p['name']:
        rr(d,(mx,sy,mx+mw,sy+20),4,'#fff',line); d.text((mx+6,sy+6),'Search NB / EN / FR',font=font(5),fill='#6a767c')
        rows=[('dataplattform','data platform','plateforme de données','Learning'),('arbeidsflyt','workflow','flux de travail','Review'),('intervju','interview','entretien','New')]
        for i,r in enumerate(rows):
            yy=sy+27+i*33; rr(d,(mx,yy,mx+mw,yy+28),3,'#fff',line); d.text((mx+5,yy+5),r[0],font=font(6,True),fill=ink); d.text((mx+61,yy+5),'EN '+r[1],font=font(4),fill='#566671'); d.text((mx+61,yy+15),'FR '+r[2],font=font(4),fill='#566671')
    elif 'Portfolio' in p['name'] and 'Galaxy' in mode:
        rr(d,(mx,sy,mx+mw,y1-7),5,'#fff',line); cx=mx+mw/2; cy=sy+60; rr(d,(cx-22,cy-9,cx+22,cy+9),7,navy); d.text((cx-14,cy-3),'Projects',font=font(4,True),fill='white')
        for i,lab in enumerate(['BI','Cloud','DE','Viz','Apps','Tools']):
            a=2*math.pi*i/6; nx=cx+math.cos(a)*60; ny=cy+math.sin(a)*38; d.line((cx,cy,nx,ny),fill='#b7c8c3'); rr(d,(nx-13,ny-7,nx+13,ny+7),5,soft,accent); d.text((nx-5,ny-2),lab,font=font(4,True),fill=accent)
    elif any(k in mode for k in ['Code workbench','Solution compare']):
        rr(d,(mx,sy,mx+mw,y1-7),5,'#fbfcfd',line); rr(d,(mx+5,sy+18,mx+mw*.49,y1-13),4,'#111827')
        for j,ln in enumerate(['WITH filtered AS (',' SELECT * FROM orders'," WHERE status='paid'",')']): d.text((mx+9,sy+25+j*10),ln,font=font(4),fill='#e5e7eb')
        rr(d,(mx+mw*.52,sy+18,mx+mw-5,y1-13),4,'#fff',line); d.text((mx+mw*.55,sy+25),'Hints / Compare',font=font(5,True),fill=accent)
    else:
        for i,t in enumerate(['Foundations','Applied Labs','Reasoning','Progress']):
            bx=mx+(i%2)*(mw/2+2); by=sy+(i//2)*46; rr(d,(bx,by,bx+mw/2-4,by+38),4,'#fff',line); d.text((bx+5,by+6),t,font=font(5,True),fill=navy); d.text((bx+5,by+19),'Source-backed surface',font=font(4),fill='#667077')

def safe_name(mode): return mode.lower().replace(' ','_').replace('/','-').replace('→','to').replace('&','and')

def board(folder,p,idx,scenario):
    mode,steps=scenario; bg,surface,ink,navy,accent,soft,line=p['colors']; W,H=800,500
    im=Image.new('RGB',(W,H),rgb(bg)); d=ImageDraw.Draw(im); rr(d,(18,13,52,47),9,navy); d.text((28,19),'D',font=font(17,True),fill='white')
    title_size=24 if len(p['name'])<=24 else 19 if len(p['name'])<=34 else 17; d.text((64,15),p['name'],font=font(title_size,True),fill=ink); d.text((65,42),p['subtitle'],font=font(10),fill='#52616a')
    d.text((445,19),f'Scenario {idx} — {mode}',font=font(12,True),fill=navy); d.line((445,40,515,40),fill=accent,width=3)
    margin,top,gap=17,64,7; cw=(W-2*margin-3*gap)//4; calls=['Start with the real product structure.','Follow the interaction or semantic change.','Shared Datapass primitives carry the flow.','Interview takeaway: useful product, no fake runtime.']
    for i,s in enumerate(steps[:4]):
        x0=margin+i*(cw+gap); x1=x0+cw; rr(d,(x0,top,x1,463),8,'#fff',line); rr(d,(x0+7,top+7,x0+31,top+31),12,accent); d.text((x0+15,top+11),str(i+1),font=font(11,True),fill='white'); wrap(d,s,x0+38,top+9,font(9,True),ink,cw-45,2,2); preview(d,(x0+6,top+44,x1-6,top+319),p,mode,i); rr(d,(x0+8,top+329,x1-8,452),6,soft); wrap(d,calls[i],x0+15,top+341,font(6),navy,cw-30,4,2)
    d.text((20,478),p['repo'],font=font(5),fill='#68757b'); d.text((630,478),f'Datapass V4 · board {idx}/5',font=font(6,True),fill=accent)
    path=folder/f'{idx:02d}_{safe_name(mode)}.png'; im=im.quantize(colors=24,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE); im.save(path,optimize=True); return path.name

for key,p in PROJECTS.items():
    folder=ROOT/key; folder.mkdir(parents=True,exist_ok=True); files=[board(folder,p,i,s) for i,s in enumerate(p['scenarios'],1)]
    hero=files[1] if key=='03_visual_algorithms' else files[2] if key=='04_cloud_architecture' else files[3] if key=='06_portfolio_consumer' else files[0]
    md=[f"# {p['name']}",'',p['subtitle'],'',f"- **GitHub:** {p['repo']}",f"- **Website:** {p['site']}",f"- **Implementation:** {p['tech']}",'','## UI preview','',f"![{p['name']} UI scenario]({hero})",'', '> Explanatory scenario views grounded in the consumer repository, CSS, components and product behavior. They are presentation assets, not fake runtime screenshots.','','## What exists now']
    md += [f'- {x}' for x in p['now']]; md += ['','## Backlog / next version']+[f'- {x}' for x in p['next']]; md += ['','## Five explanatory PNG boards']+[f"- `{fn}` — {p['scenarios'][i][0]}" for i,fn in enumerate(files)]; md += ['','## Scenario gallery','','<table>','<tr>']
    for i,fn in enumerate(files):
        md.append(f'<td><img src="{fn}" alt="{p["name"]} scenario {i+1}" width="360"></td>')
        if i%2==1 and i != len(files)-1: md += ['</tr>','<tr>']
    md += ['</tr>','</table>','']; (folder/'README.md').write_text('\n'.join(md),encoding='utf-8')

root=['# Datapass V4 — Six Consumer Interview Showcase','', 'Five explanatory PNG boards per consumer. The boards are presentation-oriented UI reconstructions grounded in current repositories, product copy, CSS tokens, component structure and available deployment evidence.','','## At-a-glance UI previews','', '<table>','<tr>', '<td><b>Formation</b><br><img src="01_formation/01_learning_home.png" width="360"></td>', '<td><b>Data Engineering Code Lab</b><br><img src="02_code_lab/01_challenge_catalog.png" width="360"></td>', '</tr><tr>', '<td><b>Visual Algorithms & Cheat Sheets</b><br><img src="03_visual_algorithms/02_step-through_animation.png" width="360"></td>', '<td><b>Pipeline & Cloud Architecture Lab</b><br><img src="04_cloud_architecture/03_cloud_architecture_lens.png" width="360"></td>', '</tr><tr>', '<td><b>Norsk Tech & Work Vocabulary</b><br><img src="05_norsk_vocab/01_browse_vocabulary.png" width="360"></td>', '<td><b>Portfolio Consumer Lab</b><br><img src="06_portfolio_consumer/04_project_galaxy.png" width="360"></td>', '</tr>','</table>','','## Shared engineering story','', '- Six independent consumers were used to validate Datapass V4 with real product requirements.', '- React/TypeScript/Fluent consumers reuse shared Datapass packages and semantic Figure/Workflow/Diagram contracts.', '- Local-only progress is used where appropriate; no backend/auth/cloud sync is invented.', '- No fake SQL/Spark/Python execution or universal judge is claimed.', '- Repeated framework friction is primarily cross-repository consumption because V4 is not yet a published SDK.','','## Project index','', '| Project | GitHub | Website | Current scope | Next-version focus |','|---|---|---|---|---|']
for p in PROJECTS.values(): root.append(f"| {p['name']} | {p['repo']} | {p['site']} | {'; '.join(p['now'][:3])} | {'; '.join(p['next'][:2])} |")
(ROOT/'README.md').write_text('\n'.join(root)+'\n',encoding='utf-8')
with (ROOT/'feature_summary.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['project','github','website','implementation','features_now','backlog_next'])
    for p in PROJECTS.values(): w.writerow([p['name'],p['repo'],p['site'],p['tech'],' | '.join(p['now']),' | '.join(p['next'])])
print('generated',len(list(ROOT.rglob('*.png'))),'PNG boards')
