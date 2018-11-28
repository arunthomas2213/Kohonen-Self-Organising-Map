from random import choice
from numpy import array, dot, random
import math

#(activation function)
unit_step = lambda x: -1 if x < 0 else 1

#training data
training_data = [
    ([1,1,0,0]),
    ([0,0,0,1]),
    ([1,0,0,0]),
    ([0,0,1,1])
    #input1, input2, input3, input4, output
]

#converting training data to input matrix
input_vector = []
desired_output_vector = []
for x in training_data:
    input_element = x
    input_vector.append(input_element)

input_vector = array(input_vector)
print("Training Data")
print(input_vector)

#specifying no of clusters
no_of_clusters = 2

#assigning random initial weight values
weights = [([.2, .6, .5, .9]), ([.8,.4,.7,.3])]
print("Weights")
print(weights)
#starting learning rate parameter
learning_rate = 0.6
#no of epochs
no_of_iterations = 100



#learning/clusturing
for i in xrange(5):
    print("==========================================COUNT=====================================")
    print(i)
    learning_rate = 0.6

    #working on each vector of input
    for j in xrange(4):
        
        print("====================================================================================")
        print("Input Vector")
        print(input_vector[j])
        print("Weights >>")
        print(weights)

        distance_vector = []

        #finding difference between weight vector and input vector
        for w in weights:
            distance = 0
            diff = w - input_vector[j]

            #finding distance
            for a in diff:
                distance += a*a
            # print(distance)
            # appending to distance vector for both weights to find position of the most min distance
            distance_vector.append(distance)
            # print(distance_vector)


        min_distance = distance_vector[0]
        position = 0

        #logic to find the min distance from the distance vector and then we find its position
        #so that we know which weight vector to update
        for index, x in enumerate(distance_vector):
            if x < min_distance:
                min_distance = x
                position = index
        print("Min Distance")
        print(min_distance)
        print(position+1)
        # print(input_vector-weights[position])
        #updating that weight vector according to the one which is of min distance
        weights[position] += learning_rate*(input_vector[j] - weights[position])
        learning_rate *= 0.5
        #printing new weights
        print("New Weight Vector")
        print(weights)


# a_array = []
# print("Enter your inputs")
# for _ in range(4):
#     a = int(input())
#     a_array.append(a)

# result = dot(a_array, w)
# print("{}: {} -> {}".format(a_array[:4], result, unit_step(result)))

input_data = array([1,1,0,0])
print("giving new input")
print(input_data)

distance_vector = []

for w in weights:
    distance = 0
    diff = w - input_data

            #finding distance
    for a in diff:
        distance += a*a
            # print(distance)
            # appending to distance vector for both weights to find position of the most min distance
    distance_vector.append(distance)
            # print(distance_vector)


min_distance = distance_vector[0]
position = 0

        #logic to find the min distance from the distance vector and then we find its position
        #so that we know which weight vector to update
for index, x in enumerate(distance_vector):
    if x < min_distance:
        min_distance = x
        position = index
print("Min Distance")
print(min_distance)
print(position+1)