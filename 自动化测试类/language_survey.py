from survey import AnonymousSurvey

question = "What language do you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any question to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you for taking this survey!")
my_survey.show_results()
