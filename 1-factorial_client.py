import xmlrpc.client

# Function to call the factorial function on the server
def calculate_factorial(n):
    # Create a proxy object for accessing the XML-RPC server
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    # Call the remote factorial function on the server
    return proxy.factorial(n)

if __name__ == "__main__":
    # Ask the user to enter a number for which to calculate the factorial
    number = int(input("Enter a number to calculate factorial: "))
    # Call the calculate_factorial function to get the result from the server
    result = calculate_factorial(number)
    # Print the result
    print(f"The factorial of {number} is: {result}")

