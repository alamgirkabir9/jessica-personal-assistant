# Jessica Personal Assistant 🤖

A web-based personal assistant built with Flask that provides conversational AI capabilities through both voice commands (local) and text input (cloud deployment).

![Jessica Assistant](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

- **Conversational AI**: Engage in natural conversations with Jessica
- **Wikipedia Integration**: Search and get summaries from Wikipedia
- **Time & Date**: Get current time and date information
- **Entertainment**: Jokes, stories, and personal conversations
- **Web Integration**: Links to popular websites (YouTube, Google, Stack Overflow)
- **Music Recommendations**: Curated playlists for different moods
- **Note Taking**: Basic note management functionality
- **Responsive Design**: Beautiful glassmorphism UI that works on all devices

## 🚀 Live Demo

[Deploy your own Jessica Assistant on Render](https://render.com)

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## 🛠️ Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/jessica-personal-assistant.git
   cd jessica-personal-assistant
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

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

### Cloud Deployment (Render)

1. **Fork this repository** or create your own based on this code

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure deployment**
   - Render will automatically detect the `render.yaml` configuration
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn --bind 0.0.0.0:$PORT app:app`

4. **Deploy**
   - Click "Create Web Service"
   - Your app will be live at `https://your-app-name.onrender.com`

## 💬 Available Commands

### General Conversation
- "How are you?" / "How r u?"
- "Who are you?" / "Who created you?"
- "Tell me a joke"
- "Tell me a story"
- "Good morning/evening"

### Information & Search
- "Wikipedia [topic]" - Search Wikipedia
- "What time is it?" / "time"
- "What's the date?" / "date"
- "Search [query]" - Google search (simulation in cloud)

### Entertainment
- "Open YouTube" - Opens YouTube (local) / Shows message (cloud)
- "Play romantic song" - Opens music playlist
- "Play sad song" - Opens sad music
- "Play bangla romantic/sad song" - Bengali music

### Web Navigation
- "Open Google"
- "Open Stack Overflow"
- "Weather" - Weather information
- "News" - Latest news

### Personal Interactions
- "I love you" / "I love u"
- "Miss you" / "Mis u"
- "You are beautiful"
- "Kiss me"
- "Do you love me?"
- "Sing for me"

### Utilities
- "Notes" - Note taking
- "Read note" - Read saved notes
- "Delete notes" - Delete all notes

## 🏗️ Project Structure

```
jessica-personal-assistant/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment config
├── runtime.txt           # Python version specification
├── templates/
│   └── index.html        # Frontend template with glassmorphism UI
├── notes.txt             # User notes (created when needed)
└── README.md            # Project documentation
```

## 🔧 Configuration

### Environment Variables
- `PORT`: Server port (automatically set by Render)
- `PYTHON_VERSION`: Python version (set in render.yaml)

### Local vs Cloud Differences

| Feature | Local | Cloud (Render) |
|---------|-------|----------------|
| Voice Recognition | ✅ Works with microphone | ❌ Not available |
| Text-to-Speech | ✅ Audio output | ❌ Not available |
| Browser Control | ✅ Opens browsers/apps | ❌ Shows simulation messages |
| Text Input | ✅ Available | ✅ Primary interaction method |
| Wikipedia Search | ✅ Works | ✅ Works |
| Time/Date | ✅ Works | ✅ Works |
| Personal Responses | ✅ Works | ✅ Works |

## 🎨 UI Features

- **Glassmorphism Design**: Modern, translucent interface
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects and smooth animations
- **Real-time Status**: Live updates of assistant status
- **Text Input Interface**: Cloud-friendly command input
- **Loading Indicators**: Visual feedback during processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Alamgir Kabir**
- Created Jessica Personal Assistant
- Passionate about AI and web development

## 🙏 Acknowledgments

- Flask framework for the web application
- SpeechRecognition library for voice processing (local)
- Wikipedia API for knowledge integration
- Render platform for cloud deployment
- All contributors and users of Jessica Assistant

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/YOUR_USERNAME/jessica-personal-assistant/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

## 🔮 Future Enhancements

- [ ] Integration with more APIs (weather, news)
- [ ] Advanced NLP capabilities
- [ ] User authentication and personalization
- [ ] Database integration for persistent data
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Voice synthesis for cloud deployment
- [ ] AI-powered conversation improvements

---

⭐ If you found this project helpful, please give it a star on GitHub!

**Made with ❤️ by Alamgir Kabir**
