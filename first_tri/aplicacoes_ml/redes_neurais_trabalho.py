import numpy as np
from sklearn.neural_network import MLPClassifier


def generate_data(num_samples: int) -> list[np.array]:
    """Irá gerar amostras aleatórias para poder treinar o modelo de ML

    Args:
        num_samples (int): Quantidade de amostras que se deseja criar

    Returns:
        np.array : Irá retornar um array do tipo: array([[0, 0, 0, 1, 0, 0, 0, 1]])
    """
    messages = np.random.randint(2, size=(num_samples, 8))
    keys = np.random.randint(2, size=(num_samples, 8))
    msg_encrypted = np.bitwise_xor(messages, keys)
    return messages, keys, msg_encrypted


def convert_binary_to_decimal(bin_num: np.array) -> int:
    """Recebe um array de numeros binários e irá converter em um numero de base decimal

    Args:
        bin_num (np.array): array no qual se deve converter em base decimal

    Returns:
        int: um numero na base decimal
    """
    decimal_num = bin_num.tolist()[0]
    decimal_num = "".join(str(num) for num in decimal_num)
    return int(decimal_num, 2)


if __name__ == "__main__":
    """
    Esse programa tem como intuito aplicar o modelo de redes neurais para solucionar um problema de criptografia XOR.

    Conceito:
    Uma imagem é feita de pixels (0 ou 1), se modificarmos aleatoriamente os pixels da imagem, obteremos uma nova imagem como resultado.
    Com base nessas informações para aplicarmos o algoritimo de criptografia XOR usamos a seguinte tabela da veradde:

    - Onde temos numeros iguais o resultado será 0
    - Onde temos numeros diferentes o resultado será 1

    Toda essa codificação é baseada em uma chave, no qual irá ser aplicada a matriz de pixels original, gerando uma nova mensagem, e caso queria descobrir a mensagem original, é necessário a chave para decodifica-lá.


    Desenvolvimento:

    Criei uma função no qual irá gerar dois array com 8 elementos aleatoriamente, um para uma mensagem de 8 bits e outro para a chave de 8 bits, após isso irei aplicar a função np.bitwise_xor, para realizar a soma dos dois arrays.

    Após o treino do modelo podemos predizer o resultado com base na mensagem e na chave que fornecermos para o modelo de rede neural.
    """

    # Gera as amostras para o treino do modelo
    train_message, train_key, train_encrypted = generate_data(10000000)

    # Cria o modelo de rede neurias
    clf1 = MLPClassifier(
        solver="lbfgs",
        activation="logistic",
        alpha=1e-5,
        hidden_layer_sizes=(1500, 1500),
        random_state=1,
    )

    # Treino do modelo
    clf1.fit(np.hstack([train_message, train_key]), train_encrypted)

    # Gera uma amostra para fazer o teste de forma aleatória
    test_msg, test_key, test_encry_msg = generate_data(1)

    # Predição do modelo
    prediction = clf1.predict(np.hstack([test_msg, test_key]))

    # Pega o array de binários e converte é um numero de base 10
    encry_msg = convert_binary_to_decimal(test_encry_msg)
    msg = convert_binary_to_decimal(test_msg)
    prediction = convert_binary_to_decimal(prediction)
    test_encry_msg = convert_binary_to_decimal(test_encry_msg)

    # Imprime o resultado para o usuário
    print(
        f"""
        O numero encriptado: {encry_msg}
        key: {test_key}
        Descriptografado pelo XOR algoritimo usando a key é o: {test_encry_msg}
        Descriptografado pela rede neural é o: {prediction}
        """
    )
