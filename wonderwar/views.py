from django.shortcuts import render_to_response

from wonderwar import markov

MC = markov.MarkovChain()
MC.load_file('alice.txt')
MC.load_file('art_of_war.txt', 3)

def _get_text(min_words=30):
    return MC.generate_text(min_words)

def index(request):
    text = _get_text()
    return render_to_response('index.html', {'message': 'hi there', 'text': text})

def new_text(request, min_words=30):
    # from pdb import set_trace; set_trace()
    text = _get_text(min_words)
    return render_to_response('new_text.html', {'text': text})
