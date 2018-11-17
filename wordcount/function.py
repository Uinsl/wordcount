from django.http import HttpResponse #用来返回一个值到网页
from django.shortcuts import render #传一个网页给用户

def home(request):
    #return HttpResponse("hlleo!")
    return render(request,'home.html')

def count1(request):
    user_text = (request.GET['text'])
    total_count = len(user_text)
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word] += 1

    sorted_dict=sorted(word_dict.items(),key=lambda w:w[1],reverse=True) #w:w[1] w[0][1] 选择w[1]去排序
    return render(request,'count.html',
                  {'total': total_count,'text': user_text,'word':word_dict,'sorted': sorted_dict})