def convert(d): # Conversion on Sept. 16, 2025
        indianRate = 88.04
        britRate = 0.73
        chinaRate = 7.12

        indian = round(d * indianRate, 2)
        brit = round(d * britRate, 2)
        china = round(d * chinaRate, 2)

        return indian, brit, china

while True:
    dollar = input("\nEnter dollar ($) (* to exit): ")

    if dollar == "*":
        print("Bye")
        break

    sdollar = dollar.split("@")
    
    print("\n{:<15} {:<20} {:<20} {:<15}".format("Dollar ($)", "Indian Ruppe (R)", "British (Pound)", "China (Y)"))
    
    for x in range (len(sdollar)):
        fdollar = float(sdollar[x])
        indian, brit, china = convert(fdollar)
        print("{:<15} {:<20} {:<20} {:<15}".format(sdollar[x], indian, brit, china))