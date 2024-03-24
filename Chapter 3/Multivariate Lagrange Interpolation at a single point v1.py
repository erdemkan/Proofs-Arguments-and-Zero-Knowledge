# This is the algorithm corresponding to Lemma 3.7 from the book.
import galois
from itertools import product


def multilinear_lagrange_interpolation(GF, evaluation_vector):
    sum = GF(0) # Initialize the sum for the interpolation polynomial
    v = len(evaluation_vector)

    # Iterate over all vertices of the unit cube {0, 1}^v
    for w in product([0, 1], repeat=v):
        f_w = example_function(GF, w)

        # Calculate the multilinear basis polynomial chi_w at x_values
        chi_w = GF(1)
        for i in range(v):
            chi_w *= evaluation_vector[i] if w[i] == GF(1) else (GF(1) - evaluation_vector[i])

        
        # Add to the interpolation sum
        sum += f_w * chi_w

    return sum 

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
    evaluation_vector = (GF(4), GF(3))

    interpolated_value = multilinear_lagrange_interpolation(GF, evaluation_vector)

    print("The value of the polynomial at the vector ", end="")
    print(evaluation_vector, end="")
    print(" is equal to ", end="")
    print(interpolated_value)

