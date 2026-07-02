import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, wordpunct_tokenize


corpus = """Hello welcome to the world of Natural Language Processing. This is a sample text for tokenization. Tokenization is the process of breaking down text into smaller units called tokens. These tokens can be words, phrases, or even sentences. Tokenization is an essential step in many NLP tasks such as text classification, sentiment analysis, and machine translation.
In this example, we will demonstrate how to perform tokenization using the NLTK library in Python. NLTK provides various tokenization methods, including word tokenization and sentence tokenization. We will use the word_tokenize function to split the text into individual words. Let's get started with the tokenization process and explore the different tokens generated from the sample text.
"""


print(corpus)

# sentance into paragraph
sentences = sent_tokenize(corpus)
print(sentences)


words = word_tokenize(corpus)
print(words)

wordpuncts = wordpunct_tokenize(corpus)
print(wordpuncts)


treebank = nltk.TreebankWordTokenizer()
print(treebank.tokenize(corpus))