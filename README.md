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

#### Results of the Second experiment
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{2482+2271+2035+3527+3914+5550+4568+2210+1050+3296+3819+2756+2676+2701+2735+3160+4411+3423+2409+3432}{20}" title="\Large x=\media" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\3121.25" title="\Large x=\media" />

#### Graphical analysis of generations with maximal fitness function 
     
![000000000](https://user-images.githubusercontent.com/74753713/134423479-d5af4764-7894-4945-90cb-3fe0e1450e19.png)



#### 3. Run the same experiment, but this time without mutation (pc = 0.7, pm = 0).

#### :arrow_down_small: Experiments and results:
  
 Execution number |  Generation in which the chromosome maximizing fitness function was found |  Execution time (Seconds)
  :---: | :---: | :---: 
  1 |  38 | 4.16633230
  2 |  20 | 2.83000810
  3 |  6 | 1.64157170          
  4 |  25 | 1.92745970          
  5 |  76 | 2.26325440           
  6 |  24 | 7.23245600           
  7 |  23 | 15.76359850           
  8 |  15 | 1.15684960           
  9 |  25 | 7.90881470           
  10 | 14 | 9.70879890            
  11 | 15 | 18.24805320           
  12 | 24 | 47.75926510          
  13 | 33 | 2.51084610           
  14 | 13 | 0.98148050           
  15 | 9  | 2.60891980           
  16 | 21  | 21.31831860            
  17 | 21  | 26.01965990           
  18 | 9  | 15.68466570           
  19 | 9  | 22.51416600            
  20 | 13 | 47.84324610

#### Results of the Third experiment
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{38+20+6+25+76+24+23+15+25+14+15+24+33+13+9+21+21+9+9+13}{20}" title="\Large x=\media" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\21.65" title="\Large x=\media" />


 
#### Graphical analysis of generations with maximal fitness function 
     
![07000000](https://user-images.githubusercontent.com/74753713/134423622-c2e0c6ab-542f-459f-9764-458e2c837342.png)


#### 4.1. Run the same experiment, but this time without mutation (pc = 0.9, pm = 0.001).
 

#### :arrow_down_small: Experiments and results:
  
 Execution number |  Generation in which the chromosome maximizing fitness function was found |  Execution time (Seconds)
  :---: | :---: | :---: 
  1 |  24 | 11.96011120
  2 |  20 | 19.76093240
  3 |  12 | 20.27765470          
  4 |  14 | 37.08264380         
  5 |  13 | 19.44398190           
  6 |  16 | 32.08531110           
  7 |  12 | 20.48242000           
  8 |  13 | 20.82789020           
  9 |  12 | 19.85624720           
  10 | 20 | 2.08549860            
  11 | 15 | 6.11905070           
  12 | 10 | 9.88138950           
  13 | 17 | 16.55346330          
  14 | 11 | 29.10531540           
  15 | 13  | 20.80233220           
  16 | 27  | 10.55097450            
  17 | 18  | 16.11696630            
  18 | 14  | 22.32696600           
  19 | 11  | 28.29959050            
  20 | 16 | 36.62015900 

#### Results of the Fourth experiment
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{24+20+12+14+13+16+12+13+12+20+15+10+17+11+13+27+18+14+11+16}{20}" title="\Large x=\media" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\15.4" title="\Large x=\media" />
    
#### Graphical analysis of generations with maximal fitness function 
 
![090001](https://user-images.githubusercontent.com/74753713/134423673-2ab32c85-2dd7-4bb8-85d8-0a785cde1aef.png)


#### 4.2. Run the same experiment, but this time without mutation (pc = 0.3, pm = 0.001).
 

#### :arrow_down_small: Experiments and results:
  
 Execution number |  Generation in which the chromosome maximizing fitness function was found |  Execution time (Seconds)
  :---: | :---: | :---: 
  1 |  17 | 1.26826350
  2 |  163 | 14.71855460
  3 |  42 | 15.85308280          
  4 |  33 | 22.10504350          
  5 |  23 | 30.34214130           
  6 |  35 | 4.27154930           
  7 |  52 | 15.41029200           
  8 |  20 | 13.16294510           
  9 |  18 | 27.38692610           
  10 | 17 | 37.38817980            
  11 | 29 | 2.73870760           
  12 | 10 | 2.81559650           
  13 | 16 | 10.29456540           
  14 | 15 | 23.55947040            
  15 | 12  | 22.22941030           
  16 | 97  | 7.35927310            
  17 | 20  | 5.83283670            
  18 | 19  | 12.34920180           
  19 | 27  | 36.9355500            
  20 | 13 | 25.75466900 

#### Results of the Fourth experiment
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{17+163+42+33+23+35+52+20+18+17+29+10+16+15+12+97+20+19+27+13}{20}" title="\Large x=\media" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\33.9" title="\Large x=\media" />
     
#### Graphical analysis of generations with maximal fitness function 
     

 ![03001](https://user-images.githubusercontent.com/74753713/134423736-2de27aee-df55-40e3-aca2-3cefd4c63472.png)

   
#### 4.3. Run the same experiment, but this time without mutation (pc = 0.5, pm = 0.001).
 

#### :arrow_down_small: Experiments and results:
  
 Execution number |  Generation in which the chromosome maximizing fitness function was found |  Execution time (Seconds)
  :---: | :---: | :---: 
  1 |  40 | 4.27282550
  2 |  20 | 7.94700230
  3 |  28 | 3.05053340          
  4 |  24 | 9.07533950         
  5 |  38 | 3.99639560           
  6 |  21 | 8.90077520           
  7 |  47 | 4.96965880           
  8 |  19 | 8.06619350          
  9 |  17 | 14.67843450           
  10 | 18 | 28.29504920           
  11 | 47 | 5.68776170           
  12 | 13 | 5.16924510           
  13 | 28 | 26.68898190           
  14 | 24 | 2.70849930            
  15 | 29  | 12.65698850           
  16 | 15  | 13.40490390            
  17 | 16  | 24.24160940            
  18 | 25  | 9.93420250           
  19 | 17  | 15.81546580            
  20 | 18 | 28.74635280 

#### Results of the Fourth experiment
<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{40+20+28+24+38+21+47+19+17+18+47+13+28+24+29+15+16+25+17+18}{20}" title="\Large x=\media" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\25.2" title="\Large x=\media" />

#### Graphical analysis of generations with maximal fitness function 
     
![0050001](https://user-images.githubusercontent.com/74753713/134423792-e1dd7c8f-e0ca-4f6a-bf91-2fa647805f5f.png)

### 5. What is the best choice of parameters according to the results obtained above? Why?

#### :arrow_down_small: Comparisons of the best times of all experiments with different parameters

![image](https://user-images.githubusercontent.com/74753713/134429140-2b2671d8-0a9c-4962-99ac-acd71e1bc37c.png)

#### :arrow_down_small: Comparisons of the best results of the generations obtained from all the experiments with different parameters
 
![image](https://user-images.githubusercontent.com/74753713/134429250-b19eda8b-2263-4b51-b6a6-ac1693970f08.png)

After the execution of the experiments carried out in the previous points, all the resulting data were taken as a reference to be able to work with them making a comparison table taking first as a priority the time in which the parameters that obtained a better performance are those of a probability of crossover of 0.7 and of mutation of 0. 001 which are executed in 0.85 seconds, now taking as priority the number of the resulting generation with the fastest maximum fitness function found, it was obtained that its resulting parameters are those of a probability of croosover of 0.7 and a probability of mutation of 0 which gives us 6 as the generation with the maximum fitness function.
It can be evidenced that a crossover probability that is less or more than 0.7 does not give us an optimal solution in terms of time and generations but all this individually since the results of the averages show that the more croosover you have, the average of all the populations that were generated will find the maximum function in one of their chromosomes faster than with a low croosover due to the continuous exchange of genes which gives a higher probability of finding the maximum fitness function.
Reviewing exhaustively the results that perform worse, it can be seen that those with a lower probability of croosover are the ones that less quickly find the chromosome that maximizes the function, so also the probability of mutation being so low does not affect in a radical way the improvement or worsening of the execution of the program. 

 


