from django.shortcuts import render


def user_interface(request):
    return render(request, 'html/word_count_homepage.html', {})


def count_word(request):
    fulltext = request.POST['content']
    wordlist = fulltext.split()
    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    print(fulltext)
    return render(request, 'html/count.html', {'fulltext':fulltext, 'count': len(wordlist)})
