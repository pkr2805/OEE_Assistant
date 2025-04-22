OEE Assistant

The OEE Assistant is a Streamlit-based chatbot designed to provide insights into Overall Equipment Effectiveness (OEE) for packaging devices used in biscuit manufacturing. It leverages Retrieval-Augmented Generation (RAG) to process data from an Excel file, store embeddings in ChromaDB, and generate detailed responses using the Groq LLaMA 3 70B model via LangChain. The application allows users to filter data by Device ID, Location, and Month-Year, and provides detailed OEE metrics, insights, and recommendations.
Features

Interactive Filters: Select Device ID, Location, and Month-Year to query specific OEE data.
Dynamic Query Generation: Automatically generates queries based on selected filters (e.g., "Show me the OEE for device Device2 at Plant2 in Apr-2025").
AI-Powered Responses: Uses Groq LLaMA 3 70B to provide detailed OEE summaries, insights, recommendations, and reasoning.
Data Validation: Checks for data availability and provides warnings if filters yield no results.
Context and Metadata: Displays the context used for responses and associated metadata, with warnings for mismatched filters.

Installation
Prerequisites

Python 3.8+
Streamlit
Pandas
LangChain
ChromaDB
Groq API Key
HuggingFace Embeddings

Setup

Clone the repository:
git clone <repository-url>
cd oee-assistant


Install dependencies:
pip install -r requirements.txt


Set up your Groq API Key:

Create a .env file in the project root.
Add your Groq API Key:GROQ_API_KEY=<your-api-key>




Prepare the data:

Ensure synthetic_oee_data_complete.xlsx is in the project directory.
Run the app to generate the ChromaDB vector store.


Run the application:
streamlit run app.py



Usage

Launch the App:

Open your browser and navigate to http://localhost:8501.


Select Filters:

Use the sidebar to choose a Device ID, Location, and Month-Year.


Submit a Query:

The app generates a query based on your filters (e.g., "Show me the OEE for device Device2 at Plant2 in Apr-2025").
Click "Ask the Assistant" to get a response.


View Results:

The app displays the AI-generated response, including OEE metrics, insights, and recommendations.
Expand sections to view the context and metadata used.



Screenshots
Initial UI State
This snapshot shows the OEE Assistant UI before a query is submitted, with filters set for Device2, Plant2, and Apr-2025.

Query Results
This snapshot shows the UI after submitting a query, displaying the AI-generated response with OEE metrics, insights, recommendations, and context for Device2 at Plant2 in Apr-2025.

Project Structure

app.py: Main Streamlit application script.
Rag_Emebddings/embeddings.py: Functions for loading data, creating documents, and setting up ChromaDB.
Rag_Emebddings/queryvdb.py: Functions for extracting metadata filters and searching similar documents.
synthetic_oee_data_complete.xlsx: Sample dataset for OEE calculations.
screenshots/: Directory containing UI snapshots.

Notes

Data: Ensure synthetic_oee_data_complete.xlsx contains valid data for the selected filters to avoid warnings.
Performance: The app may take a few seconds to process queries due to embedding generation and LLM inference.
Error Handling: Check the logs if errors occur, especially related to API keys or missing data.

Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.
License
This project is licensed under the MIT License.
