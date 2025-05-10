import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language do you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'French']


    def test_store_single_response(self):
        # question = "What language do you first learn to speak?"
        # my_survey1 = AnonymousSurvey(question)
        # my_survey1.store_response("English")l
        self.my_survey.store_response(self.responses[0])

        self.assertIn('English', self.my_survey.responses)

    def test_three_answers(self):
        # question = "What language do you first learn to speak?"
        # my_survey2 = AnonymousSurvey(question)
        # responses = ['English', 'Chinese', 'French']
        for res in self.responses:
            self.my_survey.store_response(res)

        for res in self.responses:
            self.assertIn(res, self.my_survey.responses)




if __name__ == "__main__":
    unittest.main()
