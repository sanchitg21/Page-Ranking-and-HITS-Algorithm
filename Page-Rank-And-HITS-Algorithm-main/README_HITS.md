# HITS Algorithm

This is HITS Algorithm for Information Retrieval. 
Hyperlink-Induced Topic Search (also known as hubs and authorities) is a link analysis algorithm that rates Web pages, developed by Jon Kleinberg. The idea behind Hubs and Authorities stemmed from a particular insight into the creation of web pages when the Internet was originally forming; that is, certain web pages, known as hubs, served as large directories that were not actually authoritative in the information that they held, but were used as compilations of a broad catalog of information that led users direct to other authoritative pages. In other words, a good hub represents a page that pointed to many other pages, while a good authority represents a page that is linked by many different hubs.

This assignment is provided to us by Professor N.L.Bhanu Murthy, IC of course CS F469. 

## Getting Started

- Install Python 3.6+

You need to install networkx and numpy for HITS algorithm. You can do it via pip:

```bash
pip3 install -U networkx
pip3 install -U numpy
```

### Queries

The query contains a single string s.


## Procedure

The algorithm performs a series of iterations, each consisting of two basic steps:

Authority update: Update each node's authority score to be equal to the sum of the hub scores of each node that points to it. That is, a node is given a high authority score by being linked from pages that are recognized as Hubs for information.
Hub update: Update each node's hub score to be equal to the sum of the authority scores of each node that it points to. That is, a node is given a high hub score by linking to nodes that are considered to be authorities on the subject.



HITS Algorithm includes:
1. Obtaining the root set for the query.
2. Creating the adjacency matrix.
3. Getting Hub and Authority scores.
4. Creating the Base Set.
5. Repeating the process of calculating Hub and Authority scores.

a.Obtaining the root set-while (j<=nodes):arr = np.zeros(100)
                         for i in range(0,100) :
                         document = web_graph.nodes[i]['page_content']
                         temp=document.split()
                         for q in query:
                         if q in temp:
                         arr[i]=1
                         break
                         arr=np.array(arr)

b.Create adjacency matrix:dj=nx.to_numpy_array(web_graph)

c.Getting Hub Score-np.dot(arr,adj)

d.Getting Authority score-np.dot(arr,adj.T)
    
e.Creating the Base set-connection=[]
                        for i in range (0,100):
                        if(arr[i]!=0):
                        connection.append(i)


The Hub score and Authority score for a node is calculated with the following algorithm:

1. Start with each node having a hub score and authority score of 1.
2. Run the authority update rule
3. Run the hub update rule
4. Normalize the values by dividing each Hub score by square root of the sum of the squares of all Hub scores, and dividing each Authority score by square root of the sum of the squares of all Authority scores.
5. Repeat from the second step as necessary.


Setting no. of iterations for calculaitng hub and authority score-iteration=1000
                                                                    step=0
                                                                    while(step<=1000):
                                                                    step=step+
                                                                    authorityvector=np.dot(result.T,hubvector)
                                                                    hubvector=np.dot(result,authorityvector)
                                                                    hubvector=hubvector/sum(hubvector)
                                                                    authorityvector=authorityvector/sum(authorityvector)



**Test Case**  
Query:president

Node       Hub Values:
96         0.1529109123758905
99         0.3296491550138141
70         0.0
71         0.0
39         0.12450956017589539
80         0.3929303724344

Node       Authority values:
96         0.1268823238659383
99         0.25801878064507205
70         0.2781216582118615
71         0.2781216582118615
39         0.05885557906526657
80         0.0


**Test Case**
Query: vote

Node       Hub Values:
96         0.13285015359529084
33         0.14212299732207936
99         0.0915691322519779
70         0.0
39         0.1892042739468789
71         0.0
45         0.08427404677996897
80         0.15208559502908944 
19         0.09073435241842802
20         0.0
95         0.11715944865628661


Node       Authority Values:
96         0.03898906534275263
33         0.0
99         0.20188327514969684 
70         0.1037453326180986
39         0.15571397689625235 
71         0.1037453326180986 
45         0.0805609665464924 
80         0.0
19         0.2268433022600353 
20         0.08851874856857327
95         0.0


**Test Case**
Query: Google

Node       Hub Values:
32         0.0
47         0.2679491924311227
54         0.0
27         0.36602540378443865 
63         0.36602540378443865

Node       Authority Values:
32         0.3660254037844386
47         0.2679491924311227
54         0.3660254037844386
27         0.0
63         0.0



### Contributors
Done by:
1. Sanchit Gupta (2020A7PS2069H)
2. Rahul Jauhari (2020A7PS0106H)
3. Abhiraj Khare (2020A7PS0161H)
