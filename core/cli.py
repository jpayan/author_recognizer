from train_model import ModelTrainer
from test_model import ModelTester


def main():
    trainer = ModelTrainer()

    # Generate Models
    trainer.generate_model('./training/dutch.txt', './models/dutch.pkl')
    trainer.generate_model('./training/english.txt', './models/english.pkl')
    trainer.generate_model('./training/german.txt', './models/german.pkl')
    trainer.generate_model('./training/russian.txt', './models/russian.pkl')
    trainer.generate_model('./training/spanish.txt', './models/spanish.pkl')

    print('\n')

    # Test Models
    testing_files = ['./testing/dutch.txt', './testing/english.txt', './testing/german.txt',
                     './testing/russian.txt', './testing/spanish.txt']
    models = ['./models/dutch.pkl', './models/english.pkl', './models/german.pkl',
              './models/russian.pkl', './models/spanish.pkl']

    tester = ModelTester()

    for testing_file in testing_files:
        for model in models:
            tester.test_model(testing_file, model)
        print('\n')

if __name__ == '__main__':
    main()
