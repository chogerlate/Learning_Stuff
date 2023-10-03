class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Evaluate the value of an arithmetic expression in Reverse Polish Notation

        Args:
            tokens (List[str]): list of tokens

        Returns:
            int: result of the arithmetic expression
        """
        stack = [] # use array to implement our stack
        for token in tokens :
            if (token == "+" or token == "-" or token =='*' or token =='/'):
                operand_1 = stack.pop() # get the first operand
                operand_2 = stack.pop() # get the second operand
                
                # evaluate the expression
                if token == "+":
                    result = operand_2 + operand_1
                    stack.append(result)
                if token == "-":
                    result = operand_2 - operand_1
                    stack.append(result)
                if token == "*":
                    result = operand_2 * operand_1
                    stack.append(result)
                if token == "/":
                    result = int(operand_2 / operand_1)
                    stack.append(result)
            else : # if the token is a number
                stack.append(int(token))
            
        return stack.pop()