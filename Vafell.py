import amino
import os

mail = os.environ.get('V_NAME')
passw = os.environ.get('V_PASS')


client = amino.Client()
client.login(email=mail, password=passw) 
subclient = amino.SubClient(comId='156542274', profile=client.profile) 
print('Bot - on')

def on_message(data):
    chatid = data.message.chatId
    nickname = data.message.author.nickname
    content = data.message.content
    mtype = data.message.type
    chatname = subclient.get_chat_thread(chatId=data.message.chatId).title
    mid = data.message.messageId
    uid = data.message.author.userId
    print(f'{chatname}: {nickname}: {mtype}: {content}')
    
    content = str(content).split(" ")
    if content[0][0] == "!" and content[0][1:].lower() == "ку":
        subclient.send_message(message="Дарова, отец...", chatid=chatid)
    
    if (mtype == 100) | (mtype == 109) | (mtype == 107)  | (mtype == 110) | (mtype == 108)  | (mtype == 111) | (mtype == 111):
        if mtype == 100 and content == None:
                  pass
        else:
            subclient.kick(chatId=chatid, userId = uid, allowRejoin=False)
            subclient.send_message(chatId = chatid, message = 'Не тот чатик, малыш')
methods = []
for x in client.callbacks.chat_methods:
    methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))

