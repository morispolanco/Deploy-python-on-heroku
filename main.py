from random import random, uniform
from os import system
from time import sleep

import openai

import config

openai.api_key = config.API_KEY

class Col:
    HEAD = '\033[95m'       # Headers duh
    BLUE = '\033[94m'       # Bot output & mentions
    CYAN = '\033[96m'       # Creator messages
    GREEN = '\033[92m'      # System messages
    YEL = '\033[93m'        # User input & mentions
    RED = '\033[91m'        # Errors
    END = '\033[0m'         # Clears colors and styles
    BOLD = '\033[1m'        # Bolds the font
    UNDER = '\033[4m'       # Underlines the font

# Change this number to determine how many messages are stored in the history. The higher the number, the more tokens
# it costs to operate this thing. I don't recommend going anywhere beyond 50 because 50 already surpasses 2000 tokens
# per message.

no_of_messages_stored = 20

m_log = []

def message():
    global m_log
    inp = str(input(f'{name}: {Col.YEL}'))
    print(f'{Col.END}', end='\r')


    if len(m_log) < no_of_messages_stored:
        m_log.append(f'User: {inp}')
    else:
        del m_log[0]
        m_log.append(f'User: {inp}')

    if inp == 'EXIT':
        print(f'{Col.GREEN}Exiting the program.')
        system('pause')
        print(f'{Col.END}')
        system('cls')
        exit()
    elif inp == 'RESTART':
        m_log = []
        system('cls')
        print("Type in 'EXIT' to exit the program or 'RESTART' to restart the conversation.\n")
        message()

    query = openai.Completion.create(
        engine="text-davinci-001",
        prompt='\n'.join(m_log)+'\nReply:',
        temperature=0.8,
        max_tokens=1000,
        best_of=1,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        stop=['User:', 'Reply:']
    )
    ans = query['choices'][0]['text']

    ans = ans.replace("\n", "")
    if ans[:1] == ' ':
        ans = ans[1:]

    print(f'AI: {Col.BLUE}{ans}{Col.END}')

    if len(m_log) < no_of_messages_stored:
        m_log.append(f'Reply: {ans}')
    else:
        del m_log[0]
        m_log.append(f'Reply: {ans}')

    message()

system('cls')
print(f"\n                    {Col.UNDER}{Col.BOLD}{Col.HEAD}Greetings!{Col.END}\n\n"
      f"    This chatbot was made possible by the open\n"
      f"    beta of the {Col.BLUE}GPT-3 AI{Col.END} developed by OpenAI.\n"
      f"    It is an incredibly advanced deep learning\n"
      f"    model trained to produce human-like text.\n"
      f"    \n"
      f"    This script takes {Col.YEL}user input{Col.END} and then uses\n"
      f"    {Col.BLUE}GPT-3{Col.END}'s API to query the {Col.BLUE}AI{Col.END} for a response,\n"
      f"    which it then formats into a chat-like form.\n"
      f"    \n"
      f"           {Col.CYAN}I hope you enjoy using it as\n"
      f"           much as I enjoyed making it!\n\n"
      f"             {Col.END}Coded by {Col.CYAN}FlashAndromeda{Col.END}\n\n")
shortcut = input(f'             {Col.GREEN}PRESS [ENTER] TO CONTINUE{Col.END}\n                         ')

if shortcut == 'gotta go fast':
    m_log = []
    name = str(input(f'What is your name?\n>'))
    system('cls')
    print("Type in 'EXIT' to exit the program or 'RESTART' to restart the conversation.\n")
    message()

system('cls')

print(f'\n\n    Establishing connection with the {Col.BLUE}GPT-3{Col.END} API servers.\n')

i = 0
while i in range(30):
    print(f'               Connecting {Col.RED}{i*3}%{Col.END} complete...', end='\r')
    sleep(uniform(0, 0.3))
    i += 1

print(f'              {Col.GREEN}Connection has been established!{Col.END}')
print(f"            {Col.RED}Synchronizing retroactive clocking...", end='\r')
sleep(random()*2+1)
print(f"                  {Col.GREEN}Synchronization complete!                     {Col.END}\n")
print(f"                     Waking up {Col.BLUE}GPT-3{Col.END}.")
print(f"       It's a heavy sleeper, this might take a minute...")
sleep(random()*2.5+2.5)

system('cls')

print(f'{Col.YEL}{Col.END}', end='\r')
sleep(1)
name = str(input(f'What is your name?\n>'))
system('cls')
print("Type in 'EXIT' to exit the program or 'RESTART' to restart the conversation.\n")
message()
