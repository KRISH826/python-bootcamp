import nltk
from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('averaged_perceptron_tagger_eng')

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,"""
sentences = nltk.sent_tokenize(paragraph)
print(sentences)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    filtered_words = [word for word in words if word not in set(stopwords.words('english'))]
    pos_tag = nltk.pos_tag(filtered_words)
    print(pos_tag)

sentences = "i think i love her"
for i in sentences.split():
    print(nltk.pos_tag([i]))




