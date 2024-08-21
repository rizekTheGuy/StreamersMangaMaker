from groq import Groq

def Writer(Theme, AIinput):

    client = Groq(
        api_key="PUT Your API KEY Here"
    )
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": AIinput + "\nThe theme is :" + Theme
            }
        ],
        temperature=1,
        max_tokens=8192,
        top_p=1,
        stream=True,
        stop=None,
    )

    result_string = ""
    for chunk in completion:
        result_string += chunk.choices[0].delta.content or ""
    return(result_string)