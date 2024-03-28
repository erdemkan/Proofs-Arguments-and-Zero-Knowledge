# This is the algorithm corresponding to Lemma 3.8 from the book.
import galois
from itertools import product


def multilinear_lagrange_interpolation(GF, evaluation_vector):
    v = len(evaluation_vector)
    
    temp_list1 = []
    temp_list2 = [GF(1)]
    for i in range(v):
        temp_list1 = temp_list2
        temp_list2 = []
        for j in range(len(temp_list1)):
            temp_list2.append(temp_list1[j] * (GF(1) - evaluation_vector[i]))
            temp_list2.append(temp_list1[j] * (evaluation_vector[i]))

    
    interpolated_value = GF(0)
    for idx, w in enumerate(product([0, 1], repeat=v)):
        interpolated_value += example_function(GF, w) * temp_list2[idx]

    return interpolated_value



def example_function(GF, vector): # the example function is figure 3.1 from the book
    x1 = vector[0]
    x2 = vector[1]
    if x1 == GF(0) and x2 == GF(0):
        return GF(1)
    elif x1 == GF(0) and x2 == GF(1):
        return GF(2)
    elif x1 == GF(1) and x2 == GF(0):
        return GF(1)
    elif x1 == GF(1) and x2 == GF(1):
        return GF(4)


if __name__ == "__main__":
    prime_to_work_with = 5  # 5 is an arbitrary prime number
    GF = galois.GF(prime_to_work_with)  # Create the Galois field
    evaluation_vector = (GF(1), GF(4))

    interpolated_value = multilinear_lagrange_interpolation(GF, evaluation_vector)

    print("The value of the polynomial at the vector ", end="")
    print(evaluation_vector, end="")
    print(" is equal to ", end="")
    print(interpolated_value)
