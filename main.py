#dictionary to remind user of specific definitions
dictionary = [
  {
    "Nouns": "Nouns are words that represent people, places, or things.",
    "Adjectives": "Adjectives are words that describe people, places, or things.",
    "Verbs": "Verbs are words that show an action(sing), occurence(develop), or state of being(exist).",
    "Adverbs": "Adverbs are words that desribe verbs, usually ending in '-ly'."
  }]

print("Hello! Welcome to my MadLib program. Before we start, let's remember the definitions for nouns, adjectives, verbs, and adverbs.\n") 
#print statements calling each key
print(dictionary[0]["Nouns"])
print(dictionary[0]["Adjectives"])
print(dictionary[0]["Verbs"])
print(dictionary[0]["Adverbs"])
print("\nAll righty then! Now that we understand those words, let's make a MadLib together! You'll need to provide me with some information below.\n")
#list to inquire for words from user
story_parts = [
  "1st adjective",
  "1st noun",
  "1st adverb, ending in -ly",
  "2nd adjective",
  "3rd adjective",
  "your favorite food",
  "4th adjective",
  "2nd noun",
  "2nd adverb, ending in -ly",
  "1st verb, ending in -ed",
  "3rd noun",
  "2nd verb, ending in -ed",
  "5th adjective"
]
#dictionary to hold the users words
bucket_for_story_parts = {}
#loop that fills story parts list
for part in story_parts:
  #asks the user for different word types
  word_choice = input(f"Please enter {part}: ")
  #places each chosen word inside the dictionary. It turns each word type into a key, while the user's word choice is that key's value.
  bucket_for_story_parts[part] = word_choice

# print(bucket_for_story_parts)
print("\nThank you for providing that information! Enjoy your MadLib!\n")
print(f"Once upon a time, there was a {bucket_for_story_parts['1st adjective']} little {bucket_for_story_parts['1st noun']} who grew up in a town where he was no one’s favorite. Everyday, he woke up craving for love and attention from someone, feeling so lonely… He knew he didn’t know how to get anyone to love him, so he settled for getting attention by {bucket_for_story_parts['1st adverb, ending in -ly']} committing {bucket_for_story_parts['2nd adjective']} acts he knew would only get him into trouble. All he wanted were some {bucket_for_story_parts['3rd adjective']} people to share his favorite bowl of {bucket_for_story_parts['your favorite food']} with from the {bucket_for_story_parts['4th adjective']} {bucket_for_story_parts['2nd noun']} in town. How he {bucket_for_story_parts['1st verb, ending in -ed']} the smell coming from that bowl, and he {bucket_for_story_parts['2nd adverb, ending in -ly']} wanted to share it with someone. One day, he found some {bucket_for_story_parts['3rd noun']} lying on the ground, and it was just enough to trade it for one bowl of his favorite food in the whole wide world. He knew he didn’t want to eat it all alone anymore, though… So, he {bucket_for_story_parts['2nd verb, ending in -ed']} up the courage to ask a {bucket_for_story_parts['5th adjective']} girl he’d had a crush on for quite a few years. To his surprise, she said she would join him. From that day on, he was no longer a lonely little boy. He finally found a friend to share a bowl of his favorite food with.")