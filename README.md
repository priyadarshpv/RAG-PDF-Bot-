# PDF-based Retrieval-Augmented Generation (RAG) System

This project implements a simple Retrieval-Augmented Generation (RAG) system using LangChain, FAISS, and Groq AI. It processes a PDF document, converts it into embeddings, stores them in a FAISS vector database, and allows users to query the document interactively.

## Features
- Load and process PDF documents.
- Split text into manageable chunks for embedding.
- Use FAISS as a vector store for efficient retrieval.
- Integrate with Groq AI for query-based responses.
- Interactive chatbot-style query execution.

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

1. Replace `alice_in_wonderland.pdf` with your target PDF file.
2. Run the script:
```sh
python main.py
```
3. Enter queries interactively.
4. Type 'Exit' to stop the program.

## Dependencies
- langchain
- langchain-community
- sentence-transformers
- faiss-cpu
- pypdf
- langchain-groq

## File Structure
```
/pdf-rag
│── README.md           # Project Documentation
│── requirements.txt    # List of Dependencies
│── main.py             # Main script for execution
```

## License
This project is open-source and available under the MIT License.

---
