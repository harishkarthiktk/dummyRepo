from pprint import pprint
def greet_all(names):
    for name in names:
        print(f"Hello, {name}!")
if __name__ == "__main__":
    people = ["Alice", "Bob", "Charlie"]
    pprint(people)
    greet_all(people)
