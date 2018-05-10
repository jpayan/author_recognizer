from math import log2
from utils.io_utils import open_file, load_object, BEGIN, END


class ModelTester(object):
    def calculate_lambda(self, word, probs):
        unique_ngrams = len(probs) - 1 if word in probs else len(probs)
        frequency = probs[word] if word in probs else 0
        return 1 - (unique_ngrams / (unique_ngrams + frequency))

    def test_model(self, test_file, model_file):
        test_data = open_file(test_file, 'r')
        probs = load_object(model_file)
        h = 0
        w = 0

        for line in test_data:
            words = line.split()
            words.insert(0, BEGIN)
            words.append(END)

            for i in range(1, len(words) - 1):
                previous_word = words[i - 1].lower()
                current_word = words[i].lower()
                bigram = '{} {}'.format(previous_word, current_word)

                word_probability = probs[current_word] if current_word in probs else 0
                bigram_probability = probs[bigram] if bigram in probs else 0

                # l1 = self.calculate_lambda(previous_word, probs)
                # l2 = self.calculate_lambda(current_word, probs)

                # Happy path
                l1 = 0.95
                l2 = 0.95

                p1 = l1 * word_probability + (1 - l1) / 1000000
                p2 = l1 * bigram_probability + (1 - l2) * p1
                h += -log2(p2)
                w += 1

        print('Entropy of {} in {}:\t{}'.format(test_file, model_file, str(h / w)))
