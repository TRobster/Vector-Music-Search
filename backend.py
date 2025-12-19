from data import load_documents
from search import build_store_from_docs


def run_demo():
    DOCUMENTS = load_documents()
    store = build_store_from_docs(DOCUMENTS)
    query = "acoustic folk"
    print(f"Query: {query}\n")
    results = store.search(query, k=3)
    for doc, score in results:
        print(f"- id={doc['id']} score={score:.4f}\n  text={doc['text']}")


if __name__ == "__main__":
    run_demo()
