from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for i in wordlist:
        if i in worddictionary:
            worddictionary[i] += 1
        else:
            worddictionary[i] = 1
    sortedwordd = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordd': sortedwordd})


def about(request):
    return render(request, 'about.html')
