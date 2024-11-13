from collections import Counter
import re
from os.path import split
from nltk.corpus import stopwords
import nltk
# nltk.download('stopwords')

text = """
The dog (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the wolf. Also called the domestic dog, it was selectively bred from an extinct population of wolves during the Late Pleistocene by hunter-gatherers. The dog was the first species to be domesticated by humans, over 14,000 years ago and before the development of agriculture. Experts estimate that due to their long association with humans, dogs have gained the ability to thrive on a starch-rich diet that would be inadequate for other canids.[4]
Dogs have been bred for desired behaviors, sensory capabilities, and physical attributes.[5] Dog breeds vary widely in shape, size, and color. They have the same number of bones (with the exception of the tail), powerful jaws that house around 42 teeth, and well-developed senses of smell, hearing, and sight. Compared to humans, dogs have an inferior visual acuity, a superior sense of smell, and a relatively large olfactory cortex. They perform many roles for humans, such as hunting, herding, pulling loads, protection, companionship, therapy, aiding disabled people, and assisting police and the military.
Communication in dogs includes eye gaze, facial expression, vocalization, body posture (including movements of bodies and limbs), and gustatory communication (scents, pheromones, and taste). They mark their territories by urinating on them, which is more likely when entering a new environment. Over the millennia, dogs became uniquely adapted to human behavior; this adaptation includes being able to understand and communicate with humans. As such, the human–canine bond has been a topic of frequent study, and dogs' influence on human society has given them the sobriquet of "man's best friend".
"""

def zadanie1(text):
    # usuniecia dodaktowych bialych znakow
    text = text.strip()

    # slowa
    slowa = text.split(" ")
    iloscSlow = len(slowa)
    print(iloscSlow)

    # akapit
    akapit = text.split('\n')
    iloscAkapit = len(akapit)
    print(iloscAkapit)

    # zdania
    zdania = re.split(r'[.?!]+', text)
    iloscZdan = len(zdania)
    print(iloscZdan)


zadanie1(text)

def zadanie12(text):
    stop_words = set(stopwords.words('english'))
    text_words = text.split()
    text_stopwords = list(filter(lambda x: x.lower() not in stop_words, text_words))
    word_counts = Counter(text_stopwords)
    most_common = word_counts.most_common(3)
    print(most_common)

def zmien_slowa(text):
    words = text.split()
    transformed_words = [
        word[::-1] if word.lower().startswith("a") else word for word in words ]
    return " ".join(transformed_words)

transfwords = zmien_slowa(text)
print(f'Transformed words: {transfwords}')
zadanie12(text)