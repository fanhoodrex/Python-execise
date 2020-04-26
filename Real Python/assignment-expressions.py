"""
print(walrus := True)
type(walrus)

inputs = list()
current = input("Write something: ")
while current != "quit":
    inputs.append(current)
    current = input("Write something: ")

inputs = list()
while True:
    current = input("Write something: ")
    if current == "quit":
        break
    inputs.append(current)
"""
inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)
print(inputs)