import Pyro4

# Prompt the user to input the URI of the Pyro4 server
uri = input("Enter the URI of the server: ")

# Create a Pyro4 Proxy object using the provided URI
concatenator = Pyro4.Proxy(uri)

# Prompt the user to input two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the remote method 'concatenate' on the server object with the provided strings
result = concatenator.concatenate(str1, str2)

# Print the concatenated result returned from the server
print("Concatenated string:", result)
