#Metaheuristic
    Sum of Subset Problem

* To run program you have to install:
    * NumPy
    * matplotlib

#### There are implemented 5 algorithms to solve the problem:
* BruteForce Algoritm
* HillClimbing Algoritm
* Tabu Algorithm
* Simmulated-Annealing Algorithm
* Genetic Algorithm

How to run algorithm:
<br />
Firstly, you can create new set of data by parameter -s or --size
* #####Example
```
python subset_sum.py -s {input size you wish} > {Path 
were you want to hold set of numbers}/{Name of file}
python subset_sum.py -s 10 > data/input/test
```
To Simply run program you just have to use:
```
python subset_sum.py -a {name algorithm you want to use} <{Path were
you hold set of numbers}/{Name of file}> {Path were you want to hold 
solution of the result}/{Name of file}
python subset_sum.py -a b <data/input/test> data/output/result
```
There are 2 modes yet debug -d and info -i which provide additional information of the
result

Furthermore you can simply run this program and enter set by yourself.
There is example file "tmp.png"
