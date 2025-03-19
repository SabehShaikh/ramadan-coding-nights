import chainlit as cl

# when the user sends a message
@cl.on_message
async def main(message: cl.Message):

    # whatever user said comes in .content
    response = f"You said: {message.content}"
    await cl.Message(content=response).send()

