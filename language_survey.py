'''
* @Author: csy 
* @Date: 2019-05-05 15:07:30 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-05 15:07:30 
'''
from survey import AnonymousSurvey

question="What language did you first learn to speak?"
my_survey=AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' to quit.\n")
while True:
    response=input("Language: ")
    if response=='q':
        break
    my_survey.store_response(response)
print("\nThanks for your survey!") 
my_survey.show_results()   