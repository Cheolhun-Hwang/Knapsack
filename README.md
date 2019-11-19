# Knapsack problem
- problem : `https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html`

## Class
- knapsack
 - param :
    - cross_over : method of Xover, `"one_point" [default]`, `"two_point"`
    - mutation : rate of mutation, `0.05 [default]`
    - population : size of population, `100 [default]`
    - gene_method : method of inheritance from parent to child, `"general" [default]`
    - next_parent : if you choose general inheritance method, define size of inheritance chromosome. `5 [default]`
    - selection : method of selection, now define just one. `"tournament" [default]`
    - min_generation : decide break point it stop if at least several generations of fitness are the same., `200 [default]`
 - train :
    - param :
        - capacity : `type : list`, `None [default]`
        - weight : `type : list`, `None [default]`
        - price : `type : list`, `None [default]`
    - return : 
        - opcode : `-1 : Error.` / `0 : Good.`
        - best_gene : result of generation
 - final result : 
    - best_gene : result of generation
    - getStartGene() : start datetime stamp of generation
    - getEndGene() : end datetime stamp of generation
 - log :
    - log/gene : save generation history.
    - row : generation / column[0] : fitness / column[1] : feature vector
 - fitness :
    - now defined fitness is simple. if you want to change, Change as much as you want. 
     ```
         # first, check weight and profit
         for index2 in range(0, len(vector), 1):
             if(vector[index2] == 1):
                 item_value.append([round(p[index2]/w[index2], 4), w[index2], p[index2]])
         # second, calc capacity and profit. 
         # panelty : if items overflow capacity, The maximum weight and profit are given as 0.
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
         # third, fitness = max_profit+max_weight
            temp.append([max_profit+max_weight, vector])
     ```
- solve : 
    - p01 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p01()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```
    - p02 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p02()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```
    - p03 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p03()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```
    - p04 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p04()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```
    - p05 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p05()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```
    - p06 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p06()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```
    - p07 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p07()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=200)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```
    - p08 : 
        ```
            item_size, item_capacity, item_w, item_p, true_y = data_p08()
            knapsack_01 = knapsack(cross_over="one_point", mutation=0.5, population=100,
                        gene_method="general", next_parent=5,
                        selection="tournament", min_generation=25000)
            opcode, best_gene = knapsack_01.train(capacity=item_capacity, weight=item_w, price=item_p)
        ```