import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from agent import WeatherAgent
def main():
    print("=" * 60)
    print("DAY 2 - WEATHER BUSTER")
    print("=" * 60)

    agent = WeatherAgent()

    while True:

        query=input("/nYou > ")
        if query.lower() in ["exit", "quit"]:
            break

        answer=agent.run(query)
        print("\nAgent\n")

        print(answer)


if __name__ == "__main__":
    main()