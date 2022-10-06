#!/usr/bin/env python
# coding: utf-8

# ### Criando um chatbot Inteligente

# In[6]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# isso aqui só precisa para corrigir o bug
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


# In[18]:


chatbot = ChatBot("BOT_Thiago", tagger_language=ENGSM)

conversa = [
    "Eai",
    "E aí, tranquilo?",
    "Tranquilo",
    "Qual a boa de hoje?",
    "Eu estou ensinando Python e até chatbot",
    "Caraca que doidera",
    "Maneiro não é",
    "Irado",
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)


# In[21]:


while True:
    mensagem = input("Mande uma mensagem para o chatbot:")
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)


# In[1]:


chatbot.storage.drop()


# In[ ]:




