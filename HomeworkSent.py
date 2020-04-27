userInput = input("sent? (True/False): ")
print(userInput)
StudentRecord = ["Joe", "Homework Forgotten", "-2", str(userInput)]
msg = "Letter"
if StudentRecord[3] == "False":
    msg = msg + " not"
msg = msg + " sent."
print(msg)
