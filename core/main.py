import os
import random

from train_model import ModelTrainer
from test_model import ModelTester
from utils.io_utils import get_dir_files


def generate_testing_file(training_file_path, test_file_path):
    with open(training_file_path, "r", encoding="utf8") as training_file:
        lines = training_file.readlines()
        phrase = random.choice(lines)

    with open(test_file_path, "w", encoding="utf8") as test_file:
        test_file.write(phrase)


def generate_training_data_from_dataset(dataset_path):
    files = get_dir_files(dataset_path)
    data = ""
    for file in files:
        if ".DS_Store" not in file:
            with open(os.path.join(dataset_path, file), "r", encoding="utf8") as stream:
                data += stream.read()

    training_file_name = "{}.txt".format(os.path.basename(dataset_path))
    training_file_path = os.path.join("../training/", training_file_name)

    with open(training_file_path, "w", encoding="utf8") as training_file:
        training_file.write(data)

    return training_file_path


def main():
    trainer = ModelTrainer()

    # Generate training files
    generate_training_data_from_dataset("../datasets/Dickens")
    generate_training_data_from_dataset("../datasets/GRRM")
    generate_training_data_from_dataset("../datasets/JK Rowling")
    generate_training_data_from_dataset("../datasets/Mark Twain")
    generate_training_data_from_dataset("../datasets/Seuss")
    generate_training_data_from_dataset("../datasets/Shakespeare")

    # Generate Models
    trainer.generate_model("../training/Dickens.txt", "../models/Dickens.pkl")
    trainer.generate_model("../training/GRRM.txt", "../models/GRRM.pkl")
    trainer.generate_model("../training/JK Rowling.txt", "../models/JK Rowling.pkl")
    trainer.generate_model("../training/Mark Twain.txt", "../models/Mark Twain.pkl")
    trainer.generate_model("../training/Seuss.txt", "../models/Seuss.pkl")
    trainer.generate_model("../training/Shakespeare.txt", "../models/Shakespeare.pkl")

    # Generate Testing Files
    generate_testing_file("../training/Dickens.txt", "../testing/Dickens.txt")
    generate_testing_file("../training/GRRM.txt", "../testing/GRRM.txt")
    generate_testing_file("../training/JK Rowling.txt", "../testing/JK Rowling.txt")
    generate_testing_file("../training/Mark Twain.txt", "../testing/Mark Twain.txt")
    generate_testing_file("../training/Seuss.txt", "../testing/Seuss.txt")
    generate_testing_file("../training/Shakespeare.txt", "../testing/Shakespeare.txt")

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

    # Test Models
    tester = ModelTester()

    print("\n")

    for testing_file in testing_files:
        print(os.path.basename(testing_file))
        for model in models:
            tester.test_model(testing_file, model)
        print("\n")

if __name__ == "__main__":
    main()
