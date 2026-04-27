# 📦 EDI Integration Demo  

A lightweight simulation of an EDI-based system integration workflow, demonstrating how external data formats (EDI) can be parsed, transformed, and integrated into internal applications via APIs.  

# 🚀 Overview  

This project simulates a common real-world integration scenario:  

External System → EDI File → Parser → JSON → Internal API → Processing  

It showcases practical experience in:  

- Data transformation (EDI → JSON)
- API integration
- Backend processing workflows
- System interoperability  


# 🧠 Key Features
- 📄 Parse EDI 850 (Purchase Order) files
- 🔄 Convert raw EDI data into structured JSON
- 🌐 Send parsed data to a RESTful API
- ⚙️ Simulate backend order processing
- 🧪 Debug-friendly logging output  

# 🏗 Project Structure
```
edi-integration-demo/  
├── data/  
│   └── sample.edi          # Sample EDI 850 file  
├── parser/  
│   └── edi_parser.py       # EDI → JSON parser + API client  
├── api/  
│   └── app.py              # Flask API (order processing simulation)  
├── output/  
│   └── parsed.json         # Parsed JSON output  
└── README.md  
```

# ⚙️ Tech Stack
- Python – data parsing & integration logic
- Flask – API simulation
- JSON – structured data format
- REST API – system communication  

# 🔄 Workflow
```
EDI File → Parser → JSON → API → Response
```
1. Load EDI file (sample.edi)
2. Split into segments and normalize data
3. Extract key fields (order number, date, items, etc.)
4. Convert to JSON
5. Send to API endpoint (/process-order)
6. Simulate processing response
# ▶️ How to Run
## 1️⃣ Start the API server
```
cd api  
python app.py  
```

Expected output:  
```
Running on http://127.0.0.1:5000
```
## 2️⃣ Run the parser

Open a new terminal:  
```
cd parser  
python edi_parser.py
```

# 📥 Example Output
## Parsed JSON
```
{
  "order_number": "12345",
  "date": "20210101",
  "store": "Test Store",
  "item": {
    "quantity": "10",
    "price": "15.00",
    "sku": "ITEM001"
  }
}
```

# API Response
```
{
  "status": "processed",
  "order_number": "12345",
  "message": "Order successfully received"
}
```

# 🧩 Key Implementation Details
- Handles EDI segment normalization (\n, \r, whitespace cleanup)
- Safely parses segments with boundary checks
- Simulates real-world API integration using HTTP POST
- Uses structured JSON for downstream processing

# ⚠️ Notes
- /process-order endpoint only accepts POST requests
- Accessing it via browser (GET) will return 405 Method Not Allowed
- Ensure the API server is running before executing the parser
📈 Future Improvements
- Support multiple line items (PO1 segments as array)
- Add logging & error handling
- Validate incoming API payloads
- Support additional EDI transaction types
- Batch processing for multiple EDI files

# 🎯 Why This Project Matters

This project demonstrates:  

- Practical understanding of system integration workflows
- Ability to handle external data formats
- Experience with API-based communication
- Strong debugging and data processing skills  

# 👤 Author

Yu Chen  
Web Developer / Integration-focused Engineer  