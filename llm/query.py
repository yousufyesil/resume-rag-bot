import chromadb

def ask_vdb(query :str, debug : bool = False) -> list[str]:
    # Client initialise
    client = chromadb.PersistentClient(path="./vDB")

    # vDB Verknüpfung
    collection = client.get_collection("vDB")

    #results ist ein Dictionary
    results = collection.query(
        query_texts=[f"query: {query}"],
        n_results=3)
    if debug:
        print(results["documents"])
        print(f"\n")
    return results["documents"][0]



