from openai import OpenAI

key ="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"

client = OpenAI(
    api_key=key,


)
messages =[]
def completion(message):
    global messages
    
    messages.append (
        {
            "role":"user",
            "content":message
            },
        
    ),
    chat_completion = client.chat.completions.create( messages=messages,
    model = "gpt-4o",
                                                     )

    message ={
        "role":"assistant",
        "content":chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis : {message['content']}")

if __name__=="__main__":
    print(f"Jarvis : Hi I am Jarvis , How may I help you\n")
    while True:
        user_question = input()
        print(f"User : {user_question}")

        completion(user_question)