# PDF-Based Retrieval-Augmented Generation (RAG) System

This project implements a Retrieval-Augmented Generation (RAG) system using LangChain, FAISS, and Groq AI. The system processes a PDF document, converts it into embeddings, stores them in a FAISS vector database, and allows users to query the document interactively.

## Overview of Technologies Used

### **LangChain**
LangChain is a framework designed for developing applications using Large Language Models (LLMs). It simplifies integration with external knowledge sources, retrieval mechanisms, and various embeddings.

### **FAISS (Facebook AI Similarity Search)**
FAISS is a library for efficient similarity search and clustering of dense vectors. It is used to store and retrieve document embeddings, ensuring quick and scalable information retrieval.

### **Sentence Transformers**
We use `sentence-transformers/all-mpnet-base-v2`, a pre-trained transformer model optimized for creating high-quality sentence embeddings. It converts text into vector representations suitable for similarity-based retrieval.

### **Groq AI (LLM)**
Groq AI provides a powerful and cost-efficient LLM alternative to OpenAI's models. It enables us to process natural language queries and generate context-aware responses.

## Features
- **PDF Processing:** Extracts and processes text from PDFs.
- **Text Chunking:** Splits text into manageable chunks for embedding.
- **Embedding & Storage:** Converts text into vector representations and stores them in FAISS for efficient retrieval.
- **Retrieval-Based Querying:** Uses FAISS to fetch relevant text chunks.
- **LLM Integration:** Uses Groq AI for contextual response generation based on retrieved chunks.
- **Interactive CLI:** Users can input queries and receive responses dynamically.

## Installation

Clone the repository:
```sh
git clone https://github.com/yourusername/pdf-rag.git
cd pdf-rag
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

1. Place your PDF file in the project directory.
2. Update the file path in `main.py` (default: `alice.pdf`).
3. Run the script:
```sh
python main.py
```
4. Enter queries interactively.
5. Type 'Exit' to stop the program.

## File Structure
```
/pdf-rag
│── README.md           # Project Documentation
│── requirements.txt    # List of Dependencies
│── main.py             # Main script for execution
```

## How It Works

1. **PDF Loading & Processing:**
   - The PDF document is loaded using `PyPDFLoader`.
   - Extracted text is split into chunks using `CharacterTextSplitter` to optimize embedding representation.

2. **Embedding & Vector Storage:**
   - Each chunk is converted into an embedding using `HuggingFaceEmbeddings`.
   - FAISS stores these embeddings efficiently, allowing similarity-based retrieval.

3. **Retrieval Mechanism:**
   - User queries are embedded and compared against stored document embeddings.
   - FAISS retrieves the most relevant document sections.

4. **LLM Response Generation:**
   - Retrieved text is fed into Groq AI.
   - Groq AI generates a detailed, context-aware response.

## Dependencies
- langchain
- langchain-community
- sentence-transformers
- faiss-cpu
- pypdf
- langchain-groq

## Future Enhancements
- **Web Interface:** Convert CLI into a web-based application using Streamlit or Flask.
- **Multi-PDF Support:** Extend support for multiple documents in a single query.
- **Fine-tuned LLM Integration:** Experiment with different LLMs for response accuracy.

## License
This project is open-source and available under the MIT License.

---
