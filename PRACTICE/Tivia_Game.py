#Trivia Game : Asks user questions and checks them

#Needs a set of questions and answers 
#Randomly pick questions 
#Check answers

#Steps to build 

"""
Components 

1) List of Questions 
2) Store Answers
3) Random Pick
4) Ask User 
5) CHeck Answers 
6) Tally Score 
"""
import random
#Questions : stored as dictionary for Q and A 
questions = {
    "Which AWS Service Provides virtual servers ?": "EC2",
    "Which AWS Service Provides virtual storage ?": "S3",
    "Which AWS Service Provides Relational DataBases  ?": "RDS",
    "Which AWS Service manages users and access ?": "IAM",
    "Which AWS Service is serverless ?": "Lambda",
    "Which AWS Service Provides isolated networks ?": "`VPC"
}

#Random picker 

def ask_question():
    questions_list = list(questions.keys()) #Only questions as a list 
    total_questions = 5 #No of questions to be displayed 
    score = 0

    selected = random.sample(questions_list, total_questions) #Selects 5 from sample

    for idx , question in enumerate(selected):
        print(f"{idx + 1}. {question} ")
        user_answer = input("Enter answer:   ").lower().strip() #To convert to lowercase and strip spaces

        #Comapre the answer
        
        right_answer = questions[question]
        if user_answer == right_answer.lower().strip():
            print("Correct! \n")
            score += 1
        else:
            print(f"Wrong! the right answer is {right_answer}. \n")
    print(f"Your Final Score is {score}")        


ask_question()