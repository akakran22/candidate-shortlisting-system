from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer


#function to summarize the text using sumy library and LSA algorithm
def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    stemmer = Stemmer('english')
    summarizer = LsaSummarizer(stemmer)
    summary = summarizer(parser.document, sentences_count=3)
    return ' '.join(str(sentence) for sentence in summary)