import random
import matplotlib.pyplot as plt

origen = ''
distances = {}
population = []
population_size = 25
num_generations = 30
sel = 3

max_values = []
min_values = []
avg_values = []

def convert_to_distances(routes_output):
    dist = {}
    for route in routes_output:
        key = route.name
        if key not in dist:
            dist[key] = []

        for edge in route.possibleEdges:
            dist[key].append([edge])

    return dist

def generate_random_route():
    cities = set()
    for key in distances.keys():
        city_names = key.split('->')
        cities.update(city_names)
    cities = list(cities)
    cities.remove(origen)
    cities = list(cities)
    random.shuffle(cities)
    route = [origen] + cities

    connections = []
    for i in range(len(route) - 1):
        key = f"{route[i]}->{route[i + 1]}"
        connection_options = distances.get(key, [])
        connection = random.choice(connection_options) if connection_options else None
        for con in connection:
            connections.append(con)

    return route, connections

def evaluate_route(route_connections):
    total_distance = 0
    total_time = 0
    total_complexity = 0

    for connection in route_connections:
        total_distance += connection[1]
        total_time += connection[2]
        total_complexity += connection[3]
    return 0.4*total_distance + 0.4*total_time + 0.2*total_complexity

def selection(population):
    random_routes = random.sample(population, sel)
    best_routes = sorted(random_routes, key=lambda x: evaluate_route(x[1]))[:2]
    return best_routes

def combinar_genes(caso1, caso2):
    for case in caso2:
        if case in caso1:
            return None
    return [caso1 + caso2 ]

def crossover(parent1, parent2):
    while True:
        crossover_point = random.randint(0, len(parent1[1]) - 1)

        random_index = random.randint(0, 1)
        if random_index == 0:
            genes = [parent1, parent2]
        else:
            genes = [parent2, parent1]

        gen_1 = genes[0][1][:crossover_point]
        gen_2 = genes[1][1][crossover_point:]
        child = combinar_genes(genes[0][0][:crossover_point+1], genes[1][0][crossover_point+1:])
        if child is None:
            continue  # Genera nuevos casos si hay elementos comunes
        else:
            return child + ([gen_1 + gen_2]) # Retorna la concatenación si no hay elementos comunes

def get_route_details(route):
    details = []
    list_name_routes = []
    total_distance = 0
    for i in range(len(route[0]) - 1):
        details.append(f"{route[0][i]} -> {route[0][i+1]}: a {route[1][i][1]}m por {route[1][i][0]}")
        list_name_routes.append(route[1][i][0])
        total_distance += route[1][i][1]
    return details, total_distance, list_name_routes

def genetic_algorithm():
    population = [generate_random_route() for _ in range(population_size)]
    for generation in range(num_generations):
        # print(f"Generación {generation + 1}:")
        val_gen = []
        new_pop = []
        for individual in population:
            distance_route = evaluate_route(individual[1])
            val_gen.append(distance_route)
            # print(individual, distance_route)
            
        for _ in range(population_size):
            selected_individuals = selection(population)
            children = crossover(selected_individuals[0], selected_individuals[1])
            # mutated_children = [mutation(child) for child in children]
            new_pop.append(children)

        population = new_pop
        max_values.append(max(val_gen))
        min_values.append(min(val_gen))
        avg_values.append(sum(val_gen)/len(val_gen))

    val = float('inf')
    best_route = []
    for pop in population:
        if evaluate_route(pop[1]) < val:
            best_route = pop
    print("\nRuta más óptima:")
    print(best_route)
    details, total_distance, full_route = get_route_details(best_route)
    print("\nCaminos a tomar:")
    for detail in details:
        print(detail)
    print(f"\nDistancia total: {total_distance} m")
    showGraph()
    return {"routes": full_route}

def showGraph():
    # Crear una lista de generaciones para el eje x (puede ser simplemente el número de generación)
    generaciones = list(range(1, len(max_values) + 1))

    # Graficar los valores por generación
    plt.figure(figsize=(10, 6))
    plt.plot(generaciones, max_values, label='Mayor')
    plt.plot(generaciones, min_values, label='Menor')
    plt.plot(generaciones, avg_values, label='Promedio')

    # Añadir etiquetas y leyenda
    plt.xlabel('Generación')
    plt.ylabel('Valores')
    plt.title('Valores por Generación')
    plt.legend()

    # Mostrar la gráfica

    plt.grid(True)
    plt.show()