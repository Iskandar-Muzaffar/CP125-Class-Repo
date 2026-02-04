def audit_blocklists(list_a, list_b, list_c):
    a = set(list_a)
    b = set(list_b)
    c = set(list_c)

    universal_set = a & b & c
    redundant_set = (a & b) | (b & c) | (a & c)
    unique_A_set = a - b - c

    return universal_set, redundant_set, unique_A_set
