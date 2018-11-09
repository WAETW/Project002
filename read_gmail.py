from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
from BingTTS import TTS
import sched

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
	flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
	creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()),cache_discovery=False)

user_id =  'me'
#label_id_one = 'INBOX'
label_id_one = 'IMPORTANT'
label_id_two = 'UNREAD'

unread_msgs = GMAIL.users().messages().list(userId='me',labelIds=[label_id_one, label_id_two]).execute()
mssg_list = unread_msgs['messages']

def get_unread():
	try:
		print ("未讀信件數: ", str(len(mssg_list)))
		unread_msgs_sum = "你有"+str(len(mssg_list))+"封未讀信件"
		TTS(unread_msgs_sum,'中文')
	except (KeyError):
		print("沒有新信件")
		pass

def read_gmail():
	try:
		for mssg in mssg_list:
			temp_dict = { }
			m_id = mssg['id']
			message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()
			payld = message['payload']
			headr = payld['headers']
			for one in headr:
				if one ['name'] == 'Date':
					msg_date = one ['value']
					date_parse = (parser.parse(msg_date))
					m_date = (date_parse.date())
					temp_dict['日期'] = str(m_date)
					print('日期: '+temp_dict['日期'])
				else:
					pass

			for two in headr:
				if two['name'] == 'From':
					msg_from = two['value']
					temp_dict['發送人'] = msg_from
					print('發送人: '+temp_dict['發送人'])

			for three in headr:
				if three['name'] == 'Subject':
					msg_subject = three['value']
					temp_dict['主旨'] = msg_subject
					print('主旨: '+temp_dict['主旨'])
				else:
					pass
			 
			temp_dict['信件預覽'] = message['snippet']
			TTS('日期'+temp_dict['日期']+'發送人'+temp_dict['發送人']+'主旨'+temp_dict['主旨'],'中文')
			GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'removeLabelIds': ['UNREAD']}).execute()
			#read = speech("是否繼續閱讀?",5)
			#if read == '是':
				#print (temp_dict['信件預覽'])
				#TTS('信件預覽'+temp_dict['信件預覽'],'中文')
			#elif read == '否':
				#pass

			#ans = speech("是否要標示為已讀?",5)
			'''if ans == '是':
				GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'removeLabelIds': ['UNREAD']}).execute()'''
			#elif ans == '否':
				#pass
			#important = speech("是否標示為重要訊息?",5)
			#if important == '是':
				#GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'removeLabelIds': [], 'addLabelIds': ['STARRED']}).execute()
			#elif important != '是':
				#pass
	except(KeyError):
		pass

def main():
	get_unread()
	read_gmail()
if __name__ == "__main__":
	main()

