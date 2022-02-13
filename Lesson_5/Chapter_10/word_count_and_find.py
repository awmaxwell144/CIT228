print()
def find_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word = word.lower()
        numWords = contents.count(word)
        print(f'The word {word} occurred {str(numWords)} times in the {filename} file.')
        
        
        """
e)  in the main program, below the for loop that calls count_words, prompt the user for a common word they want to search for in the text files

f)  create a new for loop that calls the find_words function and passes it the filename along with the searchWord"""


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['Lesson_5/Chapter_10/1984.txt', 'Lesson_5/Chapter_10/King_Lear.txt', 'Lesson_5/Chapter_10/One_Flew_Over_The_Cuckoos_Nest.txt']

for filename in filenames:
    count_words(filename)

word = input('What word would you like to search for? ')
for filename in filenames:
    find_words(filename,word)