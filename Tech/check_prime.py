import cgi
import math

# Enable HTML output for the CGI script
print("Content-type: text/html\n")

# Get the number from the URL
form = cgi.FieldStorage()
number = form.getvalue("number")

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

try:
    # Convert input to integer
    num = int(number)
    # Check if the number is prime and display the result
    if is_prime(num):
        result = f"<p>{num} is a prime number.</p>"
    else:
        result = f"<p>{num} is not a prime number.</p>"
except (ValueError, TypeError):
    result = "<p>Please enter a valid integer.</p>"

# Print the result as HTML
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Prime Checker Result</title>
</head>
<body>
    <h1>Prime Number Checker Result</h1>
    {result}
    <a href="input.html">Check another number</a>
</body>
</html>
""")
