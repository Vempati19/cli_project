from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(doc_id: str = Field(description="The ID of the document to read.")):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return docs[doc_id]


@mcp.tool(
    name="edit_contents",
    description="Edit the contents of a document and return the updated content as a string."
)
def edit_document(
    doc_id: str = Field(description="The ID of the document to edit."),
    new_content: str = Field(description="The new content to replace the existing document content.")
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    docs[doc_id] = new_content
    return docs[doc_id]


@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_documents() -> list[str]:
    return list(docs.keys())


@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
)
def fetch_document(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return docs[doc_id]


@mcp.prompt(
    name="rewrite_doc_markdown",
    description="Rewrite the contents of a document in markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax.

    The id of the document you need to reformat is:
    <document_id>
    {doc_id}
    </document_id>

    Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra context.
    Use the 'edit_document' tool to edit the document. After the document has been edited, return the updated content.
    """
    return [base.UserMessage(content=prompt)]


@mcp.prompt(
    name="summarize_doc",
    description="Summarize the contents of a document."
)
def summarize_doc(
    doc_id: str = Field(description="Id of the document to summarize")
) -> list[base.Message]:
    prompt = f"""
    Your goal is to summarize the contents of a document.

    The id of the document you need to summarize is:
    <document_id>
    {doc_id}
    </document_id>

    Provide a concise summary of the document's key points.
    """
    return [base.UserMessage(content=prompt)]


if __name__ == "__main__":
    mcp.run(transport="stdio")