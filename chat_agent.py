from agent import RealEstateAgent

agent = RealEstateAgent()

print("Dubai Real Estate AI Agent")
print("Type 'exit' to stop\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = agent.chat(user_input)

    print("\nAssistant:", response)