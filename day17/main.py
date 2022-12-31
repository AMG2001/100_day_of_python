from question_model import questionsBank
from  quiz_brain import QuizBrain
print(questionsBank[2].question)
print(questionsBank[2].answer)

quizbrain = QuizBrain(questionsBank)
quizbrain.startQuiz()