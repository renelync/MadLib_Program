# dictionary to remind user of specific definitions
dictionary = [
  {
    "Nouns": "Nouns are words that represent people, places, or things.",
    "Adjectives": "Adjectives are words that describe people, places, or things.",
    "Verbs": "Verbs are words that show an action(sing), occurence(develop), or state of being(exist).",
    "Adverbs": "Adverbs are words that desribe verbs, usually ending in '-ly'."
  }]

print("Hello! Welcome to my MadLib program. Before we start, let's remember the definitions for nouns, adjectives, verbs, and adverbs.\n") 
# print statements calling each key
print(dictionary[0]["Nouns"])
print(dictionary[0]["Adjectives"])
print(dictionary[0]["Verbs"])
print(dictionary[0]["Adverbs"])
print("\nNow that we understand those words, let's make a MadLib together! You'll need to provide me with some information below.\n")

city_name = input(f"First, what city would you like your main character to be from? ")

# list to inquire for words from user
story_parts = [
  "1st noun",
  "1st adverb, ending in -ly",
  "1st adjective",
  "2nd adjective",
  "number",
  "your favorite food",
  "2nd noun",
  "2nd adverb, ending in -ly",
  "1st verb, ending in -ed",
  "2nd verb, ending in -ed"
]
# dictionary to hold the users words
bucket_for_story_parts = {}
# loop that fills story parts list
for part in story_parts:
  #asks the user for different word types
  word_choice = input(f"\nNext, please enter your {part}: ")
  #places each chosen word inside the dictionary. It turns each word type into a key, while the user's word choice is that key's value.
  bucket_for_story_parts[part] = word_choice.lower()

# print(bucket_for_story_parts)
story_time = "\nawesome job! here's your madlib!"
print(story_time.upper())
print(f"\nOnce upon a time, there was a young little {bucket_for_story_parts['1st noun']} who grew up in the town of {city_name.capitalize()} where he was no one’s favorite. Everyday, he woke up craving for love and attention from someone, feeling so lonely… He knew he didn’t know how to get anyone to love him, so he settled for getting attention by {bucket_for_story_parts['1st adverb, ending in -ly']} committing {bucket_for_story_parts['1st adjective']} acts he knew would only get him into trouble. All he wanted was some other young {bucket_for_story_parts['1st noun']} to share {bucket_for_story_parts['number']} of his favorite bowl(s) of {bucket_for_story_parts['your favorite food']} with from the oldest {bucket_for_story_parts['1st noun']}, who was also the best chef, in town. How he {bucket_for_story_parts['1st verb, ending in -ed']} the smell coming from that bowl, and he {bucket_for_story_parts['2nd adverb, ending in -ly']} wanted to share it with someone. One day, he found some {bucket_for_story_parts['2nd noun']} lying on the ground, and it was just enough to trade it for {bucket_for_story_parts['number']} bowl(s) of his favorite food in the whole wide world. He knew he didn’t want to eat it all alone anymore, though… So, he {bucket_for_story_parts['2nd verb, ending in -ed']} up the courage to ask another young {bucket_for_story_parts['1st noun']} he passes by everyday. To his surprise, they said they would love to join him. Because, of course, free food! From that day on, he was no longer a lonely little {bucket_for_story_parts['1st noun']}. He finally found another young {bucket_for_story_parts['1st noun']} to share his favorite food with.")
