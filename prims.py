def prim(adj_matrix):
    num_vertices = len(adj_matrix)
    
    # Initialize key values, MST set, and parent array
    key = [999999] * num_vertices  # A large number instead of float('inf')
    mst_set = [False] * num_vertices
    parent = [-1] * num_vertices
    
    # Start from the first vertex
    key[0] = 0
    
    for _ in range(num_vertices):
        # Find the vertex with the minimum key value
        min_key = min([key[i] for i in range(num_vertices) if not mst_set[i]])
        current_vertex = key.index(min_key)
        
        # Include the current vertex in the MST
        mst_set[current_vertex] = True
        
        # Update key values of adjacent vertices
        for i in range(num_vertices):
            if 0 < adj_matrix[current_vertex][i] < key[i] and not mst_set[i]:
                key[i] = adj_matrix[current_vertex][i]
                parent[i] = current_vertex

    return key, parent


# Example usage:
print("Enter the adjacency matrix for the graph (weights, use 0 for no edge):")
adj_matrix_input = [[int(input()) for _ in range(3)] for _ in range(3)]
minimum_spanning_tree_keys, parent_array = prim(adj_matrix_input)

# Print the result
print("\nMinimum Spanning Tree:")
for i, key in enumerate(minimum_spanning_tree_keys):
    print(f"Edge {i}: Weight {key}")

# Print Shortest Paths
print("\nShortest Paths:")
for i, parent in enumerate(parent_array):
    path = [i]
    while parent != -1:
        path.append(parent)
        parent = parent_array[parent]
    path.reverse()
    print(f"Shortest path from vertex 0 to vertex {i}: {path}")
