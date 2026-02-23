import sys

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
import traceback

def getAIMessage(response):
    return response['messages'][-1].content

def displayAllMessages(response):
    for m in response['messages']:
        print(m.pretty_print())

def log_msg(msg:str):
    print(msg, file=sys.stderr)

def cliBot(graphInstance: StateGraph, config=None, show_all_msg = False):
    """

    :param graphInstance: StateGraph Instance
    :param config: Memory Configration
    :param show_all_msg: Show all messages or last AI message
    :return:
    """
    try:
        exit_phrases = ["exit", "bye", "tata"]
        flag = True
        while flag:
            inputMsg = input("Please enter your message: ")
            if inputMsg.strip().lower() in exit_phrases:
                flag = False
                print("Human requested to close session!!! Bye see you around")
            else:
                strippedMsg = inputMsg.strip()
                humanMessage = [HumanMessage(content=strippedMsg)]
                if config is None:
                    r = graphInstance.invoke({"messages": humanMessage})
                else:
                    r = graphInstance.invoke({"messages": humanMessage}, config)

                if show_all_msg == False:
                    print(f"Question:\n {strippedMsg}", end ="\n==============\n")
                    print("Assistant:\n")
                    print(getAIMessage(response=r), end ="\n=============\n")
                else:
                    displayAllMessages(r)
    except Exception as e:
        print(e)
        print(traceback.format_exc())



