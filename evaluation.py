import argparse
import os
from eval import eval_fun
import pandas as pd

my_parser = argparse.ArgumentParser()

# Add the arguments

my_parser.add_argument('--parent_dir',
                       type=str,
                       help='the path to submissions')
my_parser.add_argument('--scores_dir',
                       type=str,
                       help='the path to scores')
my_parser.add_argument("--submissions_limit",
                        type = int,
                        help = "Allowable no of submissions per day")
            
'''
This iterates through each and every folder, thereby evaluating each submission and updates the leaderboard 
accordingly.

'''


# Execute the parse_args() method
args = my_parser.parse_args()

parent_dir = args.parent_dir
lb_cv = pd.read_csv(args.scores_dir+"/leaderboard_cv.csv")
lb_nlp = pd.read_csv(args.scores_dir+"/leaderboard_nlp.csv")

for folder in os.listdir(parent_dir):
    txt_path = parent_dir+'/'+folder+'/details.txt'
    txt_file = open(txt_path).readlines()
    competition = txt_file[-1].split(":")[-1][1:-1]
    if(competition=="cv"):
        score, limit = eval_fun(parent_dir+'/'+folder, args.submissions_limit, "cv")      #eval cv will evaluate all submissions and delete them after evaluating, 
                                # it returns maximum of all scores
        k = lb_cv[lb_cv.Name==folder.split("_")[-1]].Score.values
        lb_cv.loc[lb_cv.Name==folder.split("_")[-1],'No of Submissions']+=limit
        if(len(k)!=0 or k[0]==' '):
            if(k[0]==' '):
                lb_cv.loc[lb_cv.Name==folder.split("_")[-1],'Score'] = score
            elif(k[0]<score):
                lb_cv.loc[lb_cv.Name==folder.split("_")[-1],'Score'] = score
            else:
                pass

    if(competition=="nlp"):
        score, limit = eval_fun(parent_dir+'/'+folder, args.submissions_limit, "nlp")      #eval nlp will evaluate all submissions and delete them after evaluating, 
                                # it returns maximum of all scors
        k = lb_nlp[lb_nlp.Name==folder.split("_")[-1]].Score.values
        lb_nlp.loc[lb_nlp.Name==folder.split("_")[-1],'No of Submissions']+=limit
        if(len(k)!=0 or k[0]==' '):
            if(k[0]==' '):
                lb_nlp.loc[lb_nlp.Name==folder.split("_")[-1],"Score"] = score
            elif(k[0]<score):
                lb_nlp.loc[lb_nlp.Name==folder.split("_")[-1],"Score"] = score
            else:
                pass
            
lb_cv.to_csv(args.scores_dir+'/leaderboard_cv.csv', index=False)
lb_nlp.to_csv(args.scores_dir+'/leaderboard_nlp.csv', index=False)