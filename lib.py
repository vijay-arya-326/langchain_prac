from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph
import traceback

def getAIMessage(response):
    return response['messages'][-1].content

def displayAllMessages(response):
    for m in response['messages']:
        print(m.pretty_print())


def cliBot(graphInstance: StateGraph, config=None):
    try:
        exitPrases = ["exit", "bye", "tata"]
        flag = True
        while flag:
            inputMsg = input("Please enter your message: ")
            if inputMsg.strip().lower() in exitPrases:
                flag = False
                print("Human requested to close session!!! Bye see you around")
            else:
                strippedMsg = inputMsg.strip()
                humanMessage = [HumanMessage(content=strippedMsg)]
                r = graphInstance.invoke({"messages": humanMessage})
                print(f"Question:\n {strippedMsg}", end ="\n==============\n")
                print("Assistant:\n")
                print(getAIMessage(response=r), end ="\n=============\n")
    except Exception as e:
        print(e)
        print(traceback.format_exc())
