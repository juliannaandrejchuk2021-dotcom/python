from printing_functions import print_models, show_completed_models

def main():
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)
    if __name__ == "__main__":
        main()




