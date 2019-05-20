import copy
import random
import numpy
from library.funs import *
from mlp.NeuralNetwork import NeuralNetwork


def task_Seeds():
    numpy.set_printoptions(suppress=True)  # avoid e-05 notation
    hidden_nodes = 4
    epochs = 1000
    learning_rate = 0.2
    momentum = 0.9
    bias = False
    network = NeuralNetwork(input_nodes=7, hidden_nodes=hidden_nodes, output_nodes=3,
                            learning_rate=learning_rate, momentum=momentum, bias=bias, epochs=epochs)

    input_list = initialize_data_with1stcolumn("data/seeds.csv")
    output = []
    indices = []
    test = []
    test = input_list[39:69] + input_list[109:139] + input_list[179:209]

    for i in range(int(len(input_list) / 3)):
        output.append([[1, 0, 0], input_list[i]])
    for i in range(int(len(input_list) / 3)):
        output.append([[0, 1, 0], input_list[i + int(len(input_list) / 3)]])
    for i in range(int(len(input_list) / 3)):
        output.append([[0, 0, 1], input_list[i + int(len(input_list) / 3) * 2]])

    train = []
    train = output[:39] + output[69:109] + output[139:179]

    for i in range(0,30):
        indices.append(0)
    for i in range(30,60):
        indices.append(1)
    for i in range(60,90):
        indices.append(2)

    shuffled_output = copy.copy(train)
    randomize = np.arange(len(train))

    for i in range(len(train)):
        shuffled_output[i] = shuffled_output[randomize[i]]

    for i in range(epochs):
        for e in range(len(shuffled_output)):
            network.train_manual_epochs(shuffled_output[e][1], shuffled_output[e][0], i, e == 0)

    fin = []
    for i in range(len(test)):
        fin.append(network.query(test[i]))

    error = 0
    for elem in range(len(fin)):
        if numpy.argmax(fin[elem]) != indices[elem]:
            error += 1

    print("Seeds error rate = " + str(error / len(fin) * 100) + "%")

    parameters = parameters_as_string(hidden_nodes, learning_rate, momentum, epochs, bias)
    calculate_results_table(3, indices, fin, 'Seeds result table \n' + parameters)
    print_plot(network.sampling_iteration, network.errors_for_plot, 'Zbiór: nasiona\n Wykres zależności wartości błędu od ilości epok\n' + parameters)