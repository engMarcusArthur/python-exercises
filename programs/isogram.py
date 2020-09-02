def is_isogram(string):
  stringls = string.lower().strip()
  for i in range(0,len(stringls)):
    if stringls[i] != " " and stringls[i]!= "-":
      if stringls.count(stringls[i]) > 1:
        return False
  return True

print(is_isogram(""))