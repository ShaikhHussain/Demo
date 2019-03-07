
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'index.html')


def count(request):

    data = request.GET['countTextArea']
    word_list = data.split()
    list_len = len(word_list)


    #empty dictionary
    worddictionary= {}

    for word in word_list:
        if word in worddictionary:
            #word is already present then increase the value by 1
            worddictionary[word] += 1
        else:
            #word is not present then add the value 1
            worddictionary[word] = 1

    #convert dictionary into list by items()

    #sort list by sorted()
    sortedlist = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'words':data,'count':list_len, 'sortedlist':sortedlist})


def about(request):
    return render(request,'about.html')
