import gradio as gr
import os

from mcp import StdioServerParameters
from smolagents import InferenceClientModel, CodeAgent, ToolCollection, MCPClient


mcp_client = MCPClient(
    {"url": "https://abidlabs-mcp-tools2.hf.space/gradio_api/mcp/sse"}
)

tools=mcp_client.get_tools()


model = InferenceClientModel(token="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")
agent = CodeAgent(tools=[*tools], model=model)


demo = gr.ChatInterface(
    fn=lambda message, history: str(agent.run(message)),
    type="messages",
    examples=["Prime factorization of 68"],
    title="Agent with MCP Tools",
    description="This is a simple agent that uses MCP tools to answer questions."
)

demo.launch()