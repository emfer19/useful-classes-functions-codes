#Emily Ferretti
#4/18/16

#to build a reverse dictionary with multiple values

def buildReverse(pd):
  """function that receives a dictionary and creates a reverse dictionary
        -can handle multiple values"""
  reverse={}
  for key,value in pd.items():
    if value in reverse:
      reverse[value].append(key)
    else:
      reverse[value]=[key]
  return reverse
