
# 📦 OEE Assistant

**OEE Assistant** is a smart GenAI-powered tool designed to provide insights into **Overall Equipment Effectiveness (OEE)** for packaging devices in a biscuit manufacturing plant. The assistant supports natural language queries to extract key production metrics and give performance-driven recommendations based on IoT sensor data.

---

## 🔍 Features

- ✅ Natural language query processing using LangChain and LLMs.
- 📊 Real-time OEE metric display (Availability, Performance, Quality).
- 📍 Device- and location-specific filtering.
- 📅 Month-Year based analytics.
- 💡 Actionable insights and recommendations.
- 🚀 Deployed with a user-friendly Streamlit interface.

---

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (LangChain, Llama3 via Groq API)
- **Data Processing**: Pandas, Excel (.xlsx) input
- **Vector Search**: Pinecone
- **Deployment**: Localhost / Cloud ready

---

## 🖼️ Snapshots

### 🧾 Natural Language Query & Filters
Filter your search by Device ID, Plant Location, and Month-Year:
!![Filter and Query Input](https://github.com/user-attachments/assets/e9a4f95d-f9f8-4e97-94e9-a0511619edc3)
---

### 📈 OEE Summary Generation
Displays metrics like OEE %, Availability, Performance, and Quality:
!![image](https://github.com/user-attachments/assets/0aa49e04-4f55-4adc-a3f4-61464a766e44)

---

### 🔎 Insights, Recommendations & Reasoning
Provides root-cause insights and suggestions to improve efficiency:
!![image]![image](https://github.com/user-attachments/assets/7c012262-7974-4cdb-9127-05e5cacf6076)



---

### 📊 Phase 1: Data Preparation
- **Upload Excel File**: Load machine performance metrics from a `.xlsx` file.
- **OEE Calculation**: Automatically compute Overall Equipment Effectiveness (OEE) for each row.
- **Text Chunking**: Convert each row into a descriptive natural language text chunk.
- **Embedding Generation**: Use `SentenceTransformer` to convert each chunk into a vector representation.
- **Vector Storage**: Store embeddings in **ChromaDB** along with metadata (DeviceID, Location, Month-Year).

### 💬 Phase 2: User Interaction
- **Streamlit UI**: Users interact via a user-friendly Streamlit app.
- **Filter Selection**: Choose filters like DeviceID, Location, and Month.
- **Ask a Question**: Type a natural language query (e.g., *“Show OEE for Device2 at Plant2 in Apr-2025”*).
- **Query Embedding**: Convert the query into a vector.
- **RAG Process**:
  - Retrieve relevant chunks from **ChromaDB** using **vector similarity** + **metadata filtering**.
  - Send the retrieved context + user query to **Groq LLaMA 3 70B** via **LangChain**.
- **Answer Generation**: Display the final answer in the Streamlit interface with insights and suggestions.


---

## 🚀 Future Enhancements

- Support for real-time sensor integration via APIs..
- Comparative analysis between devices and months.
- Export insights to PDF/CSV.

---

## 🤝 Contributing

Feel free to fork this project and contribute with new features, bug fixes, or performance improvements. PRs are welcome!

---

## 📬 Contact

For any queries, suggestions, or support, feel free to reach out.
