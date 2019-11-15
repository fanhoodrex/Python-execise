# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:13:22 2019

@author: Zac_Fang
"""
# Define shout_echo
"""
def shout_echo(word1, echo=1):
    #Concatenate echo copies of word1 and three
    #exclamation marks at the end of the string.
    # Initialize empty strings: echo_word, shout_words
    echo_word=""
    shout_words=""
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + "!!!"
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    # Return shout_words
    return shout_words
# Call shout_echo
shout_echo("particle", echo="accelerator")
"""

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than 0')
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    print(shout_word)
    return shout_word
# Call shout_echo
a=shout_echo("particle", 5)
b=shout_echo("particle", 1)

