import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}
print(nato_dict)

name = input("Enter your name : ").upper()

output = [nato_dict[code] for code in name]

print(output)
