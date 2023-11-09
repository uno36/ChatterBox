from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = message,
    max_token=150,
    n=1,
    stop=None,
    temperature=0.7,
  )
  print(response)
  # answer = response.choices[0].text.strip()

def chatbot(request):
  if request.method == 'POST':
    message = request.POST.get('mesage')
    response = ask_openai('message')
    return JsonResponse({'message': message, 'response': response})
  return render(request, 'chatbot.html')
