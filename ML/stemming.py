from nltk.stem import PorterStemmer, RegexpStemmer, SnowballStemmer

words = ["running", "jumps", "easily", "fairly", "sportingly", "fishing", "fished", "fisherman"]

# stemmer = PorterStemmer()

# for word in words:
#     print(f"word: {word} ---> stemmed: {stemmer.stem(word)}")


regStemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print(f"Using RegexpStemmer: {regStemmer.stem('running')}")


snowball_stemmer = SnowballStemmer("english")

for word in words:
    print(f"word: {word} ---> stemmed: {snowball_stemmer.stem(word)}")



