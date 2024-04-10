#!/usr/bin/env python3
import ipdb
import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    split_value = [char for char in self.value]
    
    if split_value[-1] == ".":
      return True
    else:
      return False

  def is_question(self):
    split_value = [char for char in self.value]
    
    if split_value[-1] == "?":
      return True
    else:
      return False

  def is_exclamation(self):
    split_value = [char for char in self.value]
    
    if split_value[-1] == "!":
      return True
    else:
      return False

  def count_sentences(self):
    sentence_endings = ['.', '!', '?']
    encountered_sentences = []
    current_sentence = ""
    
    for char in self.value:
        if char in sentence_endings:
            if current_sentence.strip():  # If the current sentence is not empty
                encountered_sentences.append(current_sentence.strip())
                # ipdb.set_trace()
                current_sentence = ""
        else:
            current_sentence += char
    
    # Check if the last sentence ended without any punctuation
    if current_sentence.strip():
        encountered_sentences.append(current_sentence.strip())

    return len(encountered_sentences)

string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
string2 = MyString("I don't know what to write. However I'm going to end without a punctuation")

string.count_sentences()
string2.count_sentences()    
    
# Iterate thru each char of string until we hit a sentence ending. 
# When that happens, we check if current_sentence is empty or not (if empty == False, if contains chars == True)
  # If it's True: We append the string captured by current_sentence.strip() to encountered_sentences
  # We then reset current_sentence to an empty string
# The last if statement handles cases where the last sentence doesn’t end with a punctuation.

  
    
    
    
    

