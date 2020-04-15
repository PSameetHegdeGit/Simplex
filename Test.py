

if __name__ == "__main__":

    m = [[1,2],[3,4]]

    n = m[1].copy()
    print(n)

    m[1][1] = 7

    print(n)