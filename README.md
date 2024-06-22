# Grafo Bipartido de Emparelhamento Estável

## Sobre

Este projeto implementa um sistema de gerenciamento de alocação de estudantes em projetos usando o algoritmo de Gale-Shapley. Desenvolvido em Python, é parte do trabalho da disciplina Teoria e Aplicação de Grafos da Universidade de Brasília (UnB), utilizando as bibliotecas NetworkX para manipulação de grafos e Matplotlib para visualização.

O sistema permite a definição de projetos com requisitos mínimos de nota e número de vagas, e estudantes com preferências por projetos e notas individuais. Os dados podem ser importados de arquivos TXT formatados especificamente ou gerados a partir deles em arquivos CSV.

## Instalação

### Pré-requisitos

Antes de começar, certifique-se de ter o Python e as bibliotecas necessárias instaladas no seu sistema.

#### 1. Instalação do Python

Se o Python não estiver instalado, siga as instruções adequadas para o seu sistema operacional:

- ##### Linux (Debian/Ubuntu):
  ```bash
  sudo apt install python3
  ```

- ##### Arch Linux:
  ```bash
  sudo pacman -S python
  ```

- ##### Fedora:
  ```bash
  sudo dnf install python3
  ```

- ##### Windows:
  Baixe o instalador do Python em python.org e siga as instruções.
  Verifique a instalação do Python no prompt de comando:
  ```bash
  python --version
  ```

- ##### macOs:
  ```bash
  brew install python
  ```
  
#### 2. Instalação das Bibliotecas Python

O projeto requer as seguintes bibliotecas Python:

- **NetworkX:** Biblioteca para criação, manipulação e estudo de estruturas, dinâmicas e funções de redes complexas.
- **Matplotlib:** Biblioteca para criação de gráficos estáticos, animações e interações.

Você pode instalá-las facilmente usando o PIP, o gerenciador de pacotes padrão do Python:

```bash
pip install networkx matplotlib
```

### Configuração do Ambiente

#### 1. Clonar o Repositório

Clone o repositório do projeto do GitHub:

```bash
git clone https://github.com/Gui-Gomes/Stable-Match-Bipartite-Graph
```

#### 2. Navegar até o Diretório do Projeto

Entre no diretório do projeto:

```bash
cd Stable-Match-Bipartite-Graph
```

#### 3. Executar o Programa

Execute o programa principal do grafo bipartido:

```bash
python main.py
```

## Estrutura do Projeto

[![Screenshot-from-2024-06-21-23-53-34.png](https://i.postimg.cc/RFDBscrt/Screenshot-from-2024-06-21-23-53-34.png)](https://postimg.cc/bDkWdSwY)

### Database

Este diretório armazena todos os dados utilizados pelo projeto. Ele é subdividido da seguinte maneira:

- **csv/:** Contém os arquivos CSV `student.csv` e `projects.csv`, que foram gerados a partir do arquivo .txt selecionado pelo usuário durante a execução do programa.
- **images/:** Este diretório armazena a imagem gerada do grafo bipartido utilizado no projeto.
- **txt/:** Aqui estão os arquivos de texto que contêm os dados de entrada para o projeto. A estrutura aceita a adição de novos arquivos `.txt`, seguindo o formato necessário para armazenamento de informações sobre estudantes e projetos. Um exemplo desse formato pode ser encontrado no arquivo `entradaProj2TAG.txt` já presente nesta pasta.

### Models

O diretório models contém definições de classes que representam as principais entidades do sistema. Cada arquivo desempenha um papel crucial na modelagem e manipulação dos dados do projeto:

- `__init__.py`: Arquivo de inicialização do módulo models, garantindo que todas as classes e funcionalidades estejam disponíveis para uso dentro do projeto.
- `graph_student_project.py`: Implementa a classe Graph, responsável pela manipulação do grafo bipartido que representa as relações entre estudantes e projetos.
- `project.py`: Define a classe Project, representando um projeto específico dentro do contexto do sistema.
- `student.py`: Contém a definição da classe Student, que modela os dados e comportamentos dos estudantes participantes do projeto.

### Utilities

Este diretório contém utilitários e funções auxiliares que são essenciais para diversas operações dentro do projeto:

- `__init__.py`: Arquivo de inicialização do módulo utilities, assegurando que todos os utilitários estejam disponíveis para uso.
- `file_handler.py`: Fornece funções para a manipulação e conversão de arquivos de texto e CSV, facilitando a integração e processamento de dados.
- `path_handler.py`: Contém funções para a manipulação e obtenção de caminhos de diretórios de arquivos, ajudando a gerenciar a estrutura de armazenamento de dados de forma eficiente.

### Arquivos Principais

Além dos diretórios específicos, o projeto inclui os seguintes arquivos principais:

- `README.md`: Este arquivo contém informações detalhadas sobre o projeto.
- `.gitignore`: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git durante o versionamento do código-fonte.
- `main.py`: O script principal do projeto, usado para iniciar e executar o programa principal.


## O Algoritmo Gale-Shapley na Perspectiva deste Projeto

O algoritmo Gale-Shapley, desenvolvido por David Gale e Lloyd Shapley em 1962, é uma técnica fundamental na teoria dos jogos cooperativos, amplamente reconhecida por resolver o problema do casamento estável. Este algoritmo facilita o emparelhamento de dois conjuntos de participantes com base em suas preferências, assegurando que não existam pares que preferem uns aos outros mais do que seus parceiros atuais. Esta análise examina uma adaptação do algoritmo Gale-Shapley implementada na classe **Graph** do arquivo **graph_student_project.py**, usada para alocar estudantes a projetos de acordo com suas preferências e restrições específicas, como requisitos mínimos de nota e disponibilidade de vagas.

### Funcionamento Detalhado:

#### 1. Inicialização:

- O grafo bipartido é construído utilizando a biblioteca NetworkX, com estudantes e projetos representados como nós. Estudantes são de um tipo (bipartite=0) e projetos de outro (bipartite=1).
- Cada estudante tem uma lista ordenada de preferências por projetos, refletindo sua ordem de prioridade.
- O grafo inicializa duas estruturas principais: `self.__students` para armazenar os estudantes e `self.__projects` para armazenar os projetos, ambos como dicionários para fácil acesso e manipulação.

#### 2. Adição de Nós ao Grafo:

- **Estudantes:** O método `add_student` adiciona estudantes ao grafo e à estrutura de dados, atribuindo a cada estudante um conjunto de projetos preferenciais e uma nota.
- **Projetos:** A função `add_project` adiciona projetos ao grafo, definindo o número de vagas disponíveis e o requisito mínimo de nota.

#### 3. Processo Iterativo:

- O algoritmo realiza um número fixo de iterações (`max_iterations`). Em cada iteração, ele potencialmente atualiza os emparelhamentos entre estudantes e projetos.
- Durante cada iteração, o algoritmo identifica quais estudantes ainda estão "livres" (não alocados a nenhum projeto) e adiciona esses estudantes a uma lista de estudantes livres (`free_students`).
  
#### 4. Emparelhamento de Preferência:

- Cada estudante livre tenta ser associado ao projeto mais alto em sua lista de preferências que ainda tenha vagas disponíveis e cujo requisito mínimo de nota seja atendido.
- Se um estudante não consegue ser associado a nenhum projeto na iteração atual, ele permanece livre para tentativas futuras.
- Se um projeto está cheio, o algoritmo verifica se o estudante pode substituir um estudante de menor nota já emparelhado ao projeto. Se a substituição for possível, ela é realizada, e o estudante desalojado retorna ao pool de estudantes livres.

#### 5. Mecanismo de Atribuição:

- Quando um estudante é aceito em um projeto, o grafo bipartido é atualizado para refletir essa conexão (`self.graph.add_edge(student_id, project_id)`).
- Se um estudante pode substituir outro devido a uma nota mais alta ou outro critério específico, o estudante desalojado retorna ao pool de estudantes livres.
  
#### 6. Convergência e Estabilidade:

- O processo continua até que todos os estudantes sejam alocados de forma estável, isto é, até que não haja mais estudantes livres que possam ser alocados a projetos dentro das condições especificadas.
- A cada iteração, o estado atual dos emparelhamentos é impresso para monitorar o progresso e a distribuição dos estudantes nos projetos.
- Ao final das iterações, o número total de arestas no grafo bipartido representa a quantidade final de emparelhamentos estáveis alcançados pelo algoritmo.

#### 7. Visualização do Grafo:

- O método `plot_bipartite_graph` permite a visualização do grafo bipartido, onde estudantes e projetos são representados como nós distintos, com espaçamento aumentado entre os vértices para melhor clareza.
- Esta visualização facilita a análise visual dos emparelhamentos e a estrutura do grafo, ajudando na identificação de padrões.

### Comparação com o Algoritmo Original

#### Semelhanças

- **Propostas Iterativas:** Assim como no algoritmo original, estudantes fazem propostas iterativas a projetos baseando-se em suas preferências.
- **Uso de Preferências:** As listas de preferências dos estudantes guiam as propostas de forma sequencial.
- **Estabilidade:** O algoritmo busca garantir emparelhamentos estáveis, ajustando-os de acordo com as notas dos estudantes, similar ao processo de rejeição e aceitação no algoritmo original.

#### Diferenças

- **Critérios Adicionais:** Além das preferências, há um critério adicional de nota mínima para os projetos, o que não está presente no problema original de casamento estável.
- **Capacidade dos Projetos:** Projetos têm um número limitado de vagas, diferente do casamento estável onde cada pessoa pode se emparelhar com apenas uma outra pessoa.
- **Substituição de Emparelhamentos:** Se um projeto está cheio, o algoritmo verifica se um novo estudante pode substituir um estudante de menor nota já emparelhado ao projeto, introduzindo um mecanismo de substituição para otimização contínua dos emparelhamentos.

### Vantagens da Adaptação

**1. Consideração de Mérito Acadêmico:** A inclusão de um critério de nota mínima para projetos garante que os estudantes com melhor desempenho acadêmico tenham preferência em projetos mais competitivos.

**2. Otimização de Recursos:** A capacidade limitada dos projetos é respeitada, refletindo melhor situações reais onde recursos e vagas são limitados.

**3. Melhoria Contínua dos Emparelhamentos:** A possibilidade de substituição de estudantes em projetos cheios por aqueles com notas superiores permite uma otimização contínua, buscando emparelhamentos mais eficientes.

**4. Eficiência e Equidade:** O algoritmo busca maximizar a satisfação dos estudantes ao alocá-los a projetos preferidos, enquanto assegura que cada projeto seja preenchido de maneira ótima, promovendo tanto eficiência quanto equidade no processo de alocação.

### Considerações Finais:

O algoritmo Gale-Shapley adaptado para a alocação de estudantes a projetos exemplifica um método robusto e eficaz para resolver problemas de emparelhamento com critérios específicos. Ao incorporar preferências e desempenho acadêmico, o algoritmo não apenas maximiza a satisfação dos estudantes ao serem alocados a projetos preferidos, mas também garante que cada projeto seja preenchido de maneira ótima. Esta adaptação mantém o espírito iterativo e de melhoria contínua do algoritmo original, promovendo eficiência e equidade no processo de alocação, com amplas aplicações em economia, teoria dos jogos e otimização combinatória. A inclusão de visualização gráfica melhora ainda mais a compreensão e análise dos emparelhamentos, facilitando a identificação de possíveis ajustes e melhorias.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.