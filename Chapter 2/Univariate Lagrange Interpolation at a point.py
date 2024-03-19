import galois
import random

# Function to calculate the value of the univariate Lagrange interpolating polynomial at a single point
def univariate_lagrange_interpolator_single_point(GF, vector, evaluation_point):

    if(evaluation_point < len(vector)): # Handle the cases when evaluation point asks for one of the numbers in the vector
        return vector[evaluation_point]
    n = len(vector)
    sum = GF(0)

    # Calculate delta_0(r)
    delta_0 = GF(1)
    for k in range(1, n):
        delta_0 *= evaluation_point - GF(k)
    for k in range(1, n):
        delta_0 *= GF(k)**(-1)
    
    # Handle the case when i = 0 separately
    sum += vector[0] * delta_0

    # Compute the remaining Lagrange basis polynomials and sum up the interpolation
    delta_i = delta_0
    for i in range(1, n):
        # Update delta_i based on the recursive relationship
        delta_i *= (evaluation_point - GF(i - 1)) * (evaluation_point - GF(i))**(-1) * GF(i)**(-1) * (-GF(n - i))
        sum += vector[i] * delta_i
    
    return sum

# Main code to test the Lagrange interpolator
if __name__ == "__main__":
    prime_to_work_with = 37  # 37 is an arbitrary prime number
    GF = galois.GF(prime_to_work_with)  # Create the Galois field
    vector = [GF(3), GF(4), GF(5)]  # vector to interpolate
    evaluation_point = GF(random.randint(0, prime_to_work_with - 1))  # Random evaluation point in the field

    # Compute the interpolation at the evaluation point
    result = univariate_lagrange_interpolator_single_point(GF, vector, evaluation_point)
    print("The value of the polynomial at the point ", end="")
    print(evaluation_point, end="")
    print(" is equal to ", end="")
    print(result)
