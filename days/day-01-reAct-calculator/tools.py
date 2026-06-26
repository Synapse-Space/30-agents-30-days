import math

SAFE_FUNCTIONS={
    "sqrt":math.sqrt,
    "pow":pow,
    "abs":abs,
    "round":round
}

def calculator(expression:str)->str:
    try:
        result=eval(expression,{
            "__builtins__":None,
            
        },
        SAFE_FUNCTIONS
        )
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"