import amino
import os
import time

mail = os.environ.get('V_NAME')
passw = os.environ.get('V_PASS')


client = amino.Client()
client.login(email=mail, password=passw) 
sub_client = amino.SubClient(comId='156542274', profile=client.profile)
reloadTime = time.time() + 197
print('Bot - on')


def on_message(data):
	chatId = data.message.chatId
	nickname = data.message.author.nickname
	content = data.message.content
	chatname = sub_client.get_chat_thread(chatId=data.message.chatId).title
	id = data.message.messageId
	print(f"{nickname}: {content} ({chatname} : {data.message.type})") 
	
	content = str(content).split(" ")
	if content[0][0] == "!" and content[0][1:].lower() == "куу":
		sub_client.send_message(message="Дарова, отец...", chatId=chatId)
	##################################Защита чата##################################################

	if data.message.content != None and data.message.type in [1, 50, 58, 57, 59, 100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 113, 114, 115, 116, 124, 125, 126]:
		#sub_client.send_message(message='Не тот чатик, малыш :)', chatId=data.message.chatId)
		sub_client.delete_message(chatId=data.message.chatId, messageId=data.message.messageId)
		sub_client.kick(userId=data.message.author.userId, chatId=data.message.chatId, allowRejoin = True)

methods = []
for x in client.callbacks.chat_methods:
	methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))
'''
methods = []
for x in client.chat_methods:
	methods.append(client.event(client.chat_methods[x].__name__)(on_message))	
'''
##################################

	

while True:
    if time.time() >= reloadTime:
        print("# Update Log: Updating socket...")
        try:
            client.socket.close()
            client.socket.start()
        except:pass
        print("# Update Log: Updated!")
        reloadTime += 197
