def tan():
    x = 20
    def rock():
        global x
        x = 40
        print(x)
    print(x)
    rock()

tan()