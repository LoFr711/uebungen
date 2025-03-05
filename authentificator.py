from typing import Tuple
import random
from math import factorial

def calculate_vector_length(num_individuals: int, hamming_distance: int) -> int:
    """
    Berechnet die notwendige Länge des Merkmalsvektors für eine gegebene Anzahl von Individuen 
    und einer Mindest-Hammingdistanz.
    
    :param num_individuals: Anzahl der eindeutigen Individuen
    :param hamming_distance: Mindest-Hammingdistanz zwischen den Merkmalsvektoren
    :return: Länge des Merkmalsvektors
    """
    # TODO: implement
    length_vector = 0
    if num_individuals == 2:
        length_vector = hamming_distance
    elif num_individuals == 1:
        length_vector = 1
    else:
        # Leider nicht optimal, aber ich bekomme es nicht besser hin :/
        length_vector = hamming_distance * (num_individuals // 2)

    return length_vector


def estimate_error_probability(vector_length: int, error_rate: float, hamming_distance: int) -> float:
    """
    Schätzt die Wahrscheinlichkeit, dass ein ausgewähltes Individuum aufgrund von Sensorfehlern 
    nicht erkannt wird.
    
    :param vector_length: Länge des Merkmalsvektors
    :param error_rate: Fehlerquote der Sensorik
    :return: Wahrscheinlichkeit eines Erkennungsfehlers
    """
    # TODO: implement
    # Vektor kann nicht erkannt werden, wenn mind (hamming_distance // 2) Fehler passieren
    # Counter_prob = Wahrscheinlichkeit, dass weniger als (hamming_distance // 2) Fehler passieren
    counter_prob = 0
    for i in range(0, hamming_distance // 2):
        prob =  (factorial(vector_length) // (factorial(i) * factorial(vector_length - i)))* (error_rate ** i) * ((1 - error_rate) ** (vector_length - i))
        #print(f"Prob = {prob}")
        counter_prob += prob
    return 1 - counter_prob
    

def adjust_for_multiple_individuals():
    """
    Beschreibt, wie die Problemlösung angepasst werden muss, um zwei verschiedene Individuen 
    korrekt zu erkennen.
    """
    # TODO: implement
    pass

def probability_of_duplicate_vectors(vector_length: int, num_vectors: int) -> float:
    """
    Berechnet die Wahrscheinlichkeit, dass unter einer gegebenen Anzahl zufällig gewählter 
    Merkmalsvektoren mindestens zwei identisch sind.
    
    :param vector_length: Länge des Merkmalsvektors
    :param num_vectors: Anzahl der generierten Merkmalsvektoren
    :return: Wahrscheinlichkeit von Duplikaten
    """
    # TODO: implement
    poss_vect = 2 ** vector_length
    if poss_vect < num_vectors:
        return 0.0
    counter_probability = 1.0
    for i in range(1, num_vectors):
        counter_probability = counter_probability * ((poss_vect - (i)) / poss_vect)
    return 1 - counter_probability

def calculate_hamming_distance(vector1: str, vector2: str) -> int:
    """
    Berechnet die Hamming-Distanz zwischen zwei Merkmalsvektoren.
    
    :param vector1: Erster Merkmalsvektor
    :param vector2: Zweiter Merkmalsvektor
    :return: Hamming-Distanz zwischen den Vektoren
    """
    # TODO: implement
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of equal length!")
    ham_dist = 0
    for bit in range(0, len(vector1)):
        if vector1[bit] != vector2[bit]:
            ham_dist += 1
    return ham_dist

def generate_random_vector(vector_length: int) -> str:
    """
    Generiert einen zufälligen Merkmalsvektor einer gegebenen Länge.
    
    :param vector_length: Länge des Merkmalsvektors
    :return: Zufällig generierter Merkmalsvektor
    """
    # TODO: implement
    vector = ""
    for i in range(0, vector_length):
        vector += str(random.randint(0,1))
    return vector

def main():
    # 1: Berechnung der Vektorlänge
    print("---Aufgabe 1 ---")
    hamming_distance = 5
    print(f" \nHamming-Distanz = {hamming_distance}\n")
    for i in [2, 3, 4, 8]:
        vector_length = calculate_vector_length(i, hamming_distance)
        print(f"Benötigte Länge des Vektors bei {i} eindeutigen Individuen: {vector_length}")
    vector_length = calculate_vector_length(8_000_000_000, hamming_distance)
    print(f"Benötigte Länge des Vektors bei 8 Milliarden eindeutigen Individuen: {vector_length}")

    # 2: Ausgewähltes Individuum wird nicht erkannt
    print("\n---Aufgabe 2 ---")
    for vector_length in [10, 100]:
        print("")
        for hamming_distance in [2, vector_length // 4, vector_length // 2]:
            vect_not_rec = estimate_error_probability(vector_length, 0.01, hamming_distance)
            print(f"Wahrscheinlichkeit, dass ein Vektor der Länge {vector_length} mit Hamming-Distanz {hamming_distance} nicht erkannt wird: {vect_not_rec}")
    
    # 3: Anpassung für mehrere Individuen
    print("\n---Aufgabe 3 ---")
    print("Nicht bearbeitet")

    #4: Wahrscheinlichkeit von Duplikaten
    print("\n---Aufgabe 4 ---")
    num_vecs = 100
    print(f"Anzahl Vektoren {num_vecs} und Hamming-Distanz 2")
    for len_vec in [num_vecs, num_vecs * 2, num_vecs * 4]:
        prob_dupl_vect = probability_of_duplicate_vectors(len_vec, num_vecs)
        print(f"\nWahrscheinlichkeit, dass zwei Vektoren von {num_vecs} der Länge {len_vec} identisch sind: {prob_dupl_vect}")
        probl_wrong_vector = estimate_error_probability(len_vec, 0.01, 2)
        print(f"Wahrscheinlichkeit, dass bei der Vektor Länge {len_vec} ein falscher Vektor ausgegeben wird: {probl_wrong_vector}")
if __name__ == "__main__":
    main()
