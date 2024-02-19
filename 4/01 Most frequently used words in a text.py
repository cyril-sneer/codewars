from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]


test_text = """In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""

# test_text = "a a a  b  c c  d d d d  e e e e e"
# test_text = "  //wont won't won't "
# test_text = "  , e   .. "
# test_text = "  '''  "
# test_text = "  ...  "

# "(?u)\b\w+\b"

from sklearn.feature_extraction.text import CountVectorizer
from string import punctuation

def top_3_words(text):
    text = text.strip(punctuation + " ")
    if len(text):
        vectorizer = CountVectorizer(stop_words=None, token_pattern=r"[a-zA-Z0-9']+")
        X = vectorizer.fit_transform([text])
        sorted_indexes = X.toarray().argsort()
        top_three_indexes = sorted_indexes[0][-1:-4:-1]
        return vectorizer.get_feature_names_out()[top_three_indexes].tolist()
    else:
        return []

if __name__ == '__main__':
    print(type(top_3_words(test_text)))
