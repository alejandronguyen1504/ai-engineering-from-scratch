
from matplotlib import font_manager
import math
import random

random.seed(42)

def factorial(n):
    # TODO: Calculate the factorial of n (n!).
    # Hint: Use a for loop from 2 to n, multiplying into a result variable (initialized to 1).
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

    

def combinations(n, k):
    # TODO: Calculate the number of combinations (nCr).
    # Formula: n! / (k! * (n-k)!)
    # Hint: Use the factorial function you just wrote. Use integer division (//).
    pass

def conditional_probability(p_a_and_b, p_b):
    # TODO: Calculate conditional probability P(A|B).
    # Formula: P(A|B) = P(A ∩ B) / P(B)
    pass

def bernoulli_pmf(k, p):
    # TODO: Calculate the Probability Mass Function (PMF) for the Bernoulli distribution.
    # Input: k (outcome, 0 or 1), p (probability of success).
    # Hint: Return p if k == 1, otherwise return (1 - p).
    pass

def categorical_pmf(k, probs):
    # TODO: Calculate the PMF for the Categorical distribution.
    # Input: k (index of the category), probs (list of probabilities).
    # Hint: Just return the k-th element in the probs list.
    pass

def poisson_pmf(k, lam):
    # TODO: Calculate the PMF for the Poisson distribution.
    # Formula: (lambda^k * e^(-lambda)) / k!
    # Hint: Use math.exp() for e^, and the factorial function.
    pass

def uniform_pdf(x, a, b):
    # TODO: Calculate the Probability Density Function (PDF) for the Uniform distribution on [a, b].
    # Hint: Return 1.0 / (b - a) if x is between a and b (inclusive). Otherwise return 0.0.
    pass

def normal_pdf(x, mu, sigma):
    # TODO: Calculate the PDF for the Normal distribution.
    # Formula: (1 / (sigma * sqrt(2*pi))) * exp(-0.5 * ((x - mu) / sigma)^2)
    # Hint: Use math.sqrt and math.pi.
    pass

def expected_value(values, probabilities):
    # TODO: Calculate the expected value E[X].
    # Formula: Sum of (x_i * p_i).
    # Hint: Use zip(values, probabilities) to iterate through pairs, multiply them, and sum the results.
    pass

def variance(values, probabilities):
    # TODO: Calculate the variance Var(X).
    # Formula: Sum of (p_i * (x_i - mu)^2).
    # Hint: Call expected_value to get mu first. Then use zip again to apply the formula.
    pass

def sample_bernoulli(p, n=1):
    # TODO: Generate n random samples from a Bernoulli(p) distribution.
    # Hint: Use a list comprehension. For each sample, generate a random number r = random.random().
    # If r < p, the sample is 1, otherwise 0. Repeat n times.
    pass

def sample_categorical(probs, n=1):
    # TODO: Generate n random samples from a Categorical distribution.
    # Hint:
    # 1. Calculate the cumulative probabilities from the probs array.
    # 2. Loop n times. Each time, generate r = random.random().
    # 3. Iterate through the cumulative array. If r <= current cumulative value, the sample belongs to that class (save the index) and break the inner loop.
    pass

def sample_uniform(a, b, n=1):
    # TODO: Generate n random samples from a Uniform(a, b) distribution.
    # Hint: random.random() returns a float in [0.0, 1.0). Scale this by the width (b-a) and add the base (a). Repeat n times.
    pass

def sample_normal_box_muller(mu, sigma, n=1):
    # TODO: Generate n samples from a Normal distribution using the Box-Muller transform.
    # Hint (for each sample):
    # 1. Generate 2 random numbers u1, u2 using random.random().
    # 2. Calculate the standard z-score = sqrt(-2 * ln(u1)) * cos(2 * pi * u2). (Use math.log, math.cos)
    # 3. Transform to the actual sample: x = mu + sigma * z. Repeat n times.
    pass

def softmax(logits):
    # TODO: Compute the Softmax function for an array of logits.
    # Hint:
    # 1. Find the maximum value in logits (max_logit) for numerical stability.
    # 2. Subtract max_logit from all logits to create a 'shifted' array.
    # 3. Calculate e^z for each z in the shifted array (use math.exp).
    # 4. Sum all these e^z values.
    # 5. Return an array where each e^z is divided by the sum.
    pass

def log_softmax(logits):
    # TODO: Compute Log-Softmax.
    # Hint:
    # 1. Find max_logit and create the shifted array just like in softmax.
    # 2. Calculate the constant log_sum_exp = max_logit + log(sum(e^z)) for z in shifted.
    # 3. Return an array where you subtract log_sum_exp from each original logit.
    pass

def cross_entropy_loss(logits, target_index):
    # TODO: Compute Cross-Entropy Loss.
    # Hint: CE Loss is simply the negative log probability at the target class index.
    # Call your log_softmax function, grab the element at target_index, and flip its sign to positive.
    pass

def joint_to_marginals(joint):
    # TODO: Compute marginal distributions from a joint distribution.
    # 'joint' is a 2D array (e.g., joint[i][j]).
    # Hint:
    # - marginal_x: an array containing the SUM of each ROW.
    # - marginal_y: an array containing the SUM of each COLUMN.
    # Return the tuple (marginal_x, marginal_y).
    pass

def check_independence(joint, marginal_x, marginal_y, tol=1e-9):
    # TODO: Check if two variables are independent.
    # Two variables are independent if P(X, Y) = P(X) * P(Y) for all pairs x, y.
    # Hint: Iterate through all rows i and columns j. If abs(joint[i][j] - marginal_x[i] * marginal_y[j]) > tol, return False immediately. Return True if the loop finishes without violations.
    pass

def demonstrate_clt(dist_fn, n_per_sample, n_averages):
    # TODO: Simulate the Central Limit Theorem (CLT).
    # Hint:
    # Loop n_averages times:
    #   1. Draw n_per_sample samples by calling dist_fn().
    #   2. Calculate the mean (average) of these samples and append it to a results array.
    # Return the array of sample means.
    pass
