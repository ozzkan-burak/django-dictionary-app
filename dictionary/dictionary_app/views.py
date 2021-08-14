from django.shortcuts import render

from .helpers import searchWord

def home(request):

  context={}

  if request.method == 'POST':

    user_word = request.POST.get('user_word')

    result = searchWord(user_word)
    
    try:
      context={
        'search_word':result['word'],
        'results': result['results'],
        'pronunciations':result['pronunciation']
      }
    except KeyError:
      context={
        'error': result['message'],
        'failure': True
      }
  return render(request, 'dictionary_app/index.html', context=context)