def analyze_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    
    # Análises básicas
    insights = {
        'total_sentences': len(sentences),
        'avg_sentence_length': sum(len(s.split()) for s in sentences) / len(sentences),
        'unique_words': len(set(' '.join(sentences).split()))
    }
    
    return insights

# Exemplo de uso
file_path = 'inputs/sentences.txt'
results = analyze_sentences(file_path)
print(results)