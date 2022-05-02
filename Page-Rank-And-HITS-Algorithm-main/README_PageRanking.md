# Page Rank Algorithm

This is a Page Rank Algorithm for Information Retrieval. 
The Page Rank Algorithm is a classical algorithm used by search engines across the globe to rank the web page in their search results.   It is named after both the term "web page" and co-founder Larry Page. PageRank is a way of measuring the importance of website pages.PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is.The underlying assumption is that more important websites are likely to receive more links from other websites.It is not the only algorithm used by Google to order search engine results, but it is the first algorithm that was used by the company, and it is the best-known.

This assignment is provided to us by Professor N.L.Bhanu Murthy, IC of course CS F469. 

## Getting Started

- Install Python 3.6+

You need to install operators,matpotlib,nltk and numpy for page ranking. You can do it via pip:

```bash
pip3 install -U operators
pip3 install -U nltk
pip3 install -U numpy
```

### Queries

number of nodes n
number of connections e
edges: (e11,e12),(e21,e22),......,(ee1,ee2)


## Procedure

a.Counting the number of outgoing connections from a node-while (j<=nodes):
                                                          cnt=0
                                                          for i in connections:
                                                          if i[0]==j:
                                                          cnt=cnt+1
                                                          outcon.append(cnt)
                                                          j=j+1

b.Probability transition matrix

c.Eigen values and Left Eigen Vector of probability transition matrix-Using the linear algebra module in scipy.
eigenval,eigenleftvector=linalg.eig(a=np.array(PTM),b=None,left=True,right=False,overwrite_a=False,overwrite_b=False,check_finite=False)

d.Power method-np.array(matrix1)
               max_iterations = 1000
               atranspose = np.transpose(a)
               x=np.ones(len(a))
               y=np.ones(len(a))

e.Eigen value by using power method-for i in range(max_iterations):
                                    y = np.dot(atranspose, y)
                                    transpoweigen, y = normalise(y)

f.Displaying Page Rank:Principal left eigen vector indicates the probability of being on a web page with that node value.
    result=sorted(result,key=itemgetter(1),reverse=True)
    index=1
    for x in result:
    print(index,end="\t")
    for j in x:
    print(j,end="\t")
    index=index+1
    print("\n")

Page Rank Algorithm includes:
1. Store connections from the graph in a list.
2. Count the number of outgoing connections from a node
3. Constructing the probability transition matrix.
4. Calculate the left eigenvectors
5.Calculating eigen value using power method.
6. Displaying the Principal left eigenvalue which indicates the probability of being on each webpage.

**Test Case**  
Query: 4
       6
       1, 2
       2, 1
       2, 3
       3, 2
       3, 4
       4, 3

       Probability transition matrix without random teleportations:
       [[0. 1. 0. 0.]
       [0.5 0. 0.5 0.]
       0. 0.5 0. 0.5]
       [0. 0. 1. 0.]]
       list1: [0.31622777 0.63245553 0.63245553 0.31622777] 
       Principal Left eigenvector of probability transition matrix without random teleportations: 
       [0.1666666666666669, 0.33333333333333337, 0.3333333333333332, 0.1666666666666666]
       Probability transition matrix with random teleportations: 
       [[0.025 0.925 0.025 0.025]
       [0.475 0.025 0.475 0.025]
       [0.025 0.475 0.025 0.475]
       [0.025 0.025 0.925 0.025]]
       list: [-0.32933246 -0.62573168 -0.62573168 -0.32933246]
        Normalized Principal Left eigenvector of probability transition matrix with random teleportations: 
        [0.17241379310344843, 0.32758620689655166, 0.3275862068965518, 0.17241379310344826]


**Test Case**
Query: 3
       4
       2, 3
       1, 3
       1, 2
       2, 2

       Probability transition matrix without random teleportations:
       [[0. 0.5 0.5] 
       [0. 0.5 0.51]
       [0. 0. 0. ]]
       list1: []
       Principal Left eigenvector of probability transition matrix without random teleportations:
       []
       Probability transition matrix with random teleportations:
       [[0.03333333 0.48333333 0.48333333)]
       [0.03333333 0.48333333 0.48333333]
       [0.03333333 0.03333333 0.03333333]]
       list: [-0.08653593 -0.70445423 -0.70445423]
       Normalized Principal Left eigenvector of probability transition matrix with random teleportations:
       [0.05786636548846087, 0.4710668172557694, 0.4710668172557697]



### Contributors
Done by:
1. Sanchit Gupta (2020A7PS2069H)
2. Rahul Jauhari (2020A7PS0106H)
3. Abhiraj Khare (2020A7PS0161H)
