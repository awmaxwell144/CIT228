#glossary
"""A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the
previous chapters. Use these words as the keys in your glossary,
and store their meanings as values.
• Print each word and its meaning as neatly formatted output.
You might print the word followed by a colon and then its meaning,
or print the word on one line and then print its meaning indented
on a second line. Use the newline character (\n) to insert a
blank line between each word-meaning pair in your output."""

glossary = {"Integer":"Whole number",
            "Float":"Decimal number",
            "String":"Text",
            "Boolean":"True/False",
            "List":"A container that can store any kind of values",
            "Tuple":"A similar container as a list that cannot be updated",
            "Index":"A number indicating the location of a specific value within a list of tuple",
            "Comment":"Text within the script that will not be compiled as code",
            "For loop":"A loop that iterates through the contents a set number of times",
            "If statement":"Executes the contents if the statement evaluates to true"
            }

for i in glossary:
    print(i)
    print(f'\t{glossary[i]}')