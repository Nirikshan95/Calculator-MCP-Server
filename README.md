# Calculator MCP Server

A simple Model Context Protocol (MCP) server built with FastMCP that provides basic calculator tools.

## Features

This MCP server exposes the following calculator tools:

- **add**: Adds two integers
- **subtract**: Subtracts two integers
- **multiply**: Multiplies two integers
- **divide**: Divides two integers (with zero division check)

## Installation

1. Clone or download this repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or directly:

   ```bash
   pip install fastmcp
   ```

## Usage

Run the server:

```bash
python dummy_MCP.py
```

The server will start on `http://0.0.0.0:8000`.

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
