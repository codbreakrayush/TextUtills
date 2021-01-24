'''
Ayush

'''
from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalizefirst = request.POST.get('capitalizefirst', 'off')
    spaceremover = request.POST.get('spaceremoved', 'off')
    analyzed = "Error"
    params = {'purpose': '', 'analyzed_text': analyzed}
    if removepunc == "on":
        punc = list(punctuation)
        analyzed = ""
        for i in djtext:
            if i not in punc:
                analyzed += i
        djtext = analyzed
        params['purpose'] += 'Remove Punctuation------ '

    if capitalizefirst == "on":
        djtext = djtext.capitalize()
        params['purpose'] += 'Capitalise First Word------ '

    if spaceremover == "on":
        l = list(djtext)
        analyzed = ""
        for i in l:
            if i != " ":
                analyzed += i
        djtext = analyzed
        params['purpose'] += 'Space Remover------ '

    params['analyzed_text'] = djtext

    return render(request, 'analyze.html', params)