def get_middle(s): return ((s[int(len(s) / 2):-int((len(s) / 2))], s[int((len(s) - 2) / 2):-int((len(s) - 2) / 2)])[len(s) % 2 == 0], s)[len(s) == 1 or len(s) == 2]

print(get_middle("Aa"))