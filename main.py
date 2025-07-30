from pprint import pprint
def greet_all(names):
    for name in names:
        print(f"Hello, {name}!")

def export_names(names):
    names_list = []
    for name in names:
        names_list.append(name)
    return(names_list)

if __name__ == "__main__":
    people = ["Alice", "Bob", "Charlie"]
    # pprint(people)
    greet_all(people)
    pprint(export_names(people))
