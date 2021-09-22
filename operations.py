from chromosome import Chromosome
import random

class Operations:

    chromosome_populations=[] 
    crossover_probability=0.00
    mutation_probability=0.000
    most_powerful_fitness=0
    reproduction_probabilities=[]

    def get_all_reproduction_probabilities(self):
        self.reproduction_probabilities=[]
        for chromosome in self.chromosome_populations:
            self.reproduction_probabilities.append(chromosome.reproduction_probability)
    
    def get_reproduction_probabilities(self):
        return self.reproduction_probabilities

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
            