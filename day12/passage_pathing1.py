def create_graph(input):
    graph = {}
    for row in input:
        node1 = row.split("-")[0]
        node2 = row.split("-")[1]
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]
        if node2 in graph:
            graph[node2].append(node1)
        else:
            graph[node2] = [node1]
    return graph

def find_paths(graph, start_node, path_so_far, all_paths):
    path_so_far_copy = path_so_far.copy()
    path_so_far_copy.append(start_node)
    if start_node == "end":
        all_paths.append(path_so_far_copy)
        return

    if start_node.islower():
        for cave in path_so_far:
            if start_node == cave:
                return

    for cave in graph[start_node]:
        find_paths(graph, cave, path_so_far_copy, all_paths)


inputFile = open("input12", "r")
input = inputFile.read().splitlines()

graph = create_graph(input)

all_paths = []
find_paths(graph, "start", [], all_paths)

print("The answer is: ", len(all_paths))



