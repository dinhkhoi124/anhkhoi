data = ["The girl bought a chocolate", "The boy ate the chocolate", "The girl bought a toy", "The girl played with the toytoy"]
input_text = input("Input: ")

def N_Gram(data, n=2):
    model = {}
    for sentence in data:
        words = sentence.split() 
        for i in range(len(words) - n + 1):
            key = tuple(words[i:i + n - 1])
            model.setdefault(key, []).append(words[i + n - 1])
    return model

def predict_word(model, input_text, n=2):
    key = tuple(input_text.split()[-(n-1):])
    return max(model.get(key, []), key=model.get(key, []).count, default=None)

print(f"Predict: {predict_word(N_Gram(data), input_text)}")
