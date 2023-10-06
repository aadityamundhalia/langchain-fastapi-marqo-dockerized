import config
from langchain.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from repository.IndexRepository import IndexRepository
from repository.PromptRepository import PromptRepository
from langchain.chains import RetrievalQA
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import load_tools, Tool
from langchain.agents import initialize_agent


# Create a class for the Chat Service
class ChatService:
    # Initialize the variables
    def __init__(self, indexName=''):
        self.index_name = indexName
        self.indexRepository = IndexRepository(self.index_name)
        self.promptRepository = PromptRepository()
        self.ollamaPath = config.ollama_url
        self.modelName = config.model_name
        self.temperature = config.temprature
        # Initialize the Chat Ollama instance
        self.chat_model = ChatOllama(
            base_url=self.ollamaPath,
            model=self.modelName,
            temperature=0.1,
            verbose=True,
            callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        )

    # Function to start the chat
    def chat(self, query):
        # Get the vector store from the Index Repository
        vectorstore = self.indexRepository.vestorstore()

        # Create the QA chain using the given parameters
        qa_chain = RetrievalQA.from_chain_type(
            self.chat_model,
            retriever=vectorstore.as_retriever(),
            chain_type_kwargs={"prompt": self.promptRepository.basicPrompt()}
        )
        result = qa_chain({"query": query})
        print(result)
        # Return the result of the QA chain
        return result

    def toolBox(self, query):
        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        search = DuckDuckGoSearchRun()
        tools = [
            Tool(
                name='wikipedia',
                func=wikipedia.run,
                description="Useful for when you need to look up a topic, country or person on wikipedia"
            ),
            Tool(
                name='DuckDuckGo Search',
                func=search.run,
                description="Useful for when you need to do a search on the internet to find information that another tool can't find. be specific with your input."
            )
        ]

        zero_shot_agent = initialize_agent(
            agent="zero-shot-react-description",
            tools=tools,
            llm=self.chat_model,
            verbose=True,
            max_iterations=3,
        )

        return zero_shot_agent.run(query)

    def duckduckgo(self, query):
        search = DuckDuckGoSearchRun()
        data = search.run(query)
        return data

