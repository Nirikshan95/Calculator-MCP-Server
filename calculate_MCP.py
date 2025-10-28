from fastmcp import FastMCP

mcp=FastMCP(name="Dummy Calculator")

@mcp.tool
def add(num1:int,num2:int):
    """
    Adds two numbers
    """
    return num1+num2

@mcp.tool
def subtract(num1:int,num2:int):
    """
    Subtracts two numbers
    """
    return num1-num2

@mcp.tool
def multiply(num1:int,num2:int):
    """
    Multiplies two numbers
    """
    return num1*num2

@mcp.tool
def divide(num1:int,num2:int):
    """
    Divides two numbers
    """
    if num2==0:
        raise ValueError("Cannot divide by zero")
    return num1/num2

if __name__=="__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)