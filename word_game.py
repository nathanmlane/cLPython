import random

WORDS = (
    "treehouse",
    "python",
    "learner",
)

def prompt_words(challenge):
    guesses = set()
    print("What words can you find in the word '{}'?".format(challenge))
    print("(Enter Q to Quit)")
    while True:
        guess = input("{} words > ".format(len(guesses)))
        if guess.upper() == 'Q':
            break
        guesses.add(guess.lower())
    return guesses

def output_results(results):
    for word in results:
        print("* " + word)


challenge_word = random.choice(WORDS)

player1_words = prompt_words(challenge_word)
player2_words = prompt_words(challenge_word)

print("Player 1 Results:")
player1_unique = player1_words - player2_words
print("{} guesses, {} unique".format(player1_words, player1_unique))
output_results(player1_unique)

print("Player 2 Results:")
player2_unique = player2_words - player1_words
print("{} guesses, {} unique".format(player2_words, player2_unique))
output_results(player2_unique)

print("Shared guesses: ")
shared_words = player1_words & player2_words
output_results(shared_words)
