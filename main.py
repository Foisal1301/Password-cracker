import string,random,timeit

start = timeit.default_timer()
user_pass = input("Enter your password:")
password = string.ascii_letters+string.digits+string.punctuation

guess = ''

while guess!=user_pass:
    guess=""
    for letter in range(len(user_pass)):
        guess_letter = password[random.randint(0,93)]
        guess=str(guess_letter)+str(guess)
        print(guess)

print("Your correct password is:",guess)
end = timeit.default_timer()
print(f"\nelapsed time:{end - start} seconds")