import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')


def preprocess(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    return words

def calculate_scores(sentences, word_freq):
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_freq:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_freq[word]
                    else:
                        sentence_scores[sentence] += word_freq[word]
    return sentence_scores

def summarize(text, num_sentences=3):
    words = preprocess(text)
    word_freq = Counter(words)
    sentences = sent_tokenize(text)
    sentence_scores = calculate_scores(sentences, word_freq)
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join(summary_sentences)
    return summary

# Example usage:
text = "This should resolve the issue by explicitly specifying the location of NLTK data, ensuring NLTK can find the necessary resources such as the stopwords corpus. If you're still facing issues, double-check that NLTK data is properly installed and accessible on your system."
summary = summarize(text)

with open("summary.txt", "w") as file:
    file.write(summary)

    
print(summary)