import chromadb
from chromadb.utils import embedding_functions
import uuid
from llm.chunck_md import split_by_h2

COLLECTION_NAME = "vDB"
EMBEDDING_MODEL = "intfloat/multilingual-e5-large-instruct"



ef = (embedding_functions.SentenceTransformerEmbeddingFunction
      (EMBEDDING_MODEL))


client = chromadb.PersistentClient(path="./vDB")

client.delete_collection(COLLECTION_NAME)

collection = client.get_or_create_collection(COLLECTION_NAME, embedding_function=ef)

with open("../data/cv.txt", "r") as f:
   raw_data = f.read()

data = split_by_h2(raw_data)


passages = [f"passage: {chunk}" for chunk in data]

collection.add(
    ids=[str(uuid.uuid4()) for _ in range(len(passages))],
    documents=passages
)


print(collection.count())
results = collection.query(
    query_texts=["Ausbildung und Stipendium"],
    n_results=1
)

for i, docs in enumerate(results["documents"]):
    print(f"Query {i}:")
    for d in docs:
        print(d)       # gibt den Text mit echten \n aus
        print("-" * 40)

def create_vDB(collection_name : str = "vDB", embedding_modell : str = "intfloat/multilingual-e5-large-instruct") -> None:
    ef = (embedding_functions.SentenceTransformerEmbeddingFunction
          (embedding_modell))
    create_client = chromadb.PersistentClient(path=f"./{collection_name}")
    create_client.get_or_create_collection(collection_name, embedding_function=ef)
    del create_client


def reload_vDB(collection_name : str = "vDB") -> None:

    delete_client = chromadb.PersistentClient(path=f"./{collection_name}")
    delete_client.delete_collection(collection_name)
    del delete_client
    return None