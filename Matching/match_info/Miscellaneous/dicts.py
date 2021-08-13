import glob
import os
from pathlib import Path as p



def get_dir_path(__file__):

    # get path to the directory
    DIR_PATH = p(os.path.dirname(__file__))
    #print("Got directory path", DIR_PATH)
    return DIR_PATH

def get_csv_path(DIR_PATH):
    
    # get the path to your .csv files
    RESPONSES_PATH, CONSTRAINTS_PATH = p(os.path.join(DIR_PATH,'match_info','SurveyResponses')), p(os.path.join(DIR_PATH,'match_info','SurveyResponses'))
    #print("Got response & constraint paths: ",RESPONSES_PATH,CONSTRAINTS_PATH)
    return RESPONSES_PATH,

######################### DICTIONARY STUFF #################################

if __name__ == "__main__":
	CSV_DATA = {}
	DIR_PATH = p(os.path.dirname(__file__))
	print("FILE: ",DIR_PATH.name)
	matching_surveys = p(os.path.join(DIR_PATH,'match_info','SurveyResponses/'))
	for survey in matching_surveys:
		print(survey.name)
		print(os.path.isdir(os.path.join(matching_surveys,survey)))
		os.path.dirname(DIR_PATH)
	#print("dir path                          ",DIR_PATH,"\nmatching_surveys                  ",matching_surveys,"\nmatching_constraints              ",matching_constraints)

	for survey in os.listdir(matching_surveys):
		print(os.path.join(matching_surveys,survey))
		if os.path.isdir(os.path.join(matching_surveys, survey)):
			print(survey)

	print(os.path.isdir("D:/school/prog_ky/PetrTogether/Matching/match_info/SurveyResponses/F20_data.csv"))
	#D:\school\prog_ky\PetrTogether\Matching\match_info\SurveyResponses\F20_data.csv

	#CSV_DATA["school_quarter"] = 
	matching_quarter = input("Fall or Winter?\n")
else:
	pass