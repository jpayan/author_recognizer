from utils.io_utils import open_file, save_object, BEGIN, END


class ModelTrainer(object):

    def __init__(self):
        self.__ngram_frequency = {}
        self.__context_frequency = {'': 0}

    def handle_ngram_frequency(self, bigram, ngram):
        if bigram in self.__ngram_frequency:
            self.__ngram_frequency[bigram] += 1
        else:
            self.__ngram_frequency[bigram] = 1
        if ngram in self.__ngram_frequency:
            self.__ngram_frequency[ngram] += 1
        else:
            self.__ngram_frequency[ngram] = 1

    def handle_context_frequency(self, context):
        if context in self.__context_frequency:
            self.__context_frequency[context] += 1
        else:
            self.__context_frequency[context] = 1
        self.__context_frequency[''] += 1

    def clean_frequencies(self):
        self.__ngram_frequency = {}
        self.__context_frequency = {'': 0}

    def generate_model(self, training_file, model_file):
        # Read training data
        training_data = open_file(training_file, 'r')

        for line in training_data:
            words = line.split()
            words.insert(0, BEGIN)
            words.append(END)

            # Generate bigrams
            for i in range(1, len(words) - 1):
                previous_word = words[i - 1].lower()
                current_word = words[i].lower()
                bigram = '{} {}'.format(previous_word, current_word)

                # Handle frequency
                self.handle_ngram_frequency(bigram, current_word)
                self.handle_context_frequency(previous_word)

        model = {}
        for ngram, frequency in self.__ngram_frequency.items():
            words = ngram.split()
            words.pop()
            context = ''.join(words)

            # Calculate Probability of ngram
            probability = self.__ngram_frequency[ngram] / self.__context_frequency[context]

            # Add to model
            model[ngram] = probability

        # Write model
        save_object(model, model_file)
        self.clean_frequencies()
        print('Generated model file: {}\tFrom training data: {}'.format(model_file, training_file))
