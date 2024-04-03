import sys

# Check if at least one number is provided
if len(sys.argv) < 2:
    print("Please provide numbers as arguments to sum.")
    sys.exit(1)  # Exit with an error status code

try:
    # Convert arguments to floats and sum them
    total = sum(map(float, sys.argv[1:]))
    print(f"Sum: {total}")
except ValueError:
    print("All arguments must be valid numbers.")
