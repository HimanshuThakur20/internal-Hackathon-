from nltk.chat.util import Chat, reflections



pairs = [
         ['(.*)my name is (.*)', ['Hello %2, How are you today ?']],
         ['(hi|hello|huii|hoii|helloo)', ['Hello', 'Hey there', 'Hii']],
         ['(.*)fine(.*)', ['Nice']],
         ['(.*)i am not (.*)', ['ooh...what happend dear?']],
         ['(.*)to register a complaint(.*)', ['Go to this link (https://forms.gle/iufjL1dBKf76quck7) '
                                              'to register your complain online'
                                              ' or you can reach your nearby police station']],
         ['(.*)helpline(.*)', ['Police- 100\n'
                               'Ambulance- 108\n'
                               'Fire station- ']],
         ['(.*)emergency numbers(.*)', ['Police- 100\n'
                                        'Ambulance- 108\n'
                                        'Fire station- ']],
         ['(.*)laws(.*)', ['The law of India refers to the system of law across the Indian nation. ...'
                           'On the basis of IPC (Indian Penal Code)'
                           'The exception to this rule is in the state of Goa,where a uniform civil code is in place,'
                           'in which all religions have a common law regarding marriages, divorces, and adoption.']],
         ['(.*)I am (.*)', ['Hello I am Nayaya the chatbot, How can i help you %2 ?']],
         ['(.*)Chief Justice of India(.*)', ['Nuthalapati Venkata Ramana is the new CJI of India']],
         ['(.*) the Chancellor of the NALSAR University of Law (.*) in Hyderabad(.*)', ['Chief Justice of A.P.'
                                                                                        ' High Cour']],
         ['(.*)Legal Advisor to the Government of a State(.*)', ['The Advocate General']],
         ['(.*)age of retirement of a Judge of a High Court(.*)', ['62 years']],
         ['(.*)first woman judge to be appointed Chief Justice of a High Court(.*)', ['Justice Smt Leila Seth']],
         ['(.*)High courts in India(.*)', ['There are 25 High Courts in India,'
                                           'six having control over more than one State/UT.'
                                           'Delhi has a High Court of its own among the Union Territories.']],
         ['(.*)types of courts(.*)', ['The court system of India comprises the Supreme Court of India,'
                                      'the High Courts and subordinate courts at district,'
                                      ' municipal and village levels.']],
         ['(.*)States in India(.*)', ['India is a federal union comprising 28 states and 8 union territories,'
                                      'for a total of 36 entities']],
         ['(.*)ok(.*)', ['Always here to help :)']],
         ['(.*)bye(.*)', ['Byee...take care']],
         ['(.*)quit(.*)', ['Byee...take care']],
         ['(thanks|thank you|thank you so much|thank you very much)', ['Welcome', 'Always here to help you', 'You don'
                                                                       't have to mention']],
         ['(.*)', ['I did''t get you...\n Do you want to report a complaint?']],

]


# default message at the start of chat
print("Hi, I'm Nyaya.I am here to help you out with your problems. "
      "Please type lowercase English language.Type quit to leave ")

# Create Chat Bot
chat = Chat(pairs, reflections)

# Start conversation
chat.converse()
