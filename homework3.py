import random
import math
import numpy as np

with open("input.txt") as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    no_of_cities = int(lines[0])
    cities = []
    #print(no_of_cities)
    for i in range(1,no_of_cities+1):
        cities.append([int(dim) for dim in lines[i].split(" ")])
#print(cities) 

def generate_population(pop_size, population):
    for i in range(int(pop_size)):
        city_copy = []
        city_copy = cities.copy()
        random.shuffle(city_copy)
        city_copy.append(city_copy[0])
        population.append(city_copy[:])
    return population

#print(population)

def calc_fitness(population):
    fitness = []
    for i in population:
        dist = 0
        for j in range(0, len(i)-1):
            dist += round(math.sqrt((i[j][0] - i[j+1][0])**2 + (i[j][1] - i[j+1][1])**2 + (i[j][2] - i[j+1][2])**2),4)
        fitness.append(dist)
    return fitness
    #print(fitness)

def fitness_prob(fitness):
    sum_fitness = sum(fitness)
    prob_fitness = [1/i for i in fitness]
    prob_fitness_final = [(i - min(prob_fitness))/(max(prob_fitness) - min(prob_fitness)) for i in prob_fitness]
    return prob_fitness_final



def roulette_wheel_selection(val, fitness, population):    
    # Computes for each chromosome the probability 
    #chromosome_probabilities = [chromosome.fitness/fitness_sum for chromosome in population]
    # Selects one chromosome based on the computed probabilities
    temp_pop = [i for i in range(0,len(population))]
    prob_fitness_final = fitness_prob(fitness)
    return random.choices(temp_pop, weights=prob_fitness_final, k=math.floor(val))

def mutate(num, population, fitness):
    temp_pop = [i for i in range(0,len(population))]
    temp_mutated_pop = random.choices(temp_pop, weights=fitness_prob(fitness), k=math.floor(num))
    mutated_pop =  [population[i] for i in temp_mutated_pop]
    #print(mutated_pop)
    for i in range(math.floor(num)):
        a = random.randint(0, no_of_cities)
        b = random.randint(0, no_of_cities)
        #print(a,b)
        #print(mutated_pop[i])
        #print(population[a], population[b])
        temp = mutated_pop[i][a]
        mutated_pop[i][a] = mutated_pop[i][b]
        mutated_pop[i][b] = temp
        #print(population[a], population[b])
    for i in mutated_pop:
        if i[0] != i[-1]:
            i[-1] = i[0]
    return mutated_pop
        
#mutate(1, population)

def crossover():
    pass

# def mate(num, population):
#     mutate(num, population)
#     crossover()



def new_population(pop_size, fitness, population):
    new_pop_max = []
    temp_set1 = roulette_wheel_selection(0.6*pop_size, fitness, population)
    set1 = [population[i] for i in temp_set1]
    set2 = mutate(0.3*pop_size, population, fitness)
    set3 = generate_population(0.1*pop_size, population)
    new_pop_max.extend(population)
    new_pop_max.extend(set1)
    new_pop_max.extend(set2)
    new_pop_max.extend(set3)
    #print(new_pop_max)
    new_pop_fitness = calc_fitness(new_pop_max)
    #print(new_pop_fitness)
    #print()
    new_pop = []
    while len(new_pop) <= pop_size:
        new_pop.append(new_pop_max[new_pop_fitness.index(min(new_pop_fitness))])
        #print(new_pop)
        new_pop_max.remove(new_pop_max[new_pop_fitness.index(min(new_pop_fitness))])
        #print(new_pop_max)
    return new_pop

def main():
    iterations = 100
    pop_size = 10
    population = []
    population = generate_population(pop_size, population)
    #print(population)
    fitness = calc_fitness(population)
    #print(fitness)
    prob_fitness_final = fitness_prob(fitness)
    #print(prob_fitness_final)
    #neww = roulette_wheel_selection( 0.5*pop_size, fitness, population)
    new_pop = new_population(pop_size, fitness, population)
    # for _ in range(iterations):
    #     #population = new_pop
    #     new_pop = new_population(pop_size, fitness, population)
    new_pop_fitness = calc_fitness(new_pop)
    print(new_pop_fitness)
    print(new_pop[new_pop_fitness.index(min(new_pop_fitness))])
    new_pop_final = new_pop[new_pop_fitness.index(min(new_pop_fitness))]
    f1 = open("output.txt", "w")
    for i in new_pop_final:
        for j in i:
            f1.write(str(j)+" ")
        f1.write("\n")
    f1.close()
    #print(new_pop)
    #print(neww)

main()
#[[173, 101, 186], [153, 196, 97], [199, 173, 30], [120, 199, 34], [137, 199, 93], [175, 53, 76], [144, 39, 130], [173, 101, 186]]

    



