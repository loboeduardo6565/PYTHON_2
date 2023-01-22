# crear una función
def switch(CPU):
 
  # definition of the dictionary
  cputester = {
 
  # case 1
  "celeron": "Forget about it and play Minesweeper instead...",
 
  # case 2
  "core i3": "Good luck with that ;)",
 
  # case 3
  "core i5": "Yeah, you should be fine.",
 
  # case 4
  "core i7": "Have fun!",
 
  # case 5
  "core i9": "Our teams designed nice loading screens... too bad you won't see them..."
 
  }
 
  # if not found, return message
  return cputester.get(CPU, "Is that even a thing?")
 
# ask the player about their CPU
cpuModel = str.lower(input("Please enter your CPU model: "))
 
# call and print the function
print(switch(cpuModel))

#https://www.udacity.com/blog/2021/10/python-match-case-statement-example-alternatives.html