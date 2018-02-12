from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def shorten(request):
    html = """<html><body><form action="" method="POST">
    <label>
        Enter sentence to shorten:
        <input type="text" name="sentence_to_short">
    </label>
    <button type="submit">Send</button>
</form></body></html>"""

    if request.method == "GET":
        return HttpResponse(html)
    else:
        fullstring = request.POST.get("sentence_to_short")
        shrtd = ''
        for word in fullstring.split():
            shrtd += word[0].upper()
        return HttpResponse("shorten: {}".format(shrtd))


@csrf_exempt
def panic(request):
    html = """<html><body><form action="" method="POST">
    <label>
        Enter words to iterate:
        <input type="text" name="word_to_iterate">
    </label>
    <button type="submit">Send</button>
</form></body></html>"""

    if request.method == "GET":
        return HttpResponse(html)
    else:
        sentence = request.POST.get("word_to_iterate")
        word = sentence.replace(" ", "")
        words_list = []
        a = 0
        b = len(word)
        for i in word:
            words_list.append(word[a:b] + word[0:a])
            a += 1
            b += 1
        final_words = '<br>'.join(words_list)
        return HttpResponse(final_words.upper())
