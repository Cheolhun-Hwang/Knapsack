import pandas as pd
import numpy as np
from random import *
import datetime

class knapsack:
    def __init__(self, cross_over="one_point", mutation=0.05, population=100,
                 gene_method="general", selection="tournament", min_generation=200, next_parent=5):
        print(">> Init knapsack..")
        self.cross_over = cross_over
        self.mutation = mutation
        self.population = population
        self.gene_method = gene_method
        self.selection = selection
        self.gene_history = []
        self.best_gene = []
        self.min_generation = min_generation
        self.next_parent=next_parent
        self.init_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def startGene(self):
        self.start_gene_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def endGene(self):
        self.end_gene_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def getStartGene(self):
        return self.start_gene_datetime

    def getEndGene(self):
        return self.end_gene_datetime

    def breakPoint(self):
        if(len(self.gene_history) > self.min_generation):
            if(self.gene_history[len(self.gene_history)-1][0] ==
                    self.gene_history[len(self.gene_history)-self.min_generation-1][0]):
                return False
        return True

    def saveBestGenHistory(self, vec, fit):
        import csv
        print("CSV >> " + str(vec))
        print("CSV >> " + str(fit))
        file_path = './log/gene/'
        file_name = str(self.init_datetime)+'_gene_history.csv'
        file_csv = open(file_path + file_name, mode='a', encoding='utf-8', newline="")
        wr = csv.writer(file_csv, delimiter=',')
        wr.writerow([fit, vec])
        file_csv.close()

    def orderFitness(self, w, p, vectors, capacity):
        temp = []
        for index in range(0, len(vectors), 1):
            vector = vectors[index]
            item_value = []
            for index2 in range(0, len(vector), 1):
                if(vector[index2] == 1):
                    item_value.append([round(p[index2]/w[index2], 4), w[index2], p[index2]])
            # Best fitness order, top is best!
            # item_value.sort(key=lambda x: x[0])
            # item_value.reverse()
            # Check Capacity And Calc Profit
            max_capacity = capacity
            max_profit = 0
            max_weight = 0
            for item in item_value:
                if((max_capacity-item[1])>=0):
                    max_profit+=item[2]
                    max_weight+=item[1]
                else:
                    max_profit = 0
                    max_weight = 0
                max_capacity -= item[1]
            temp.append([max_profit+max_weight, vector])
        # Best fitness order, top is best!
        temp.sort(key=lambda x: x[0])
        temp.reverse()
        return temp

    def initChromosome(self, list_length):
        chromo = []
        for index in range(0, self.population, 1):
            row = []
            for index2 in range(0, list_length, 1):
                row.append(randint(0, 1))
            chromo.append(row)
        return chromo

    def onePointXover(self, x1, x2):
        x1_next = []
        cut_size = randint(0, len(x2) - 1)
        for index in range(0, cut_size, 1):
            x1_next.append(self.callMutation(x1[index]))
        for index in range(cut_size, len(x2), 1):
            x1_next.append(self.callMutation(x2[index]))
        return x1_next

    def twoPointXover(self, x1, x2):
        x1_next=[]
        cut_size_1 = randint(0, len(x2) - 2)
        cut_size_2 = randint(cut_size_1, len(x2) - 1)
        for index in range(0, cut_size_1, 1):
            x1_next.append(self.callMutation(x1[index]))
        for index in range(cut_size_1, cut_size_2, 1):
            x1_next.append(self.callMutation(x2[index]))
        for index in range(cut_size_2, len(x2), 1):
            x1_next.append(self.callMutation(x1[index]))
        return x1_next


    def callMutation(self, number):
        if random() < self.mutation:
            return number
        else:
            return randint(0, 1)

    def geneMethod(self, before_chromo):
        if(self.selection == 'tournament'):
            # Select 5 of Best Fitness gene
            temp = []
            for index in range(0, self.next_parent, 1):
                temp.append(before_chromo.pop(0)[1])

            # Other Crossover and Mutation
            for index in range(0, len(before_chromo), 1):
                if(self.cross_over == "one_point"):
                    if(index == len(before_chromo)-1):
                        cross_result = self.onePointXover(before_chromo[index][1], before_chromo[0][1])
                    else:
                        cross_result = self.onePointXover(before_chromo[index][1], before_chromo[index + 1][1])
                    temp.append(cross_result)
                elif(self.cross_over == "two_point"):
                    if (index == len(before_chromo) - 1):
                        cross_result = self.twoPointXover(before_chromo[index][1], before_chromo[0][1])
                    else:
                        cross_result = self.twoPointXover(before_chromo[index][1], before_chromo[index + 1][1])
                    temp.append(cross_result)
                else:
                    print(">> Error... Not define crossover method...")
            return temp
        elif(self.selection == "roulette"):
            print(">> Error... Not define roulette selection method...")
        else:
            print(">> Error... Not define selection method...")

    def train(self, weight=None, price=None, capacity=0):
        gene = 0
        print(">>Train X, y")
        if( (weight==None) or (price==None) or  (capacity==0)):
            print(">> Error : Check input dataset...")
            return -1, None

        # Start Gene
        self.startGene()

        # Init Chromosome
        self.gene_chromosome = self.initChromosome(list_length=len(weight))

        # repeat Generation
        while(self.breakPoint()):
            print("####################################################################")
            print("Gene : " + str(gene))
            print("Population : " + str(len(self.gene_chromosome)))
            fitness_list = self.orderFitness(w=weight, p=price, vectors=self.gene_chromosome, capacity=capacity)

            # Best Gene
            self.best_gene = fitness_list[0]

            # Save History
            self.gene_history.append(self.best_gene)

            # Save Log
            self.saveBestGenHistory(vec=self.best_gene[1], fit=self.best_gene[0])

            # Cross_over, Mutation, Selection
            self.gene_chromosome = self.geneMethod(before_chromo=fitness_list)

            # Next Generation
            gene+=1

        # End Gene
        self.endGene()

        return 0, self.best_gene