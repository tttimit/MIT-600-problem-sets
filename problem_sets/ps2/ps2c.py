def evaluate_poly(poly, x):
    result = 0.0
    n = 0
    for i in poly:
        result += i * (x ** n)
        n += 1
    return result

#poly = (0.0, 0.0, 5.0, 9.3, 7.0)
#x = -13
#print(evaluate_poly(poly, x))

def compute_deriv(poly):
    n = 0
    result = ()
    for i in poly:
        if n != 0:
            result += (i * n,)
        n += 1
    return result

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
#print(compute_deriv(poly))
##times = 1
##def compute_root(poly, x_0, epsilon):
##    if abs(evaluate_poly(poly, x_0)) < epsilon:
##        return (x_0, times)
##    else:
##        x_0 = x_0 - evaluate_poly(poly, x_0) / evaluate_poly(compute_deriv(poly), x_0)
##    times += 1

def compute_root(poly, x_0, epsilon):
    root = x_0
    counter = 1
    while abs(evaluate_poly(poly, root)) >= epsilon:
        root = (root - evaluate_poly(poly, root) /
                evaluate_poly(compute_deriv(poly), root))
        counter += 1
    return [root, counter]

x_0 = .1
epsilon = .0001
print(compute_root(poly, x_0, epsilon))
        
