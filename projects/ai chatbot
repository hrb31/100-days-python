from openai import OpenAI

client = OpenAI()

print("AI Chatbot")
print("Say exit, quit, or bye to exit the chatbot")
print("-----------------------------------------")
print()

while True:
    
    user = input("You: ")
    
    if user.lower() in ["exit", "quit", "bye",]:
        print("AI Chatbot: Goodbye!")
        break
        
    response = client.responses.create(
        model="gpt-4.1",
        tools=[{"type": "web_search_preview"}],
        input=user
    )
    print("AI Chatbot:", response.output_text)

