import numpy as np

nodes_in_layers = [5,4,3]#[10000, 1000, 100, 10]
num_of_transforms = len(nodes_in_layers) - 1
num_of_outputs = nodes_in_layers[-1]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def store_weights(input_matrices):
    open("weights.txt", "w").close()
    f = open("weights.txt", "a")
    for i in range(0,num_of_transforms):
        string = ""
        for j in range(0,nodes_in_layers[i+1]):
            for k in range(0,nodes_in_layers[i]):
                string += str(input_matrices[i][j][k]) + " "
        f.write(string + "\n")
    f.close()

def retrieve_weights():
    f = open("weights.txt", "r")
    overall_output = []
    for i in range(0,num_of_transforms):
        output = f.readline().split(" ")
        try:
            output.remove("\n")
        except:
            pass
        output_matrix = np.zeros((nodes_in_layers[i+1],nodes_in_layers[i]))
        for j in range(0,nodes_in_layers[i+1]):
            for k in range(0,nodes_in_layers[i]):
                output_matrix[j][k] = output[nodes_in_layers[i]*j + k]
        overall_output.append(output_matrix)
    return overall_output

def function(input_column):
    matrices = retrieve_weights()
    for i in range(0,num_of_transforms):
        input_column = sigmoid(np.matmul(matrices[i], input_column))
    return input_column

def access_data():
    f = open("data_set.txt", "r")
    data = []
    for x in f:
        unit = [x[2]]
        input_string = ""
        for i in range(0,100):
            input_string += x[7 + 100 * i: 107 + 100 * i]
        input_column = []
        for i in range(0,len(input_string)):
            input_column.append(input_string[i])
        unit.append(np.array(input_column))
        data.append(unit)
    return data

def train():
    pass
    
#column = np.array([1,1,0,0])
#access_data()
matrices = [np.random.rand(4,5), np.random.rand(3,4)]
print(matrices)
print("")
store_weights(matrices)
print(retrieve_weights())