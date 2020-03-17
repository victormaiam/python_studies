def driver(speed):
    if speed < 70:
        print("Ok")
    else:
        pts_demerito = (speed - 70) // 5
        if pts_demerito > 12:
            print("Licença Suspensa")
        else:
            print(f"Pontos: {pts_demerito} ")


speed = int(input("> "))
driver(speed)