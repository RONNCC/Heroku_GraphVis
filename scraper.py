"""
Scrapes MAL for animedata given a URL starting link!
No parallelization because currently Google App Engine doesn't have much in the way of free computing power :/ and I don't want to accidentally eat a ton of MAL's server resources
"""
DEPTH = 20
def make_graph():
	import re,urllib,networkx as nx
	##pylab as plt
	from collections import deque
	
	"""
	Wanted to use Matplotlib's colormaps but it seems installing it via pip is a pain, so instead I'm using an interpolating function for one of them: "RdBu"
	"""
	

	url="http://myanimelist.net/anime/3389/Bus_Gamer/userrecs"
	pattern = re.compile('(?<=<div style="margin-bottom: 2px;"><a href=").*?(?=")')
	G = nx.Graph()
	q = deque([[(x[29:]).split('/') for x in [url]][0][0:2]])
	for x in range(DEPTH):
	    ci,cn = q.popleft()
	    urld = urllib.urlopen("http://myanimelist.net/anime/"+ci+"/"+cn+"/userrecs").read()
	    d = [(x[29:]).split('/') for x in pattern.findall(urld)]
	    for z in d:
		q.append((z[0],z[1]))
		G.add_edge(cn,unicode(z[1],'utf-8'))
	
	###Locally I'll just use Matplotlib. In Heroku I doubt it will work
	def colormap(g):
		#what matplotlib color map?
		CMAP="RdBu"
		from matplotlib.cm import get_cmap
		cmap = get_cmap(name=CMAP)
		maxdegree=max(g.degree(g.nodes()).values())
		for y in g.nodes():
			c = cmap(1.0*g.degree(y)/maxdegree)
			g.node[y]['viz']={'color':{'r':255*c[0],'g':255*c[1],'b':255*c[2],'a':0}}
				

	colormap(G)

#nx.draw(G)
	#plt.show()
	nx.write_gexf(G,"static/MALgraph.gexf",version="1.2draft")

if __name__=='__main__':
	make_graph()
	print 'Graph Made'
