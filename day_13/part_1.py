print((lambda P:int(sum(1/P.count(p) for p in P)))((lambda P,F:[P,[[P.__setitem__(i,f(P[i])) for f in F[0:1]] for i,_ in enumerate(P)]][0])(*(lambda P,F:[(P,F),[[F.append((lambda A,V:(lambda p:[2*V-p[0] if V<p[0] else p[0],p[1]]) if A=='x' else (lambda p:[p[0],2*V-p[1] if V<p[1] else p[1]]))(a.strip(),int(v))) for a,v in [tuple(l[11:].split('='))]] if l.startswith("fold") else P.append([int(v) for v in l.split(',')]) for l in open("input") if l.strip()]][0])([],[]))))