
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
![Filter and Query Input](./8553fa60-e594-4f34-a0c3-0fe856c8a502.png)

---

### 📈 OEE Summary Generation
Displays metrics like OEE %, Availability, Performance, and Quality:
![OEE Metrics Display](./cab03e96-edc0-40d4-b711-29a97117fc56.png)

---

### 🔎 Insights, Recommendations & Reasoning
Provides root-cause insights and suggestions to improve efficiency:
![Insights & Recommendations](./a05707c5-7e7a-491f-bc34-0893fe8f10b6.png)

---

## ⚙️ How It Works

1. **Upload sensor data** in `.xlsx` format.
2. Select your desired filters from the sidebar.
3. Ask a natural language question (e.g., _"Show OEE for Device2 at Plant2 in Apr-2025"_).
4. The assistant processes the query and shows metrics, insights, and improvement suggestions.

---

## 🚀 Future Enhancements

- Support for real-time sensor integration via APIs.
- Alerts on underperforming equipment.
- Comparative analysis between devices and months.
- Export insights to PDF/CSV.

---

## 🤝 Contributing

Feel free to fork this project and contribute with new features, bug fixes, or performance improvements. PRs are welcome!

---

## 📬 Contact

For any queries, suggestions, or support, feel free to reach out.
