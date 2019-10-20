from textblob import TextBlob, Word
from spellchecker import SpellChecker
from django.shortcuts import render, redirect
from .forms import CheckForm
from .models import Check


def text_views(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)

        if form.is_valid():
            form.save()
            # return redirect('result')
    else:
        form = CheckForm()
    return render(request, 'check.html', {'form': form})


def result_views(request):
    qs = Check.objects.latest('time')

    tb = TextBlob(qs.text)
    spell = SpellChecker()
    res = {}
    ck = []
    for word in tb.words:
        word = word.lower()
        w = Word(word)
        # res.update({word})
        # if word != word.correct() and word != spell.correction(word):
        #     res.update({word: spell.candidates(word)})

        val = w.spellcheck()

        if len(val) == 1:
            if word != val[0][0]:
                res[word] = [val[0][0]]
            else:
                if val[0][1] == 0.0:
                    res[word] = ['Irrelevant spelling.']
        else:
            for it in val:
                ck.append(it[0])
            res[word] = ck
            ck = []

    return render(request, 'result.html', {'queryset': res})
