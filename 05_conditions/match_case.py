seat_type=input("Enter your seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Non AC, beds available")
    case "AC":
        print("AC-air conditioned")
    case "general":
        print("General , cheapest option")
    case "luxury":
        print("luxury premium")
    case _:
        print("invalid seat type")