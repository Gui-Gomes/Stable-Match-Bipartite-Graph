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

O algoritmo Gale-Shapley, nomeado em homenagem aos matemáticos David Gale e Lloyd Shapley, é uma técnica clássica de emparelhamento na teoria dos jogos cooperativos, amplamente reconhecida por seu papel na resolução do problema de alocação estável e eficiente de recursos. Proposto originalmente em 1962, este método é implementado como parte da classe **Graph** no arquivo `graph_student_project.py` do pacote **models**. Operando em um grafo bipartido, ele facilita o emparelhamento de estudantes a projetos com base em suas preferências individuais e nas restrições específicas de cada projeto, como requisitos mínimos de nota e disponibilidade de vagas. Essa abordagem não apenas maximiza a satisfação dos estudantes ao serem alocados a projetos preferidos, mas também garante que cada projeto seja preenchido de maneira ótima, promovendo eficiência e equidade no processo de alocação.

### Funcionamento Detalhado:

#### 1. Inicialização:

- Os estudantes e projetos são representados como vértices em um grafo bipartido utilizando NetworkX. Estudantes são de um tipo (bipartite=0) e projetos são de outro tipo (bipartite=1).
- Cada estudante possui uma lista ordenada de preferências por projetos, refletindo sua ordem de prioridade.

#### 2. Processo Iterativo:

- O algoritmo é iterado por um número fixo de vezes (`max_iterations`), onde cada iteração potencialmente atualiza os emparelhamentos entre estudantes e projetos.
- Em cada iteração, o algoritmo verifica quais estudantes ainda estão "livres" (não alocados a nenhum projeto).

#### 3. Emparelhamento de Preferência:

- Para cada estudante livre, o algoritmo tenta associá-lo ao projeto mais alto em sua lista de preferências que ainda tem vagas disponíveis e cujo requisito mínimo de nota é atendido.
- Se um estudante não consegue ser associado a nenhum projeto na iteração atual, ele permanece livre para tentativas futuras.
  
#### 4. Mecanismo de Atribuição:

- Quando um estudante é aceito em um projeto, o grafo bipartido é atualizado para refletir essa conexão (`self.graph.add_edge(student_id, project_id)`).
- Se um estudante substitui outro devido a uma nota mais alta ou outro critério específico, o estudante desalojado retorna ao pool de estudantes livres.

#### 5. Convergência e Estabilidade:

- O processo continua até que todos os estudantes sejam alocados de forma estável, isto é, até que não haja mais estudantes livres que possam ser alocados a projetos dentro das condições especificadas.
  
#### 6. Saída e Avaliação:

- Após cada iteração, o estado atual dos emparelhamentos é impresso para monitorar o progresso e a distribuição dos estudantes nos projetos.
- Ao final das iterações, o número total de arestas no grafo bipartido representa a quantidade final de emparelhamentos estáveis alcançados pelo algoritmo.

### Considerações Finais:

O algoritmo Gale-Shapley é robusto para problemas de emparelhamento como este, garantindo que todos os estudantes sejam alocados da melhor maneira possível de acordo com suas preferências e as restrições dos projetos. Ele exemplifica um método eficaz para resolver problemas de alocação com critérios específicos, com aplicações amplas em economia, teoria dos jogos e otimização combinatória.


## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.