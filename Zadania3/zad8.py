def zakupy(**a):
  c=0
  for i in range(len(a.values())):
    c = sum(a.values())
  return c

print(zakupy(baton = 3, sok = 2.34, jablko = 1.5))
