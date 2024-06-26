
# Definir descrições dos clusters
cluster_descriptions = {
    0: "Alunos com desempenho acadêmico mais baixo, média de notas finais G3 em torno de 4.19.",
    1: "Alunos com desempenho acadêmico intermediário, média de notas finais G3 em torno de 10.74.",
    2: "Alunos com desempenho acadêmico mais alto, média de notas finais G3 em torno de 15.11."
}

# Exemplos de prompts para recomendações
prompts = {
    0: f"Para alunos com desempenho acadêmico mais baixo, média de notas finais G3 em torno de 4.19. Quais recomendações de estudo e hábitos você sugeriria para melhorar seu desempenho?",
    1: f"Para alunos com desempenho acadêmico intermediário, média de notas finais G3 em torno de 10.74. Quais recomendações de estudo e hábitos você sugeriria para alcançar um desempenho mais alto?",
    2: f"Para alunos com desempenho acadêmico mais alto, média de notas finais G3 em torno de 15.11. Quais recomendações você sugeriria para manter ou melhorar ainda mais seu desempenho?"
}

def get_recommendations(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um conselheiro acadêmico."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Gerar recomendações para cada cluster
recommendations = {cluster: get_recommendations(prompt) for cluster, prompt in prompts.items()}

# Exibir recomendações
for cluster, recommendation in recommendations.items():
    print(f"Cluster {cluster}:\n{recommendation}\n")
