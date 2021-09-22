from chromosome import Chromosome
class Operations:
    chromosome_populations=[] 
    crossover_probability=0.00
    mutation_probability=0.000
    most_powerful_fitness=0
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