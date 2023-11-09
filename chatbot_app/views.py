from django.shortcuts import render
from django.http import JsonResponse
import openai
from openai import OpenAI

client = OpenAI()

# Create your views here.

openai_api_key = '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'
raise Exception("The 'openai.api_key' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key=openai_api_key)'")

def ask_openai(message):
  response = client.completions.create(engine = "text-davinci-003",
  prompt = message,
  max_token=150,
  n=1,
  stop=None,
  temperature=0.7)
  print(response)
  # answer = response.choices[0].text.strip()

def chatbot(request):
  if request.method == 'POST':
    message = request.POST.get('mesage')
    response = ask_openai('message')
    return JsonResponse({'message': message, 'response': response})
  return render(request, 'chatbot.html')
