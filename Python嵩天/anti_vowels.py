#method one
def anti_vowel1(text):
    for i in "aeiouAEIOU":
        text = text.replace(i,"")
    return text

print (anti_vowel1("HappIEAOy"))

#method two
def anti_vowel2(c):
    newstr = c
    vowels = ['a', 'e', 'i', 'o', 'u']
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")
    return newstr

print (anti_vowel2("Happy"))

#method three
def anti_vowel3(c):
    newstr = ''
    for i in c:
        if i not in 'aeiouAEIOU':
            newstr += i
    return newstr

print (anti_vowel3("Happy"))

#method four 
def anti_vowel4(text) :
  result = list(text)         # I want to work with a list
  for l in result :           # For every item of the list
      if l in "AEIOUaeiou" :  # I check if it is a vowel
        result.remove(l)      # If it is I remove it
  return "".join(result)
print (anti_vowel4("Happy"))

