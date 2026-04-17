import os
import gradio as gradio
from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()


# for this I will use the same model I have been using for cost-efficiency gpt-5.4-nano

agent = Agent(
    'openai:gpt-5.4-nano',
    system_prompt='You are a helpful assistant that provides concise and accurate answers to user queries. Always respond in a clear and informative manner.',
)

async def interact(user_message, history, pydantic_history):
    """
    Handle user interaction
    user_message: str- the current user message
    history: list - gradio chatbot history (list of dicts)
    pydantic history: list- List of Pydantic AI ModelMessage objects
    """
    if pydantic_history is None:
        pydantic_history = []

    if history is None:
        history = []

    # append the user message to gradio history
    history.append({"role": "user", "content": user_message})

    # Yield initial state: Update the chatbot with user message, keep pydantic history same, clear input

    yield history, pydantic_history, ""

    # run the agent stream, pass the full pydantic history and the agent will append the new user message (from the prompt) and its response to the result
    async with agent.run_stream(user_message, message_history=pydantic_history) as result:
        # Prepare an empty assistant message in history
        history.append({"role": "assistant", "content": ""})
        partial_text = ""

        async for chunk in result.stream_text(delta=True):
            partial_text += chunk
            # update the last message in history
            history[-1]["content"] = partial_text
            yield history, pydantic_history, ""

        # After stream finishes, update the pydantic_history with new messages, result.all_messages() returns full history including the new interaction
        pydantic_history = result.all_messages()

    yield history, pydantic_history, ""

# Create the gradio interface

with gradio.Blocks()as demo:
    gradio.Markdown("# Pydantic AI Agent (gpt-5.4-nano)")

    chatbot = gradio.Chatbot(label="Agent", height=600)
    msg = gradio.Textbox(placeholder="Type for your message here....", label="User Input")

    # State to hold the pydantic AI message history (ModelMessage objects)
    pydantic_history_state = gradio.State([])

    # Subtmit handler
    msg.submit(
        interact,
        inputs=[msg, chatbot, pydantic_history_state],
        outputs=[chatbot, pydantic_history_state, msg]
    )

if __name__ == "__main__":
    demo.launch()