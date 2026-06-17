cli_project — MCP Server & Client in Python
Built as a hands-on project from the Anthropic Introduction to Model Context Protocol course.
This project demonstrates how to build MCP (Model Context Protocol) servers and clients from scratch using Python. It covers all three core MCP primitives — Tools, Resources, and Prompts — and shows how they integrate with Claude AI to create powerful AI-connected applications.

📁 Project Structure
cli_project/
├── core/                  # Core shared utilities and base classes
├── app.egg-info/          # Package metadata (auto-generated)
├── main.py                # Entry point to run the project
├── mcp_server.py          # MCP Server — defines tools, resources, and prompts
├── mcp_client.py          # MCP Client — connects to server and queries Claude
├── pyproject.toml         # Project config and dependencies
├── uv.lock                # Lock file for reproducible installs (uv)
├── .env                   # Environment variables (not committed)
└── .gitignore

🤔 What is MCP?
Model Context Protocol (MCP) is an open standard by Anthropic that lets AI models like Claude connect with external tools and data sources in a structured, transport-agnostic way.
Instead of writing custom integrations for every service, MCP shifts the tool definition and execution responsibility to specialized MCP servers. A client (like Claude) discovers and uses these servers without needing to know the implementation
The 3 Core MCP Primitives
Tools, resources, Prompts

🔄 How It Works — Request Flow
User Input
    ↓
MCP Client (mcp_client.py)
    ↓  [sends query + available tools]
Claude AI (Anthropic API)
    ↓  [decides which tool/resource to use]
MCP Server (mcp_server.py)
    ↓  [executes the tool / returns resource]
Claude AI
    ↓  [synthesizes the final response]
User
⚙️ Setup & Installation
Prerequisites
Python 3.10+
An Anthropic API key(You have to buy the API from [claudeconsole -Pay as you use]


📚 Course Reference
This project was built following the Anthropic Introduction to Model Context Protocol course:
🔗 https://anthropic.skilljar.com/introduction-to-model-context-protocol
Topics Covered:
MCP architecture and transport-agnostic communication
Setting up a project with the MCP Python SDK
Defining tools using decorators (no manual JSON schemas)
Using the MCP Server Inspector to debug
Building a full MCP client that connects to the server
Defining and accessing static + templated resources
Handling MIME types (JSON and text) in resource responses
Creating reusable prompt templates
Understanding when to use Tools vs Resources vs Prompts


