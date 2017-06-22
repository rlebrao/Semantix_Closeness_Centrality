# Semantix_Closeness_Centrality

Repositório com resolução para o desafio de analise por proximidade pela empresa Semantix

O código .py em questão resolve o problema da análise de rede social proposta no desafio. O resultado irá trazer cada nó do grafo dado, ordenado por o seu valor de proximidade

Para a resolução do problema, primeiro o arquivo de grafo é percorrido e a partir dele é montado um dicionário onde ira relacionar cada nó do gráfo com suas conexões. Em seguida, é chamado uma função ("ClosenessCentrality") passando como parâmetro o dicionário do grafo recém criado, a função percorrerá o dicionario e em cada linha chamará outra função ("findShortestPath") que encontrará o menor caminho para o nó passado como parâmetro(a função utiliza uma busca exaustiva para encontrar o menor caminho). Após descobrir o coeficiente de proximidade, a função imprimi na tela os valores ordenados pelo seu coeficiente.

Como Executar o script:

1.Instalar o python versão 3.6

2.Fazer o download do repositório zipado

3.Descompactar o arquivo e entrar na pasta com o mesmo nome

4.Dentro da pasta você verá os arquivos: edges.dat, README.md e semantix_test.py


No linux: Entrar pelo bash e navegar até a pasta recém descompactada (**Semantix_Closeness_Centrality-master**), onde tera os arquivos edges.dat e semantix_test.(Navegue até a pasta utiliazando o comando "cd Nome\do\diretorio")

No Windows: Entrar pelo cmd e navegar até a pasta recém descompactada (**Semantix_Closeness_Centrality-master**), onde tera os arquivos edges.dat e semantix_test.(Navegue até a pasta utiliazando o comando "cd Nome\do\diretorio")

Estando dentro da pasta que contem o arquivo.py, executar o seguinte comando:

  _python semantix_test.py_


O script deverá mostrar o valor de proximidade de cada vértice, ordedado de form crescente
