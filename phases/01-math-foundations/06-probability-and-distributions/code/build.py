import math
import random

random.seed(42)

# ==============================================================================
# Step 1: Probability basics
# ==============================================================================

def factorial(n):
    # TODO: Calculate the factorial of n (n! = 1 * 2 * ... * n, with 0! = 1).
    # Example: n = 5 -> returns 120
    # Hint: Initialize a result to 1 and multiply integers from 2 up to n.
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combinations(n, k):
    # TODO: Calculate the number of combinations (nCr: n choose k without regard to order).
    # Example: n = 5, k = 2 -> returns 10
    # Mathematical Formula: n! / (k! * (n - k)!)
    # Hint: Use the factorial function and integer division.
    return factorial(n) // (factorial(k) * factorial(n - k))


def conditional_probability(p_a_and_b, p_b):
    # TODO: Calculate conditional probability P(A|B) - probability of A given B has occurred.
    # Example: p_a_and_b = 4/52, p_b = 12/52 -> returns 1/3 (0.3333)
    # Mathematical Formula: P(A|B) = P(A ∩ B) / P(B)
    return p_a_and_b / p_b


# ==============================================================================
# Step 2: PMF and PDF from scratch
# ==============================================================================

def bernoulli_pmf(k, p):
    # TODO: Compute PMF for a Bernoulli distribution with success probability p.
    # Outcome k represents: 1 (success) or 0 (failure).
    # Example: k = 1, p = 0.7 -> returns 0.7; k = 0, p = 0.7 -> returns 0.3
    # Formula: P(X = 1) = p, P(X = 0) = 1 - p.
    return p if k == 1 else 1 - p


def categorical_pmf(k, probs):
    # TODO: Compute PMF for a Categorical distribution (single trial with discrete categories).
    # Input: k is the target category index, probs is the list of category probabilities (summing to 1).
    # Example: k = 0, probs = [0.7, 0.2, 0.1] -> returns 0.7
    # Hint: Look up the probability corresponding to category k.
    return probs[k]


def poisson_pmf(k, lam):
    # TODO: Compute PMF for a Poisson distribution: counts of rare events with average rate lambda.
    # Example: k = 3, lam = 2.5 -> returns ~0.2138
    # Mathematical Formula: P(X = k) = (lambda^k * e^(-lambda)) / k!
    # Hint: Use math.exp for the exponential term and factorial for the denominator.
    return (lam ** k) * math.exp(-lam) / factorial(k)


def uniform_pdf(x, a, b):
    # TODO: Compute PDF for a continuous Uniform distribution over interval [a, b].
    # Probability density is constant over [a, b] such that total area equals 1, and 0 elsewhere.
    # Example: x = 2.5, a = 1.0, b = 4.0 -> returns 1.0 / (4.0 - 1.0) = 0.3333
    # Formula: f(x) = 1 / (b - a) when a <= x <= b, otherwise 0.
    pass


def normal_pdf(x, mu, sigma):
    # TODO: Compute PDF for a Normal (Gaussian) distribution with mean mu and standard deviation sigma.
    # Example: x = 0.0, mu = 0.0, sigma = 1.0 -> returns ~0.3989
    # Mathematical Formula: f(x) = (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma)^2)
    # Hint: Break computation into the normalization coefficient and the exponential term using math.sqrt, math.pi, math.exp.
    pass


# ==============================================================================
# Step 3: Expected value and variance
# ==============================================================================

def expected_value(values, probabilities):
    # TODO: Calculate expected value E[X] (the probability-weighted average of all outcomes).
    # Example: values = [1, 2, 3, 4, 5, 6], probabilities = [1/6] * 6 -> returns 3.5
    # Mathematical Formula: E[X] = sum over i of (x_i * p_i)
    # Hint: Iterate through paired values and probabilities, multiply each pair, and sum the products.
    pass


def variance(values, probabilities):
    # TODO: Calculate variance Var(X), measuring expected squared deviation from the mean.
    # Example: values = [1, 2, 3, 4, 5, 6], probabilities = [1/6] * 6 -> returns ~2.9167
    # Mathematical Formula: Var(X) = sum over i of (p_i * (x_i - mu)^2), where mu = E[X].
    # Hint: Compute mean mu first using expected_value, then sum weighted squared differences.
    pass


# ==============================================================================
# Step 4: Sampling from distributions
# ==============================================================================

def sample_bernoulli(p, n=1):
    # TODO: Draw n independent random samples from Bernoulli(p).
    # Example: p = 0.7, n = 5 -> returns e.g. [1, 1, 0, 1, 0]
    # Hint: For each sample, generate uniform random float r in [0, 1). If r < p, outcome is 1, else 0.
    pass


def sample_categorical(probs, n=1):
    # TODO: Draw n independent samples from a Categorical distribution using inverse transform sampling.
    # Example: probs = [0.7, 0.2, 0.1], n = 5 -> returns e.g. [0, 0, 1, 0, 2]
    # Hint:
    # 1. Build a cumulative probability array where each element is the running sum of probs.
    # 2. For each sample, draw random float r in [0, 1).
    # 3. Find the first category index whose cumulative probability is >= r.
    pass


def sample_normal_box_muller(mu, sigma, n=1):
    # TODO: Draw n samples from Normal(mu, sigma) using the Box-Muller transform.
    # Example: mu = 0.0, sigma = 1.0, n = 3 -> returns e.g. [0.42, -1.15, 0.08]
    # Hint: For each sample:
    # 1. Generate two independent uniform random numbers u1, u2 in (0, 1).
    # 2. Compute standard normal z-score: z = sqrt(-2 * ln(u1)) * cos(2 * pi * u2).
    # 3. Scale and shift: x = mu + sigma * z.
    pass


# ==============================================================================
# Step 5: Softmax and log probabilities
# ==============================================================================

def softmax(logits):
    # TODO: Convert raw unnormalized scores (logits) into a valid probability distribution.
    # Example: logits = [2.0, 1.0, 0.1] -> returns ~[0.6590, 0.2424, 0.0986]
    # Formula: softmax(z_i) = exp(z_i) / sum(exp(z_j))
    # Hint: For numerical stability (prevent overflow), subtract max(logits) from all logits before exponentiating.
    pass


def log_softmax(logits):
    # TODO: Compute log(softmax(z)) with numerical stability using the LogSumExp identity.
    # Example: logits = [2.0, 1.0, 0.1] -> returns ~[-0.4170, -1.4170, -2.3170]
    # Mathematical Identity: log(softmax(z_i)) = z_i - LogSumExp(z)
    # where LogSumExp(z) = max(z) + ln(sum(exp(z_j - max(z))))
    # Hint: Shift logits by max, calculate log_sum_exp scalar, then subtract it from each original logit.
    pass


def cross_entropy_loss(logits, target_index):
    # TODO: Calculate Cross-Entropy Loss for multi-class classification.
    # Definition: Negative log-probability assigned to the ground-truth class.
    # Example: logits = [2.0, 1.0, 0.1], target_index = 0 -> returns ~0.4170
    # Loss = -log(P(target))
    # Hint: Use log_softmax to obtain log probabilities, take the value at target_index, and negate it.
    pass


# ==============================================================================
# Step 6: Central Limit Theorem demonstration
# ==============================================================================

def demonstrate_clt(dist_fn, n_samples, n_averages):
    # TODO: Simulate Central Limit Theorem (sample mean of independent variables approaches normal distribution).
    # Example: dist_fn = random.random, n_samples = 30, n_averages = 1000 -> returns list of 1000 sample means (mean ~ 0.5)
    # Hint: Run n_averages iterations. In each iteration, draw n_samples using dist_fn(), compute their average, and record it.
    # Return the list of all computed sample averages.
    pass


# ==============================================================================
# Extra 1: Bayes' Theorem
# ==============================================================================

def bayes_theorem(p_b_given_a, p_a, p_b):
    # TODO: Compute posterior probability P(A|B) using Bayes' Theorem.
    # Example: p_b_given_a = 0.95 (sensitivity), p_a = 0.01 (prior), p_b = 0.05 (test positive) -> returns 0.19 (19%)
    # Mathematical Formula: P(A|B) = (P(B|A) * P(A)) / P(B)
    pass


# ==============================================================================
# Extra 2: Continuous Uniform Sampling
# ==============================================================================

def sample_uniform(a, b, n=1):
    # TODO: Draw n random float samples uniformly distributed in continuous interval [a, b].
    # Example: a = 1.0, b = 4.0, n = 3 -> returns e.g. [2.14, 3.85, 1.07]
    # Hint: Scale a standard uniform random number in [0, 1) by interval width (b - a) and offset by base a.
    pass


# ==============================================================================
# Extra 3: Joint to Marginals
# ==============================================================================

def joint_to_marginals(joint):
    # TODO: Compute marginal probability distributions P(X) and P(Y) from a 2D joint probability matrix.
    # Example: joint = [[0.40, 0.10], [0.05, 0.45]] -> returns ([0.5, 0.5], [0.45, 0.55])
    # Mathematical Definition:
    # - Marginal P(X = x_i) is obtained by summing joint probabilities across row i.
    # - Marginal P(Y = y_j) is obtained by summing joint probabilities down column j.
    # Return tuple (marginal_x, marginal_y).
    pass


# ==============================================================================
# Extra 4: Statistical Independence Check
# ==============================================================================

def check_independence(joint, marginal_x, marginal_y, tol=1e-9):
    # TODO: Test whether random variables X and Y are statistically independent.
    # Example: joint = [[0.40, 0.10], [0.05, 0.45]], marginal_x = [0.5, 0.5], marginal_y = [0.45, 0.55] -> returns False
    # Condition: P(X = x_i, Y = y_j) == P(X = x_i) * P(Y = y_j) for all i and j.
    # Hint: If the absolute difference exceeds tol for any cell, return False; if all match, return True.
    pass
