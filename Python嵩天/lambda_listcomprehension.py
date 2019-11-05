languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (list(filter(lambda x: x != 'Python', languages)))


print ([x for x in languages if x != 'Python'])
