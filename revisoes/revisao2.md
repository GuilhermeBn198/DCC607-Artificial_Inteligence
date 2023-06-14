# revisão 2
- agente  = tudo que pode ser considerado capaz de perceber seu ambiente por meio de sensores, usando seus atuadores para poder agir
    - exemplo do aspirador de pó, caso o quadrado esteja sujo, então aspirar, caso contrário mover-se para o outro
    - AGENTE RACIONAL = faz tudo conceitualmente certo, ou seja, passar por uma sequencia de estados desejáveis em um ambiente, com base em uma medida de desempenho.

- racionalidade = depende de quatro fatores:
    - para cada sequencia de percepções possível, um agente racional deve selecionar uma ação que se espera venha a maximizar sua medida

- Oniciência:
    - um agente onisciente sabe o resultado real de suas ações, porém isso na realidade é impossível.

- PEAS (Performance, environment, actuators, sensors  -  desempenho, ambiente, atuadores, sensores)

- agente único vs multiagente
    - agente unico = aprendizagem de máquina
    - multiagente = algoritmo genético

## ambientes 
- deterministico vs estocástico
    - deterministico = a ação dita o resultado
    - estocástico = não

- episódico vs sequencial
    - episódico = a experiencia do agente é dividida em episódios atômicos. cada episódio consiste na percepção do agente
    - ambiente sequenciais = a decisão atual poderia afetar todas as decisões futuras

- estatico vs ambiente
    - estático = o ambiente não se altera durante a deliberação de um agente
    - dinâmico = o ambiente pode se alterar enquanto o agente está agindo

- contúnuo vs discreto
    - a distinção entre discreto e contínuo pode ser aplicada ao estado do ambiente. por exemplo, um ambiente de estados 

## resumindo agentes e ambientes

- o programa do agente implementa ma função do agente. existe uma variedade de projetos básicos de programas de agentes, refletindo o tipo de informação explicidata e usada no processo de de cisão.
- os **agentes reativos simples** respondem diretamente a percepções  
- os **agentes reativos baseados** em modelos mantêm o estado interno para controlar aspectos do mundo que não estão evidentes na percepção atual. 
- **agentes baseados em objetivos** agem para alcançar seus objetivos
- **agentes baseados em utilidade** tentam maximizar sua própria "felicidade/utilidade" esperada
- **todos os agentes podem melhorar seu desempenho por meio do aprendizado.**