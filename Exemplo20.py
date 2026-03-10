while True:
    try:
        numerador = 0
        denominador = 0
        m = int(input())
        if m >= 1 and m <= 40:
          for i in range(m):
            linha = input().split()
            n, c = list(map(int, linha))
            numerador += n * c

            denominador += c
          ira = numerador / (denominador * 100)
          print("%.4f" % ira)
    except EOFError:
        break