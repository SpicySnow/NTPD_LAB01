import joblib
import pandas as pd
from sklearn.datasets import load_iris
import random


def main():
    filename = 'LAB01/model_v1.0.0.joblib'
    model = joblib.load(filename)
    iris = load_iris(as_frame=True)

    rnd = random.randint(0, len(iris.frame) - 1)

    sample = iris.frame[iris.feature_names].iloc[[rnd]]
    prediction = model.predict(sample)
    predicted_class = iris.target_names[prediction[0]]
    real_class = iris.target_names[iris.frame["target"].iloc[rnd]]

    print("=== Rekord testowy ===")
    print(sample)
    print("\n=== Predykcja ===")
    print(f"Przewidziana klasa: {predicted_class}")
    print(f"Prawdziwa klasa: {real_class}")


if __name__ == "__main__":
    main()
