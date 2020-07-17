def hello_world(upcase=False, repeat=1):
  for i in range(repeat):
    if upcase:
      print("HELLO WORLD!")
    else:
      print("Hello World!")

hello_world()
hello_world(True)
hello_world(False, 3)
