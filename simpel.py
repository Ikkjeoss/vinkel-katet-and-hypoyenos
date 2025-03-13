import math
ask = input("hav vil du finne hosligendekatet = h motståendekatet = m hypotenus= hy")
vinkler_i_grader = int(input("plz legg in vinkel graden"))
vinkler_i_radian= math.radians(vinkler_i_grader)
if ask == "h":
  hy = int(input("plz sett in hypo verdigen"))
  h = math.cos(vinkler_i_radian)*hy
  print(f"hosligendekatet er {h:.3f}")
elif ask == "m":
  hy = int(input("plz sett in hypo verdigen"))
  m = math.sin(vinkler_i_radian)