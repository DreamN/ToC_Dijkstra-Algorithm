import graphviz as gv
import csv
G = {}
root = ''
end = ''
Distance = {}
Path = {}
Grouped = []

#findmin function
def fineMin():
	x = 2000000
	minNode = 0
	for node in G:
		if Distance[node] < x and (not node in Grouped):
			x = Distance[node]
			minNode = node
	return minNode

i=0; j=0

with open('G.CSV', newline='') as csvfile:
	a = csv.reader(csvfile)
	nodelist = next(a)
	for row in a:
		G[nodelist[i]]={};j=0
		for co in row:
			if co != '-':
				G[nodelist[i]][nodelist[j]]=int(co)
			j += 1
		i += 1

root = input('Enter root node: ')
end = input('Enter end node: ')

# make Infinity
for node in G:
	Distance[node] = 2000000
	Path[node] = node
Distance[root] = 0

print('=================== Time 0 ===================')
for node in G:
	print("Distance from \'"+root+"\' to \'"+node+"\' is "+str(Distance[node]))

for x in range(len(G)):
	minNode = fineMin()
	for node in G[minNode]:
		if (not node in Grouped) and Distance[minNode] + G[minNode][node] < Distance[node]:
			Distance[node] = Distance[minNode] + G[minNode][node]
			Path[node]=Path[minNode]+node
	Grouped.append(minNode)
	print('=================== Time '+str(x+1)+' ===================')
	for node in G:
		print("Distance from \'"+root+"\' to \'"+node+"\' is "+str(Distance[node]))

print("Distance from root to end (" + root + " to " + end + ") is " + str(Distance[end]))
print("Path is "+' --> '.join(Path[end]))

displayG = gv.Graph(format='png', engine='sfdp')
#display Graph
for node in G:
	if node == root:
		displayG.node(node, node+" : "+str(Distance[node]), color='green')
	elif node == end:
		displayG.node(node, node+" : "+str(Distance[node]), color='blue')
	elif node in Path[end]:
		displayG.node(node, node+" : "+str(Distance[node]), color='red')
	else:
		displayG.node(node, node+" : "+str(Distance[node]))
	# print('Added node: \''+node+'\'')
	for edge in G[node]:
		if G[edge][node] != -1:
			if edge+node in Path[end] or node+edge in Path[end]:
				displayG.edge(str(node),str(edge),str(G[node][edge]), color='red', fontcolor='red')
			else:
				displayG.edge(str(node),str(edge),str(G[node][edge]))
			# print('Linked between node: \''+node+'\' and \''+edge+'\'')
			G[node][edge] = -1
displayG.view()