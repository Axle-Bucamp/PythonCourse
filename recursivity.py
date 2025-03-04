"""
recursivity.py: Explanation and demonstration of recursion in Python

This module covers:
1. Basic concept of recursion
2. Simple recursion examples
3. Tail recursion
4. Complex recursive algorithms
5. Advantages and pitfalls of recursion

Each concept is explained with comments and demonstrated with code examples.
"""

def factorial(n):
    """
    Calculate the factorial of a number using simple recursion.
    
    Args:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_tail(n, accumulator=1):
    """
    Calculate the factorial of a number using tail recursion.
    
    Args:
    n (int): The number to calculate the factorial of.
    accumulator (int): The accumulated product (default is 1).
    
    Returns:
    int: The factorial of n.
    """
    if n == 0 or n == 1:
        return accumulator
    else:
        return factorial_tail(n - 1, n * accumulator)

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    """
    Perform an inorder traversal of a binary tree using recursion.
    
    Args:
    root (TreeNode): The root of the binary tree.
    
    Returns:
    list: The values of the nodes in inorder.
    """
    if root is None:
        return []
    return (inorder_traversal(root.left) + 
            [root.value] + 
            inorder_traversal(root.right))

def demonstrate_recursion():
    """Demonstrate various recursive functions and discuss recursion."""
    print("1. Simple Recursion - Factorial:")
    print(f"Factorial of 5: {factorial(5)}")
    
    print("\n2. Tail Recursion - Factorial:")
    print(f"Factorial of 5 (tail recursion): {factorial_tail(5)}")
    
    print("\n3. Complex Recursion - Fibonacci:")
    print(f"10th Fibonacci number: {fibonacci(10)}")
    
    print("\n4. Tree Traversal - Inorder:")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(f"Inorder traversal: {inorder_traversal(root)}")
    
    print("\n5. Advantages and Pitfalls of Recursion:")
    print("Advantages:")
    print("- Can lead to clean, elegant code for problems that have a recursive nature")
    print("- Often mirrors the mathematical definition of the problem")
    print("- Useful for tree-like structures and divide-and-conquer algorithms")
    
    print("\nPitfalls:")
    print("- Can lead to stack overflow for deep recursions")
    print("- May have higher memory usage compared to iterative solutions")
    print("- Can be slower due to function call overhead")
    print("- Might be less intuitive for some problems, leading to harder-to-understand code")
    
    print("\nNote: In Python, tail recursion is not optimized, so deep recursions can still lead to stack overflow.")

if __name__ == "__main__":
    demonstrate_recursion()