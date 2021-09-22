# FOURTH PRACTICE INTELLIGENT SYSTEMS :computer:
# GENETIC ALGORITHMS

<p align="center">
     <img src="https://i.pinimg.com/originals/74/9f/d0/749fd043d6359a42556018a07f085c2e.gif?raw=true" alt="Sublime's custom image"/>
</p>

## NAMES 📋
* Balderrama Mauricio
* Canedo Juan Luis
* La Fuente Mercedes

### IMPORTANT! HOW TO USE :hammer:
* For a better reading of the document desable dark mode if your git is configured that way because the formulas in latex do not change the font color to white so it is lost with the background.
* Clone from the main repository using: 

     -git clone (repository link)
* For the correct functioning of the code you first need to install numpy and matplotlib from the console with the following command:                   

     -pip install numpy

     -pip install matplotlib
* Insert in the console terminal 'python operations.py' to start the program
* The program will ask you to enter the size of the chromosome population, the number of genes it will have, its probability of crossover and mutation.

## PROBLEM SOLVER AGENT ⚙️

### Objective Formulation:
Implement a genetic algorithm that allows to create new generations and from these to find the chromosome with the fitness function.

### Problem Formulation:

### Initial State:
A population of 100 chromosomes with random values varying from 0 to 1 and each with 20 genes.  

![Cromosomas](https://user-images.githubusercontent.com/74753713/134265512-3477ec4f-3f20-4f2b-8e10-1327aee62dd1.png)

### Objective State:
A generation of chromosomes that has one chromosome that gives its maximum fitness function of the entire population.


![Cromosomas solution](https://user-images.githubusercontent.com/74753713/134265649-00761b29-31a4-4eb8-8367-e77a27e003d8.png)

 
### Test of Objective:
Does the new generation of chromosomes have one that gives the maximum fitness function?
  
### Actions:
* Selection
* Crossover
* Mutation


## DESCRIPTION OF THE PROBLEM
Generate a genetic algorithm that uses the three operations of selection, crossover and mutation where each chromosome has a size of 20 genes formed by 0 and 1 randomly and with a fitness function that is the sum of all the 1's it has.

## SOLUTION DESCRIPTION
The program allows to generate a population of n chromosomes with m genes that can result in new generations with the same dimensions until a population is found that has a chromosome that maximizes the fitness function. 

## EXPERIMENTS :round_pushpin:
#### 1. Execute the algorithm 20 times, for each run report in which generation the strongest chromosome was found. It reports the average of this value.

#### :arrow_down_small: Experiments and results:
  
 Execution number |  Generation in which the chromosome maximizing fitness function was found |  Execution time (Seconds)
  :---: | :---: | :---: 
  1 |  27 | 2.0920228
  2 |  46 | 3.51054270
  3 |  31 | 4.17165080           
  4 |  21 | 4.05299050           
  5 |  17 | 9.58204390            
  6 |  16 | 2.05639420            
  7 |  16 | 4.99665710           
  8 |  15 | 5.08417860           
  9 |  21 | 2.99087550            
  10 | 17 | 1.31381980            
  11 | 19 | 1.4611559           
  12 | 39 | 3.01303800           
  13 | 11 | 0.84852360           
  14 | 137 | 10.60351280            
  15 | 18  | 2.08811830           
  16 | 26  | 1.99200670            
  17 | 26  | 2.05647480            
  18 | 26  | 1.99472350           
  19 | 42  | 3.20709420            
  20 | 259 | 19.74819710 

#### Results of the First experiment
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{27+46+31+21+17+16+16+15+21+17+19+39+11+137+18+26+26+26+42+259}{20}" title="\Large x=\media" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\41.5" title="\Large x=\media" />

#### Graphical analysis of generations with maximal fitness function 
     
![070001](https://user-images.githubusercontent.com/74753713/134423433-8eec0623-1b69-4233-b004-91647d8e94f0.png)

     
  
#### 2. Run the same experiment, but this time without a crossover (pc = 0, pm = 0.001).
 

#### :arrow_down_small: Experiments and results:
  
 Execution number |  Generation in which the chromosome maximizing fitness function was found |  Execution time (Seconds)
  :---: | :---: | :---: 
  1 |  2482 | 808.68809650
  2 |  2271 | 189.15336200
  3 |  2035 | 165.90020550           
  4 |  3527 | 283.52049000          
  5 |  3914 | 318.77318160           
  6 |  5550 | 467.17887110            
  7 |  4568 | 385.61297700           
  8 |  2210 | 185.97664470           
  9 |  1050 | 80.76308920            
  10 | 3296 | 256.78795930            
  11 | 3819 | 324.55585480           
  12 | 2756 | 245.24642600           
  13 | 2676 | 225.60762970           
  14 | 2701 | 221.87798070            
  15 | 2735  | 226.80944650          
  16 | 3160  | 252.98513080            
  17 | 4411  | 372.09641260            
  18 | 3423  | 237.83675700           
  19 | 2409  | 190.25674710            
  20 | 3432 | 283.31913680 

#### Results of the First experiment
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{2482+2271+2035+3527+3914+5550+4568+2210+1050+3296+3819+2756+2676+2701+2735+3160+4411+3423+2409+3432}{20}" title="\Large x=\media" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\3121.25" title="\Large x=\media" />

#### Graphical analysis of generations with maximal fitness function 
     
![000000000](https://user-images.githubusercontent.com/74753713/134423479-d5af4764-7894-4945-90cb-3fe0e1450e19.png)


