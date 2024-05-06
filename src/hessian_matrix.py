import sympy as sp

def get_gradient_vectors(func):
    syms = func.free_symbols
    return sp.Matrix([func.diff(sym) for sym in syms])

def get_hessian(func):
    syms = func.free_symbols
    return sp.Matrix([[func.diff(sym).diff(other_sym) for sym in syms] for other_sym in syms])

def main():
    x = sp.Symbol('x')
    y = sp.Symbol('y')

    two_variable_func = x ** 2 * y - 2 * x - 4 * y
    gradient_vectors = get_gradient_vectors(two_variable_func)
    print(gradient_vectors)
    # stationary_points = sp.solve(gradient_vectors, x, y)
    st_points = sp.solve(gradient_vectors)
    print(f'Stationary points: {st_points}')
    hessian_matrix = get_hessian(two_variable_func)
    print(hessian_matrix)
    hesses = [hessian_matrix.subs(sol) for sol in st_points]
    # if any pd is true this is a local maxima for the optimisation
    pd = [h.is_positive_definite for h in hesses]
    print(pd)
    # if any nd is true this is a local minima for the optimisation
    nd = [h.is_negative_definite for h in hesses]
    print(nd)
    return two_variable_func, gradient_vectors, st_points, hessian_matrix

if __name__ == '__main__':
    main()
    