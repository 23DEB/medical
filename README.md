# 🏥 Medical Diagnosis System

A GenAI-powered medical diagnosis system that helps patients get AI-based diagnosis from their medical reports and allows doctors to access patient diagnosis history.

## 🚀 Features

- **Patient Portal**: Upload medical reports (PDF) and get AI-powered diagnosis
- **Doctor Dashboard**: View patient diagnosis history and records
- **Secure Authentication**: Role-based access control (Patient/Doctor)
- **AI-Powered Analysis**: Uses LangChain + Groq LLM for intelligent diagnosis
- **Vector Search**: Pinecone integration for semantic search through medical reports
- **Modern UI**: Clean Streamlit interface for easy interaction

## 🛠️ Tech Stack

### Backend (FastAPI)
- **FastAPI**: Modern Python web framework
- **MongoDB**: Document database for user data and diagnosis records
- **Pinecone**: Vector database for semantic search
- **LangChain**: LLM orchestration framework
- **Groq**: Fast LLM inference (Llama 3.1)
- **HuggingFace**: Sentence transformers for embeddings

### Frontend (Streamlit)
- **Streamlit**: Interactive web application framework
- **Requests**: HTTP client for API communication

## 📋 Prerequisites

- Python 3.8+
- MongoDB Atlas account
- Pinecone account
- Groq API key
- HuggingFace API key

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/23DEB/medical.git
   cd medical
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r client/requirements.txt
   ```

4. **Environment Setup**
   Create a `.env` file in the root directory:
   ```env
   MONGO_URI=your_mongodb_connection_string
   DB_NAME=medicalDiagnosis
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_INDEX_NAME=medicaldiagnosis-384
   PINECONE_ENV=us-east-1
   GROQ_API_KEY=your_groq_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   UPLOAD_DIR=./uploaded_dir
   ```

## 🚀 Running the Application

### Start Backend Server
```bash
uvicorn server.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`

### Start Frontend Application
```bash
cd client
streamlit run app.py
```
The web app will be available at `http://localhost:8501`

## 📖 API Documentation

Once the backend is running, visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### Key Endpoints

- `POST /auth/signup` - User registration
- `GET /auth/login` - User authentication
- `POST /reports/upload` - Upload medical reports (Patients only)
- `POST /diagnosis/from_report` - Get AI diagnosis (Patients only)
- `GET /diagnosis/by_patient_name` - View patient records (Doctors only)

## 👥 User Roles

### Patient
- Upload medical reports (PDF format)
- Get AI-powered diagnosis from uploaded reports
- View their own diagnosis history

### Doctor
- Access patient diagnosis records
- View detailed diagnosis history by patient name
- Monitor patient health insights

## 🔒 Security Features

- HTTP Basic Authentication
- Role-based access control
- Secure file upload handling
- Environment variable configuration
- CORS middleware for cross-origin requests

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   👤 Patient    │    │   👨‍⚕️ Doctor     │    │   🖥️ Streamlit   │
│                 │────│                 │────│   Frontend      │
│   Dashboard     │    │   Dashboard     │    │   Port: 8501    │
└─────────────────┘    └─────────────────┘    └─────────┬───────┘
                                                        │
                                                        │ HTTP Requests
                                                        ▼
                                              ┌─────────────────┐
                                              │   🚀 FastAPI    │
                                              │   Backend       │
                                              │   Port: 8000    │
                                              └─────────┬───────┘
                                                        │
                        ┌───────────────────────────────┼───────────────────────────────┐
                        │                               │                               │
                        ▼                               ▼                               ▼
              ┌─────────────────┐             ┌─────────────────┐             ┌─────────────────┐
              │  📄 PDF Upload  │             │  🩺 Diagnosis   │             │  🔐 Auth System │
              │                 │             │                 │             │                 │
              │ • File Storage  │             │ • Query Process │             │ • Login/Signup  │
              │ • Text Extract  │             │ • LLM Response  │             │ • Role Check    │
              └─────────┬───────┘             └─────────┬───────┘             └─────────┬───────┘
                        │                               │                               │
                        ▼                               ▼                               ▼
              ┌─────────────────┐             ┌─────────────────┐             ┌─────────────────┐
              │ ⚙️ Text Process │             │ 🔍 Vector Search │             │ 💾 MongoDB      │
              │                 │             │                 │             │                 │
              │ • Chunk Text    │◄────────────│ • Semantic Query│             │ • Users         │
              │ • Generate      │             │ • Context Fetch │             │ • Reports       │
              │   Embeddings    │             │                 │             │ • Diagnosis     │
              └─────────┬───────┘             └─────────┬───────┘             └─────────────────┘
                        │                               │
                        ▼                               ▼
              ┌─────────────────┐             ┌─────────────────┐
              │ 🗂️ Pinecone DB  │             │ 🤖 Groq LLM     │
              │                 │             │                 │
              │ • Store Vectors │             │ • Llama 3.1     │
              │ • 384 Dimension │             │ • Generate      │
              │ • Metadata      │             │   Diagnosis     │
              └─────────────────┘             └─────────────────┘
                        ▲                               ▲
                        │                               │
                        └───────────┬───────────────────┘
                                    │
                                    ▼
                          ┌─────────────────┐
                          │ 🤗 HuggingFace  │
                          │                 │
                          │ • Embeddings    │
                          │ • Transformers  │
                          │ • MiniLM-L6-v2  │
                          └─────────────────┘
```

### Data Flow:
1. **User Authentication** → Login/Signup via FastAPI
2. **File Upload** → PDF processing and text extraction
3. **Text Processing** → Chunking and embedding generation
4. **Vector Storage** → Store embeddings in Pinecone
5. **Diagnosis Request** → Query processing and context retrieval
6. **AI Response** → LLM generates medical diagnosis
7. **Result Display** → Show diagnosis in Streamlit UI

### Key Components:
- **Frontend**: Streamlit (Port 8501)
- **Backend**: FastAPI (Port 8000)
- **Database**: MongoDB Atlas
- **Vector DB**: Pinecone (384-dim)
- **AI Models**: Groq Llama 3.1 + HuggingFace Embeddings
- **Authentication**: HTTP Basic Auth with role-based access

## 🚀 Deployment

### Backend (Render)
The repository includes `render.yaml` for easy deployment to Render.

### Frontend (Streamlit Cloud)
Deploy the `client/` folder to Streamlit Cloud with environment variable:
```
API_URL=https://your-render-backend-url.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Streamlit](https://streamlit.io/) for the intuitive frontend framework
- [LangChain](https://langchain.com/) for LLM orchestration
- [Groq](https://groq.com/) for fast LLM inference
- [Pinecone](https://pinecone.io/) for vector database services

## 📞 Support

For support, email your-email@example.com or create an issue in this repository.

---

**⚠️ Disclaimer**: This application is for educational purposes only. Always consult with qualified healthcare professionals for medical advice and diagnosis.