# 🤖 Document Chatbot

A beautiful web application that allows users to upload files and get AI-powered analysis using AI model. Built with Flask and featuring a modern, responsive UI with drag-and-drop functionality. Here I have used google gemini ai model, let's see how you can do that too.

![Document Chatbot](https://img.shields.io/badge/AI-Gemini%202.0-blue?style=flat-square&logo=google)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=flat-square&logo=python)

## ✨ Features

- 🎨 **Modern UI** - Beautiful gradient design with glassmorphism effects
- 📁 **Drag & Drop Upload** - Intuitive file upload with drag-and-drop support
- 🤖 **AI Analysis** - Powered by Google's Gemini 2.0 Flash model
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile
- ⚡ **Real-time Feedback** - Loading animations and instant results
- 🔍 **File Support** - Supports images, documents, videos, and more
- 💬 **Custom Prompts** - Add custom instructions for AI analysis

## 🚀 Demo

Upload any file and get instant AI-powered insights:
- Image analysis and description
- Document summarization
- Code review and explanation
- Data analysis from spreadsheets
- Video content analysis
- And much more!

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI API key (Gemini)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shohagcsediu/Document-Chatbot.git
   cd Document-Chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   PORT=5000
   ```

5. **Get your Gemini API key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add it to your `.env` file

## 🏃‍♂️ Running the Application

### Development
```bash
python app.py
```
The app will be available at `http://localhost:5000`

## 📁 Project Structure

```
Document-Chatbot/
├── app.py                 # Main Flask application
├── templates/
│   └── upload.html        # Beautiful UI template
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## 🎯 Usage

1. **Start the application**
2. **Open your browser** and navigate to `http://localhost:5000`
3. **Upload a file** by clicking or dragging and dropping
4. **Add a custom prompt** (optional) to guide the AI analysis
5. **Click "Analyze"** and wait for results
6. **View the AI-generated analysis** in the response section below

## 🔧 API Endpoints

- `GET /` - Serves the main upload interface
- `POST /upload` - Handles file upload and AI analysis
- `GET /health` - Health check endpoint

### Upload Endpoint Response
```json
{
  "filename": "example.pdf",
  "content_type": "application/pdf",
  "gemini_response": "AI analysis of the uploaded file..."
}
```

## 🎨 UI Features

- **Gradient Background** - Modern purple gradient design
- **Glassmorphism Effects** - Semi-transparent containers with backdrop blur
- **Interactive Elements** - Hover effects and smooth transitions
- **Loading States** - Spinner animation during processing
- **Error Handling** - Clear error messages with visual feedback
- **File Information** - Display file details (name, size, type)
- **Mobile Responsive** - Optimized for all screen sizes

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your Google API key secure and rotate it regularly
- Consider implementing file size limits for production use
- Add input validation for enhanced security

## 📦 Dependencies

- **Flask 3.0.0** - Web framework
- **google-generativeai 0.3.2** - Google's Gemini AI SDK
- **python-dotenv 1.0.0** - Environment variable management
- **gunicorn 21.2.0** - WSGI server for production
- **Werkzeug 3.0.1** - Flask's WSGI toolkit

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for the powerful Gemini AI model
- Flask community for the excellent web framework
- Contributors who help improve this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/shohagcsediu/Document-Chatbot/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

⭐ **Star this repository if you found it helpful!**

Made with ❤️ by [Shohag](https://github.com/shohagcsediu)
