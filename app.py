import streamlit as st
import pandas as pd
import os

from Rag_embeddings.embeddings import load_data, setup_vector_store
from Rag_embeddings.queryvdb import search_similar_documents
from groq import Groq

st.set_page_config(page_title="📦 OEE Assistant", page_icon="🤖")

# ---- Groq client ----
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm_with_context(context: str, query: str) -> str:
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert assistant specialized in packaging devices used in biscuit manufacturing. "
                    "You understand how to calculate and interpret OEE (Overall Equipment Efficiency) and can answer user "
                    "queries about device performance, efficiency, and related metrics using contextual data. Always respond "
                    "clearly and accurately, and provide numeric OEE values when available.\n"
                    "Your response must include:\n"
                    "- A summary of the key OEE-related values (availability, performance, quality, total OEE)\n"
                    "- Insights: Highlight patterns, anomalies, or potential issues in the data\n"
                    "- Recommendations: Suggest how to improve performance, quality, or availability\n"
                    "- Reasoning: Explain why something may be underperforming or needs attention"
                )
            },
            {
                "role": "user",
                "content": f"{context}\n\nQuestion: {query}" 
            }
        ]
    )
    return response.choices[0].message.content

st.markdown("Ask about equipment performance, availability, or OEE and queries related to it.")

# Load data
df = load_data()

# Function to check if data exists for given filters
def check_data_exists(device=None, location=None, month=None):
    query = df.copy()
    if device:
        query = query[query['DeviceID'] == device]
    if location:
        query = query[query['Location'] == location]
    if month:
        query = query[query['Month'] == month]
    return len(query) > 0

# Filters
device_ids = sorted(df['DeviceID'].unique())
months = sorted(df['Month'].unique())
locations = sorted(df['Location'].unique())

selected_device = st.sidebar.selectbox("Device ID", device_ids)
selected_location = st.sidebar.selectbox("Location", locations)
selected_month = st.sidebar.selectbox("Month-Year", months)

# Build query
user_query = "Show me the OEE"
user_query += f" for device {selected_device}"
user_query += f" at {selected_location}"
user_query += f" in {selected_month}"

st.text_input("Generated Query", value=user_query)

# Submit button
if st.button("🔍 Ask"):
    with st.spinner("Thinking..."):
        filters = {
            'DeviceID': selected_device,
            'Location': selected_location,
            'Month': selected_month
        }

        doc = search_similar_documents(user_query, filters=filters, top_k=1)

        try:
            data_exists = check_data_exists(
                device=selected_device,
                location=selected_location,
                month=selected_month
            )

            if not data_exists:
                st.warning(f"No data found for Device: {selected_device}, Location: {selected_location}, Month: {selected_month}. Please try different filters.")
            elif doc:
                answer = ask_llm_with_context(doc.page_content, user_query)

                st.markdown("### 🤖 AI Answer")
                st.success(answer)

                st.markdown("### 📄 Context Snippet")
                st.code(doc.page_content)

                st.markdown("### 🏷️ Metadata")
                st.write(doc.metadata)

                if doc.metadata.get("DeviceID") != selected_device:
                    st.warning(f"Note: Retrieved data is for {doc.metadata.get('DeviceID')}, not {selected_device}.")
                if doc.metadata.get("Location") != selected_location:
                    st.warning(f"Note: Retrieved data is for {doc.metadata.get('Location')}, not {selected_location}.")
                if doc.metadata.get("Month") != selected_month:
                    st.warning(f"Note: Retrieved data is for {doc.metadata.get('Month')}, not {selected_month}.")
            else:
                st.warning("No relevant information found.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please try different filter combinations or check the application logs for more details.")
