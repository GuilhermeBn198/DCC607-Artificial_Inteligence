# **Exercícios**
Nota: As terminologias mostradas nesta aula serão utilizadas com frequência no decorrer desta disciplina. Assim, é importantíssimo que o aluno responda o seguinte exercício antes da próxima aula.

## **1. Como você definiria aprendizagem de máquina?**
	
	R: É a ciência (e arte) de programar computadores a fim de que eles possam aprender através dos dados


## **2. Você poderia mencionar quatro tipos de problemas onde aprendizagem de máquina seria aplicável?**
	
	R: filtro de spam, Reconhecimento de voz, Sistemas de recomendação, Reconhecimento de objetos em imagens

## **3. O que é um conjunto de treinamento com labels?**
	
	R: Um conjunto de treinamento com labels é um conjunto de dados usado para treinar um modelo de aprendizado de máquina. Cada exemplo no conjunto de treinamento tem um rótulo ou uma resposta conhecida que o modelo deve aprender a prever.

## **4. Quais são as duas tarefas mais comuns em aprendizagem de máquina supervisionada?**
	
	R: As duas tarefas mais comuns em aprendizado de máquina supervisionado são classificação e regressão.

## **5. Cite duas tarefas comuns em aprendizagem de máquina não supervisionada?**
	
	R: agrupamento e redução de dimensionalidade.

## **6. Que tipo de aprendizagem de máquina seria usada para permitir que um robô andasse em vários terrenos desconhecidos?**
	
	R: Aprendizagem por reforço

## **7. Qual tipo de algoritmo você usaria para segmentar consumidores em múltiplos grupos?**
	
	R: Clusterização pois consigo agrupar os consumidores em diferentes clusters(grupos)

## **8. O problema de detecção de spam é supervisionado ou não supervisionado?**
	
	R: supervisionado, pois usa rotularização das mensagens usadas como spam para se adaptar a futuros problemas

## **9. O que é um método online em aprendizagem de máquina?**
	
	R: é um método incremental que permite separar os dados de treinamento em mini-batches, que após as rodadas, irão incrementando a AM pouco a pouco

## **10. Que tipo de algoritmo de aprendizagem de máquina usa uma métrica de similaridade para realizar a predição?**
	
	R: instance-based

## **11. Mencione 4 dos principais desafios em AM.**
	
	R: 1 - quantidade insuficiente de dados de treino
	   2 - dados não representativos
	   3 - dados com má qualidade
	   4 - atributos irrelevantes

## **12. Se o modelo preditivo tem boa performance no conjunto de treino mas generaliza mal em novos exemplos, o que está acontecendo? Você pode enumerar 3 soluções potenciais?**
	
	R: OVERFITTING,  usar tecnicas de regularização, aumentar quantidade de dados(até certo ponto), reduzir quantidade de ruídos.


## **13. O que é um conjunto de teste e por que é importante usá-lo?**
	
	R: o conjunto de teste serve para avaliar o desempenho do modelo de AM em relação a dados diferentes dos dados de treino

## **14. O que é um conjunto de validação e por que é importante usá-lo?**
	
	R: serve para Testar os diferentes algoritmos em validação e escolher a com menor erro em validação; Encerrar o treinamento quando o erro em validação começar a aumentar critério de parada;


## **15. Qual a relação do dilema viés-variância com overfitting e underfitting?**
	
	R: Deve existir um equilibrio entre os dois, pois viés é o ato de aprender demais uma parte errada dos dados, não tendo adaptabilidade, enquanto variancia
