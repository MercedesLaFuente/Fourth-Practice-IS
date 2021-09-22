from chromosome import Chromosome
import random
import copy






class Operations:

    chromosome_populations=[] 
    
    crossover_probability=0.00
    
    mutation_probability=0.000
    
    most_powerful_fitness=0
    
    reproduction_probabilities=[]



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
    
