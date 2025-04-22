import pandas as pd
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import streamlit as st


def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def load_data():
    df = pd.read_excel("synthetic_oee_data_complete.xlsx")
    
    # Calculating OEE
    df['Availability'] = df['OperatingTime'] / df['PlannedTime']
    df['Performance'] = df['ActualOutput'] / df['IdealOutput']
    df['Quality'] = df['GoodOutput'] / df['ActualOutput']
    df['OEE'] = df['Availability'] * df['Performance'] * df['Quality'] * 100  # In percentage
    
    # Handling any NaN or infinite values
    df = df.replace([np.inf, -np.inf], np.nan).dropna()
    
    return df

# Creating documents for RAG (row-based chunking)
def create_documents(df):
    documents = []
    for _, row in df.iterrows():
        content = (
            f"Device ID: {row['DeviceID']}, Location: {row['Location']}, "
            f"Month: {row['Month']}, OEE: {row['OEE']:.2f}%, "
            f"Availability: {row['Availability']:.2f}, Performance: {row['Performance']:.2f}, "
            f"Quality: {row['Quality']:.2f}, Operating Time: {row['OperatingTime']} min, "
            f"Actual Output: {row['ActualOutput']}, Good Output: {row['GoodOutput']}"
        )
        documents.append(Document(page_content=content, metadata={
            'DeviceID': row['DeviceID'],
            'Location': row['Location'],
            'Month': row['Month']
        }))
    return documents

# Setting up the Chroma vector store
def setup_vector_store():
    df = load_data()
    embeddings = get_embeddings()  # Use cached embedding model
    
    documents = create_documents(df)
    
    # Creating Chroma vector store with persistent storage
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    # Ensuring the vector store is persisted
    vector_store.persist()
    
    return vector_store, df