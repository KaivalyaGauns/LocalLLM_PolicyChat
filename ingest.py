from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma 
import os 
from constants import CHROMA_SETTINGS
from addspace import add_space


persist_directory = "db"


def main():
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                loader = PDFMinerLoader(os.path.join(root, file))
    documents = loader.load()
    for i in range(len(documents)):
        documents[i].page_content = add_space(documents[i].page_content)
        
    print(documents, end="\n\n")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    for text in texts:
        print(text, end="\n ----------------------------- \n")
    print(len(texts))
    #create embeddings here
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory, client_settings=CHROMA_SETTINGS)
    print(db)
    db.persist()
    db=None

if __name__ == "__main__":
    main()
