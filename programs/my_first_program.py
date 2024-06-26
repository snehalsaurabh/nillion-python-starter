from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute (my_int1^2 + my_int2^2) - (my_int1 * my_int2)
    result = (my_int1 * my_int1 + my_int2 * my_int2) - (my_int1 * my_int2)

    return [Output(result, "my_output", party1)]
