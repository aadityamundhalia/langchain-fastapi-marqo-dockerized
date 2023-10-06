from langchain.prompts import PromptTemplate


class PromptRepository:

    def basicPrompt(self):
        template = """[INST] <<SYS>> Use the following pieces of context to
         answer the question at the end.
        Use minimum sentences and keep the answer as concise as possible.
        <</SYS>>
        {context}
        Question: {question}
        Helpful Answer:[/INST]"""
        QA_CHAIN_PROMPT = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )

        return QA_CHAIN_PROMPT
