```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

# Load PDF
doc_path = "alice.pdf"  # Change this to your file path
loader = PyPDFLoader(doc_path)
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
docs = text_splitter.split_documents(documents)

# Embed text
embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name, model_kwargs={"device": "cpu"})

# Store embeddings in FAISS
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# Initialize LLM
api_key = "your_api_key_here"  # Replace with your actual API key
llm = ChatGroq(api_key=api_key)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Interactive querying
while True:
    query = input("Type your query (or type 'Exit' to quit): \n")
    if query.lower() == "exit":
        break
    try:
        result = qa.run(query)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
