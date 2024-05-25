def sum_of_terms_in_gp(a: float, r: int, n: int) -> float:
    gp = a * ((1 - r **(n)) * (1 - r))
    return gp

print(sum_of_terms_in_gp(0.5, 2, 10))