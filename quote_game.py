from random import choice
from csv import DictReader

def read_quotes(filename):
	with open(filename, "r") as file:
		csv_reader = DictReader(file)
		return list(csv_reader)

def start_game(quotes):
	quote = choice(quotes)
	remaining_guesses = 4
	print(f"Here is a quote")
	print(quote["text"])
	print(quote["author"])

	guess = ''
	while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
		print(f"Who said this quote? Guess remaining: {remaining_guesses}")
		guess = input("Answer: ")
		if guess.lower() == quote["author"].lower():
			print("CONGRATULATION! YOU GOT IT RIGHT!")
			break
		remaining_guesses -= 1
		print_hint(quote, remaining_guesses)

	again = ''
	while again.lower() not in ('y','yes','n','no'):
			again = input("Play again (y/n)?: ")
	if again.lower() in ('y','yes'):
		return start_game(quotes)
	else: 
		print("See you again!")

def print_hint(quote, remaining_guesses):
	if remaining_guesses == 3:
		print(f"Here is the hint: The author was born on {quote['bio']}.")
	elif remaining_guesses == 2:
		print(f"Here is the hint: The author first name start with {quote['author'][0]}")
	elif remaining_guesses == 1:
		last_initial = quote["author"].split(" ")[1][0]
		print(f"Here is the hint: The author last name start with {last_initial}")
	else:
		print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

q = read_quotes("quotes.csv")
start_game(q)

