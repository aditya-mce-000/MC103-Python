lang = ['Python', 'C', 'Java', 'Javascript', 'HTML']
print(lang)

lang.append('CSS')
print(lang)

lang.insert(2,'Matlab')
print(lang)

x = lang.pop()
print(lang)
print(x)

lang.remove('C')
print(lang)

del lang[4]
print(lang)