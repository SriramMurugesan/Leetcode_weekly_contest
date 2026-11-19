# ==============================================================================
# PROBLEM EXPLANATION:
# We are given a sorted array 'a' of length 'n' and a minimum gap 'g'.
# We want to partition the elements into 2 groups (or color them with 2 colors: e.g., Red and Blue)
# such that ANY two elements assigned to the SAME group have an absolute difference >= g.
# We need to find the number of valid partitionings modulo 998244353.
#
# ------------------------------------------------------------------------------
# CONCRETE EXAMPLES:
#
# Example 1 (Impossible case - Pigeonhole Principle violation):
#   n = 3, g = 4, a = [1, 2, 3]
#   - Check triple: a[2] - a[0] = 3 - 1 = 2 < 4 (g).
#   - With 3 elements and only 2 groups, at least 2 elements MUST share the same group.
#   - But the max difference among any of these 3 elements is 2, which is < g (4).
#   - Any 2 elements in the same group will have difference < 4. Impossible!
#   - Output: 0
#
# Example 2 (Valid case - Multiple components):
#   n = 4, g = 3, a = [1, 2, 5, 8]
#   1. Step 1 (Triple check):
#      - a[2] - a[0] = 5 - 1 = 4 >= 3 (OK)
#      - a[3] - a[1] = 8 - 2 = 6 >= 3 (OK)
#      No triple violates the gap constraint.
#   2. Step 2 (Count components):
#      - Start with components = 1 (element a[0] = 1).
#      - i = 1: a[1] - a[0] = 2 - 1 = 1 < 3.
#        Because difference < g, a[1] cannot have the same color as a[0].
#        It MUST have the opposite color. They belong to the SAME component.
#      - i = 2: a[2] - a[1] = 5 - 2 = 3 >= 3.
#        Because difference >= g, a[2] has no conflict with a[1] (or earlier).
#        It starts a NEW independent component -> components = 2.
#      - i = 3: a[3] - a[2] = 8 - 5 = 3 >= 3.
#        Starts another NEW independent component -> components = 3.
#   3. Step 3 (Calculate ways):
#      - Component 1: {1, 2} -> 2 colorings: (Red, Blue) or (Blue, Red).
#      - Component 2: {5}    -> 2 colorings: Red or Blue.
#      - Component 3: {8}    -> 2 colorings: Red or Blue.
#      - Total valid ways = 2^3 = 8.
# ==============================================================================

# Standard modulo for competitive programming combinatorics
MOD = 998244353

# Number of test cases
t = int(input())

for _ in range(t):
    # Read n (number of elements) and g (required minimum gap)
    n, g = map(int, input().split())
    # Read sorted array a
    a = list(map(int, input().split()))

    ans = 1
    possible = True
    components = 1

    # --------------------------------------------------------------------------
    # CHECK 1: Triple check using the Pigeonhole Principle
    # Look at any 3 consecutive sorted elements: a[i], a[i+1], a[i+2].
    # By Pigeonhole Principle, at least 2 of these 3 elements must be placed in the
    # same group (since there are only 2 groups).
    # If a[i+2] - a[i] < g, then the difference between ANY pair among them is < g.
    # Thus, two elements in the same group will violate the gap >= g condition.
    # --------------------------------------------------------------------------
    for i in range(n - 2):
        if a[i + 2] - a[i] < g:
            possible = False
            break

    # If any triple violates the condition, 0 valid partitions exist.
    if not possible:
        print(0)
        continue

    # --------------------------------------------------------------------------
    # CHECK 2: Count independent components
    # If all triples have a[i+2] - a[i] >= g, then any elements with index difference >= 2
    # will NEVER conflict with each other even in the same group.
    # The only potential conflict is between immediately adjacent elements:
    # - If a[i] - a[i-1] < g:
    #     They cannot be in the same group; their colors must alternate (same component).
    # - If a[i] - a[i-1] >= g:
    #     There is no conflict; a[i] can be chosen independently (starts a new component).
    # --------------------------------------------------------------------------
    for i in range(1, n):
        if a[i] - a[i - 1] >= g:
            components += 1

    # Each independent component has 2 choices for coloring its elements (e.g. Red/Blue).
    # Total combinations = 2^(number of components) % MOD.
    ans = pow(2, components, MOD)

    print(ans)
