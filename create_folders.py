'''
creates folders and blank leaderboard for both the competitions
This is to be run once at the beginning of competition

'''

import argparse
import pandas as pd
import os
from pathlib import Path
# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments

my_parser.add_argument('--path',
                       type=str,
                       help='the path to participants csv file')


my_parser.add_argument('--parent_dir',
                       type=str,
                       help='the path to submissions')

my_parser.add_argument("--lb",
                        type=str,
                        help = "the path to leaderboard")
# Execute the parse_args() method
args = my_parser.parse_args()

participants_csv = args.path
parent_dir = args.parent_dir

participants_csv = pd.read_csv(participants_csv)

def write_details(name, rollno, year, competition, root_dir):
    with open(root_dir+"/details.txt", 'w') as f:
        f.write("Name :  {}\n".format(name))
        f.write("RollNo : {}\n".format(rollno))
        f.write("year : {}\n".format(year))
        f.write("competition : {}\n".format(competition))

lb_cv = []
lb_nlp = []

for i in range(0, len(participants_csv)):
    name = participants_csv.iloc[i]["Name"]
    rollno = participants_csv.iloc[i]["RollNo"]
    year = participants_csv.iloc[i]["Year"]
    competition = participants_csv.iloc[i]["competition"]
    if competition=="cv":
        lb_cv.append({
            "Name" : rollno,
            "Score" : " ",
            "No of Submissions" : 0
        })
    if competition=="nlp":
        lb_nlp.append({
            "Name": rollno,
            "Score": " ",
            "No of Submissions" : 0
        })
    if not os.path.exists(parent_dir+"/"+name+"_"+rollno):
        os.mkdir(parent_dir + "/" + name+"_"+rollno)
    write_details(name, rollno, year, competition, parent_dir+"/"+name+"_"+rollno)

if lb_cv == []:
    lb_cv.append({
        "Name" : " ",
        "Score": " ",
        "No of Submissions": " "
    })
if lb_nlp == []:
    lb_nlp.append({
        "Name" : " ",
        "Score": " ",
        "No of Submissions": " "
    })
df_cv = pd.DataFrame.from_dict(lb_cv)
df_nlp = pd.DataFrame.from_dict(lb_nlp)
df_nlp.to_csv(args.lb+"/leaderboard_nlp.csv", index=False)
df_cv.to_csv(args.lb+"/leaderboard_cv.csv", index=False)