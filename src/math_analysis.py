import sys
import random

def generate_math_analysis():
    # Calcula a raiz de 2
    base_root = 1.41421356237
    
    # Simula uma variação computacional (não-determinismo artificial)
    # Ora exibe com 4 casas decimais, ora com 6, ora com 2...
    precision = random.choice([2, 4, 6])
    
    print(f"The square root of 2 with simulated precision is: {base_root:.{precision}f}")

if __name__ == "__main__":
    generate_math_analysis()