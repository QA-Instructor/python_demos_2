text = "Remarkable bird, the Norwegian Blue"

print("Length of a string", len(text))
print("String a lowercase:", text.lower())
print("String a uppercase:", text.upper())
print("String a titlecase:", text.title())
print("String a capital case:", text.capitalize())

print("String with replacement:", text.replace("bird", "cocktail"))
print("\nNOTE: strings are immutable so the original string has not changed")
print(text)

bird_position = text.find("bird")
print(bird_position)