import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from bible import get_bible
from wikipedia import get_wikipedia


def join(user_list):
    string = ""
    for char in user_list:
        string = string + " " + str(char)
    return string


def horiz_graph(height, labels):
    y_pos = np.arange(len(labels))

    plt.barh(y_pos, height)
    plt.yticks(y_pos, labels)

    font = {'family': 'sans-serif',
            'color': 'darkblue',
            'weight': 'bold',
            'size': 16,
            }

    plt.xlabel('Usages', fontdict=font)
    plt.ylabel('Word', fontdict=font)
    plt.title('20 Most Common Words in 1000 Wikipedia Pages', fontdict=font)

    plt.subplots_adjust(bottom=0.15, left=0.17)

    plt.show()


def most_frequent(list_, num):
    occurrence_count = Counter(list_)
    return occurrence_count.most_common(num)


def graph(data):
    labels = []
    usages = []
    for pair in data:
        labels.append(str(list(pair)[0]))
        usages.append(list(pair)[1])

    horiz_graph(usages, labels)


data = [get_bible(),
        get_wikipedia(10)]

text = []
for i in data:
    text.extend(i)

words = [word.lower() for word in text]
print(words)

graph(most_frequent(words, 20))
