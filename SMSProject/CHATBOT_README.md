# AI ChatBot Integration Guide

## Overview
This project includes an AI-powered ChatBot built with Gemini API, Django, and modern web technologies. The ChatBot is integrated into every page and appears as a stylish widget in the bottom-left corner.

## Setup Instructions

### 1. Environment Configuration
The `.env` file has been created at the project root. Configure your Gemini API key:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

**To get a Gemini API key:**
1. Visit: https://ai.google.dev/
2. Click "Get API Key"
3. Create a new project or select existing one
4. Copy your API key
5. Paste it in the `.env` file

### 2. Install Dependencies
Required packages have been installed:
- `google-generativeai` - For Gemini API integration
- `python-dotenv` - For environment variable management
- `mysqlclient` - For MySQL database support

### 3. Database Migration
Run migrations to create ChatMessage table:
```bash
python manage.py migrate chatbot
```

### 4. Features

#### ChatBot Widget
- **Location**: Bottom-left corner of every page
- **Appearance**: Stylish gradient header with robot avatar
- **Responsive**: Works on all device sizes
- **Interactive**: Smooth animations and transitions

#### Functionality
- Send and receive messages from Gemini AI
- View chat history
- Minimize/maximize chat window
- Message formatting (URLs, bold, italic text)
- Loading indicators and typing animations
- Error handling and user feedback

#### Database
- Stores all chat messages for future reference
- Accessible through Django admin
- Can retrieve chat history via API

### 5. URL Endpoints

**Frontend:**
- `/chatbot/` - ChatBot page (standalone view)

**Backend APIs:**
- `POST /chatbot/api/response/` - Send message and get AI response
- `GET /chatbot/api/history/` - Get chat history (optional limit parameter)

### 6. Customization

#### CSS Colors
Edit `static/css/chatbot.css` to customize:
- Primary color: `--primary-color: #009879`
- Avatar/header styling
- Message bubble colors
- Animations

#### JavaScript Behavior
Edit `static/js/chatbot.js` to modify:
- Welcome message
- Message formatting
- API endpoints
- Error handling

#### Avatar Icon
Change in `templates/main.html`:
```html
<i class="fas fa-robot"></i>  <!-- Change to any Font Awesome icon -->
```

### 7. Admin Interface
Access ChatBot messages in Django Admin:
1. Navigate to `/admin/`
2. Go to Chatbot section
3. View all chat messages
4. Search and filter messages

### 8. API Response Format

**Send Message Request:**
```json
{
    "message": "User's question here"
}
```

**Response:**
```json
{
    "success": true,
    "response": "Bot's answer here",
    "timestamp": "2026-03-29 10:30:45"
}
```

**Error Response:**
```json
{
    "success": false,
    "error": "Error description"
}
```

### 9. File Structure
```
chatbot/
├── migrations/
│   ├── 0001_initial.py
│   └── __init__.py
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── urls.py
└── views.py

static/
├── css/
│   └── chatbot.css
└── js/
    └── chatbot.js

templates/
├── chatbot/
│   └── chat.html
└── main.html (updated with chatbot widget)
```

### 10. Features Walkthrough

**Message Sending:**
1. User types message in input field
2. Press Enter or click Send button
3. Message appears in chat immediately
4. Loading indicator shows while waiting
5. Bot response appears with animations

**Responsive Design:**
- Desktop: 380px width widget
- Tablet: Adjusted sizing
- Mobile: Full-width responsive (90% of viewport)
- Minimum height: Adjusts content on small screens

**Animations:**
- Slide-in effect on widget load
- Bounce effect on toggle button
- Pulse effect on avatar
- Typing indicator dots animation
- Message fade-in effect
- Hover effects on buttons

### 11. Troubleshooting

**ChatBot not appearing?**
- Check if JavaScript is enabled
- Verify CSS file is loaded
- Check browser console for errors
- Ensure .env file has valid API key

**API errors?**
- Verify GEMINI_API_KEY in .env is correct
- Check internet connection
- Review browser console for CORS issues
- Ensure CSRF token is properly handled

**Database errors?**
- Run migrations: `python manage.py migrate`
- Check MySQL connection settings in settings.py
- Verify database exists and is accessible

### 12. Performance Optimization

- Messages are stored efficiently in database
- CSS optimized with proper prefixes
- JavaScript uses event delegation
- Lazy loading of chat history
- Responsive scrolling performance

### 13. Security Considerations

- CSRF protection enabled
- Environment variables for sensitive data
- Input sanitization for XSS prevention
- API key not exposed in frontend
- Proper error messages without sensitive info

## Support
For more information about Gemini API: https://ai.google.dev/docs
