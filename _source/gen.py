import html, re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root: pages live here
SRC = os.path.dirname(os.path.abspath(__file__))
HOME = open(os.path.join(ROOT,'index.html')).read()
CSS = re.search(r'<style>(.*?)</style>', HOME, re.S).group(1)

VAQ = '<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script>'
EXTRA = """
.phero .pguar{display:inline-flex;align-items:center;gap:9px;margin-top:14px;color:var(--gold2);font-weight:600;font-size:14.5px;text-decoration:none}
.phero .pguar span{flex:0 0 auto;display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--gold);color:#fff;font-size:11px}
.phero .pguar:hover{text-decoration:underline}
.phero .proofrow{list-style:none;padding:16px 0 0;margin:20px 0 0;border-top:1px solid rgba(255,255,255,.14);display:grid;grid-template-columns:repeat(5,auto);gap:12px 22px;justify-content:start}
.phero .proofrow li{font-size:12px;color:#c9cedb;line-height:1.3;font-weight:600}
.phero .proofrow b{display:block;font-family:var(--display);font-size:26px;color:var(--gold2);font-weight:600;line-height:1.05;margin-bottom:3px}
.phero p.outcomes{color:#fff;font-size:18px;line-height:1.5;max-width:44ch}
.ggroup{margin-top:34px}
.ggroup h3{font-size:22px;display:flex;align-items:center;gap:10px}
.ggroup h3::before{content:"";width:22px;height:3px;background:var(--gold);border-radius:2px}
.ggroup .items{margin-top:14px}
.notinc{margin-top:26px;padding:16px 20px;border-left:3px solid var(--gold);background:var(--surface);font-size:16px;max-width:none}
@media(max-width:820px){.phero .proofrow{grid-template-columns:repeat(3,1fr);gap:14px 12px}.phero .proofrow b{font-size:23px}.phero p.outcomes{font-size:16.5px}}
.fl{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:center;background:var(--surface);border:1px solid var(--rule);border-left:4px solid var(--gold);border-radius:10px;padding:30px}
.fl-copy p{margin-top:12px}
.fl-f{display:flex;gap:8px;flex-wrap:wrap}
.fl-f input{flex:1 1 140px;min-width:0;padding:11px 12px;font-size:16px;border:1px solid var(--rule);border-radius:7px;background:var(--bg);color:var(--ink)}
.fl-f input:focus{outline:2px solid var(--gold);border-color:var(--gold)}
.fl-f .btn{flex:0 0 auto}
.fl-m{margin:8px 0 0;font-size:14px;color:var(--quiet)}
.fl-m:empty{display:none}
.fl-share{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin-top:20px;padding-top:18px;border-top:1px solid var(--rule);font-size:15px}
.fl-share span{flex:1 1 100%;color:var(--ink)}
.fl-share .btn.ghost{color:var(--navy);border-color:var(--navy);padding:9px 16px;font-size:14px}
.fl-share a{color:var(--gold);font-weight:600;text-decoration:none;font-size:14px}
@media(max-width:820px){.fl{grid-template-columns:1fr;gap:20px;padding:22px}}
.phero{background:var(--navy);color:var(--navy-ink)}
.phero .wrap{padding-block:56px 48px}
.phero h1{color:#fff;font-size:clamp(34px,5vw,56px);max-width:18ch}
.phero p{color:#dfe3ec;max-width:60ch;margin-top:18px;font-size:17px}
.phero .eyebrow{color:var(--gold2)}
.phero .btn.ghost{color:#fff;border-color:rgba(255,255,255,.6)}
.pane .wrap{padding-block:4px 36px}
.phero .price{margin-top:22px;font-family:var(--display);font-size:28px;color:var(--gold2);font-weight:600}
.phero.split .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:end;padding-block:24px 0}
.phero.split .copy{align-self:center;padding-block:16px 40px}
.phero.split .pic img{width:100%;height:auto;max-width:100%;display:block;border-radius:10px 10px 0 0;object-fit:cover;aspect-ratio:5/4;}
.phero.split .pic{overflow:hidden;border-radius:10px 10px 0 0}
@media(max-width:820px){.phero.split .wrap{grid-template-columns:1fr;gap:20px;padding-block:20px 36px}.phero.split .copy{padding-bottom:0}.phero.split .pic{order:-1}.phero.split .pic img{border-radius:10px;aspect-ratio:16/10}}
.phero.split.abouthero .pic img{aspect-ratio:6/5;object-position:50% 0%;transform:scale(1.06);transform-origin:50% 0}
.phero.photo{position:relative;min-height:440px;display:grid;align-items:center}
.phero.photo::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(13,26,51,.88) 0%,rgba(13,26,51,.7) 50%,rgba(13,26,51,.25) 100%)}
.phero.photo .wrap{position:relative;z-index:1}
.phero.photo h1,.phero.photo p{text-shadow:0 2px 8px rgba(0,0,0,.35)}
.phero .price small{font-family:var(--body);font-size:14px;color:#c9cedb;font-weight:400}
.tabs{position:sticky;top:calc(env(safe-area-inset-top,0px) + 61px);z-index:15;background:var(--bg);border-bottom:1px solid var(--rule)}
.tabs .wrap{display:flex;gap:0}
.tabs button{appearance:none;background:none;border:0;border-bottom:3px solid transparent;padding:16px 22px 14px;font:600 15px var(--body);color:var(--quiet);cursor:pointer;letter-spacing:.04em;text-transform:uppercase}
.tabs button[aria-selected="true"]{color:var(--navy);border-bottom-color:var(--gold)}
.pane[hidden]{display:none}
.sec{padding-block:40px;border-bottom:1px solid var(--rule)}
.sec:last-child{border-bottom:0}
.sec h2{font-size:clamp(32px,4.2vw,50px)}
.sec .lead{margin-top:16px;font-size:18px}
.items{display:grid;grid-template-columns:repeat(2,1fr);gap:22px 36px;margin-top:30px}
.item{display:grid;grid-template-columns:44px 1fr;gap:14px;padding-top:16px;border-top:1px solid var(--rule)}
.item .num{font-family:var(--display);font-size:26px;color:var(--gold);font-weight:500;line-height:1}
.item b{font-family:var(--display);font-size:20px;color:var(--navy);font-weight:600;display:block;margin-bottom:4px}
.item p{font-size:16px;max-width:none;margin:0}
.rhythm{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:30px}
.rhythm div{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:20px}
.rhythm b{display:block;font-family:var(--display);font-size:19px;color:var(--navy);margin-bottom:8px}
.rhythm p{font-size:16px;max-width:none;margin:0}
.check{list-style:none;padding:0;margin:20px 0 0;display:grid;gap:10px}
.check li{padding-left:28px;position:relative;font-size:17px}
.check li::before{content:"";position:absolute;left:0;top:9px;width:14px;height:14px;border-radius:50%;background:var(--gold)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start}
.two img{width:100%;height:auto;border-radius:8px;object-fit:cover;aspect-ratio:4/3;max-width:100%}
.qa{display:grid;gap:14px;margin-top:24px}
.qa div{display:grid;grid-template-columns:1fr 1.4fr;gap:20px;padding-top:14px;border-top:1px solid var(--rule)}
.qa i{font-family:var(--display);font-size:18px;color:var(--navy)}
.qa p{font-size:15.5px;max-width:none;margin:0}
.pay{display:grid;grid-template-columns:1.2fr .8fr;gap:40px;align-items:start}
.paycard{background:var(--surface);border:1px solid var(--rule);border-top:5px solid var(--gold);border-radius:10px;padding:32px}
.paycard .big{font-family:var(--display);font-size:46px;color:var(--navy);font-weight:600;line-height:1}
.paycard .big small{font-family:var(--body);font-size:15px;color:var(--quiet);font-weight:400;display:block;margin-top:8px}
.paycard .btn{display:block;text-align:center;margin-top:24px}
.paycard .fine{font-size:13px;color:var(--quiet);margin-top:14px;max-width:none}
.guar{margin-top:28px;background:var(--navy);color:var(--navy-ink);padding:26px 28px;border-radius:8px}
.guar b{color:var(--gold2);font-family:var(--display);font-size:22px;display:block;margin-bottom:8px}
.guar p{color:#dfe3ec;font-size:15.5px;max-width:none;margin:0 0 8px}
.steps{counter-reset:s;list-style:none;padding:0;margin:20px 0 0;display:grid;gap:14px}
.steps li{counter-increment:s;padding-left:46px;position:relative;font-size:16px}
.steps li::before{content:counter(s);position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;background:var(--gold);color:#fff;font-weight:700;display:grid;place-items:center;font-size:14px}
.booklist{display:grid;grid-template-columns:repeat(2,1fr);gap:32px;margin-top:30px}
.bk{display:grid;grid-template-columns:150px 1fr;gap:22px;align-items:start}
.bk img{width:100%;height:auto;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,.18);max-width:100%}
.bk b{font-family:var(--display);font-size:22px;color:var(--navy);display:block;margin-bottom:6px}
.bk p{font-size:15.5px;max-width:none;margin:0 0 12px}
.letter{background:var(--surface);border:1px solid var(--rule);border-left:5px solid var(--gold);border-radius:8px;padding:30px 34px;margin-top:28px}
.letter p{max-width:none;font-size:17px}
.letter .sig{font-family:var(--display);font-size:20px;color:var(--navy);margin-top:18px}
.letter .sig small{display:block;font-family:var(--body);font-size:13px;color:var(--quiet);margin-top:4px}
.qlist{list-style:none;margin:24px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:0 36px}
.qlist li{display:grid;grid-template-columns:40px 1fr;gap:12px;padding:9px 0;border-top:1px solid var(--rule);font-family:var(--display);font-style:italic;font-size:18px;line-height:1.3;color:var(--navy)}
.qlist li span{font-style:normal;font-family:var(--body);font-weight:700;font-size:13px;color:var(--gold);padding-top:6px}
.answer{margin-top:28px;padding:22px 26px;background:var(--navy);color:var(--navy-ink);border-radius:8px;font-size:17px}
.answer strong{color:var(--gold2);font-family:var(--display);font-size:22px;display:block;margin-bottom:6px;font-weight:600}
.chain{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:28px;counter-reset:c}
.chain div{counter-increment:c;background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:18px 14px 16px;position:relative}
.chain div::before{content:counter(c);display:block;width:30px;height:30px;border-radius:50%;background:var(--gold);color:#fff;font-weight:700;font-size:14px;display:grid;place-items:center;margin-bottom:10px}
.chain div::after{content:"→";position:absolute;right:-12px;top:22px;color:var(--gold);font-size:18px;font-weight:700}
.chain div:last-child::after{content:none}
.chain b{font-family:var(--display);font-size:17px;color:var(--navy);display:block;line-height:1.2}
.chain p{font-size:13.5px;max-width:none;margin:6px 0 0;color:var(--quiet)}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:28px}
.trio div{background:var(--surface);border-top:4px solid var(--gold);border:1px solid var(--rule);border-top:4px solid var(--gold);border-radius:8px;padding:22px}
.trio .ey{font-weight:700;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.trio b{font-family:var(--display);font-size:20px;color:var(--navy);display:block;margin:6px 0 8px}
.trio p{font-size:16px;max-width:none;margin:0}
.pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.pills span{border:1.5px solid var(--gold);color:var(--navy);border-radius:999px;padding:7px 16px;font-weight:600;font-size:14px}
.quoteband{margin-top:32px;background:var(--navy);color:#fff;border-radius:8px;padding:28px 32px}
.quoteband b{font-family:var(--display);font-size:26px;color:var(--gold2);display:block;font-weight:500}
.quoteband p{color:#dfe3ec;max-width:none;margin:10px 0 0;font-size:16px}
.cur{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:28px}
.cur div{text-align:left}
.cur img{width:100%;height:auto;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,.18);max-width:100%}
.cur b{font-family:var(--display);font-size:18px;color:var(--navy);display:block;margin-top:12px}
.cur i{display:block;font-style:normal;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:8px}
.cur p{font-size:14px;max-width:none;margin:4px 0 0}
.seats4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:26px}
.seats4 div{border-top:3px solid var(--gold);padding-top:12px}
.seats4 b{font-family:var(--display);font-size:18px;color:var(--navy);display:block;margin-bottom:4px}
.seats4 p{font-size:16px;max-width:none;margin:0}
.cmp{width:100%;border-collapse:collapse;margin-top:28px;font-size:16px}
.cmp th,.cmp td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--rule);vertical-align:top}
.cmp th{font-family:var(--display);font-size:18px;color:var(--navy);font-weight:600}
.cmp td:first-child{font-weight:600;color:var(--navy);width:30%}
.cmp tr.hl td{background:var(--card)}
.cmpwrap{overflow-x:auto}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:26px}
.g4 div{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:20px}
.g4 .num{font-family:var(--display);font-size:24px;color:var(--gold);line-height:1}
.g4 b{font-family:var(--display);font-size:18px;color:var(--navy);display:block;margin:8px 0 6px}
.g4 p{font-size:14px;max-width:none;margin:0}
@media(max-width:900px){.chain{grid-template-columns:1fr}.chain div::after{content:none}.trio,.cur,.seats4,.g4{grid-template-columns:1fr 1fr}.qlist{grid-template-columns:1fr}}
@media(max-width:560px){.trio,.cur,.seats4,.g4{grid-template-columns:1fr}}
footer .social{display:flex;gap:16px}
footer .social a{color:var(--navy);font-weight:600;text-decoration:none;border:1.5px solid var(--rule);border-radius:999px;padding:6px 14px;font-size:13px}
.sec .two p+p{margin-top:14px}
.back{display:inline-block;margin-top:10px;color:var(--gold);font-weight:600;text-decoration:none;font-size:14px}
@media(max-width:820px){.items,.two,.pay,.booklist,.qa div{grid-template-columns:1fr}.rhythm{grid-template-columns:1fr 1fr}.bk{grid-template-columns:110px 1fr}.tabs button{padding:14px 14px 12px;font-size:13px}}
"""

NAV = '''<nav><div class="wrap">
  <a href="index.html" class="brand"><img src="img/mark.png" alt="Play Golf In College"><span>Play Golf In College</span></a>
  <ul class="left">
    <li><a class="tab" href="index.html">Home</a></li>
    <li><a class="tab" href="about.html"><span class="full">About Coach Spar</span><span class="short">About</span></a></li>
    <li class="dd"><button class="tab" type="button" aria-haspopup="true" aria-expanded="false">Services <span class="car">&#9660;</span></button>
      <div class="menu">
        <a href="elite.html">Elite Performance Coaching<small>Weekly, hands-on, by application</small></a>
        <a href="advisory.html">Advisory Performance Coaching<small>Monthly guidance, by application</small></a>
        <a href="recruiting.html">College Recruiting<small>The recruiting process, run with me</small></a>
        <a href="teaching.html">Teaching<small>Weekly lessons, Central Ohio</small></a>
        <a href="international.html">International Families<small>Playing college golf in the US</small></a>
        <div class="sep"></div>
        <a href="foundations.html">Foundations<small>Year-long membership: all four books, scripts, templates, newsletter</small></a>
        <a href="books.html">Books<small>The four-book curriculum</small></a>
      </div></li>
    <li><a class="tab" href="pay.html">Pay</a></li>
    <li><a class="tab" href="testimonials.html">Testimonials</a></li>
  </ul>
  <ul class="right"><li><a href="apply.html" class="btn gold" style="padding:10px 18px;font-size:14px">Apply</a></li></ul>
</div></nav>'''

FOOT = '''<footer><div class="wrap">
  <a class="brand" href="index.html"><img src="img/mark.png" alt=""><span>Play Golf<br>In College</span></a>
  <div class="social"><a href="https://www.instagram.com/playgolfincollege" target="_blank" rel="noopener">Instagram @playgolfincollege</a><a href="https://x.com/playgolfcollege" target="_blank" rel="noopener">X @playgolfcollege</a></div>
  <div>Play Golf In College · Central Ohio · Est. 2009 · Questions first? Email me at <a href="mailto:coachsparling@gmail.com" style="color:inherit;font-weight:600">coachsparling@gmail.com</a></div>
</div></footer>
<script>
(function(){document.querySelectorAll('nav li.dd').forEach(function(li){var b=li.querySelector('.tab');b.addEventListener('click',function(e){e.stopPropagation();var o=li.classList.toggle('open');b.setAttribute('aria-expanded',o)});});document.addEventListener('click',function(){document.querySelectorAll('nav li.dd.open').forEach(function(li){li.classList.remove('open');li.querySelector('.tab').setAttribute('aria-expanded','false')})});})();
</script>
<script>
if('scrollRestoration' in history){history.scrollRestoration='manual'}
window.addEventListener('pageshow',function(){if(!location.hash){window.scrollTo(0,0)}});
</script>'''

HERO_ALT = {'international':'Coach Spar with his Duke golf team','foundations':'Coach Spar with a young junior golfer and his trophy','elite':'Coach Spar watching a player at a tournament','advisory':'A junior golfer hitting a tee shot','recruiting':'Coach Spar walking the course with a player','teaching':'Coach Spar congratulating a player','books':'Coach Spar holding his books Becoming Elite and Start Here'}
HERO_IMG = {'international':'img/duke.jpg 60% 30%','foundations':'img/young.jpg 50% 30%','elite':'img/watch.jpg 50% 30%','advisory':'img/swing.jpg 45% 40%','recruiting':'img/shake.jpg 50% 20%','teaching':'img/arm.jpg 50% 15%','books':'img/books-brad.jpg 50% 62%'}

def page(fname, title, eyebrow, h1, sub, price, program_html, pay_html, tab1='The program', after_btns=''):
    hi = HERO_IMG.get(fname)
    img_src = hi.split()[0] if hi else ''
    img_pos = ' '.join(hi.split()[1:]) if hi else '50% 30%'
    out = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)} · Play Golf In College</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Public+Sans:wght@400;600;700&display=swap">
<style>{CSS}{EXTRA}</style>{VAQ}<script defer src="/_vercel/insights/script.js"></script></head><body>
{NAV}
<header class="phero split"><div class="wrap"><div class="copy">
  <div class="eyebrow">{eyebrow}</div>
  <h1 style="margin-top:14px">{h1}</h1>
  {sub if sub.startswith("<p") else "<p>"+sub+"</p>"}
  {('<div class="price">'+price+'</div>') if price else ''}
  <div class="btns">{'' if fname=='books' else ('<a class="btn gold" href="https://www.lighthousegolfparent.com" target="_blank" rel="noopener">Join Foundations</a>' if fname=='foundations' else '<a class="btn gold" href="apply.html">Apply</a>')}<a class="btn ghost" href="index.html">&larr; Back to home</a></div>{after_btns}
</div><div class="pic"><img src="{img_src}" alt="{HERO_ALT.get(fname,'')}" style="object-position:{img_pos}"></div></div></header>
<section class="pane" id="program"><div class="wrap">{program_html}</div></section>
{FOOT}
</body></html>'''
    open(os.path.join(ROOT,f'{fname}.html'),'w').write(out)

def items(rows):
    return '<div class="items">' + ''.join(f'<div class="item"><div class="num">{i+1:02d}</div><div><b>{t}</b><p>{d}</p></div></div>' for i,(t,d) in enumerate(rows)) + '</div>'
def check(rows): return '<ul class="check">' + ''.join(f'<li>{r}</li>' for r in rows) + '</ul>'
def rhythm(rows): return '<div class="rhythm">' + ''.join(f'<div><b>{t}</b><p>{d}</p></div>' for t,d in rows) + '</div>'
def sec(h2, body, eyebrow=None):
    return f'<div class="sec">{("<div class=eyebrow>"+eyebrow+"</div>") if eyebrow else ""}<h2 style="margin-top:10px">{h2}</h2>{body}</div>'

GUAR = '''<div class="guar"><b>Do the work. Get better. Guaranteed.</b>
<p><strong>30-Day Promise.</strong> If the first 30 days aren't what I promised, you get a full refund. No questions asked.</p>
<p><strong>Performance Promise.</strong> Follow the plan for 12 months. If your family doesn't see measurable improvement in practice, scoring, clarity and the family environment, I'll coach you for another year, free. Full terms in the client agreement.</p></div>'''

def paycard(price, per, button, fine, steps):
    return f'''<div class="pay"><div>
<h2>How to get started</h2>
<ol class="steps">{''.join(f'<li>{s}</li>' for s in steps)}</ol>
{GUAR if 'Performance' in button or 'Elite' in button or 'Advisory' in button else ''}
</div>
<div class="paycard"><div class="big">{price}<small>{per}</small></div>
<a class="btn gold" href="#">{button}</a>
<p class="fine">{fine}</p></div></div>'''

ROADMAP = sec('The Family Golf Roadmap', '''<p class="lead">Most junior golf stress comes from unspoken expectations. Once a year, the player, the parents and I sit down and put everything on the table, so everyone knows the goal, their role, the standard and how we will keep score.</p>''' + items([
 ('Goals','Season and long-term goals for performance, development and college. Clear, measurable, and owned by the player.'),
 ('Responsibilities','Who owns what: the player, the parents, the swing coach and me. No overlap, no gaps, and no parent doing the player\'s job.'),
 ('Standards','What we expect in practice, in tournaments, in the classroom and in conduct. Standards we agree on, not rules handed down.'),
 ('Accountability','How progress is measured and reviewed through the year, and what happens when a standard slips. The data keeps everyone honest.')]) + '''
<p style="margin-top:28px">Every family starts with an honest evaluation of the player and the parents: where are we today, what do great players and parents do, what is the gap, what strengths to do more of, and what habits to do less of. The result is a written 12-month plan, coordinated with your swing coach and anchored by baseline tournament statistics, so we measure progress from day one.</p>''', 'Where it starts')

LAB = sec('Practice you can measure.', '''<div class="two"><div><p class="lead">Most junior golfers practice hard and still can't tell you whether they are getting better. The PGIC Practice Lab is my proprietary app. It measures two practice sessions a week and adjusts the plan over time to meet the real needs of your player.</p>''' + check([
 '<b>Improve.</b> Every session has a plan built around your player\'s game. No more beating balls or practicing only what already feels good.',
 '<b>Measure.</b> Every session is tracked, so improvement shows up in the numbers, not in guesswork.',
 '<b>Connect.</b> Practice data is compared with tournament results to find the skills that look fine on the range but leak strokes when it counts.',
 '<b>Separation Value.</b> Practice time goes where improvement is possible and where it saves strokes. That is where the gap to the next level gets closed.']) + '</div><img src="img/phone.jpg" alt="Reviewing Practice Lab data with a player"></div>', 'PGIC Practice Lab')

MENTAL = sec('Why your player can\'t take their game to tournaments.', '''<p class="lead">It's rarely the swing. Under pressure, players fall back on how they practiced, how they think, how they slept and what they heard on the car ride over. Great players have a process that holds up when it counts. Every shot hit without one costs strokes, and most players never know how many, because nobody measures it. We do.</p>''' + items([
 ('Identify','A mental scorecard, tracked in practice and tied to tournament play, shows which parts of the process hold up and which break down.'),
 ('Understand','We name the strengths to lean on and the weaknesses that cost strokes: a rushed routine, half-committed swings, one bad shot turning into three.'),
 ('Improve','Targeted routines, pressure practice and post-round reflection train the mental game like any other skill.'),
 ('Compete with a plan','A tournament schedule built for development and recruiting, a prep plan for each event, course strategy from your player\'s own patterns, and a post-event review.')]), 'Mental game and tournaments')


LETTER = sec('Every family deserves a plan.', """<div class="letter"><p>I've spent 25 years in junior and college golf: as a college coach, a high school coach, a recruiting advisor, a junior golf development expert, and a dad. I've also written four books on it.</p>
<p>Every role taught me the same thing. Talented players and loving parents struggle when there's no plan, and they thrive when there is one.</p>
<p>This program is everything I've learned, put together so your family can enjoy the journey, worry less, and give your player the best chance to reach their goals.</p>
<div class="sig">Brad "Spar" Sparling<small>Founder, Play Golf In College · Head Boys Golf Coach, Dublin Jerome High School · Former Division I coach, Duke and Ohio State</small></div></div>""", 'Why I do this')

QUESTIONS = ["My kid gets so frustrated on the course, and I don't know how to help.", 'When I offer advice I know is right, they get angry and defensive.', 'Am I doing this right as a parent?', 'Is my player good enough?', 'What do we do about recruiting?', 'Are they practicing correctly, and how would I know?', 'Why do they play great at home, but not in tournaments?', 'Is our tournament schedule right, and are we spending money wisely?']

CURRICULUM = sec('25 years, distilled into four books.', """<p class="lead">This program isn't a collection of opinions. It's 25 years of playing, teaching and coaching golf, distilled into four books. They are the foundation of everything we do.</p><div class="cur">
<div><img src="img/becoming.jpg" alt="Becoming Elite"><b>Becoming Elite</b><i>In the program</i><p>The weekly summary chapter your player works through every week.</p></div>
<div><img src="img/lighthouse.jpg" alt="The Lighthouse Golf Parent"><b>The Lighthouse Golf Parent</b><i>In the program</i><p>The foundation of parent guidance and the Family Golf Roadmap.</p></div>
<div><img src="img/starthere.jpg" alt="Start Here"><b>Start Here</b><i>In the program</i><p>The starting point for every family, so the common mistakes are avoided from day one.</p></div>
<div><img src="img/bep.jpg" alt="Building Elite Programs"><b>Building Elite Programs</b><i>In the program</i><p>The culture, standards and accountability behind a #1 nationally ranked team, applied to your family.</p></div>
</div>""", 'The curriculum')

SEATS = sec("I've seen junior golf from every seat.", """<div class="seats4">
<div><b>The parent</b><p>Raised three Division I golfers.</p></div>
<div><b>High school coach</b><p>Head coach of Dublin Jerome: back-to-back state champions (2025, 2026) and #1 team in the nation.</p></div>
<div><b>College coach</b><p>Two NCAA Championships at Duke. Top 5 recruiting classes at Duke and Ohio State.</p></div>
<div><b>Recruiting expert</b><p>17 years with Play Golf In College. 165 players placed in college golf.</p></div>
</div><p style="margin-top:22px">For 25 years I've worked only with junior golfers and their families, and I've written four books on how to do it right.</p>""", 'Who is running the plan')

GUAR_SEC = sec('Do the work. Get better. Guaranteed.', """<div class="two"><div><p class="lead"><b>30-Day Promise.</b> If the first 30 days aren't what I promised, you get a full refund. No questions asked.</p><p class="lead"><b>Performance Promise.</b> Follow the plan for 12 months. If your family doesn't see measurable improvement in all four areas, I'll coach you for another year, free.</p><p style="color:var(--quiet);font-size:14px">The plan: Practice Lab twice a week, the check-ins, tournament rounds tracked and Becoming Elite chapters completed. Measured against the baseline from your initial evaluation and a family survey at the start and end of the year. Full terms in the client agreement.</p></div>
<div class="g4" style="grid-template-columns:1fr 1fr;margin-top:0">
<div><div class="num">01</div><b>Better practice</b><p>Higher Practice Lab benchmark scores and a stronger mental scorecard than at the start.</p></div>
<div><div class="num">02</div><b>Lower scores</b><p>A lower tournament scoring differential against course rating than the starting baseline.</p></div>
<div><div class="num">03</div><b>A clear path</b><p>You know where your player stands, what comes next and why.</p></div>
<div><div class="num">04</div><b>A better family environment</b><p>Less pressure, better conversations about golf, and a home where your player can compete freely.</p></div>
</div></div>""", 'The PGIC guarantee')

GUAR_SHORT = sec('Do the work. Get better. Guaranteed.', """<div class="two"><div><p class="lead"><b>30-Day Promise.</b> If the first 30 days aren't what I promised, you get a full refund. No questions asked.</p></div><div><p class="lead"><b>Performance Promise.</b> Follow the plan for 12 months. If your family doesn't see measurable improvement in practice, scoring, clarity and the family environment, I'll coach you for another year, free.</p></div></div>""", 'The PGIC guarantee')

def compare(which):
    rows = [
      ('Contact with Coach Spar','Weekly one-on-one with the player','Monthly call with player and parents'),
      ('Who runs the week','I do. I review Practice Lab data every week and set the next week\'s plan.','You do. Practice Lab adjusts the plan; I review the trend with you monthly.'),
      ('Tournament prep and mental game','Yes, planned with me event by event','Yes, using the framework and templates'),
      ('College recruiting','I run it with you: list, outreach, tracking, decisions','Recruiting roadmap and templates; you run it'),
      ('Foundations membership','Included','Included'),
      ('Parent guidance and reporting','Lighthouse Golf Parent guidance; Coach Dashboard report every two weeks','Lighthouse Golf Parent guidance; Coach Dashboard report monthly'),
    ]
    hl = 1 if which=='Elite' else 2
    body = '<div class="cmpwrap"><table class="cmp"><tr><th></th><th>Elite</th><th>Advisory</th></tr>' + ''.join(f'<tr><td>{a}</td><td{" style=font-weight:600" if hl==1 else ""}>{b}</td><td{" style=font-weight:600" if hl==2 else ""}>{c}</td></tr>' for a,b,c in rows) + '</table></div>'
    other = 'advisory' if which=='Elite' else 'elite'
    return sec('Elite or Advisory?', '<p class="lead">Same Roadmap, same evaluation and plan, same Practice Lab and curriculum, same guarantee. The difference is how hands-on I am week to week.</p>' + body + f'<p style="margin-top:20px"><a class="back" href="{other}.html">See {other.capitalize()} &rarr;</a></p>', 'Which program')

CAP = {'elite': '10 Elite', 'advisory': '20 Advisory'}
PERF_QUESTIONS = ['Am I doing this right as a parent?', 'Is my player good enough?', 'Why do they play great at home, but not in tournaments?', 'Is our tournament schedule right, and are we spending money wisely?', 'Is their swing coach enough to get them to the next level?', 'How do I stay involved without becoming the pressure?', 'Coaches aren\'t responding. What should we do?', 'Do they need a mental coach, a trainer, or both?']
PERF_QUOTE = {'elite': ('He will help your child realize his or her dream of playing golf in college.', 'Dan Brooks', 'Head Women\'s Golf Coach, Duke University · Seven-Time National Champion Coach · NGCA Hall of Fame'),
  'advisory': ('Coach Spar has been a great mentor and has helped me develop as a player and person. There is no one better when it comes to developing players to the Division I level and beyond.', 'Brady Barnum', 'Two-Time OHSAA Individual State Champion · Junior Presidents Cup Team · University of Georgia')}
def ggroups(groups):
    out=''; n=0
    for title, rows in groups:
        cells=''
        for t_,d_ in rows:
            n+=1; cells+=f'<div class="item"><div class="num">{n:02d}</div><div><b>{t_}</b><p>{d_}</p></div></div>'
        out+=f'<div class="ggroup"><h3>{title}</h3><div class="items">{cells}</div></div>'
    return out

def perf_page(fname, name, price, intro, tab3, recruiting_item, report_item, rhythm_rows, notinc, answers, steps, fine, lab_measure, pressure_review):
    prog_intro = sec('Most families don\'t have anyone running the plan.', """<p class="lead">Most families build junior golf piece by piece: a swing coach here, a trainer there, a schedule borrowed from other parents. Nobody owns the whole plan, so the parent ends up in charge by default.</p>
<h3 style="margin-top:36px;font-size:22px">The questions every golf parent asks</h3>
<ul class="qlist">""" + ''.join(f'<li><span>{i+1:02d}</span>"{q}"</li>' for i,q in enumerate(PERF_QUESTIONS)) + """</ul>
<p style="margin-top:18px">You're not doing anything wrong. You've been handed a job nobody should do alone.</p>""", 'The biggest mistake in junior golf')
    answer = sec('The missing piece: a Performance Director.', f"""<p class="lead">Think of me as the head coach of your player's junior golf journey. One plan for development, practice, tournaments, the mental game, recruiting and the golf parent, with everyone on the team pulling the same way. {intro}</p>""", 'The answer')
    glance = sec('The 80% the swing coach doesn\'t cover.', items([
      ('Family Golf Roadmap','Goals, responsibilities, standards and accountability, set together every year.'),
      ('Evaluation & Plan','Where your player stands today and the plan for the next 12 months.'),
      tab3,
      ('Becoming Elite Weekly','A summary chapter from <i>Becoming Elite</i> every week: the curriculum behind the program.'),
      ('PGIC Practice Lab','My proprietary app. It measures two practice sessions a week and adjusts the plan to your player\'s real needs.'),
      ('Tournament Play','Scheduling, event prep, course strategy and post-event review.'),
      ('Mental Game','Identify mental strengths and weaknesses, then train them like any other skill.'),
      ('Athlete Development','Guidance on sleep, nutrition, hydration, and strength and speed training.'),
      recruiting_item, report_item, ('Foundations Membership','A year of Lighthouse Golf Parent is included: all four books, the 10 Pillars, the scripts and templates, the Parent Assessment and the members newsletter.')]) + '<h3 style="margin-top:40px;font-size:24px">The rhythm</h3>' + rhythm(rhythm_rows) + f'<p class="notinc">{notinc}</p>', 'The program at a glance')
    roadmap = sec('The Family Golf Roadmap', """<p class="lead">Most junior golf stress comes from unspoken expectations. Once a year, the player, the parents and I sit down and put everything on the table, so everyone knows the goal, their role, the standard and how we will keep score.</p>""" + items([
      ('Goals','Season and long-term goals for performance, development and college. Clear, measurable, and owned by the player.'),
      ('Responsibilities','Who owns what: the player, the parents, the swing coach and me. No overlap, no gaps, and no parent doing the player\'s job.'),
      ('Standards','What we expect in practice, in tournaments, in the classroom and in conduct. Standards we agree on, not rules handed down.'),
      ('Accountability','How progress is measured and reviewed through the year, and what happens when a standard slips. The data keeps everyone honest.')]) + """
<h3 style="margin-top:40px;font-size:24px">Initial evaluation and plan</h3>
<p>Every family starts with an honest evaluation of the player and the parents, built on a five-step framework:</p>
<div class="chain">
<div><b>Where are we today?</b></div><div><b>What do great players and parents do?</b></div><div><b>What is the gap?</b></div><div><b>Strengths to do more of</b></div><div><b>Habits to do less of</b></div>
</div>
<p style="margin-top:22px">The result is a written 12-month plan, coordinated with your swing coach and anchored by baseline tournament statistics, so we measure progress from day one.</p>
<div class="quoteband"><b>"Be the lighthouse, not a tugboat."</b><p>Parents don't need to push their player through junior golf. They need to be the steady light the player steers by. The Family Golf Roadmap is where that starts.</p></div>""", 'Where it starts')
    lab = sec('Practice you can measure.', f"""<div class="two"><div><p class="lead">Most junior golfers practice hard and still can't tell you whether they are getting better. The PGIC Practice Lab is my proprietary app. It measures two practice sessions a week and adjusts the plan over time to meet the real needs of your player. All other practice and play is planned alongside their swing coach.</p></div><img src="img/phone.jpg" alt="Reviewing Practice Lab data with a player"></div>
<div class="trio">
<div><div class="ey">Improve</div><b>Practice with purpose</b><p>Every Practice Lab session has a plan built around your player's game. No more winging it, beating balls, or only practicing what already feels good.</p></div>
<div><div class="ey">Measure</div><b>Progress in black and white</b><p>Every session is tracked, so improvement (or the lack of it) shows up in the numbers, not in guesswork. {lab_measure}</p></div>
<div><div class="ey">Connect</div><b>Practice vs. tournaments</b><p>Practice data is compared with tournament results to find the gaps: the skills that look fine on the range but leak strokes when it counts.</p></div>
</div>
<div class="two" style="margin-top:36px"><div><h3 style="font-size:22px">Separation Value</h3><p>Not all practice is equal. Separation Value means spending practice time where improvement is actually possible and where it actually saves strokes. That is where the gap between your player and the next level gets closed.</p></div>
<div><h3 style="font-size:22px">The basics of every practice</h3>""" + check(['<b>Have a plan.</b> Don\'t just do what you feel like or what you\'re already good at.','<b>Practice where it saves shots.</b> Work the areas with the most Separation Value.','<b>Make every shot important.</b> Every rep has a routine and a consequence.','<b>Train in focused blocks.</b> Short, intense sessions build skill faster.','<b>Reflect afterward.</b> What went well, what you learned, what to improve.','<b>Keep a growth mindset.</b> Get a little better every practice.']) + """</div></div>
<div class="answer" style="margin-top:32px"><strong>The outcome</strong>Better practice habits, faster improvement, and a player who knows exactly what to work on and why. Parents finally get a real answer to "Are they practicing correctly?"</div>""", 'PGIC Practice Lab')
    mental = sec("Why your player can't take their game to tournaments.", f"""<p class="lead">It's rarely the swing. Under pressure, players fall back on how they practiced, how they think, how they slept and what they heard on the car ride over. Great players have a process that holds up when it counts. Every shot hit without one costs strokes, and most players never know how many, because nobody measures it. We do.</p>
<div class="chain">
<div><b>Routine</b><p>Same steps, every shot.</p></div><div><b>Commitment</b><p>One club, one shot, one decision.</p></div><div><b>Visualization</b><p>See it before you hit it.</p></div><div><b>Trust</b><p>Let the practice do its job.</p></div><div><b>Acceptance</b><p>The shot is over. Next.</p></div>
</div>
<div class="trio">
<div><div class="ey">Identify</div><b>The mental scorecard</b><p>Tracked in practice and tied to tournament play, showing which parts of the process hold up and which break down, and in which part of the game.</p></div>
<div><div class="ey">Understand</div><b>Name what costs strokes</b><p>The strengths to lean on and the weaknesses that cost strokes, whether that's a rushed routine, half-committed swings, or one bad shot turning into three.</p></div>
<div><div class="ey">Improve</div><b>Train it like a skill</b><p>Targeted routines, pressure practice and post-round reflection train the mental game like any other skill, and the scorecard shows whether it's working.</p></div>
</div>
<div class="two" style="margin-top:36px"><div><div class="eyebrow">Tournament performance</div><h3 style="font-size:22px;margin-top:8px">Compete with a plan</h3>""" + check(['A tournament schedule built for development and recruiting','A prep plan for each event, with pressure practice two days out and light practice the day before','Course strategy for key events, built from your player\'s own patterns','Smart course management: keep it in play, avoid penalties, never trouble to trouble', pressure_review]) + """</div>
<div><div class="eyebrow">Athlete development</div><h3 style="font-size:22px;margin-top:8px">Train the athlete, not just the golfer</h3><p>The best junior golfers are athletes. Your player gets guidance on the habits that support performance and recovery.</p><div class="pills"><span>Sleep</span><span>Nutrition</span><span>Hydration</span><span>Strength &amp; speed</span></div></div></div>
<div class="answer" style="margin-top:32px"><strong>The point of all of it</strong>When every performance factor is covered, golf gets more fun, and players finally play like themselves.</div>""", 'Mental game')
    rec_par = sec('Recruiting and the golf parent.', """<div class="two"><div><div class="eyebrow">College recruiting</div><h3 style="font-size:22px;margin-top:8px">165 players placed. 3 were my own kids.</h3><p>I have been on both sides of recruiting: as a college coach at Duke and Ohio State who recruited Top 5 classes, and as a dad who walked all three of his kids into Division I golf.</p>""" + check(REC_LIST[fname]) + """</div>
<div><div class="eyebrow">Parent guidance</div><h3 style="font-size:22px;margin-top:8px">Guidance for the golf parent.</h3><p>Parents are the most important and least coached people in junior golf. Through Lighthouse Golf Parent, you get the framework, the tools and the perspective to support your player without adding pressure.</p>""" + check(PAR_LIST[fname]) + '</div></div>', 'The other two jobs')
    who = sec('A select program for a limited number of families.', check([
      '<b>Middle school golfers</b> who love the game but aren\'t elite yet. The best time to start a plan.',
      '<b>High school golfers</b> who want to play college golf and are willing to be held to a standard.',
      '<b>Families who already have a swing coach,</b> or who want help building the right team.',
      '<b>Parents who want a plan,</b> a guide, and the confidence that they\'re helping, not hovering.']) + f'<p style="margin-top:22px"><b>Limited to {CAP[fname]} families a year, from anywhere.</b> By application only, so every player gets my personal attention.</p>', 'Who it\'s for')
    q_, qn_, qr_ = PERF_QUOTE[fname]
    cta = f'<div class="sec"><div class="pq" style="margin:0 0 26px"><p>&ldquo;{q_}&rdquo;</p><span><b>{qn_}</b>, {qr_}</span></div>' + '<div class="answer" style="margin-top:0;padding:30px"><strong>Apply confidentially.</strong>' + name + ' Performance Coaching is limited to ' + CAP[fname].split()[0] + ' families a year, from anywhere. Tell me about your player and your family in a short, confidential application. I review every one personally and will be in touch about next steps.<div class="btns" style="margin-top:18px"><a class="btn gold" href="apply.html">Apply for ' + name + '</a></div></div></div></div>'
    pay = paycard(price, 'per year · by application', f'Pay for {name}', fine, steps)
    h1_ = 'I run your player\'s plan. Every week, all year.' if name=='Elite' else 'You run the plan. I make sure it\'s the right one.'
    extras = '<a class="pguar" href="#guarantee"><span aria-hidden="true">&#10003;</span>Do the work. Get better. Guaranteed.</a><ul class="proofrow"><li><b>2</b>NCAA titles</li><li><b>2</b>state titles</li><li><b>165+</b>in college golf</li><li><b>95%+</b>earned offers</li><li><b>3 of 3</b>my kids played D1</li></ul>'
    page(fname, f'{name} Performance Coaching', f'{name} Performance Coaching &middot; {CAP[fname].split()[0]} families a year', h1_, '<p class="outcomes">Your player gets better. Your family has more fun and less stress. You find the right college.</p>', '', prog_intro+answer+glance+compare(name)+GUAR_SHORT+who+cta, pay, after_btns=extras)

REC_LIST = {
 'elite': ['A school list matched to your player\'s level, academics and goals','Coach outreach that gets answered, with letter and résumé templates','A running log of every contact and every response','A timeline that starts in 9th grade, so there\'s no panic junior year','Help evaluating visits, offers and the final decision'],
 'advisory': ['The 9th-to-12th grade recruiting roadmap, step by step','Letter, résumé and video guidelines, with templates','A contact log you keep, reviewed at the monthly check-in','A timeline that starts in 9th grade, so there\'s no panic junior year','Guidance on visits, offers and the final decision at the monthly check-in'],
}
PAR_LIST = {
 'elite': ['Lighthouse Golf Parent guidance and the 10 Pillars of Effective Golf Parenting','A Coach Dashboard report every two weeks: tournament stats, practice data and recruiting progress','A clear picture of what\'s next, so you always know where things stand'],
 'advisory': ['Lighthouse Golf Parent guidance and the 10 Pillars of Effective Golf Parenting','A Coach Dashboard report every month: tournament stats, practice data and recruiting progress','A monthly call where you and your player review the plan with me and set the next month'],
}

perf_page('elite','Elite','$10,500',
 'In Elite, I run it: weekly contact with your player, every Practice Lab session reviewed, recruiting done together, a report to you every two weeks.',
 ('Weekly Player Contact','A one-on-one check-in with your player every week.'),
 ('College Recruiting','School list, coach outreach, contact tracking and decision support, run with you.'),
 ('Parent Guidance & Reporting','Lighthouse Golf Parent guidance, plus a progress report through the Coach Dashboard every two weeks.'),
 [('Every week','One-on-one player contact, a Becoming Elite chapter, Practice Lab review and plan.'),('Twice a week','Practice Lab sessions, measured and tracked.'),('Every two weeks','Coach Dashboard report to parents.'),('Every year','Family Golf Roadmap, set and reset.')],
 '<b>Your swing coach keeps the swing.</b> I handle the 80% around it, so every hour of their work counts more.',
 [('Am I doing this right as a parent?','The Family Golf Roadmap, Lighthouse Golf Parent coaching, and a clear split of who is responsible for what.'),
  ('Is my player good enough?','An honest initial evaluation against what great players actually do, and a plan to close the gap.'),
  ('What do we do about recruiting?','A plan that starts in 9th grade, guided by someone who has recruited Top 5 classes and placed 165 players.'),
  ('Are they practicing correctly, and how would I know?','A comprehensive and strategic practice plan, including two measured Practice Labs a week.'),
  ('Are they actually getting better?','Data from practice and tournaments, analyzed every week and reported to the player weekly and parents every two weeks.'),
  ('Why do they play great at home, but not in tournaments?','Mental game training, pressure practice and tournament prep, tracked with a mental scorecard.')],
 ['<b>Apply.</b> A short, confidential application about your player and your family. I read every one personally and reply within two working days.',
  '<b>Talk.</b> A call with the parents, and usually the player, to make sure Elite is the right fit.',
  '<b>Accept and pay.</b> Once accepted, you\'ll receive the client agreement. Payment of $10,500 is due on acceptance and covers 12 months.',
  '<b>Start.</b> Player and parent pre-work, the Family Golf Roadmap meeting, the initial evaluation, and your first Practice Lab, all inside the first 30 days.'],
 'Elite is limited to 10 families a year and is by application. Use this button once you\'ve been accepted. Payment covers 12 months of coaching and is backed by the 30-Day Promise and the Performance Promise.',
 'Each week I review the results and adjust the next week\'s plan.',
 'A post-event review with me comparing tournament stats with practice data')

perf_page('advisory','Advisory','$4,000',
 'Advisory is the same plan, tools and curriculum, run by your family, with a monthly check-in and report from me.',
 ('Monthly Check-In','A one-on-one call with your player and you every month to review progress and set the plan.'),
 ('Recruiting Roadmap','The 9th-to-12th grade plan, templates and guidelines to run recruiting yourselves.'),
 ('Parent Guidance & Reporting','Lighthouse Golf Parent guidance, plus a monthly progress report through the Coach Dashboard.'),
 [('Every month','One-on-one check-in, plan review, Coach Dashboard report.'),('Every week','A Becoming Elite chapter, Practice Lab review and plan.'),('Twice a week','Practice Lab sessions, measured and tracked.'),('Every year','Family Golf Roadmap, set and reset.')],
 '<b>Your swing coach keeps the swing.</b> I handle the 80% around it, so every hour of their work counts more. In Advisory you run recruiting with my roadmap; in Elite I run it with you.',
 [('Am I doing this right as a parent?','The Family Golf Roadmap, Lighthouse Golf Parent coaching, and a clear split of who is responsible for what.'),
  ('Is my player good enough?','An honest initial evaluation against what great players actually do, and a plan to close the gap.'),
  ('What do we do about recruiting?','A recruiting roadmap from 9th grade, with the structure, templates and guidelines to run it yourselves.'),
  ('Are they practicing correctly, and how would I know?','A comprehensive and strategic practice plan, including two measured Practice Labs a week.'),
  ('Are they actually getting better?','Data from practice and tournaments, reviewed every week by Practice Lab and every month with me.'),
  ('Why do they play great at home, but not in tournaments?','Mental game training, pressure practice and tournament prep, tracked with a mental scorecard.')],
 ['<b>Apply.</b> A short, confidential application about your player and your family. I reply within two working days.',
  '<b>Talk.</b> A call to make sure Advisory is the right fit, or whether Elite would serve you better.',
  '<b>Accept and pay.</b> Once accepted, you\'ll receive the client agreement. Payment of $4,000 is due on acceptance and covers 12 months.',
  '<b>Start.</b> Pre-work, the Family Golf Roadmap meeting, the initial evaluation, and your first Practice Lab, all inside the first 30 days.'],
 'Advisory is limited to 20 families a year and is by application. Use this button once you\'ve been accepted. Payment covers 12 months and is backed by the 30-Day Promise and the Performance Promise.',
 'Practice Lab adjusts the next week\'s plan, and I review the trend with you every month.',
 'A post-event review using the framework, with your tournament stats and practice data compared at the monthly check-in')

# Recruiting
rec_prog = sec('165 players placed. 3 were my own kids.', '''<div class="two"><div><p class="lead">I have been on both sides of recruiting: as a college coach at Duke and Ohio State who received the emails and recruited Top 5 classes, and as a dad who walked all three of his kids into Division I golf. I know what gets a player noticed, what gets an email deleted, and what a coach is really asking when they call.</p>
<p>College Recruiting is the recruiting process, run with me, for families who have development covered and want the college search done right.</p></div><img src="img/duke.jpg" alt="Brad Sparling celebrating with his Duke team" style="aspect-ratio:4/3;object-position:50% 40%"></div>''', 'College recruiting')
rec_glance = sec('What we do together over 12 months.', items([
 ('Honest evaluation','Where your player really stands: scoring, stats, academics and how college coaches will see them. Which levels are realistic now, and which could be with work.'),
 ('School list','A list matched to your player\'s level, academics, goals and the kind of school they\'ll thrive at. Reach, match and safety, the way coaches think about it.'),
 ('Coach outreach','Letters, a golf résumé and a swing video that get answered. I review every message before it goes out.'),
 ('Contact log','A running log of every email, call, camp and visit, and every response, so nothing slips.'),
 ('Timeline','A plan from 9th grade through signing, built around the NCAA calendar, so there\'s no panic junior year.'),
 ('Tournament schedule','Events chosen for exposure and ranking, not just convenience.'),
 ('Visits and offers','How to prepare for visits, what to ask, how to read an offer, and how to compare them.'),
 ('The decision','Help weighing fit, money, academics and golf, and handling the conversations with coaches at the end.')]) + '<h3 style="margin-top:40px;font-size:24px">The rhythm</h3>' + rhythm([('Monthly','A recruiting call with the player and parents.'),('As needed','Review of every email and message before it goes to a coach.'),('Each season','Schedule and target-list update.'),('Signing','Guidance through visits, offers and the final decision.')]), 'The program')
rec_who = sec('Who it\'s for', check(['<b>High school golfers</b> who want to play college golf at any level, Division I to Division III and NAIA.','<b>Families starting in 9th or 10th grade.</b> Earlier is better, and it\'s rarely too late.','<b>Players who already have a development plan</b> and a swing coach, and want the recruiting piece handled by someone who has done it 165 times.']) + '<p style="margin-top:22px">If you also want the development plan, Practice Lab and weekly coaching, look at Elite, which includes recruiting.</p>')

rec_cta = '<div class="sec"><div class="answer" style="margin-top:0;padding:30px"><strong>Ready to start, or have a question?</strong>Apply and tell me about your player, or email me directly at coachsparling@gmail.com. I reply within two working days.<div class="btns" style="margin-top:18px"><a class="btn gold" href="apply.html">Apply</a></div></div></div>'
rec_pay = paycard('$5,000','12 months','Pay for College Recruiting','Payment covers 12 months of recruiting guidance. You\'ll receive a short intake form and we\'ll schedule the first call within a week.',
 ['<b>Pay.</b> Use the button to pay for 12 months of College Recruiting.','<b>Intake.</b> You\'ll receive a short form about your player\'s golf, academics and goals, and a request for their stats and swing video.','<b>First call.</b> We go through the evaluation, the realistic levels, and the first version of the school list.','<b>Go.</b> Outreach starts. From there, a call every month and a review of every message before it goes out.'])
page('recruiting','College Recruiting','College recruiting','The recruiting process, run with me.','From the first email to the final decision. Guided by a coach who has received the emails, recruited Top 5 classes and placed more than 165 players into college golf.','', rec_prog+rec_glance+rec_who+rec_cta, rec_pay)


# ---------------- INTERNATIONAL PAGE ----------------
i_prog = sec('College golf in the US, without the guesswork.', """<div class="two"><div><p class="lead">Every year, more of the best junior golfers in the world choose American college golf. It's the best development system in the game: elite coaching, world-class facilities, a full tournament schedule, and a degree. For a family outside the US, though, the path is twice as confusing.</p>
<p>Different school calendars. Different exams. Rules from the NCAA that nobody at home has heard of. College coaches who have never seen your player swing. And all of it on a recruiting clock that doesn't wait.</p>
<p>I was the college coach on the other end of those emails at Duke and Ohio State, and I've placed more than 165 players into college golf. I know exactly what a US coach needs to see from an international player, and how to get it in front of them.</p></div><img src="img/osu.jpg" alt="Brad Sparling coaching at Ohio State" style="object-position:50% 20%"></div>""", 'International families')
i_q = sec('The questions international families ask.', '<ul class="qlist">' + ''.join(f'<li><span>{i+1:02d}</span>"{q}"</li>' for i,q in enumerate([
 'Is my player good enough for US college golf, and at what level?',
 'How do coaches find a player they have never seen play?',
 'What is the NCAA Eligibility Center, and when do we register?',
 'Which exams does my player need, and when?',
 'Division I, II, III, NAIA or junior college: which is right?',
 'How much scholarship money is realistic for an international player?',
 'Will playing or competing at home affect eligibility?',
 'When should we start, and are we already behind?'])) + '</ul>', 'Sound familiar?')
i_what = sec('What I do for international families.', items([
 ('Honest evaluation','Where your player stands against US college rosters: scoring, rankings, World Amateur Golf Ranking position, and which levels are realistic now and with work.'),
 ('A school list that fits','Golf level, academics, location, climate, cost, and the programs with a track record of developing international players.'),
 ('Getting seen from overseas','A player profile, swing video and results that a US coach can evaluate in five minutes, and outreach that gets answered.'),
 ('Eligibility, step by step','NCAA Eligibility Center registration, amateurism, academic records and the exam timeline, so nothing is missed or late.'),
 ('The US tournament plan','Which American events are worth the trip, and when, so coaches can see your player in person.'),
 ('Offers and the decision','How to read an offer, compare scholarship packages, and choose the program where your player will thrive.')]), 'How I help')
i_how = sec('Work with me from anywhere.', """<div class="two"><div><p class="lead">Elite Performance Coaching, Advisory Performance Coaching and College Recruiting all work remotely. Calls are scheduled around your time zone, Practice Lab and the reports run online, and recruiting is handled from here, where the coaches are.</p>""" + check([
 '<b>Elite Performance Coaching.</b> The complete program: development, practice, tournaments, mental game and recruiting, run by me every week.',
 '<b>Advisory Performance Coaching.</b> The same plan, run by your family, with a monthly check-in from me.',
 '<b>College Recruiting.</b> The recruiting process only, run with me, from the first email to the decision.']) + '<p style="margin-top:18px">Families of players from 9 to 22, beginner through college, anywhere in the world.</p></div><img src="img/headshot.jpg" alt="Brad Sparling today" style="object-position:50% 20%"></div>', 'Programs')
i_talk = sec('How we stay in touch.', items([
 ('Video calls on your time','Scheduled sessions on Zoom or WhatsApp video, set at a time that works where you live, morning or evening here.'),
 ('Messages between calls','WhatsApp, text or email, whichever your family already uses. Quick questions get quick answers.'),
 ('Everything in writing','The plan, the reports and Practice Lab are all online, so parents and players can read, re-read and share them in their own time.'),
 ('A reply within two working days','Every application and email is read by me personally, wherever in the world it comes from.')]), 'Communication')
i_cta = rec_cta.replace('Apply and tell me about your player','Apply and tell me about your player and where you live')
page('international','International Families','International families','Playing college golf in the United States.','For families outside the US who want their player in American college golf: an honest evaluation, a plan, and a guide through recruiting, eligibility and the decision, from a former Duke and Ohio State coach.','', i_prog+i_q+i_what+i_how+i_talk+i_cta, '')

# Teaching
t_prog = sec('Yes, I teach the swing too.', """<div class="two"><div><p class="lead">Most of what I do works alongside your player's swing coach, wherever you live. But for families in Central Ohio, I also teach. Weekly, in person, one-on-one, for junior golfers only.</p>
<p>I started as a teaching professional at Duke University Golf Club under PGA Master Professional Ed Ibarguen, before I ever coached a college team. Teaching is where I began, and 25 years later it's still the part of the week I look forward to most.</p>
<p>The difference is what the lesson is connected to. A lesson from me is built around what your player's stats say is costing them strokes, not around what looks pretty on video. The swing, the short game, putting and course management all get worked on in proportion to what actually matters for their scores.</p></div><img src="img/bw.jpg" alt="Coach Spar with a player on the course" style="object-position:50% 20%"></div>""", 'Teaching')
t_phil = sec('How I teach.', """<p class="lead">The approach in <i>Becoming Elite</i> is the approach on the lesson tee. Six words cover it.</p>""" + items([
 ('Holistic','The swing is one piece. I teach the whole player: technique, short game, putting, course management, practice habits, the mental game, and the athlete. Technique is never king; it serves the score.'),
 ('Positive','Players learn fastest when they feel good about what they\'re building. We find what works, do more of it, and fix what costs strokes without tearing anything down.'),
 ('Fun','Kids who enjoy practice keep practicing. Lessons have games, scoring and consequences, because a rep that counts teaches more than a hundred that don\'t.'),
 ('Functional and consistent','I don\'t teach a model swing. I teach your player\'s swing to produce a reliable ball flight they can trust under pressure. Repeatable beats pretty.'),
 ('Simple','One thing at a time, explained in words a 12-year-old understands. If a player can\'t say what they\'re working on and why, the lesson hasn\'t worked yet.'),
 ('Latest technology','Launch monitor and video on the range, strokes-gained stats from every round, and the PGIC Practice Lab between lessons, so we work from what the numbers say rather than what the swing looks like.')]), 'The philosophy')
t_glance = sec('What a year of lessons looks like.', items([
 ('Weekly lesson','One in-person lesson every week, about an hour, at a course in Central Ohio.'),
 ('Full game','Full swing, short game, bunker play and putting, in proportion to what the numbers say your player needs.'),
 ('Stats first','We track your player\'s rounds, so lessons go where the strokes are being lost, not where it\'s most fun to practice.'),
 ('Practice plan','Every lesson ends with a plan for the week between lessons, so the hour isn\'t wasted by the next seven days.'),
 ('Course management','On-course sessions through the season: targets, decisions, and how to avoid the big numbers.'),
 ('Tournament prep','Before key events, lessons shift to preparation: course strategy, pressure practice, and the routine.'),
 ('Equipment','Guidance on fitting, loft gapping and when it\'s time to change something.'),
 ('Parent updates','A short note after each lesson so you know what was worked on and what to look for.')]), 'The program')
t_who = sec('Who it\'s for', check(['<b>Junior golfers in Central Ohio,</b> elementary through high school.','<b>Players who are ready to commit</b> to a weekly lesson and the practice in between. Not ready for a full year? Single lessons are available too; see the Pay page.','<b>Families who want their swing coach and their performance coach to be the same person.</b> Teaching can be combined with Elite or Advisory.']) + '<p style="margin-top:22px">I don\'t teach adults. 25 years, junior golfers only.</p>')
t_cta = rec_cta.replace('tell me about your player','tell me about your player and where you are in Central Ohio')
t_pay = paycard('$6,000','12 months · weekly lessons','Pay for Teaching','Payment covers 12 months of weekly in-person lessons in Central Ohio. Limited spots; if the schedule is full, you\'ll be offered the next opening before being charged.',
 ['<b>Pay.</b> Use the button to reserve 12 months of weekly lessons.','<b>Schedule.</b> We find a standing weekly time that works around school and other sports.','<b>First lesson.</b> An evaluation of the full game, plus the stats we\'ll track all year.','<b>Every week after.</b> The lesson, the plan for the week, and a short note home.'])
page('teaching','Teaching','Teaching · Central Ohio','Weekly in-person instruction for junior golfers.','Full swing, short game, putting and course management, taught one-on-one and connected to what your player\'s scores say matters most.','', t_prog+t_phil+t_glance+t_who+t_cta, t_pay)

# Books
AMAZON = {'becoming':'https://a.co/d/03UcbFsi','lighthouse':'https://a.co/d/0gnjxayt','starthere':'https://a.co/d/05E4Mk7f','bep':'https://a.co/d/0iaPOUIv'}
books = [('becoming','Becoming Elite','A complete guide to junior golf, college golf and life. The curriculum behind every PGIC program: how great junior golfers practice, compete, think and prepare for college golf, and what the rest of life looks like when they do it right.'),
 ('lighthouse','The Lighthouse Golf Parent','The junior golf parenting playbook. Be the lighthouse, not a tugboat. How to support your player without adding pressure, what to say on the car ride home, and the 10 Pillars of Effective Golf Parenting.'),
 ('starthere','Start Here','The top 50 most common mistakes in junior golf, and the foundation that fixes them. If you are new to the junior golf world and don\'t know where to begin, begin here.'),
 ('bep','Building Elite Programs','A guide for coaches at every level. The culture, standards and accountability behind a #1 nationally ranked, back-to-back state champion high school team, and how to build the same thing in your program.')]
b_prog = sec('25 years, distilled into four books.', '''<p class="lead">These books are the foundation of everything I do with families. If you're not sure where to start, start with the one that matches where you are: a new golf parent, a player who wants to get serious, or a coach building a program.</p><div class="booklist">''' + ''.join(f'<div class="bk"><img src="img/{k}.jpg" alt="{t} cover"><div><b>{t}</b><p>{d}</p><a class="btn gold" style="padding:10px 18px;font-size:14px" href="{AMAZON[k]}" target="_blank" rel="noopener">Buy on Amazon</a></div></div>' for k,t,d in books) + '</div>', 'The books')
b_pay = '<h2>Buy the books</h2><p class="lead">All four are available on Amazon in paperback and Kindle.</p><div class="booklist">' + ''.join(f'<div class="bk"><img src="img/{k}.jpg" alt="{t} cover"><div><b>{t}</b><a class="btn gold" style="padding:10px 18px;font-size:14px" href="{AMAZON[k]}" target="_blank" rel="noopener">Buy on Amazon</a></div></div>' for k,t,d in books) + '</div>'
b_quotes = sec('What readers say.', '<div class="quotes two">' + '<div class="q"><p>"The book that every parent of an aspiring junior golfer needs to read. The ultimate guide for any family raising a junior golfer."</p><b>Ed Ibarguen</b><span>PGA Master Professional · Duke University Golf Club · Golf Magazine Top 100 Instructor · on <i>The Lighthouse Golf Parent</i></span></div><div class="q"><p>"This book is invaluable for anyone raising or supporting a junior golfer. You are the single biggest influence on your child\'s performance, for better or worse, and this book shows you how to make it for the better."</p><b>Grant Martin</b><span>Golfweek Jr. Tour Director · on <i>The Lighthouse Golf Parent</i></span></div>' + '</div>', 'Praise for The Lighthouse Golf Parent')
page('books','Books','The curriculum','Four books on junior golf, college golf and golf parenting.','Written from every seat at the table: college coach, high school coach, recruiting expert, and parent of three Division I golfers.','', b_prog+b_quotes, b_pay, tab1='The books')
print('pages built')

# ---------------- RATES PAGE ----------------
RATE_CSS = """
.rates{display:grid;gap:18px;margin-top:8px}
.rate{display:grid;grid-template-columns:minmax(0,1fr) 180px 220px;gap:24px;align-items:center;background:var(--surface);border:1px solid var(--rule);border-left:5px solid var(--gold);border-radius:8px;padding:24px 26px}
.rate b{font-family:var(--display);font-size:22px;color:var(--navy);display:block}
.rate p{font-size:16px;max-width:none;margin:6px 0 0;color:var(--quiet)}
.rate .amt{font-family:var(--display);font-size:32px;color:var(--navy);font-weight:600;line-height:1}
.rate .amt small{display:block;font-family:var(--body);font-size:13px;color:var(--quiet);font-weight:400;margin-top:6px}
.rate .act{display:flex;justify-content:flex-end}
.rate .act .btn{padding:11px 18px;font-size:14px;white-space:nowrap}
.rate .act .btn{padding:11px 18px;font-size:14px}
.rnote{margin-top:28px;font-size:14px;color:var(--quiet);max-width:none}
@media(max-width:820px){.rate{grid-template-columns:1fr}}
"""
rates_rows = [
 ('Elite Performance Coaching','Weekly, hands-on performance coaching. The complete program, including recruiting and a Foundations membership. Limited to 10 families a year. By application.','$10,500','per year','<a class="btn gold" href="https://www.paypal.com/ncp/payment/UQDFMW4V68REG" target="_blank" rel="noopener">Pay on acceptance</a>','elite.html'),
 ('Advisory Performance Coaching','The same plan, tools and curriculum, run by your family with a monthly check-in and report. Foundations membership included. Limited to 20 families a year. By application.','$4,000','per year','<a class="btn gold" href="https://www.paypal.com/ncp/payment/H924FRBWJJL7W" target="_blank" rel="noopener">Pay on acceptance</a>','advisory.html'),
 ('College Recruiting','The recruiting process, run with me: evaluation, school list, coach outreach, visits and the decision.','$5,000','for 12 months','<a class="btn gold" href="https://www.paypal.com/ncp/payment/W5Z742RFZY3SA" target="_blank" rel="noopener">Pay $5,000</a>','recruiting.html'),
 ('Teaching, weekly','A year of weekly in-person lessons for junior golfers in Central Ohio.','$6,000','for 12 months','<a class="btn gold" href="https://www.paypal.com/ncp/payment/X2PY2KMJKKQD2" target="_blank" rel="noopener">Pay $6,000</a>','teaching.html'),
 ('Teaching, single lesson','One in-person lesson in Central Ohio, about an hour. For families who want to start with one.','$250','per lesson','<a class="btn gold" href="https://www.paypal.com/ncp/payment/TY74HLM58ZEA8" target="_blank" rel="noopener">Pay $250</a>','teaching.html'),
 ('Foundations','A year-long membership on Lighthouse Golf Parent, and the right way for any junior golf parent to start. Includes all four of my books, the 10 Pillars framework, the scripts and templates for the car ride home, practice and recruiting, the Parent Assessment, and a members newsletter, with Ask Coach Spar coming soon. You run the plan; everything you need is inside. <a href="https://www.lighthousegolfparent.com" target="_blank" rel="noopener" style="color:var(--gold);font-weight:600;text-decoration:none">lighthousegolfparent.com &rarr;</a>','$249','per year','<a class="btn ghost" href="https://www.lighthousegolfparent.com" target="_blank" rel="noopener">Join</a>','foundations.html'),
 ('Books','Becoming Elite, The Lighthouse Golf Parent, Start Here and Building Elite Programs.','Amazon','paperback and Kindle','<a class="btn ghost" href="books.html">On Amazon</a>','books.html'),
 ('Enter another amount','For anything not listed, or an amount agreed with Coach Spar. You type the amount on the PayPal page.','Any','amount you choose','<a class="btn gold" href="https://www.paypal.com/ncp/payment/HBLFGDLSLTB8N" target="_blank" rel="noopener">Pay another amount</a>',''),
]
rates_html = '<div class="sec"><p class="lead" style="margin-top:0">Everything I offer, and what it costs. Elite and Advisory are by application; use their Pay buttons once you&rsquo;ve been accepted. Recruiting and Teaching can be paid directly. Foundations is purchased on Lighthouse Golf Parent, and the books on Amazon.</p><div class="rates" style="margin-top:28px">' + ''.join(
  f'<div class="rate"><div><b>{n}</b><p>{d}' + (f' <a href="{lnk}" style="color:var(--gold);font-weight:600;text-decoration:none">Details &rarr;</a>' if lnk else '') + f'</p></div><div class="amt">{a}<small>{per}</small></div><div class="act">{act}</div></div>' for n,d,a,per,act,lnk in rates_rows) + '</div><p class="rnote">Elite and Advisory are backed by the 30-Day Promise (full refund if the first 30 days aren\'t what I promised) and the Performance Promise (follow the plan for 12 months and see measurable improvement, or I coach you for another year, free). Payment for Elite and Advisory is due on acceptance and covers 12 months.</p></div>'

out = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Pay · Play Golf In College</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Public+Sans:wght@400;600;700&display=swap">
<style>{CSS}{EXTRA}{RATE_CSS}</style>{VAQ}<script defer src="/_vercel/insights/script.js"></script></head><body>
{NAV}
<header class="phero"><div class="wrap">
  <div class="eyebrow">Play Golf In College</div>
  <h1 style="margin-top:14px">Pay</h1>
  <p>Rates for every way to work with me, from a book to a full year of hands-on coaching. Each Pay button opens PayPal with the amount already filled in.</p>
  <div class="btns"><a class="btn gold" href="apply.html">Apply for coaching</a></div>
</div></header>
<section><div class="wrap">{rates_html}</div></section>
{FOOT}
</body></html>'''
open(os.path.join(ROOT,'pay.html'),'w').write(out)
print('rates built')

# ---------------- APPLY PAGE ----------------
FORM_CSS = """
.form{max-width:760px}
.fs{margin-top:36px}
.fs h3{font-size:22px;margin-bottom:6px}
.fs .fh{font-size:14px;color:var(--quiet);margin:0 0 14px;max-width:none}
.row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.f{display:grid;gap:6px;margin-top:14px}
.f label{font-weight:600;font-size:14px;color:var(--navy)}
.f label small{font-weight:400;color:var(--quiet)}
.f input,.f select,.f textarea{font:16px var(--body);color:var(--ink);background:var(--surface);border:1.5px solid var(--rule);border-radius:6px;padding:11px 12px;width:100%;box-sizing:border-box;min-width:0}
.f textarea{min-height:110px;resize:vertical}
.f input:focus,.f select:focus,.f textarea:focus{outline:2px solid var(--gold2);border-color:var(--gold)}
.radios{display:grid;gap:8px;margin-top:4px}
.radios label{display:flex;gap:10px;align-items:flex-start;justify-content:flex-start;text-align:left;width:100%;box-sizing:border-box;font-weight:400;font-size:15px;color:var(--ink);padding:10px 12px;border:1.5px solid var(--rule);border-radius:6px;background:var(--surface);cursor:pointer}
.radios label b{font-weight:600;color:var(--navy)}
.radios input{margin:3px 0 0;flex:0 0 auto;width:auto}
.radios span{flex:1}
.conf{margin-top:28px;background:var(--card);border-radius:8px;padding:16px 18px;font-size:14px;color:var(--quiet);max-width:none}
.submit{margin-top:28px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.done{display:none;margin-top:36px;background:var(--navy);color:var(--navy-ink);border-radius:10px;padding:32px}
.done b{font-family:var(--display);font-size:26px;color:var(--gold2);display:block;margin-bottom:10px;font-weight:500}
.done p{color:#dfe3ec;max-width:none}
.err{color:#b4322b;font-size:14px;display:none}
@media(max-width:600px){.row{grid-template-columns:1fr}}
"""
def fld(id_, label, kind='text', ph='', hint='', req=True):
    r = ' required' if req else ''
    h = f' <small>({hint})</small>' if hint else ''
    if kind=='textarea':
        return f'<div class="f"><label for="{id_}">{label}{h}</label><textarea id="{id_}" name="{id_}" placeholder="{ph}"{r}></textarea></div>'
    return f'<div class="f"><label for="{id_}">{label}{h}</label><input id="{id_}" name="{id_}" type="{kind}" placeholder="{ph}"{r}></div>'
def sel(id_, label, opts, req=True):
    return f'<div class="f"><label for="{id_}">{label}</label><select id="{id_}" name="{id_}"{" required" if req else ""}><option value="">Choose one</option>' + ''.join(f'<option>{o}</option>' for o in opts) + '</select></div>'

PL="Player's name"
form = f'''<form class="form" id="app" novalidate action="https://formspree.io/f/xbggrkll" method="POST">
<input type="hidden" name="_subject" value="PGIC application, step 1"><input type="hidden" name="step" value="1"><input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
<div class="fs"><h3>Step 1 of 2: the basics</h3><p class="fh">Two minutes. I reply with a few more questions once I've read this.</p>
<div class="row">{fld('pname','Your name')}{fld('rel','Relationship to the player',ph='Mom, Dad, guardian')}</div>
<div class="row">{fld('email','Email','email')}{fld('phone','Mobile phone','tel')}</div>
<div class="row">{fld('player',PL)}{sel('grade','Player\'s grade',['4th or younger','5th','6th','7th','8th','9th','10th','11th','12th','College'])}</div>
{fld('city','City and state, or country',ph='Where you live')}
<div class="f"><label>Which program are you interested in?</label><div class="radios">
<label><input type="radio" name="program" value="Elite" required><span><b>Elite Performance Coaching</b> · weekly, hands-on, 10 families a year</span></label>
<label><input type="radio" name="program" value="Advisory"><span><b>Advisory Performance Coaching</b> · monthly guidance, 20 families a year</span></label>
<label><input type="radio" name="program" value="Recruiting"><span><b>College Recruiting</b> · the recruiting process, run with me</span></label>
<label><input type="radio" name="program" value="Teaching"><span><b>Teaching</b> · weekly lessons, Central Ohio</span></label>
<label><input type="radio" name="program" value="Not sure"><span><b>Not sure yet</b> · help me figure out the right fit</span></label>
</div></div>
{fld('why','In a sentence or two, what made you reach out?',kind='textarea',ph='Optional, but it helps me reply with the right questions.',req=False)}
</div>
<p class="conf">Confidential and read only by me. I reply to every application personally, usually within two working days. Applying doesn&rsquo;t commit you to anything.</p>
<div class="submit"><button class="btn gold" type="submit" data-label="Send step 1">Send step 1</button><span class="err" id="err">Please fill in the required fields.</span></div>
</form>
<div class="done" id="done"><b>Thank you. Step 1 is in.</b><p>I read every application personally and will reply within two working days, usually sooner, with a few more questions about your player so our first conversation is a good one.</p><p style="margin-top:14px">Coach Spar</p></div>
<script>
(function(){{var f=document.getElementById('app');f.addEventListener('submit',function(e){{e.preventDefault();var err=document.getElementById('err');var btn=f.querySelector('button[type=submit]');if(!f.checkValidity()){{err.textContent='Please fill in the required fields.';err.style.display='inline';var bad=f.querySelector(':invalid');if(bad)bad.focus();return}}err.style.display='none';btn.disabled=true;btn.textContent='Sending\u2026';
fetch(f.action,{{method:'POST',body:new FormData(f),headers:{{'Accept':'application/json'}}}}).then(function(r){{if(!r.ok)throw new Error('bad');f.style.display='none';var d=document.getElementById('done');d.style.display='block';d.scrollIntoView({{behavior:'smooth',block:'start'}});}}).catch(function(){{btn.disabled=false;btn.textContent=btn.getAttribute('data-label');err.textContent='Something went wrong sending this. Please try again, or email coachsparling@gmail.com.';err.style.display='inline';}});}});}})();
</script>'''

form2 = f'''<form class="form" id="app" novalidate action="https://formspree.io/f/xbggrkll" method="POST">
<input type="hidden" name="_subject" value="PGIC application, step 2"><input type="hidden" name="step" value="2"><input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
<div class="fs"><h3>Step 2 of 2: about your player</h3><p class="fh">Thanks for step 1. These answers shape our first conversation. Honest beats impressive.</p>
<div class="row">{fld('pname','Your name')}{fld('player',PL)}</div>
<div class="row">{fld('avg','Current tournament scoring average',ph='e.g. 78',hint='best guess is fine',req=False)}{sel('level','Where they compete now',['Not in tournaments yet','Local or club events','State-level junior tour','Regional and national (AJGA, USGA, Golfweek, etc.)'])}</div>
{fld('coach','Swing coach',ph='Name, or none yet',req=False)}
{fld('goal','What does your player want from golf?',kind='textarea',ph='College golf, a state title, to make varsity, to love the game again. In their words if you can.')}
{fld('problem',"What isn't working right now?",kind='textarea',ph='The thing that made you look for help. Practice, tournaments, recruiting, the car ride home, all of it.')}
{fld('year','If this works, what is different a year from now?',kind='textarea',ph='For your player, and for your family.')}
{fld('heard','How did you hear about Coach Spar?',ph='A friend, Instagram, one of the books, a tournament',req=False)}
{fld('else','Anything else I should know?',kind='textarea',ph='Optional',req=False)}
<p class="fh" style="margin-top:14px">If your player has a stats report from their last 5 to 10 rounds, email it to coachsparling@gmail.com and we&rsquo;ll be a step ahead when we talk.</p>
</div>
<div class="submit"><button class="btn gold" type="submit" data-label="Send step 2">Send step 2</button><span class="err" id="err">Please fill in the required fields.</span></div>
</form>
<div class="done" id="done"><b>Thank you. That&rsquo;s everything I need.</b><p>I&rsquo;ll read this before we talk and be in touch to set up a call.</p><p style="margin-top:14px">Coach Spar</p></div>
<script>
(function(){{var f=document.getElementById('app');f.addEventListener('submit',function(e){{e.preventDefault();var err=document.getElementById('err');var btn=f.querySelector('button[type=submit]');if(!f.checkValidity()){{err.textContent='Please fill in the required fields.';err.style.display='inline';var bad=f.querySelector(':invalid');if(bad)bad.focus();return}}err.style.display='none';btn.disabled=true;btn.textContent='Sending\u2026';
fetch(f.action,{{method:'POST',body:new FormData(f),headers:{{'Accept':'application/json'}}}}).then(function(r){{if(!r.ok)throw new Error('bad');f.style.display='none';var d=document.getElementById('done');d.style.display='block';d.scrollIntoView({{behavior:'smooth',block:'start'}});}}).catch(function(){{btn.disabled=false;btn.textContent=btn.getAttribute('data-label');err.textContent='Something went wrong sending this. Please try again, or email coachsparling@gmail.com.';err.style.display='inline';}});}});}})();
</script>'''

def apply_page(fname, title, eyebrow, h1, sub, body):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · Play Golf In College</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Public+Sans:wght@400;600;700&display=swap">
<style>{CSS}{EXTRA}{FORM_CSS}</style>{VAQ}<script defer src="/_vercel/insights/script.js"></script></head><body>
{NAV}
<header class="phero"><div class="wrap">
  <div class="eyebrow">{eyebrow}</div>
  <h1 style="margin-top:14px">{h1}</h1>
  <p>{sub}</p>
</div></header>
<section><div class="wrap" style="padding-block:8px 48px">{body}</div></section>
{FOOT}
</body></html>'''
open(os.path.join(ROOT,'apply.html'),'w').write(apply_page('apply','Apply','Confidential application · Step 1 of 2','Tell me about your player.','Two minutes. No commitment. I read every application personally and reply within two working days with a few more questions.', form))
open(os.path.join(ROOT,'apply-step2.html'),'w').write(apply_page('apply-step2','Apply, step 2','Confidential application · Step 2 of 2','A few more questions.','Five minutes. This is the link I send after reading step 1.', form2))
print('apply built')

# ---------------- ABOUT PAGE ----------------
ABOUT_CSS = """
.about-page .sec{padding-block:28px}
.about-page .sec h2{margin-top:6px}
.about-page .tl{margin-top:20px}
.about-page .tl>div{padding:14px 0}
.about-page .kids{margin-top:18px}
.story{display:grid;grid-template-columns:1.35fr .65fr;gap:40px;align-items:center}
.story img{width:100%;height:auto;border-radius:8px;max-width:100%}
.story .lead{font-size:18px}
.tl{margin-top:36px;display:grid;gap:0}
.tl>div{display:grid;grid-template-columns:150px 1fr;gap:20px;padding:18px 0;border-top:1px solid var(--rule)}
.tl b{font-family:var(--display);font-size:18px;color:var(--gold);font-weight:600;line-height:1.2}
.tl h4{font-family:var(--display);font-size:21px;color:var(--navy);margin:0 0 6px;font-weight:600}
.tl p{font-size:17px;max-width:none;margin:0}
.gal2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}
.gal2 img{width:100%;height:auto;border-radius:8px;object-fit:cover;aspect-ratio:4/3;max-width:100%}
.famwide{width:100%;height:auto;max-width:100%;border-radius:8px;margin-top:22px;aspect-ratio:16/9;object-fit:cover;object-position:50% 40%}
.fam{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:22px}
.fam.three{grid-template-columns:repeat(3,1fr);margin-top:14px}
.fam figure{margin:0}
.fam img{width:100%;height:auto;max-width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:8px}
.fam figcaption{font-size:13px;color:var(--quiet);margin-top:6px}
@media(max-width:820px){.fam,.fam.three{grid-template-columns:1fr 1fr}.famwide{aspect-ratio:4/3}}
.kids{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:28px}
.kids div{background:var(--surface);border:1px solid var(--rule);border-top:4px solid var(--gold);border-radius:8px;padding:22px}
.kids b{font-family:var(--display);font-size:21px;color:var(--navy);display:block;margin-bottom:6px}
.kids p{font-size:16px;max-width:none;margin:0}
.story p+p,.sec .two p+p{margin-top:14px}
.sec h2+.two,.sec h2+.lead{margin-top:18px}
@media(max-width:820px){.story,.kids{grid-template-columns:1fr}.tl>div{grid-template-columns:1fr;gap:4px}}
"""
about_body = '''
<div class="sec"><div class="story"><div>
<p class="lead">I'm Brad Sparling. Most people call me Spar. I've spent 25 years in competitive golf, and I've sat in every seat at the table: the player, the teaching pro, the college coach, the recruiter, the high school coach, the author, and the dad in the parking lot. That's the whole reason Play Golf In College exists. Junior golf is a long process, and I've lived every step of it from every angle.</p>
<p>I don't coach adults. For 25 years I've worked only with junior golfers and their families, and I've written four books about how to do it well.</p>
</div><div><img src="img/headshot.jpg" alt="Brad Sparling" style="aspect-ratio:4/4.6;object-fit:cover;object-position:50% 20%"></div></div></div>

<div class="sec"><div class="eyebrow">The story</div><h2>Every seat at the table.</h2>
<div class="tl">
<div><b>The player</b><div><h4>Guilford College</h4><p>I played college golf at Guilford, which is where I learned what it takes to make a roster, hold a spot, and what nobody tells you before you get there.</p></div></div>
<div><b>The teacher</b><div><h4>Duke University Golf Club</h4><p>My first job in golf was teaching, as a professional at Duke University Golf Club under PGA Master Professional Ed Ibarguen, a Golf Magazine Top 100 Instructor. Four years on the lesson tee, learning to teach people, not just golf. I still teach today, in Central Ohio, and it's still the part of the week I like best.</p></div></div>
<div><b>The college coach</b><div><h4>Duke University, then Ohio State</h4><p>At Duke I went from assistant to associate head coach to interim head coach, working under Hall of Fame coaches Rod Myers and Dan Brooks. I was part of two NCAA Championships and programs that produced 14 All-Americans, two National Players of the Year and an NCAA individual champion. I recruited Top 5 classes. Then Ohio State, as associate head coach under Jim Brown. Five years of reading the emails, evaluating the recruits, and making roster decisions from the other side of the table.</p></div></div>
<div><b>The recruiter</b><div><h4>Play Golf In College, 2009</h4><p>I founded PGIC to give families the insider's view of recruiting that I'd had as a coach. Seventeen years later, more than 165 players placed in college golf, with 95% of our players receiving offers, at schools from Duke, Ohio State, Texas, Tennessee, TCU and Miami of Ohio to Harvard, Columbia, Penn and Georgetown. Along the way PGIC grew from a recruiting service into development, performance coaching and parent guidance, because recruiting is the last step of a long process and families needed help with the whole thing.</p></div></div>
<div><b>The high school coach</b><div><h4>Dublin Jerome, since 2024</h4><p>I coach Dublin Jerome in addition to running Play Golf In College. In 2025 we won the Ohio Division I state championship and finished the season ranked #1 in the country. In 2026 we won it again, with what was statistically the best team in Ohio high school history. Across my career I've worked with 20 OHSAA individual state champions. Coaching a team every fall keeps me current with today's players and today's recruiting, and it makes me a better coach for every family I work with.</p></div></div>
<div><b>The author</b><div><h4>Four books</h4><p><i>Becoming Elite</i>, the complete guide to junior golf, college golf and life. <i>The Lighthouse Golf Parent</i>, the junior golf parenting playbook. <i>Start Here</i>, the top 50 mistakes in junior golf. <i>Building Elite Programs</i>, for coaches. They are the curriculum behind everything I do with families.</p></div></div>
</div></div>

<div class="sec"><div class="eyebrow">The parent</div><h2>Three kids. Three Division I golfers.</h2>
<p class="lead" style="margin-top:18px">My wife Suzie and I raised three golfers, and all three played Division I. I've driven the car home after the bad rounds, sat through the recruiting calls, and made the mistakes I now help families avoid. That's where <i>The Lighthouse Golf Parent</i> came from.</p>
<div class="fam">
<figure><img src="img/family.jpg" alt="The Sparling family" style="object-position:50% 40%"><figcaption>The whole family</figcaption></figure>
<figure><img src="img/nick-state.jpg" alt="Nick with his state championship medal" style="object-position:50% 35%"><figcaption>Nick, state champion</figcaption></figure>
<figure><img src="img/jack.jpg" alt="Jack with the MAC championship trophy" style="object-position:50% 25%"><figcaption>Jack, MAC champion</figcaption></figure>
<figure><img src="img/emma.jpg" alt="Brad and his wife with Emma at Dayton" style="object-position:50% 30%"><figcaption>Emma at Dayton</figcaption></figure>
</div>
<div class="kids">
<div><b>Nick</b><p>Two-time OHSAA Division I individual state champion. Played at Ohio State and Western Washington.</p></div>
<div><b>Jack</b><p>All-Ohio. Academic All-American at Miami of Ohio, then played professionally.</p></div>
<div><b>Emma</b><p>Academic All-American at the University of Dayton.</p></div>
</div></div>

<div class="sec"><div class="eyebrow">How I coach</div><h2>Holistic. Positive. Fun. Functional. Simple.</h2>
<div class="two"><div><p>Technique is not king. The best junior golfers I've coached, and the three I raised, were built on character, habits, practice that counts, a mental game that holds up, and a family that knew its role. The swing is one piece of a much bigger picture, which is why I coach the whole picture: the player, the plan, the team around them, and the parents.</p>
<p>I keep it simple and I keep it positive, because kids who enjoy the work keep doing it. And I use the best tools available, from strokes-gained stats to the PGIC Practice Lab, so we work from what the numbers say rather than what a swing looks like on video.</p>
<p><b>"Be the lighthouse, not a tugboat."</b> Parents don't need to push their player through junior golf. They need to be the steady light the player steers by. Everything I do with families starts there.</p></div>
<img src="img/water.jpg" alt="Coach Spar and a player looking down the fairway"></div></div>

<div class="sec"><div class="answer" style="margin-top:0;padding:30px"><strong>Want to talk about your player?</strong>I work with a small number of families each year, from all over the country. Tell me about your player in a short, confidential application and I'll reply within two working days.<div class="btns" style="margin-top:18px"><a class="btn gold" href="apply.html">Apply for coaching</a><a class="btn ghost" href="index.html#programs" style="color:#fff;border-color:rgba(255,255,255,.6)">See the programs</a></div></div></div>
'''
out = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>About Coach Spar · Play Golf In College</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Public+Sans:wght@400;600;700&display=swap">
<style>{CSS}{EXTRA}{ABOUT_CSS}</style>{VAQ}<script defer src="/_vercel/insights/script.js"></script></head><body>
{NAV}
<header class="phero split abouthero"><div class="wrap"><div class="copy">
  <div class="eyebrow">About Coach Spar</div>
  <h1 style="margin-top:14px">I've seen junior golf from every angle.</h1>
  <p>College coach. Recruiting expert. Swing teacher. High school coach. Author. Parent of three D1 golfers.</p>
</div><div class="pic"><img src="img/solo.jpg" alt="Coach Spar on the course"></div></div></header>
<section class="about-page"><div class="wrap" style="padding-block:0 24px">{about_body}</div></section>
{FOOT}
</body></html>'''
open(os.path.join(ROOT,'about.html'),'w').write(out)
print('about built')

# ---------------- FOUNDATIONS PAGE ----------------
f_prog = sec('The right way to start.', """<p class="lead">Foundations is a year-long membership on Lighthouse Golf Parent, built for any junior golf parent who wants to do this the right way from the beginning. Everything I teach families in Elite and Advisory, in a form you run yourself.</p>""" + items([
 ('All four books','Becoming Elite, The Lighthouse Golf Parent, Start Here and Building Elite Programs, included with membership.'),
 ('The 10 Pillars','The framework behind The Lighthouse Golf Parent: the ten things a golf parent controls that shape how a player develops.'),
 ('Scripts and templates','What to say on the car ride home, how to structure practice, and the letters and résumés that get a college coach\'s attention.'),
 ('Parent Assessment','Know where you are as a golf parent right now, and what to improve on to help your kid.'),
 ('Members newsletter','Regular guidance from me on development, tournaments, recruiting and the parent\'s role.'),
 ('Ask Coach Spar','Coming soon: answers to your questions, in my voice, whenever you need them.')]), 'What\'s inside')
f_who = sec('Who it\'s for', check(['<b>Parents of younger players</b> who want to get the environment right before the stakes rise.','<b>Families who want the plan and will run it themselves</b>, without weekly or monthly contact with me.','<b>Anyone considering Elite or Advisory</b> who wants to start with the foundation first. Foundations is included in both.']) + '<p style="margin-top:22px">Join at <a href="https://www.lighthousegolfparent.com" target="_blank" rel="noopener" style="color:var(--gold);font-weight:600;text-decoration:none">lighthousegolfparent.com</a>.</p>')
f_cta = '<div class="sec"><div class="answer" style="margin-top:0;padding:30px"><strong>Start here.</strong>Foundations lives on Lighthouse Golf Parent, my site for the parent side of junior golf. You can join today.<div class="btns" style="margin-top:18px"><a class="btn gold" href="https://www.lighthousegolfparent.com" target="_blank" rel="noopener">Join at lighthousegolfparent.com</a></div></div></div>'
f_letter = """<div class="sec" id="letter"><div class="fl">
<div class="fl-copy"><div class="eyebrow">Free weekly newsletter</div>
<h2 style="margin-top:8px">The Lighthouse Letter.</h2>
<p>Not ready for a membership yet? Start with my free letter for golf parents. Every Tuesday I send one update, one thought and one question to talk about as a family. You can unsubscribe anytime.</p></div>
<div class="fl-box">
<form class="fl-f" id="flForm" novalidate>
<input type="text" id="flName" placeholder="First name" autocomplete="given-name" aria-label="First name" required>
<input type="email" id="flEmail" placeholder="Email" autocomplete="email" aria-label="Email" required>
<button type="submit" class="btn gold">Get it free</button>
</form>
<p class="fl-m" id="flMsg" role="status"></p>
<div class="fl-share"><span>Know a golf parent who would like it?</span><button type="button" class="btn ghost" id="flShare">Share the Letter</button><a id="flMail" href="mailto:?subject=The%20Lighthouse%20Letter%20for%20golf%20parents&amp;body=I%20thought%20you%27d%20like%20this%20free%20weekly%20letter%20for%20golf%20parents%20from%20Coach%20Spar%3A%20https%3A%2F%2Fwww.playgolfincollege.com%2Ffoundations%23letter">or email it</a></div>
<p class="fl-m" id="flShareMsg" role="status"></p>
<iframe name="flSink" title="Newsletter signup" hidden tabindex="-1" style="display:none"></iframe>
<div hidden aria-hidden="true" id="flKajabi"><script src="https://www.lighthousegolfparent.com/forms/2149766365/embed.js"></script></div>
</div></div></div>
<script>
(function(){
  var f=document.getElementById('flForm'), msg=document.getElementById('flMsg');
  if(f) f.addEventListener('submit',function(e){
    e.preventDefault();
    var n=document.getElementById('flName').value.trim(), m=document.getElementById('flEmail').value.trim();
    if(!n||!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(m)){msg.textContent='Please enter your first name and a valid email.';return;}
    var k=document.querySelector('#flKajabi form');
    if(!k){window.open('https://www.lighthousegolfparent.com/#letter','_blank');return;}
    k.querySelector('[name="form_submission[name]"]').value=n;
    k.querySelector('[name="form_submission[email]"]').value=m;
    k.removeAttribute('data-parsley-validate');
    k.target='flSink'; k.submit();
    try{ localStorage.setItem('pgicLetterJoined','1'); }catch(x){}
    f.style.display='none';
    msg.textContent='Thanks, '+n+'! Check your inbox and click the button to confirm. Your first letter arrives Tuesday.';
  });
  var url='https://www.playgolfincollege.com/foundations#letter', sb=document.getElementById('flShare'), sm=document.getElementById('flShareMsg');
  if(sb) sb.addEventListener('click',function(){
    var data={title:'The Lighthouse Letter',text:'A free weekly letter for golf parents from Coach Spar.',url:url};
    if(navigator.share){ navigator.share(data).catch(function(){}); return; }
    var done=function(){ sm.textContent='Link copied. Paste it into a text or email.'; };
    if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(url).then(done,function(){ sm.textContent=url; }); }
    else { sm.textContent=url; }
  });
})();
</script>"""
page('foundations','Foundations','Foundations · Lighthouse Golf Parent','The right way for any junior golf parent to start.','A year-long membership with all four of my books, the 10 Pillars framework, the scripts and templates, the Parent Assessment and a members newsletter. You run the plan; everything you need is inside.','', f_prog+f_who+f_letter+f_cta, '')

# ---------------- TESTIMONIALS PAGE ----------------
import re as _re
TSEC = open(os.path.join(SRC,'testimonials_section.html')).read()
inner = TSEC[TSEC.index('<div class="feature-q">'):TSEC.rindex('</div></section>')]
T_CSS = """
.feature-q{margin-top:8px;padding:34px 40px;background:var(--navy);border-radius:10px;color:var(--navy-ink)}
.feature-q p{font-family:var(--display);font-style:italic;font-size:clamp(22px,2.6vw,30px);color:#fff;max-width:none;line-height:1.35;margin:0}
.feature-q b{display:block;margin-top:18px;font-size:15px;color:var(--gold2)}
.feature-q span{display:block;font-size:13px;color:#c9cedb;margin-top:2px}
.qgroup{margin-top:40px;font-weight:700;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);padding-bottom:10px;border-bottom:1px solid var(--rule)}
.quotes{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:20px}
.quotes.two{grid-template-columns:1fr 1fr}
.q{background:var(--card);border-radius:8px;padding:26px}
.q p{font-family:var(--display);font-style:italic;font-size:18px;color:var(--navy);max-width:none;line-height:1.45}
.q b{display:block;margin-top:16px;font-size:15px;font-weight:600}
.q span{display:block;font-size:14px;color:var(--quiet)}
@media(max-width:820px){.quotes,.quotes.two{grid-template-columns:1fr}.feature-q{padding:26px}}
"""
inner_groups = inner[inner.index('<div class="qgroup">'):]
out = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 '<title>Testimonials \u00b7 Play Golf In College</title>\n'
 '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Public+Sans:wght@400;600;700&display=swap">\n'
 '<style>'+CSS+EXTRA+T_CSS+'.phero.split .quote{font-family:var(--display);font-style:italic;font-size:clamp(24px,2.8vw,36px);color:#fff;line-height:1.3;margin-top:14px;max-width:none}.phero.split .who{margin-top:18px;color:var(--gold2);font-weight:700;font-size:15px}.phero.split .who small{display:block;color:#c9cedb;font-weight:400;font-size:13px;margin-top:3px}</style>'+VAQ+'<script defer src="/_vercel/insights/script.js"></script></head><body>\n'+NAV+'\n'
 '<header class="phero split"><div class="wrap"><div class="copy">\n  <h1 class="eyebrow" style="font-family:var(--body);font-size:14px;line-height:1.5;color:var(--gold2);max-width:none;margin:0">What coaches, parents and players say</h1>\n'
 '  <p class="quote">"The book that every parent of an aspiring junior golfer needs to read. The ultimate guide for any family raising a junior golfer."</p>\n'
 '  <div class="who">Ed Ibarguen<small>PGA Master Professional \u00b7 Duke University Golf Club \u00b7 Golf Magazine Top 100 Instructor \u00b7 on <i>The Lighthouse Golf Parent</i></small></div>\n'
 '</div><div class="pic"><img src="img/coaches.jpg" alt="Coach Spar with his players" style="object-position:50% 35%"></div></div></header>\n'
 '<section><div class="wrap" style="padding-block:8px 56px">'+inner_groups+'</div></section>\n'+FOOT+'\n</body></html>')
open(os.path.join(ROOT,'testimonials.html'),'w').write(out)
print('testimonials built')

# Keep the homepage menu in sync with NAV (index.html is otherwise edited by hand)
_h = open(os.path.join(ROOT,'index.html')).read()
_h2 = re.sub(r'<nav>.*?</nav>', lambda m: NAV.strip(), _h, count=1, flags=re.S)
open(os.path.join(ROOT,'index.html'),'w').write(_h2)
import sys as _sys; _sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo as _seo; _seo.apply(ROOT)
print('Built all pages.')
