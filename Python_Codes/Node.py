from copy import deepcopy
import math


class Node:

    def __init__(self, initial_input, node_number):

        self.real_cost = [int(i) for i in initial_input[node_number]]
        self.vector = [int(i) for i in initial_input[node_number]]
        self.total_distance_vector = []
        self.node_number = node_number
        self.iteration_number = 0
        self.new_information = 1
        self.neighbors = []
        self.queue = []

        for i in range(len(self.real_cost)):

            if (self.real_cost[i] == 0) & (i != self.node_number):

                (self.vector[i]) = math.inf

        for i in range(len(self.real_cost)):

            if (self.vector[i] != 0) & (self.vector[i] != math.inf):

                self.neighbors.append(i)

        self.all_nodes = deepcopy(self.neighbors)
        self.all_nodes.append(node_number)
        self.all_nodes.sort()
        self.distance_vector = [[]] * (len(self.all_nodes))

    def vector_update(self):

        # this method updates the distance vector in each interation

        if len(self.queue) > 0:  # checks to see if there is new information

            temp_vector = [[] for _ in self.vector]
            temp_queue = deepcopy(self.queue)
            self.queue = []

            for queued in temp_queue:

                self.distance_vector[self.all_nodes.index(queued.index(0))] = queued

            # updating distance vector based on Bellman-Ford equation
            for node in range(len(self.vector)):

                if node == self.node_number:

                    temp_vector[node].append(0)
                    continue

                for neighbor in self.neighbors:

                    self_to_neighbor = deepcopy(self.real_cost[neighbor])
                    neighbor_to_node = self.distance_vector[self.all_nodes.index(neighbor)][node]
                    self_to_node = self_to_neighbor + neighbor_to_node
                    temp_vector[node].append(self_to_node)

            temp_vector = [min(i) for i in temp_vector]

            if temp_vector != self.vector:

                self.vector = temp_vector
                self.new_information = 1

            self.distance_vector[self.all_nodes.index(self.node_number)] = temp_vector
            self.total_distance_vector.append([])

            for vector in self.distance_vector:

                self.total_distance_vector[self.iteration_number].append(vector)

            self.iteration_number += 1

    def link_update(self, other_node, new_cost):

        # this method updates the link cost to its new value

        if self.real_cost[other_node] != new_cost:

            self.real_cost[other_node] = new_cost
            self.new_information = 1

    def show_dv(self):

        # this method shows the distance vector for all iteration

        for i in range(len(self.total_distance_vector)):

            print(f"\n----iteration number {i+ 1}----")

            for vector in self.total_distance_vector[i]:

                print(f"node {vector.index(0)} --> {vector}")
