from django.shortcuts import render
from django.conf import settings
import os
import pickle
from scipy import integrate
import numpy as np
# Create your views here.

def diabetesprediction(request):
    d = True
    ans = None
    if request.method == 'POST':
        a = []
        print(type(a))
        print(request.POST)
        print(len(request.POST))
        for key,value in request.POST.items():
            print(type(value))
            a.append(value)
        del a[0]
        del a[-1]
        print(a)
        scale = pickle.load(open('pca.pkl','rb'))
        knn = pickle.load(open('knnmodel.pkl','rb'))
        a = np.array(a)
        for i in range(len(a)):
            if i==5 or i==6:
                a[i] = float(a[i])
            else:
                a[i] = int(a[i])
        print(a)
        print(type(a[0]))
        a = scale.transform(a.reshape(1,-1))
        b = knn.predict(a)
        print(a)
        f={1:'YES', 0:'NO'}
        val =int(b)
        ans = f[val]
        d = False
    return render(request,'diabetesprediction.html',{'d':d,'ans':ans})