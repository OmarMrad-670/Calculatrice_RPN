from fastapi import FastAPI, HTTPException
import urllib.parse

app = FastAPI(title="RPN API")

stacks = {}

operations = ['+', '-', '*', 'div']



########################################## 1


@app.get("/rpn/op")
async def list_all_the_operand():
    return {"operations": operations}


############################################ 2

@app.post("/rpn/op/{op}/stack/{stack_id}")
async def apply_an_operand_to_a_stack(op: str, stack_id: str):


    ########################### Vérifier si la pile existe
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")
    
    stack = stacks[stack_id]
    
    ########################### Vérifier si la pile est vide
    if not stack:
        raise HTTPException(status_code=400, detail="Stack is empty")
    
    ############################ Vérifier si l'opération est valide
    if op not in ['+', '-', '*', 'div']:
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    ############################ Vérifier si la pile contient au moins deux éléments pour effectuer l'opération
    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Not enough elements in stack for operation")
    
    ############################# Effectuer l'opération correspondante
    num2 = stack.pop()
    num1 = stack.pop()
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = num1 / num2
    
    stack.append(result)
    
    return {"result": result}



########################################### 3

@app.post("/rpn/stack")
async def create_a_new_stack():
    ############################### Générer un nouvel identifiant de pile
    stack_id = str(len(stacks) + 1)
    
    ############################## Créer une nouvelle pile vide
    stacks[stack_id] = []
    
    return {"stack_id": stack_id}



############################################# 4


@app.get("/rpn/stack")
def list_the_available_stacks():
    return stacks


############################################### 5

@app.delete("/rpn/stack/{stack_id}")
async def delete_a_stack(stack_id: str):
    ##################################### Vérifier si la pile existe
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")
    
    ##################################### Supprimer la pile correspondante
    del stacks[stack_id]
    
    return {"message": "Stack deleted"}


################################################# 6


@app.post("/rpn/stack/{stack_id}")
async def push_a_new_value_to_a_stack(stack_id: str, value: float):
    # Vérifier si la pile existe
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")
    
    ################################## Ajouter la valeur à la pile correspondante
    stacks[stack_id].append(value)
    
    return {"message": "Value added to stack"}


################################################# 7

@app.get("/rpn/stack/{stack_id}")
async def get_a_stack(stack_id: str):
    #################################### Vérifier si la pile existe
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")
    
    ##################################### Renvoyer la pile correspondante
    return {"stack_id": stack_id, "stack": stacks[stack_id]}
















