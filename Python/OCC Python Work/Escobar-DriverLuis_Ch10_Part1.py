## A question with a text & an answer (only handles strings)(SUPERCLASS)
#
class Question:
    ## Constructs a question with an empty question & answer strings
    #
    def __init__(self):
        self._text = ''
        self._answer = ''
        
    ## Sets the question text.
    # @param questionText the text of this
    #
    def setText(self,questionText):
        self._text = questionText

    ## Sets the answer for this question
    # @param correctReponse the answer
    #
    def setAnswer(self,correctResponse):
        self._answer = correctResponse

    ## Checks a given response for correctness
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    #
    def checkAnswer(self,response):
        return response.upper() == self._answer.upper()

    ## Displays this question
    #
    def display(self):
        print(self._text)


##
#  This program shows a simple quiz with one question.
#

# Create the question and expected answer.
q = Question()
q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")      

# Display the question and obtain user's response.
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))
