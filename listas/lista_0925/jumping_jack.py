'''
Ideias:
Finding all cycles containing a vertex v in O(2^n * n^2), then removing v from the graph and repeating, so that the total number of operations is about is 2^n * n^2 + 2^(n - 1) * n^2 +... = O(2^n * n^2), instead of O(2^n * n^3) achieved by a simple DP approach.
'''