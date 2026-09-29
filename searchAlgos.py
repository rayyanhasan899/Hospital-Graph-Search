import math
import heapq

# Hospital coordinates from Task 3

locations = {
    "Pharmacy": (0, 0),
    "Main_Corridor": (2, 1),
    "Patient_Wing": (1, 4),
    "Nursing_Station": (4, 2),
    "Laboratory": (5, 5),
    "Emergency_Ward": (8, 6)
}

# Hospital weighted graph from Task 3

hospital_graph = {
    "Pharmacy": {
        "Main_Corridor": 2.2,
        "Patient_Wing": 4.1
    },
    "Main_Corridor": {
        "Nursing_Station": 2.2
    },
    "Patient_Wing": {
        "Laboratory": 5.0
    },
    "Nursing_Station": {
        "Laboratory": 3.2,
        "Emergency_Ward": 6.0
    },
    "Laboratory": {
        "Emergency_Ward": 3.2
    },
    "Emergency_Ward": {}
}


def heuristic(current, goal):
    x1, y1 = locations[current]
    x2, y2 = locations[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def reconstruct_path(came_from, current):
    path = []

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


def gbfs(start, goal):
    frontier = []
    counter = 0

    heapq.heappush(
        frontier,
        (heuristic(start, goal), counter, start)
    )

    came_from = {start: None}
    visited = set()

    while frontier:
        _, _, current = heapq.heappop(frontier)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = reconstruct_path(came_from, goal)
            cost = sum(
                hospital_graph[path[i]][path[i + 1]]
                for i in range(len(path) - 1)
            )
            return path, cost

        for neighbor in hospital_graph[current]:
            if neighbor not in visited and neighbor not in came_from:
                counter += 1
                came_from[neighbor] = current

                heapq.heappush(
                    frontier,
                    (
                        heuristic(neighbor, goal),
                        counter,
                        neighbor
                    )
                )

    return None, None


def a_star(start, goal):
    frontier = []
    counter = 0

    heapq.heappush(
        frontier,
        (heuristic(start, goal), counter, start)
    )

    g_cost = {start: 0.0}
    came_from = {start: None}
    visited = set()

    while frontier:
        _, _, current = heapq.heappop(frontier)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return reconstruct_path(came_from, goal), g_cost[goal]

        for neighbor, edge_cost in hospital_graph[current].items():
            tentative_g = g_cost[current] + edge_cost

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                came_from[neighbor] = current
                counter += 1

                f_cost = tentative_g + heuristic(
                    neighbor,
                    goal
                )

                heapq.heappush(
                    frontier,
                    (f_cost, counter, neighbor)
                )

    return None, None
