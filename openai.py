#@title Openai
import openai
openai.api_key = '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'

while True:
    msg = input()
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=msg,
        max_tokens=128,
        temperature=0.5
    )

    completed_text = response['choices'][0]['text']
    print(completed_text)
