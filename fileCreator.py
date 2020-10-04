import botCreator
import os
import shutil

def makePyFile(x):
    f=open(x,"a")
    botCreator.addImportOptions(f)
    botCreator.addLoad(f)
    botCreator.addDict(f)
    botCreator.addVariables(f)
    botCreator.addMakeClient(f)
    botCreator.addConnectUsingClient(f)
    botCreator.addListOfMembers(f)
    botCreator.addMemberWelcome(f,"Welcome to the guild!")
    botCreator.addMessageReaction(f,'kry')
    botCreator.addMessageReaction2(f)
    botCreator.addExceptionHandling(f)
    botCreator.addClientRun(f)

def moveFilesToDir():
    os.mkdir('Abe Bot')
    shutil.copyfile('scraped-hate-speech-data','Abe bot/scraped-hate-speech-data')
    shutil.move('Abe-bot.py',"Abe bot")
    shutil.move('.env',"Abe bot")
    shutil.move('Botresponses',"Abe bot")

makePyFile('Abe-bot.py')
moveFilesToDir()
