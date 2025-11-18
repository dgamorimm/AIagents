from langchain.agents import create_agent
from langchain.messages import SystemMessage
from langchain.tools import tool

from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
import os 
from dotenv import load_dotenv

# 1 - Configuraçoes iniciais
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
model = ChatOpenAI(
    model="o4-mini",
    api_key=API_KEY
)

# 2 - Prompt do Sistema
system_message = SystemMessage(content="""
Você é um pesquisador muito sarcástico e irônico.
Use ferramenta 'search' sempre que necessário, especialmente
para perguntas que exigem informaçõesa da web
"""
)

# 3 - Criando a ferramenta search
@tool("search")
def search_web(query: str = "") -> str:
    """
    Busca informações na web baseada na consulta fornecida.
    
    Args:
        query: Termos para buscar dados na web
        
    Returns: 
        As informações encontradas na web ou uma mensagem indicando
        que nenhuma informação foi encontrada.
    """
    tavily_search = TavilySearchResults(max_results=3)
    search_docs = tavily_search.invoke(query)
    return search_docs
    
# 4 - Criação do agente ReAct
tools = [search_web]
graph = create_agent(
    model, 
    tools=tools,
    system_prompt=system_message.content
)

export_graph = graph