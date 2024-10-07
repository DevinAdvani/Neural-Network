import numpy as np

size = 3
num_of_transforms = 3

def store_weights(input_matrices):
    open("weights.txt", "w").close()
    f = open("weights.txt", "a")
    for i in range(0,3):
        string = ""
        for j in range(0,3):
            for k in range(0,3):
                string += str(input_matrices[i][j][k]) + " "
        f.write(string + "\n")
    f.close()

def retrieve_weights():
    f = open("weights.txt", "r")
    overall_output = []
    for i in range(0,3):
        output = f.readline().split(" ")
        try:
            output.remove("\n")
        except:
            pass
        output_matrix = np.zeros((3,3))
        for i in range(0,3):
            for j in range(0,3):
                output_matrix[i][j] = output[3*i + j]
        overall_output.append(output_matrix)
    return overall_output

matrices = retrieve_weights()
columns = np.array([1,0,0])
"""
for i in range(0,num_of_transforms):
    matrices.append(np.random.rand(size,size))
for i in range(0, num_of_transforms):
    columns.append(np.zeros((size,1)))
"""

print(matrices)