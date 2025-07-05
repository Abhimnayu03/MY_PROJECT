# print("hello world!!")
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatBot= ChatBot("My BOT")
trainers=ListTrainer(chatBot)

convo=[
    'Hi!!',
    'bol bhai!!',
    'How you doing!!',
    'I\'m fine',
    'From which country you belong?',
    'India!!'
]
trainers.train(convo)
# answer=chatBot.get_response("you belong to which place?")
# print(answer)
while True:
    query=input()
    if query=='exit':
        break;
    answer=chatBot.get_response(query)
    print("Bot :",answer)
