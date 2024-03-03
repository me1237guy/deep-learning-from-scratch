def and_op(x1, x2, w1, w2, theta):
    return w1*x1 + w2*x2 > theta


if __name__ == "__main__":
    # Use list('X') when you have collections of items that need to be accessed or modified by index
    X = [[0, 0], [1, 0], [0, 1], [1, 1]]
    # Use tuple(Y) when you have collections of items that are immutable and represent fixed sequences  
    Y = [(0, 0), (1, 0), (0, 1), (1, 1)]
    w1, w2 = 0.5, 0.5
    theta = 0.8
        
    for x in X:
        v = and_op(x1=x[0], x2=x[1], w1=w1, w2=w2, theta=theta)
        print(f"{w1}*{x[0]}+{w2}*{x[1]}>={theta}:{v}")
        