def binomial(n, m):
    if n == m or m == 0:
        return 1
    else:
        return binomial(n-1, m-1) + binomial(n-1,m)
    pass



if __name__ == "__main__":
    print(binomial(10, 4))