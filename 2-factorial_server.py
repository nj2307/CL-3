import xmlrpc.server

# Function to calculate factorial
def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive calculation of factorial

# Create an XML-RPC server
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# Register the factorial function to be exposed as an XML-RPC method
server.register_function(factorial, "factorial")

print("Server running...")

# Start the server and keep it running indefinitely
server.serve_forever()
