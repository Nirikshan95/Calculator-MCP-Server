# Calculator MCP Server

A simple Model Context Protocol (MCP) server built with FastMCP that provides basic calculator tools.

## Remote Access

You can access this MCP server remotely at: **https://calculator-mk.fastmcp.app/mcp**

## Using with Claude Desktop or Other Applications

To use this MCP server with Claude Desktop or any other MCP-compatible application:

1. Configure your MCP client to connect to the remote URL: `https://calculator-mk.fastmcp.app/mcp`
2. Once connected, you can use calculator functions directly in your conversations:
   - Ask Claude to "add 10 and 5" 
   - Request calculations like "multiply 25 by 4"
   - Perform complex math operations through natural language

The server supports the following calculator operations:
- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`) - Includes zero division protection

## Features

This MCP server exposes the following calculator tools:

- **add**: Adds two integers
- **subtract**: Subtracts two integers
- **multiply**: Multiplies two integers
- **divide**: Divides two integers (with zero division check)

## API Tools

### add(num1: int, num2: int) -> int
Adds two numbers.

### subtract(num1: int, num2: int) -> int
Subtracts num2 from num1.

### multiply(num1: int, num2: int) -> int
Multiplies two numbers.

### divide(num1: int, num2: int) -> float
Divides num1 by num2. Raises ValueError if dividing by zero.

## Development

- Python 3.x required
- Uses FastMCP for MCP implementation

## License

This project is open source. Feel free to use and modify.
