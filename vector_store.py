# -*- coding: utf-8 -*-
"""# Install the package

# Installing the dependencies

Install dependencies
"""


"""Set up OpenAI API key"""

import os
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

"""Set up Pinecone API keys"""

import pinecone

# initialize pinecone
pinecone.init(
    api_key="YOUR_API_KEY",  # find at app.pinecone.io
    environment="YOUR_ENVIRONMENT_NAME"  # next to api key in console
)

"""# Index

#### jq schema to actualize the json files for the model to learn
"""



"""### JSONLoader to upload JSON files

"""

from pickle import FALSE
from google.colab import files

uploaded = files.upload()

# Check the uploaded file's name
uploaded_file_name = list(uploaded.keys())[0]

from langchain.document_loaders import JSONLoader

loader = JSONLoader(
    file_path=uploaded_file_name,
    jq_schema='.[]',
    text_content=False)

data = loader.load()
print(data)

"""### CSVLoader to upload CSV Files"""

from langchain.document_loaders.csv_loader import CSVLoader
from google.colab import files

uploaded = files.upload()

uploaded_file_name = list(uploaded.keys())[0]

print(list(uploaded.keys())[0])

loader = CSVLoader(file_path=uploaded_file_name)
data = loader.load()

print(data)

"""#### TextLoader to upload Text Files"""

from langchain.document_loaders import TextLoader

loader = TextLoader(uploaded_file_name)
data = loader.load()

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1200,
    chunk_overlap  = 1200,
    length_function = len,
)

docs_chunks = text_splitter.split_documents(data)
print(docs_chunks)

"""Create embeddings"""

from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

from langchain.vectorstores import Pinecone

index_name = "ind"

# #create a new index
docsearch = Pinecone.from_documents(docs_chunks, embeddings, index_name=index_name)

# if you already have an index, you can load it like this
#docsearch = Pinecone.from_existing_index(index_name, embeddings)

"""Vectorstore is ready. Let's try to query our docsearch with similarity search"""

query = ""
docs1 = docsearch.similarity_search(query)
print(docs1[0])



from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
llm=OpenAI()

qa_with_sources = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(), return_source_documents=True)

query = " instagram"
result = qa_with_sources({"query": query})
result["result"]

"""Output source documents that were found for the query"""

result["source_documents"]