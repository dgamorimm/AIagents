1. Abrir o terminal e digitar o seguinte comando
```bash
 langgraph
```

2. Criar um arquivo `langgraph.json` para realizar a integração com o LangSmith

3. Dentro do arquivo você tem que passar<br>
    3.1 As dependências do projeto
    3.2 dentro de graphs colocar em chave:valor no agent o nome do arquivo.py e a variavel e que nesse caso será `teste:export_graph`

4. Colocar nas variaveis de embiente diretamento no terminal 
```bash
export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
export LANGSMITH_API_KEY=------------------------------------------KEY
export LANGSMITH_PROJECT=douglas-estudo
```

5. Executar o comando no terminal para habilitar o tracing do LangSmith em dev
```bash
 langgraph dev
```