import pandas as pd

def jaccard(f, GT="/home/manoj/environments/inductions_21/test.csv"):
    submission_csv = pd.read_csv(f)
    prediction_file = submission_csv["PredictionString"]
    test_df = pd.read_csv(GT)
    target = test_df["answer_text"]
    score = 0
    for pred, tar in zip(prediction_file, target):
        str1 = pred
        str2 = tar
        a = set(str1.lower().split()) 
        b = set(str2.lower().split())
        c = a.intersection(b)
        score += float(len(c)) / (len(a) + len(b) - len(c))
    return float(score)/len(prediction_file)
