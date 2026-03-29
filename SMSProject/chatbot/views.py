import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from dotenv import load_dotenv
from .models import ChatMessage

load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def chat_home(request):
    """Render the main chat interface"""
    return render(request, 'chatbot/chat.html')

@csrf_exempt
@require_http_methods(["POST"])
def chat_response(request):
    """Handle chat responses from Gemini API"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()

        if not user_message:
            return JsonResponse({
                'success': False,
                'error': 'Message cannot be empty'
            })

        if not GEMINI_API_KEY:
            return JsonResponse({
                'success': False,
                'error': 'API key not configured'
            })

        # Generate response from Gemini
        # Using gemini-2.5-flash (latest model) - fallback to gemini-pro-latest if unavailable
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(user_message)
            bot_response = response.text
        except Exception as model_error:
            # Fallback to gemini-pro-latest if gemini-2.5-flash is not available
            try:
                model = genai.GenerativeModel('gemini-pro-latest')
                response = model.generate_content(user_message)
                bot_response = response.text
            except Exception as fallback_error:
                raise Exception(f"Model error: {str(fallback_error)}")

        # Save to database
        chat = ChatMessage.objects.create(
            user_message=user_message,
            bot_response=bot_response
        )

        return JsonResponse({
            'success': True,
            'response': bot_response,
            'timestamp': chat.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def chat_history(request):
    """Get chat history"""
    try:
        limit = request.GET.get('limit', 10)
        messages = ChatMessage.objects.all()[:int(limit)]
        
        history = [{
            'user_message': msg.user_message,
            'bot_response': msg.bot_response,
            'timestamp': msg.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for msg in reversed(messages)]
        
        return JsonResponse({
            'success': True,
            'history': history
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
