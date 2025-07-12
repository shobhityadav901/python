letter ='''Dear<|NAME|>,
you are selected!
<|DATE|> '''
print(letter.replace("<|NAME|>", input("Enter your name:")).replace("<|DATE|>", input("Enter today's date:")))