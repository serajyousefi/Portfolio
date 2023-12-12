from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ['OPENAI_API_KEY'] = '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'

loader = PyPDFLoader("DGEA.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(data)

vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

question = "who is ceo of dgea ?"
docs = vectorstore.similarity_search(question)
len(docs)

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
result = qa_chain({"query": question})

print(result)
