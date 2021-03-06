from chromosome import Chromosome
import random
import copy
import timeit
import time
import numpy as np
from matplotlib import pyplot as plt


class Operations:

    chromosome_populations=[] 
    reproduction_probabilities=[]
    generations=[]
    fitness_minimums=[]
    fitness_maximums=[]
    fitness_average=[]
    crossover_probability=0.00
    mutation_probability=0.000
    most_powerful_fitness=0
    generation=1
    

    def set_crossover_probability(self,probability):
        self.crossover_probability=probability
    
    def set_mutation_probability(self,mutation):
        self.mutation_probability=mutation

    def get_gene_number(chromosome):
        return chromosome.gene_number

    def add_chromosome(self,chromosome): 
        self.chromosome_populations.append(chromosome) 

    def set_powerful_fitness(self,number):
        self.most_powerful_fitness=number


    def get_chromosome(self,position):
        return self.chromosome_populations[position]

    def get_chromosomes_populations_size(self): 
        count=0
        for chromosome in self.chromosome_populations:
            count=count+1
        return count
    
    def generate_random_chromosome(gene_number):
        chromosome = [0] * gene_number
        for i in range(gene_number):
            chromosome[i]=random.randint(0,1)
        return chromosome
    
    def generate_random_chromosome_populations(self,population_size,gene_number,crossover,mutation):
        for i in range(population_size):
            random_chromosome=Operations.generate_random_chromosome(gene_number)
            self.chromosome_populations.append(Chromosome(random_chromosome,gene_number,0.0,self.get_fitness_function_master(random_chromosome)))
        self.set_powerful_fitness(gene_number)
        self.crossover_probability=crossover
        self.mutation_probability=mutation

    def get_fitness_function_master(self,chromosome):
        return sum(chromosome)

    def get_fitness_function(self,position):
        chromosome=self.get_chromosome(position).chromosome
        return sum(chromosome)


    def get_fitness_population_function(self):
        total_sum=0
        count=0
        for chromosome in self.chromosome_populations:
            total_sum=total_sum+chromosome.fitness
            count=count+1
        return total_sum
    
    def get_probabilities_reproduction(self):
        fitness_population=self.get_fitness_population_function()
        populations=self.chromosome_populations
        i=0
        for chromosome in populations:
            individual_fitness=self.get_fitness_function_master(chromosome.chromosome)
            if fitness_population>0:
                reproduction_probability=individual_fitness/fitness_population
            else:
                reproduction_probability=0.0
            chromosome.reproduction_probability=reproduction_probability
            i=i+1

    def get_all_reproduction_probabilities(self):
        self.reproduction_probabilities=[]
        for chromosome in self.chromosome_populations:
            self.reproduction_probabilities.append(chromosome.reproduction_probability)
    
    def get_reproduction_probabilities(self):
        return self.reproduction_probabilities

    def crossover(self,chromosome1,chromosome2,position):
        copy_1=copy.deepcopy(chromosome1)
        copy_2=copy.deepcopy(chromosome2)
        offspring1=copy.deepcopy(chromosome1)
        offspring2=copy.deepcopy(chromosome2)
        offspring1.chromosome=copy_1.chromosome[:position]+copy_2.chromosome[position:]
        copy_1=copy.deepcopy(chromosome1)
        copy_2=copy.deepcopy(chromosome2)
        offspring2.chromosome=copy_2.chromosome[:position]+copy_1.chromosome[position:]
        fitness1=self.get_fitness_function_master(offspring1.chromosome)
        fitness2=self.get_fitness_function_master(offspring2.chromosome)
        offspring1.fitness=fitness1
        offspring2.fitness=fitness2
        offspring1.reproduction_probability=0.0
        offspring2.reproduction_probability=0.0
        return offspring1,offspring2

    def mutation(self,chromosome):
        new_chromosome=copy.deepcopy(chromosome)
        position_to_mutate=random.randint(0,(new_chromosome.gene_number-1))
        new_chromosome.chromosome[position_to_mutate]=(new_chromosome.chromosome[position_to_mutate]+1)%2
        fitness=self.get_fitness_function_master(new_chromosome.chromosome)
        new_chromosome.fitness=fitness
        new_chromosome.reproduction_probability=0.0
        return new_chromosome


    def create_new_generation_of_chromosomes(self):
        new_chromosome_population=[]
        self.get_probabilities_reproduction()
        self.get_all_reproduction_probabilities()
        while len(new_chromosome_population) < self.get_chromosomes_populations_size():
            if sum(self.reproduction_probabilities)>0:
                selected_chromosomes=tuple(random.choices(copy.deepcopy(self.chromosome_populations),weights=copy.deepcopy(self.reproduction_probabilities),k=2))
                chromosomex=selected_chromosomes[0]
                chromosomey=selected_chromosomes[1]
                if random.random() < self.crossover_probability:
                    position=random.randint(0,(len(chromosomex.chromosome)-1))
                    tuple_chromosome=self.crossover(chromosomex,chromosomey,position)
                    chromosomex=tuple_chromosome[0]
                    chromosomey=tuple_chromosome[1]
                if random.random() < self.mutation_probability:
                    chromosomex=self.mutation(chromosomex)
                    chromosomey=self.mutation(chromosomey)
                if len(new_chromosome_population) < self.get_chromosomes_populations_size():
                    chromosomex.reproduction_probability=0.0
                    new_chromosome_population.append(chromosomex)
                if len(new_chromosome_population) < self.get_chromosomes_populations_size():
                    chromosomey.reproduction_probability=0.0
                    new_chromosome_population.append(chromosomey)  
            else:
                new_chromosome_population=self.chromosome_populations
                return new_chromosome_population
        return new_chromosome_population    
    

    def find_the_most_powerful_fitness(self,poblations):
        count=0
        for poblation in poblations:
            fitness=self.get_fitness_function_master(poblation.chromosome)
            count=count+fitness
            if fitness == self.most_powerful_fitness:
                return self.generation
        if  count==0:
            return -1 
        return 0
    
    def find_the_fitness_maximums(self,poblations):
        max_fitness=0
        for poblation in poblations:
            current_fitness=self.get_fitness_function_master(poblation.chromosome)
            if current_fitness > max_fitness:
                max_fitness=current_fitness
        self.fitness_maximums.append(max_fitness)

    def find_the_fitness_minimums(self,poblations):
        min_fitness=100
        for poblation in poblations:
            current_fitness=self.get_fitness_function_master(poblation.chromosome)
            if current_fitness < min_fitness:
                min_fitness=current_fitness
        self.fitness_minimums.append(min_fitness)
    
    def find_the_fitness_average(self,poblations):
        sum=0
        cont=1
        for poblation in poblations:
            sum=sum+self.get_fitness_function_master(poblation.chromosome)
            cont=cont+1
        average=sum/cont
        self.fitness_average.append(average)


    def print_solution_population(self,poblations):
        print("------------------------------------     POPULATION SOLUTION         ----------------------------------------")
        for poblation in poblations:
            fitness=self.get_fitness_function_master(poblation.chromosome)
            if fitness == self.most_powerful_fitness:
                print("------------------------------------     CHROMOSOME RESULT          ----------------------------------------")
                Operations.print_chromosome(poblation.chromosome)
                print(" Fitness="+str(poblation.fitness))
                print("------------------------------------------------------------------------------------------------------------")
            else:
                Operations.print_chromosome(poblation.chromosome)
                print(" Fitness="+str(poblation.fitness))
                
    def print_chromosome(chromosome):
        print('[',end='')
        for value in chromosome:
            print(value ,end='') 
            print(' ',end='')
        print(']',end='')
        print()

    def print_chromosomes(self):
        print('{',end='')
        for chromosome in self.chromosome_populations:
            Operations.print_chromosome(chromosome.chromosome)
            print(' ',end='')
        print('}',end='')
        print()


    def genetic_algorithm(self):
        current_fitness=self.find_the_most_powerful_fitness(self.chromosome_populations)
        while current_fitness == 0  :
            new_poblation=self.create_new_generation_of_chromosomes()
            self.generation=self.generation+1
            self.chromosome_populations=new_poblation
            current_fitness=self.find_the_most_powerful_fitness(new_poblation)
        if current_fitness != 0:
            self.print_solution_population(new_poblation)
            self.generations.append(current_fitness)
            return current_fitness

    def genetic_algorithm_with_limit(self,num_generation):
        cont=0
        while cont < num_generation:
            new_poblation=self.create_new_generation_of_chromosomes()
            self.generation=self.generation+1
            self.chromosome_populations=new_poblation
            self.find_the_fitness_maximums(self.chromosome_populations)
            self.find_the_fitness_minimums(self.chromosome_populations)
            self.find_the_fitness_average(self.chromosome_populations)
            cont=cont+1
        x=np.array(range(len(self.fitness_maximums)))
        y=np.zeros(len(x))
        for i in range(len(x)):
            y[i]=self.fitness_maximums[i]
        x_2=np.array(range(len(self.fitness_minimums)))
        y_2=np.zeros(len(x_2))
        for i in range (len(x)):
            y_2[i]=self.fitness_minimums[i]
        x_3=np.array(range(len(self.fitness_average)))
        y_3=np.zeros(len(x_3))
        for i in range(len(x_3)):
            y_3[i]=self.fitness_average[i]
        #graphic 1
        plt.figure(figsize=(11,11))
        plt.subplot(2,2,1)
        plt.plot(x, y,'r')
        plt.title('Max')
        plt.xlabel('Generation')
        plt.ylabel('Fitness Fuction')

        #graphic 2
        plt.subplot(2,2,2)
        plt.plot(x_2, y_2,'g')
        plt.title('Min')
        plt.xlabel('Generation')
        plt.ylabel('Fitness Fuction')

        #graphic 3
        plt.subplot(2,2,3.3)
        plt.plot(x_3, y_3,'b')
        plt.title('Average')
        plt.xlabel('Generation')
        plt.ylabel('average fitness')
        plt.show()
        


    def initializate_all(self,poblation_size,number_genes,crossover,mutation):
        operation=Operations()
        operation.generate_random_chromosome_populations(poblation_size,number_genes,crossover,mutation)
        operation.print_chromosomes()
        values=operation.genetic_algorithm()
        return values

    def initializate_all_with_generation(self,poblation_size,number_genes,crossover,mutation,num_generation):
        operation=Operations()
        operation.generate_random_chromosome_populations(poblation_size,number_genes,crossover,mutation)
        values=operation.genetic_algorithm_with_limit(num_generation)

def main():
    option=0
    operation= Operations()
    while option != 3:
        print("Welcome to the Genetic Algorithm Menu")
        print("To run the algorithm remember to enter the number of chromosomes and the number of genes you will have. ")
        print("1) Run algorithm")
        print("2) Plot the program running in 100 generations")
        print("3) Exit")
        option=int(input())
        if option == 1:
            print("Enter the chromosome numbers")
            chromosome_number=int(input())
            print("Enter the numbers of the genes of each chromosome.")
            genes_number=int(input())
            print("Enter the crossover probability")
            crossover=float(input())
            print("Enter the mutation probability.")
            mutation=float(input())
            start=timeit.default_timer()
            generation=operation.initializate_all(chromosome_number,genes_number,crossover,mutation)
            if generation == -1:
                print("The generation could no longer be reproduced")
            else:
                print("The strongest chromosome was found in the generation: "+ str(generation))
            end=timeit.default_timer()
            times=end-start
            print("Time of ejecution: " + format(times, '.8f'))
        if option == 2:
            print("Remember that the default test data is 100 chromosome populations with 20 genes each with croossover probabilities of 0.7 and 0.001.")
            time.sleep(2)
            chromosome_number=100
            genes_number=20
            crossover=0.7
            mutation=0.001
            num_generation=100
            result=operation.initializate_all_with_generation(chromosome_number,genes_number,crossover,mutation,num_generation)







if __name__ == '__main__':
    main()
