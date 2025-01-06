import sys
from scripts.train_agent import main as train
from scripts.test_agent import main as test

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [train|test]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "train":
        train()
    elif command == "test":
        test()
    else:
        print("Invalid command. Use 'train' or 'test'.")

