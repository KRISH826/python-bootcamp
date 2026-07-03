from nltk.stem import WordNetLemmatizer

words = ["running", "jumps", "easily", "fairly", "sportingly", "fishing", "fished", "fisherman", "better", "best", "good", "bad", "worse", "worst"]

lemma = WordNetLemmatizer()
print(lemma.lemmatize("running", pos="v"))

for word in words:
    print(f"word: {word} ---> lemmatized: {lemma.lemmatize(word, pos='v')}")