import pickle

with open("house_prices.pickle", "rb") as file:
    load_model = pickle.load(file)

    