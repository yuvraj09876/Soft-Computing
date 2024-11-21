import random

# Parameters
POPULATION_SIZE = 10
CHROMOSOME_LENGTH = 8
MUTATION_RATE = 0.1
GENERATIONS = 20

# Fitness function: Counts the number of 1s in the chromosome
def fitness(chromosome):
    return sum(chromosome)

# Generate a random chromosome
def create_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

# Initialize population
def initialize_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]

# Selection: Roulette Wheel Selection
def select_parent(population):
    total_fitness = sum(fitness(chromosome) for chromosome in population)
    if total_fitness == 0:  # Avoid division by zero
        return random.choice(population)
    selection_probs = [fitness(chromosome) / total_fitness for chromosome in population]
    return population[random.choices(range(POPULATION_SIZE), weights=selection_probs)[0]]

# Crossover: Single-point Crossover
def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Mutation: Flip bits randomly
def mutate(chromosome):
    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]  # Flip bit
    return chromosome

# Main Genetic Algorithm
def genetic_algorithm():
    # Initialize population
    population = initialize_population()

    for generation in range(GENERATIONS):
        print(f"Generation {generation + 1}")

        # Evaluate fitness of the population
        population = sorted(population, key=fitness, reverse=True)
        print("Best fitness:", fitness(population[0]), "Chromosome:", population[0])

        # Selection and creation of the next generation
        next_generation = population[:2]  # Elitism (keep top 2)

        while len(next_generation) < POPULATION_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            next_generation.append(mutate(offspring1))
            if len(next_generation) < POPULATION_SIZE:
                next_generation.append(mutate(offspring2))

        population = next_generation

    # Final result
    best_chromosome = max(population, key=fitness)
    print("\nBest solution:", best_chromosome, "Fitness:", fitness(best_chromosome))

# Run the Genetic Algorithm
if __name__ == "__main__":
    genetic_algorithm()