class Chromosome:
    def __init__(self, chromosome,gene_number,reproduction_probability,fitness):
        self.chromosome=chromosome
        self.gene_number=gene_number
        self.reproduction_probability=reproduction_probability
        self.fitness=fitness
        if self.gene_number > 0 :
            self.map=''.join(str(chromosomee) for chromosomee in chromosome)
    
    def __eq__(self,another_chromosome):
        return self.map == another_chromosome.map