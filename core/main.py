import os
import operator
from train_model import ModelTrainer
from test_model import ModelTester
from utils.io_utils import get_dir_files


def generate_training_data_from_dataset(dataset_path):
    files = get_dir_files(dataset_path)
    data = ""
    for file in files:
        if file == ".DS_Store":
            continue
        with open(os.path.join(dataset_path, file), "r", encoding="utf8") as stream:
            data += stream.read()
    training_file_path = "{}.txt".format(os.path.basename(dataset_path))

    with open(os.path.join("../training/", training_file_path), "w", encoding="utf8") as training_file:
        training_file.write(data)

    return training_file_path


def main():
    trainer = ModelTrainer()

    # # Generate training files
    # generate_training_data_from_dataset("../datasets/Dickens")
    # generate_training_data_from_dataset("../datasets/GRRM")
    # generate_training_data_from_dataset("../datasets/JK Rowling")
    # generate_training_data_from_dataset("../datasets/Mark Twain")
    # generate_training_data_from_dataset("../datasets/Seuss")
    # generate_training_data_from_dataset("../datasets/Shakespeare")

    # # Generate Models
    # trainer.generate_model("../training/Dickens.txt", "../models/Dickens.pkl")
    # trainer.generate_model("../training/GRRM.txt", "../models/GRRM.pkl")
    # trainer.generate_model("../training/JK Rowling.txt", "../models/JK Rowling.pkl")
    # trainer.generate_model("../training/Mark Twain.txt", "../models/Mark Twain.pkl")
    # trainer.generate_model("../training/Seuss.txt", "../models/Seuss.pkl")
    # trainer.generate_model("../training/Shakespeare.txt", "../models/Shakespeare.pkl")

    # Test Models
    testing_files = [
        "../testing/Dickens.txt",
        "../testing/GRRM.txt",
        "../testing/JK Rowling.txt",
        "../testing/Mark Twain.txt",
        "../testing/Seuss.txt",
        "../testing/Shakespeare.txt"
    ]

    models = [
        "../models/Dickens.pkl",
        "../models/GRRM.pkl",
        "../models/JK Rowling.pkl",
        "../models/Mark Twain.pkl",
        "../models/Seuss.pkl",
        "../models/Shakespeare.pkl"
    ]

    tester = ModelTester()

    print("\n")

    for testing_file in testing_files:
        filename = os.path.basename(testing_file)
        print(filename)
        tests = {}
        for model in models:
            modelfilename = os.path.basename(model)
            entropy = tester.test_model(testing_file, model)
            print(('Entropy of {} in {}:\t{}'.format(filename, modelfilename, entropy)))
            tests[modelfilename] = entropy
        bestMatch =min(tests.items(), key=operator.itemgetter(1))[0]
        print("MOST LIKELY AUTHOR: ",bestMatch)
        print("\n\n")


if __name__ == "__main__":
    main()
