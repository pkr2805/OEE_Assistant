OEE Assistant
  
The OEE Assistant is a Streamlit-based chatbot that provides insights into Overall Equipment Effectiveness (OEE) for packaging devices in biscuit manufacturing. It uses Retrieval-Augmented Generation (RAG) with ChromaDB and the Groq LLaMA 3 70B model to deliver detailed OEE metrics, insights, and recommendations.
Overview
The OEE Assistant helps manufacturing engineers analyze equipment performance by allowing them to filter data by Device ID, Location, and Month-Year. It processes data from an Excel file, stores embeddings in ChromaDB, and generates AI-driven responses with actionable insights.
⬆ Back to Top
Features

🖥️ Interactive Filters: Select Device ID, Location, and Month-Year to query specific OEE data.
📋 Dynamic Query Generation: Auto-generates queries (e.g., "Show me the OEE for device Device2 at Plant2 in Apr-2025").
🤖 AI-Powered Responses: Leverages Groq LLaMA 3 70B for detailed OEE summaries, insights, and recommendations.
✅ Data Validation: Warns if no data exists for selected filters.
📄 Context & Metadata: Displays the context and metadata used for responses, with mismatch warnings.

⬆ Back to Top
Installation

🔧 Setup Instructions

Prerequisites

Python 3.8 or higher
Streamlit
Pandas
LangChain
ChromaDB
Groq API Key
HuggingFace Embeddings

Steps

Clone the Repository:
git clone <repository-url>
cd oee-assistant


Install Dependencies:
pip install -r requirements.txt


Set Up Groq API Key:

Create a .env file in the project root.
Add your Groq API Key:GROQ_API_KEY=<your-api-key>




Prepare the Data:

Place synthetic_oee_data_complete.xlsx in the project directory.
Run the app to generate the ChromaDB vector store.


Run the Application:
streamlit run app.py





⬆ Back to Top
Usage

📖 How to Use


Launch the App:

Navigate to http://localhost:8501 in your browser.


Select Filters:

Use the sidebar to choose a Device ID, Location, and Month-Year.


Submit a Query:

The app generates a query based on your filters.
Click "Ask the Assistant" to get a response.


View Results:

See the AI-generated response with OEE metrics, insights, and recommendations.
Expand sections to view context and metadata.





⬆ Back to Top
Screenshots
Initial UI State
This snapshot shows the OEE Assistant UI before submitting a query, with filters set for Device2, Plant2, and Apr-2025.

Query Results
This snapshot shows the UI after submitting the query, displaying the AI-generated response with OEE metrics, insights, and recommendations for Device2 at Plant2 in Apr-2025.

⬆ Back to Top
Project Structure

📂 File Structure


app.py: Main Streamlit application script.
Rag_Emebddings/embeddings.py: Functions for loading data, creating documents, and setting up ChromaDB.
Rag_Emebddings/queryvdb.py: Functions for extracting metadata filters and searching similar documents.
synthetic_oee_data_complete.xlsx: Sample dataset for OEE calculations.
screenshots/: Directory containing UI snapshots.



⬆ Back to Top
Notes

Typo Fix: The directory Rag_Emebddings should be renamed to Rag_Embeddings for clarity. Update import paths in app.py and queryvdb.py accordingly.
Data: Ensure synthetic_oee_data_complete.xlsx contains valid data for your filters.
Performance: Query processing may take a few seconds due to embedding generation and LLM inference.

⬆ Back to Top
Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.
⬆ Back to Top
License
This project is licensed under the MIT License.
⬆ Back to Top
