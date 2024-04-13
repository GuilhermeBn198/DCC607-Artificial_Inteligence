# questão das N-rainhas usando algoritmos genéticos

## feito com base nos vídeos

[veja o vídeo de explicação do algoritmo feito pela Michelle Gomes da UFMG](https://youtu.be/pkxn9LgVQyQ)
[veja o vídeo de execução feito pela Michelle Gomes da UFMG](https://youtu.be/CH7FozAv5Yw)

## caracteristicas do algoritmo implementado

- percebe-se na execução que, por trabalhar com 2 variáveis separadas 1 para determinar o numero de raínhas e 1 para determinar o numero de gerações, esta ultima sendo diretamente relacionada com a população, faz com que seja necessário o ajuste fino dos parâmetros individualmente para se conseguir chegar no numero ótimo de posições desejado
- se colocarmos 8 rainhas para uma população de 100, o algoritmo n achará o resultado , mas se colocarmos uma população de 1000, ele conseguirá achar o resultado e assim seguirá. Isso se dá pelo numero de gerações que é feito nos testes, caso queiramos achar resultados para uma maior quantidade de raínhas
- por vezes pode ocasionar erro pois ele não achou O MELHOR RESULTADO possível que seria encontrar a posição de todas as raínhas, esse fenomeno ocorre pois como as gerações são diretamente atreladas a quantidade da população, dependendo da forma q os dados forem dispostos no array o numero de egerações necessárias para aquela iteração do algoritmo pode não ser suficiente para encontrar o resultado. Por exemplo 7 raínhas para 100 gerações, terá vezes que encontrará o resultado facilmente, mas terá vezes que ocorrerá erro de index out of range.
