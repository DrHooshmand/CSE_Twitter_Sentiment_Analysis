import numpy as np
from DicGen import *

tweets=np.load('data.npy')
for tweet in tweets:
    tweet[3]=tweet[3].strip()
correctcount=0.0
for i in range(0,100):
    sentcal=sentimentdeg(tweets[i][3])
    sent=float(tweets[i][1])
    print('{},{}'.format(sentcal,sent))
    if (sentcal>1.5 and sent==1) or (sentcal<0.1 and sent==0) or (sentcal>=1 and sentcal<=1.5 and sent==0.5):
        correctcount+=1

print(correctcount/100)
