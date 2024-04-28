import Pyro4

# Expose the StringConcatenator class to make its methods available for remote invocation
@Pyro4.expose
class StringConcatenator:
    # Method to concatenate two strings
    def concatenate(self, str1, str2):
        return str1 + str2

# Create a Pyro4 daemon
daemon = Pyro4.Daemon()

# Register the StringConcatenator class with the Pyro4 daemon
uri = daemon.register(StringConcatenator)

# Print the URI of the server, which clients will use to connect to it
print("Server URI:", uri)

# Enter the request loop to keep the server running and responding to client requests
daemon.requestLoop()
