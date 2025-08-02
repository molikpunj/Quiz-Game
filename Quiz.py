'''WELCOME TO THE QUIZ GAME!!!'''

questions = [
    {
        "quest" : "Q1. What is Artificial Intelligence (AI)?",
        "choice" : ["A. A type of hardware", "B. A system that can perform tasks requiring human intelligence", "C. A mobile app", "D. A form of spreadsheet software"],
        "correct" : "B"
    },
    {
        "quest" : "Q2. Which of the following is a type of AI that performs a specific task?",
        "choice" : ["A. General AI", "B. Super AI", "C. Narrow AI", "D. Natural AI"],
        "correct" : "C"
    },
    {
        "quest" : "Q3. What is the main difference between AI and Machine Learning (ML)?",
        "choice" : ["A. AI is a subset of ML", "B. ML is unrelated to AI", "C. ML is a subset of AI", "D. They are exactly the same"],
        "correct" : "C"
    },
    {
        "quest" : "Q4. How does machine learning work?",
        "choice" : ["A. It follows hard-coded rules", "B. It learns from data and improves over time", "C. It relies only on human feedback", "D. It uses trial-and-error with no data"],
        "correct" : "B"
    },
    {
        "quest" : "Q5. Which of the following is a common real-life application of AI?",
        "choice" : ["A. Web hosting", "B. Word processors", "C. Voice assistants like Siri and Alexa", "D. Textbooks"],
        "correct" : "C"
    },
    {
        "quest" : "Q6. What is a neural network?",
        "choice" : ["A. A physical brain component", "B. A method of connecting computers", "C. A machine learning model inspired by the human brain", "D. A type of database"],
        "correct" : "C"
    },
    {
        "quest" : "Q7. What is Natural Language Processing (NLP) used for?",
        "choice" : ["A. Storing documents", "B. Understanding and generating human language", "C. Playing video games", "D. Data encryption"],
        "correct" : "B"
    },
    {
        "quest" : "Q8. Which programming language is most commonly used in AI development?",
        "choice" : ["A. HTML", "B. Python", "C. CSS", "D. PHP"],
        "correct" : "B"
    },
    {
        "quest" : "Q9. Which of the following is an advantage of AI?",
        "choice" : ["A. It gets tired like humans", "B. It can work 24/7 without breaks", "C. It makes decisions emotionally", "D. It needs constant supervision"],
        "correct" : "B"
    },
    {
        "quest" : "Q10. What is one ethical concern about AI?",
        "choice" : ["A. It can get physically injured", "B. It consumes too much water", "C. It can cause job displacement", "D. It cannot store information"],
        "correct" : "C"
    }
]

def printques(questions):
    score = 0
    for question in questions:
        print(question["quest"])
        for option in question["choice"]:
            print(option)
        answer = input("Enter your answer(A, B, C or D):")
        if (answer == question["correct"]):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print("Your Score: ", score, "\n")
    

printques(questions)