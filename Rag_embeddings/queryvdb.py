import re
from langchain.vectorstores import Chroma
from Rag_embeddings.embeddings import setup_vector_store

# 1️⃣ Load your pre‐built vectorstore
vectorstore, _ = setup_vector_store()

# 2️⃣ Extract flat filters from user query
def extract_metadata_filters(query: str) -> dict:
    filters = {}

    # e.g. “device Device2”
    m = re.search(r'device\s+(Device\d+)', query, re.IGNORECASE)
    if m:
        filters['DeviceID'] = m.group(1)

    # e.g. “at Plant2”
    m = re.search(r'at\s+(Plant\d+)', query, re.IGNORECASE)
    if m:
        filters['Location'] = m.group(1)

    # e.g. “in Apr-2024”
    m = re.search(r'in\s+([A-Za-z]{3}-\d{4})', query, re.IGNORECASE)
    if m:
        filters['Month'] = m.group(1)

    return filters



def search_similar_documents(query, filters=None, top_k=1):
    where_clause = {}

    # 👉 Convert filters into Chroma's expected format
    if filters:
        and_conditions = []
        for key, value in filters.items():
            and_conditions.append({key: {"$eq": value}})
        if len(and_conditions) == 1:
            where_clause = and_conditions[0]
        else:
            where_clause = {"$and": and_conditions}

    results = vectorstore.similarity_search(
        query,
        k=top_k,
        filter=where_clause
    )

    return results[0] if results else None






# ─── Example ───
if __name__ == "__main__":
    q = "Show me data for device Device2 at Plant2 in Apr-2024"
    doc = search_similar_documents(q)
    if doc:
        print("Found Document:", doc.page_content)
    else:
        print("No document matched.")
