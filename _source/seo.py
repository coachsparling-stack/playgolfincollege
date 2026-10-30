# Search-engine basics, applied to every built page by gen.py (run last).
# Edit titles/descriptions here. Builds sitemap.xml and robots.txt too.
import os, re, json, html
SITE = 'https://www.playgolfincollege.com'
PAGES = {
 'index':        ('Play Golf In College | Coach Brad Sparling | Junior Golf Coaching & College Recruiting',
                  'Junior golf is confusing. You need more than a swing coach. Player development, performance coaching, parent guidance and college recruiting from Coach Brad Sparling, former Duke and Ohio State coach.',
                  'img/share.jpg', '1.0'),
 'elite':        ('Elite Junior Golf Performance Coaching | Coach Brad Sparling',
                  'Weekly performance coaching for junior golfers: practice, tournaments, mental game, parent guidance and college recruiting, run by former Duke and Ohio State coach Brad Sparling. 10 families a year.',
                  'img/watch.jpg', '0.9'),
 'advisory':     ('Advisory Junior Golf Coaching for Families | Coach Brad Sparling',
                  'You run your junior golfer\'s plan with a monthly check-in from former Duke and Ohio State coach Brad Sparling. Practice Lab, tournament plan, parent guidance and recruiting roadmap. 20 families a year.',
                  'img/swing.jpg', '0.9'),
 'recruiting':   ('College Golf Recruiting Help | Coach Brad Sparling',
                  'College golf recruiting, run with a coach who has placed 165+ players in college golf: school list, coach outreach, contact tracking and the final decision. Division I to Division III and NAIA.',
                  'img/shake.jpg', '0.9'),
 'teaching':     ('Junior Golf Lessons in Central Ohio | Coach Brad Sparling',
                  'Weekly one-on-one golf lessons for junior golfers in Central Ohio: full swing, short game, putting and course management, taught by former Duke and Ohio State coach Brad Sparling.',
                  'img/arm.jpg', '0.8'),
 'international':('College Golf in the USA for International Players | Play Golf In College',
                  'For families outside the US: an honest evaluation, a school list, NCAA eligibility and recruiting help to play college golf in America, from former Duke and Ohio State coach Brad Sparling.',
                  'img/duke.jpg', '0.8'),
 'foundations':  ('Foundations: Junior Golf Parent Membership | Lighthouse Golf Parent',
                  'A year-long membership for junior golf parents: all four of Brad Sparling\'s books, the 10 Pillars, scripts and templates, the Parent Assessment and a members newsletter.',
                  'img/young.jpg', '0.7'),
 'letter':       ('The Lighthouse Letter: Free Weekly Letter for Golf Parents | Coach Brad Sparling',
                  'A free email for golf parents every Tuesday from Coach Brad Sparling: one junior golf news item, one idea fully explained, three quotes and one question for your family.',
                  'img/letter-share.png', '0.7'),
 'books':        ('Junior Golf & Golf Parenting Books by Brad Sparling',
                  'Becoming Elite, The Lighthouse Golf Parent, Start Here and Building Elite Programs: four books on junior golf, college golf, golf parenting and coaching by Brad Sparling.',
                  'img/books-brad.jpg', '0.7'),
 'about':        ('About Coach Brad Sparling | Former Duke & Ohio State Golf Coach',
                  'Brad "Spar" Sparling: former Duke and Ohio State golf coach, two NCAA championships, Dublin Jerome head coach, author of four books and dad of three Division I golfers.',
                  'img/headshot.jpg', '0.8'),
 'testimonials': ('Testimonials | Coach Brad Sparling | Play Golf In College',
                  'What college coaches, parents and players say about working with Coach Brad Sparling, including Duke\'s Dan Brooks and Ohio State\'s Jim Brown.',
                  'img/coaches.jpg', '0.7'),
 'apply':        ('Apply | Play Golf In College',
                  'Tell Coach Brad Sparling about your junior golfer in a short, confidential application. He reads every one personally and replies within two working days.',
                  'img/share.jpg', '0.6'),
 'apply-step2':  ('Apply, step 2 | Play Golf In College', None, None, None),   # not indexed
 'pay':          ('Pay | Play Golf In College', None, None, None),             # not indexed
}
LD_INDEX = {"@context":"https://schema.org","@graph":[
  {"@type":"Organization","@id":SITE+"/#org","name":"Play Golf In College","url":SITE+"/","logo":SITE+"/img/logo.png",
   "foundingDate":"2009","founder":{"@id":SITE+"/#brad"},"areaServed":"Central Ohio and worldwide",
   "description":"Player development, performance coaching, parent guidance and college recruiting for junior golfers.",
   "email":"coachsparling@gmail.com","sameAs":["https://www.instagram.com/playgolfincollege","https://x.com/playgolfcollege","https://www.lighthousegolfparent.com"]},
  {"@type":"Person","@id":SITE+"/#brad","name":"Brad Sparling","alternateName":"Coach Spar","jobTitle":"Junior golf performance coach",
   "url":SITE+"/about","image":SITE+"/img/headshot.jpg","worksFor":{"@id":SITE+"/#org"},
   "alumniOf":"Guilford College","address":{"@type":"PostalAddress","addressRegion":"OH","addressCountry":"US"}},
  {"@type":"WebSite","@id":SITE+"/#site","url":SITE+"/","name":"Play Golf In College","publisher":{"@id":SITE+"/#org"}}]}
BOOKS = [('Becoming Elite','https://a.co/d/03UcbFsi'),('The Lighthouse Golf Parent','https://a.co/d/0gnjxayt'),('Start Here','https://a.co/d/05E4Mk7f'),('Building Elite Programs','https://a.co/d/0iaPOUIv')]

def url_for(name): return SITE + '/' if name=='index' else f'{SITE}/{name}'

def apply(root, extra_urls=()):
    for name,(title,desc,img,_) in PAGES.items():
        p=os.path.join(root,name+'.html')
        if not os.path.exists(p): continue
        s=open(p).read()
        s=re.sub(r'\n?<!--seo-->.*?<!--/seo-->','',s,flags=re.S)
        s=re.sub(r'<meta name="description"[^>]*>','',s)
        s=re.sub(r'<meta (property="og:|name="twitter:)[^>]*>','',s)
        s=re.sub(r'<title>.*?</title>','<title>'+html.escape(title,quote=False)+'</title>',s,count=1,flags=re.S)
        tags=[]
        if desc is None:
            tags.append('<meta name="robots" content="noindex">')
        else:
            e=lambda x: html.escape(x,quote=True)
            tags+= [f'<meta name="description" content="{e(desc)}">', f'<link rel="canonical" href="{url_for(name)}">',
              '<meta property="og:type" content="website">', '<meta property="og:site_name" content="Play Golf In College">',
              f'<meta property="og:url" content="{url_for(name)}">', f'<meta property="og:title" content="{e(title)}">',
              f'<meta property="og:description" content="{e(desc)}">', f'<meta property="og:image" content="{SITE}/{img}">',
              '<meta name="twitter:card" content="summary_large_image">']
            if name=='index': tags.append('<meta name="google-site-verification" content="dP4-1q0FvVkhkVfF0OC6_50pNzifXGTBJ8s_JqvggkQ">')
            if name=='index': tags.append('<script type="application/ld+json">'+json.dumps(LD_INDEX)+'</script>')
            if name=='books':
                ld={"@context":"https://schema.org","@graph":[{"@type":"Book","name":b,"author":{"@type":"Person","name":"Brad Sparling"},"url":u} for b,u in BOOKS]}
                tags.append('<script type="application/ld+json">'+json.dumps(ld)+'</script>')
        s=s.replace('</title>','</title>\n<!--seo-->'+''.join(tags)+'<!--/seo-->',1)
        open(p,'w').write(s)
    urls=''.join(f'<url><loc>{url_for(n)}</loc><priority>{v[3]}</priority></url>' for n,v in PAGES.items() if v[1] is not None)
    urls+=''.join(f'<url><loc>{u}</loc><priority>0.6</priority></url>' for u in extra_urls)
    open(os.path.join(root,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>\n')
    open(os.path.join(root,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    print('seo applied')
