from random import choice

def get_best_child(node, problem):
    # Best child with minimum cost
    children = node.get_children()
    children_cost = [problem.cost_function(child) for child in children]
    min_cost = min(children_cost)
    best_child = choice([child for child_index, child in enumerate(children) if children_cost[child_index] == min_cost])
    return best_child

def steepest_ascent(problem, allow_sideways=False, max_sideways=100):
    # Steepest ascent with option of sideway move
    node = problem.start_state
    node_cost = problem.cost_function(node)
    path = []
    sideways_moves = 0
    while True:
        path.append(node)
        best_child = get_best_child(node, problem)
        best_child_cost = problem.cost_function(best_child)
        if best_child_cost > node_cost:
            break
        elif best_child_cost == node_cost:
            if not allow_sideways or sideways_moves == max_sideways:
                break
            else:
                sideways_moves += 1
        else:
            sideways_moves = 0
        node = best_child
        node_cost = best_child_cost
    return {'outcome': 1 if problem.is_goal(node) else 0, 'solution': path , 'problem': problem}

def random_restart(random_problem_generator, num_restarts=100, allow_sideways=False, max_sideways=100):
    # Random restart using steepest ascent
    path = []
    for _ in range(num_restarts):
        result = steepest_ascent(random_problem_generator(), allow_sideways, max_sideways)
        path += result['solution']
        if result['outcome'] == 1:
            break
    result['solution'] = path
    return result
