# I Have Created this file -Nabeel

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')


def aboutme(request):
    return HttpResponse (" <a href='https://nb786.github.io/Ncoder/about.html' > Aboutme</a>")

def contact(request):
    return HttpResponse ("<a href='https://nb786.github.io/Ncoder/contact.html' > contact us </a>")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off') #on & off
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(removepunc)

    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
             if char not in punctuations:
                 analyzed=analyzed + char
             dics = {'purpose':'Removed Punctuations' , 'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',dics)



    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        dics = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
       # return render(request, 'analyze.html', dics)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        dics = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
       #return render(request, 'analyze.html', dics)



    if (extraspaceremover == "on"):
        analyzed = ""
        for  index, char in enumerate(djtext):
             if not (djtext[index] == "" and djtext[index+1] == ""):
                analyzed = analyzed + char

        dics = {'purpose': 'Removed the Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', dics)

    if (charcount == "on"):
     analyzed = ""
     for char in djtext:
      analyzed = len(djtext)
      dics = {'purpose': 'Total no. of Character in your text are', 'analyzed_text': analyzed}
    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount!= "on"):

      return HttpResponse("Please Select Any Function And Try Again!")

    return render(request, 'analyze.html', dics)













