import math
while True:
    ask = input("hav vil du finne hosligendekatet = h motståendekatet = m hypotenus= hy\n").lower()
    try:
     vinkler_i_grader = float(input("legg in vinkel graden\n"))
    except ValueError:
     print("sett in nummer og ikke bokstav")
    vinkler_i_radian= math.radians(vinkler_i_grader)
    if ask == "h":
     try:
      hy = float(input("sett in hypo verdigen\n"))
     except ValueError:
      print("sett in nummer og ikke bokstav")
     h = math.cos(vinkler_i_radian)*hy
     print(f"hosligendekatet er {h:.3f}")
    elif ask == "m":
     try:
      hy = float(input("sett in hypo verdigen\n"))
     except ValueError:
      print("sett in nummer og ikke bokstav")
     m = math.sin(vinkler_i_radian)*hy
     print(f"motsåendekatet er {m:.3f}")
    elif ask == "hy":
     ask_k = input("hvis du har verdigen til motsåendekatet skriv m og hvis du har verdigen til hosligendekatet skriv h\n").lower()
     if ask_k == "m":
      try:
       ask_m = float(input("hva er verdigen til kateten\n"))
      except ValueError:
       print("sett in nummer og ikke bokstav")
      hy = ask_m/math.sin(vinkler_i_radian)
      print(f"hypotenuse er {hy:.3f}")
     elif ask_k == "h":
      try:
       ask_h = float(input("hva er verdigen til kateten\n"))
      except ValueError:
       print("sett in nummer og ikke bokstav")
      hy = ask_h/math.cos(vinkler_i_radian)
      print(f"hypotenusen er {hy:.3f}")
    else:
     pass