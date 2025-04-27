from functools import wraps
from pydantic import BaseModel, Field
from typing import Type, Callable, Optional, Any
import json

# Define a base class for input validation using Pydantic
class InputSchema(BaseModel):
    # Placeholder for any inputs; can be extended later
    example_field: Optional[str] = Field(None, description="Example field for input validation")

# Tool decorator definition
def Tool(name: str, input_schema: Type[BaseModel]):
    def decorator(func: Callable[..., Any]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Schema validation for inputs (if any)
            if input_schema:
                schema_instance = input_schema(**kwargs)
                # Optionally print or log the validated input
                print(f"Validating input: {schema_instance.json()}")
            
            # Call the wrapped function
            return func(*args, **kwargs)
        
        wrapper.tool_name = name  # Attach a tool name to the function
        return wrapper
    return decorator

# Example usage of the Tool decorator
if __name__ == "__main__":
    # Define an example function using the Tool decorator
    @Tool(name="example_tool", input_schema=InputSchema)
    def example_function(example_field: str):
        print(f"Running {example_function.__name__} with input: {example_field}")
        return f"Processed {example_field}"

    # Call the function with some example input
    result = example_function(example_field="Test")
    print(result)
