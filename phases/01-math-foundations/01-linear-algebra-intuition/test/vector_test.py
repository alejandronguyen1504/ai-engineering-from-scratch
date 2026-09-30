import math

class Vector:
    def __init__(self, components):
        self.components = list(components)
        self.dim = len(self.components)

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.components])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        return Vector([x / mag for x in self.components])

    def cosine_similarity(self, other):
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def angle_between(self, other):
        import math
        # TODO:
        # 1. Calculate the cosine similarity between the two vectors.
        # 2. Clamp the cosine value to the range [-1.0, 1.0] to prevent floating-point errors with math.acos.
        # 3. Return the angle in degrees.
        
        cos_similarity = self.cosine_similarity(other); 

        clamped_result = max(-1.0 , min(1.0, cos_similarity))

        radian_ver = math.acos(clamped_result)

        return math.degrees(radian_ver)



    def project_onto(self, other):
        # TODO:
        # 1. Calculate the scalar projection factor of self onto other.
        # 2. Return a new Vector representing the projected component along the 'other' direction.
        scalar = (self.dot(other)) / (other.dot(other))
        return other * scalar

    def __repr__(self):
        return f"Vector({self.components})"


def is_independent(vectors):
    # TODO:
    # Determine if the given list of vectors is linearly independent.
    # 1. Handle edge cases (e.g., empty list of vectors).
    # 2. Form a matrix (list of lists) from the vector components.
    # 3. Perform Gaussian elimination (row reduction) to find the rank of this matrix.
    # 4. Return True if the rank equals the number of input vectors, False otherwise.
    if (not vectors): 
        return True
    n = len(vectors)

    dim = vectors[0].dim

    rows = [list(v.components) for v in vectors]
    rank = 0 
    for col in range(dim): 
        pivot = None 

        for row in range(rank,n): 
            if (abs(rows[row][col]) > 1e-10 ): 
                pivot = row
                break
        if (pivot == None): 
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]

        scale = rows[rank][col]

        rows[rank] = [item / scale for item in rows[rank]]  

        for row in range(n):
            if (row == rank): continue
            if (abs(rows[row][col]) < 1e-10): continue
        
            factor = rows[row][col]

            rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim) ]

        rank +=1 
    return rank == n





def gram_schmidt(vectors):
    # TODO:
    # Convert a list of vectors into an orthonormal basis using the Gram-Schmidt process.
    # 1. Initialize an empty list for the resulting orthonormal vectors.
    # 2. Iterate over each vector in the input list.
    # 3. For the current vector, subtract its projection onto all previously found orthonormal vectors.
    # 4. If the resulting vector is close to zero (magnitude < 1e-10), ignore it.
    # 5. Otherwise, normalize it and add it to the orthonormal list.
    # 6. Return the list of orthonormal vectors.
    result_vectors = []
    
    for vector in vectors: 
        i_vector = vector 
        for o_vector in result_vectors: 
            i_vector = i_vector - i_vector.project_onto(o_vector)
        if (i_vector.magnitude() < 1e-10): 
            continue
        else: 
            result_vectors.append(i_vector.normalize())
    return result_vectors


class Matrix:
    def __init__(self, rows):
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))

    def __matmul__(self, other):
        # TODO:
        # Implement matrix multiplication (the @ operator).
        # 1. Check if 'other' is an instance of Vector. If so, perform Matrix-Vector multiplication and return a Vector.
        # 2. Otherwise, perform Matrix-Matrix multiplication and return a new Matrix.
        if (isinstance(other, Vector)): 
            result_vector = [other.dot(Vector(row)) for row in self.rows]
            return Vector(result_vector)
        

            



    def transpose(self):
        # TODO:
        # Return a new Matrix representing the transpose of the current matrix (rows become columns and vice versa).
        pass

    def rank(self):
        # TODO:
        # Calculate the rank of the matrix using Gaussian elimination (row reduction).
        # 1. Create a copy of the matrix rows so you don't mutate the original matrix.
        # 2. Iterate through each column to find a non-zero pivot.
        # 3. If a non-zero pivot is found in the current or subsequent rows, swap rows to bring the pivot to the current rank position.
        # 4. Scale the pivot row so the pivot element becomes 1.
        # 5. Eliminate the corresponding column entries in all other rows (make them 0).
        # 6. Keep track of the number of valid pivots found.
        # 7. Return the final count of pivots (the rank).
        pass

    def __repr__(self):
        return f"Matrix({self.rows})"

# ==============================================================================
# TESTS / RUNNER
# ==============================================================================
if __name__ == "__main__":
    print("=== Vectors ===")
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * 3 = {a * 3}")
    print(f"a · b = {a.dot(b)}")
    print(f"|a| = {a.magnitude():.4f}")
    print(f"â (normalized) = {a.normalize()}")
    print(f"cosine_similarity(a, b) = {a.cosine_similarity(b):.4f}")

    print("\n=== Matrices ===")
    rotation_90 = Matrix([[0, -1], [1, 0]])
    point = Vector([3, 1])
    rotated = rotation_90 @ point
    print(f"Rotate {point} by 90° → {rotated}")

    print("\n=== Angle Between Vectors ===")
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    v3 = Vector([1, 1])
    print(f"Angle between {v1} and {v2}: {v1.angle_between(v2):.1f} degrees")
    print(f"Angle between {v1} and {v3}: {v1.angle_between(v3):.1f} degrees")
    print(f"Angle between {v1} and {v1}: {v1.angle_between(v1):.1f} degrees")

    print("\n=== Projection ===")
    a = Vector([3, 4])
    b = Vector([1, 0])
    proj = a.project_onto(b)
    residual = a - proj
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"proj_b(a) = {proj}")
    print(f"residual = {residual}")
    print(f"residual dot b = {residual.dot(b):.6f}")

    print("\n=== Linear Independence ===")
    e1 = Vector([1, 0, 0])
    e2 = Vector([0, 1, 0])
    e3 = Vector([0, 0, 1])
    dep = Vector([2, 1, 0])
    print(f"{{e1, e2, e3}} independent: {is_independent([e1, e2, e3])}")
    print(f"{{e1, e2, 2*e1+e2}} independent: {is_independent([e1, e2, dep])}")

    print("\n=== Gram-Schmidt Orthogonalization ===")
    u1 = Vector([1, 1, 0])
    u2 = Vector([1, 0, 1])
    u3 = Vector([0, 1, 1])
    basis = gram_schmidt([u1, u2, u3])
    for i, vec in enumerate(basis):
        print(f"u{i+1} = {vec}")
    print(f"u1 dot u2 = {basis[0].dot(basis[1]):.6f}")
    print(f"u1 dot u3 = {basis[0].dot(basis[2]):.6f}")
    print(f"u2 dot u3 = {basis[1].dot(basis[2]):.6f}")
    for i, vec in enumerate(basis):
        print(f"|u{i+1}| = {vec.magnitude():.6f}")

    print("\n=== Matrix Rank ===")
    full_rank = Matrix([[1, 0], [0, 1]])
    rank_deficient = Matrix([[1, 2], [2, 4]])
    rectangular = Matrix([[1, 0, 0], [0, 1, 0]])
    print(f"Identity 2x2 rank: {full_rank.rank()}")
    print(f"[[1,2],[2,4]] rank: {rank_deficient.rank()}")
    print(f"[[1,0,0],[0,1,0]] rank: {rectangular.rank()}")

    print("\n=== Neural Network Layer (Matrix x Vector) ===")
    import random
    random.seed(42)
    weights = Matrix([[random.gauss(0, 0.1) for _ in range(3)] for _ in range(2)])
    input_vec = Vector([1.0, 0.5, -0.3])
    output = weights @ input_vec
    print(f"Input (3D):  {input_vec}")
    print(f"Output (2D): {output}")
    print("^ This is literally what a neural network layer does.")
