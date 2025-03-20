# -*- coding: utf-8 -*-
"""a_star_search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sopKqWmX1hgw6eUvWcATTcCAHtr9h9CI
"""

from os import path
from queue import PriorityQueue


def a_star_tree_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    path = {}

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("Goal node found!")
            route = reconstruct_path(path, start, goal)
            print("Route optimal:", route)
            return True

        for neighbour, cost in graph[current_node].items():
            priority = heuristic[neighbour] + cost
            frontier.put((priority, neighbour))
            path[neighbour] = current_node

    print("Goal node not found!")
    return False


def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    path = {}
    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("Goal node found!")
            route = reconstruct_path(path, start, goal)
            print("Route optimal:", route)
            return True

        explored.add(current_node)

        for neighbour, cost in graph[current_node].items():  # Corrected spelling
            if neighbour not in explored:
                total_cost = cost + heuristic[neighbour]
                frontier.put((total_cost, neighbour))  # Corrected spelling
                path[neighbour] = current_node  # Corrected spelling

    print("Goal node not found!")
    return False


def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
       current = path[current]
       route.append(current)
    route.reverse()
    return route

heuristic = {
    'A': 4, 'B': 3, 'C': 3, 'D': 1, 'S': 6, 'G': 0
}

graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'D': 5, 'B': 1},
    'B': {'C': 2, 'D': 3},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1}
}



start_node = 'S'
goal_node = 'G'

a_star_tree_search(graph, start_node, goal_node, heuristic)

a_star_graph_search(graph, start_node, goal_node, heuristic)