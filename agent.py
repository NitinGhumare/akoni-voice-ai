from llm import stream_response, system_prompt


class RealEstateAgent:

    def __init__(self, model_name):

        self.model_name = model_name

        self.messages = [
            {"role": "system", "content": system_prompt}
        ]


    def chat_stream(self, user_input):

        self.messages.append(
            {"role": "user", "content": user_input}
        )

        full_response = ""

        for token in stream_response(self.messages, self.model_name):

            full_response += token

            yield token

        self.messages.append(
            {"role": "assistant", "content": full_response}
        ) 

