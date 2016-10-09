# ToC_Dijkstra-Algorithm
![](https://github.com/DreamN/ToC_Dijkstra-s-Algorithm/blob/master/az_graph.PNG?raw=true)  

dijkstra's algorithm for finding shortest paths between nodes using python and Graphviz (for graph visualization) this project is submitted to *Theory of Computation* subject CE, KMITL  
***for undirected graph**
#### G.LSV
Edit **G.LSV** if you want to change graph detail in adjacency matrix ('-' for unconnected)
Ex. if you have graph **'G'** that have nodes A, B, C, D node   

![](https://github.com/DreamN/ToC_Dijkstra-s-Algorithm/blob/master/example_graph.PNG?raw=true)

- p is connected to q with length 3
- p is connected to r with length 8
- p is connected to s with length 2
- r is connected to s with length 4

```python
p,q,r,s
-,3,8,2
3,-,-,- 
8,-,-,4
2,-,4,-
```
##### To Install Graphviz
We have to install “Graphviz Python Package” for generate DOT(DOT is a plain text graph description language.) and “Graphviz” for render generated dot source code to picture
-	Graphviz Python package
Just Enter Command “pip install graphviz” (pip is a package management system used to install and manage software packages written in Python. for more detail please visit https://pip.pypa.io/en/stable/installing/)
-	Graphviz
Program Installer can be found on the link http://www.graphviz.org/Download.php)
