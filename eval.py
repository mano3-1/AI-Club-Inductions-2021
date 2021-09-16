import numpy as np
import os
from ssim import ssim
from jaccard import jaccard
    
def eval_fun(folder_dir, limit, tag):
    files = os.listdir(folder_dir)
    files.remove("details.txt")
    if(len(files)==0):
        return 0,0
    if(len(files)>limit):
        files = files[-limit:]
    past_scores = []
    for f in files:
        if(tag=="cv"):
            past_scores.append(ssim(folder_dir+"/"+f))
        if(tag=="nlp"):
            past_scores.append(jaccard(folder_dir+'/'+f))

        os.remove(folder_dir+'/'+f)
    for f in os.listdir(folder_dir):
        if(f=="details.txt"):
            continue
        os.remove(folder_dir+'/'+f)
    return max(past_scores), len(files)


