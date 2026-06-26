import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import ReActAgent

def main():
    print("="*60)
    agent=ReActAgent()

    while True:
        query=input("\nYou> ")

        if query.lower() in ["exit","quit"]:
            print("Exiting...")
            break

        result=agent.run(query)

        if result:
            print("\nFinal Answer:",result)

if __name__=="__main__":
    main()
