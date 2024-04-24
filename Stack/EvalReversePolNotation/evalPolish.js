exports.calculate = function(expression) {
    // we can use a stack based approach to pop the numbers that we come across in the string that is reversed
    // and then if there is a operator found we can perform the operation on the two numbers popped and push it back
    //into the stack
  
    const exp_arr = expression.split(' ');
    const stack = [];
  
    const operator_list = new Set(['+', '-', '/', '*']);
    // We want to iterate in reverse to start from the right side of array to get the prefix Notation last after numbers
    for (let i = exp_arr.length-1; i >= 0; i--){
      const exp = exp_arr[i];
  
      // if we found a operator then pop two numbers, perform the operation and push it into the stack again
      if (operator_list.has(exp)){ 
        const a = stack.pop();
        const b = stack.pop();
  
        let res = -1;
  
        switch(exp){
          case '+': res = a+b; break;
          case '-': res = a-b; break;
          case '/': res = a/b; break;
          case '*': res = a*b; break;
          default: throw new Error('Non-Arithmetic operator found'); // we want to have a default case just in case some unknown operator gets added
        }
  
        stack.push(res);
      }
      else{
        stack.push(parseFloat(exp));
      }
    }
  
    return stack.pop();
  }
  
  