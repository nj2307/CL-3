import random 

# Define the objective function 
def objective_function(x): 
    return -x**2 + 4 

# Generate initial population 
def generate_initial_population(pop_size=10): 
    return [random.uniform(-10, 10) for _ in range(pop_size)] 

# Calculate fitness of each antibody 
def calculate_fitness(population): 
    return [objective_function(x) for x in population] 

# Clone and mutate 
def clone_and_mutate(antibody, clone_factor=1): 
    # Simple mutation: slight random change 
    return antibody + random.uniform(-clone_factor, clone_factor) 

# The Clonal Selection Algorithm 
def clonal_selection(iterations=100, pop_size=10): 
    population = generate_initial_population(pop_size) 
    for _ in range(iterations): 
        # Calculate fitness 
        fitness = calculate_fitness(population) 
         
        # Select the best half of the population 
        sorted_pop = [x for _, x in sorted(zip(fitness, population), reverse=True)] 
        selected = sorted_pop[:len(sorted_pop)//2] 
         
        # Clone and mutate the selected antibodies 
        clones = [clone_and_mutate(x) for x in selected for _ in range(2)]  # Each selected antibody generates 2 clones 
         
        # Form new population with clones and calculate new fitness 
        population = clones 
        fitness = calculate_fitness(population) 
         
        # Keep the best solution 
        best_index = fitness.index(max(fitness)) 
     
    return population[best_index] 

# Run the algorithm 
best_solution = clonal_selection() 
print(f"Best solution: {best_solution}") 
print(f"Maximum value: {objective_function(best_solution)}")
