# Import the 'os' module, which provides a way of using operating system dependent functionality.
# It's used here for path manipulations to save the output file.
import os

# Import the 'diagrams' module. This library is used for creating cloud system architecture diagrams.
# This module is currently imported but not used in this script.
# Consider removing it if it's not planned for future use to keep the script clean.
import diagrams

# Print a simple greeting message to the console.
# This could be an initial test print or part of the script's intended startup.
# Git Commit Check 2
print("hi there")

def get_valid_float_input(prompt_message: str) -> float:
  """
  Prompts the user for input using prompt_message and continues to ask
  until a valid floating-point number is entered.

  Args:
    prompt_message: The message to display to the user when asking for input.

  Returns:
    The valid floating-point number entered by the user.
  """
  while True:
    try:
      user_input_str = input(prompt_message)
      return float(user_input_str)
    except ValueError:
      print("Invalid input. Please enter a valid number (e.g., 10, -5.5, or 3.14).")
    except KeyboardInterrupt:
      print("\nInput cancelled by user. Exiting number input.")
      raise # Re-raise to allow the main function to handle or exit gracefully

def add_numbers_from_user_input():
  """
  Prompts the user to enter two numbers, ensuring valid numeric input.
  It then adds them, prints the sum to the console, and writes the result
  to a text file named 'addition_result.txt' in the script's directory.
  """
  print("\nLet's add two numbers!")
  try:
    # Get the first number from the user, ensuring it's valid
    num1 = get_valid_float_input("Enter the first number: ")

    # Get the second number from the user, ensuring it's valid
    num2 = get_valid_float_input("Enter the second number: ")

    # Calculate the sum
    total_sum = num1 + num2
    result_message = f"The sum of {num1} and {num2} is: {total_sum}"

    # Print the result to the console for immediate feedback
    print(result_message)

    # --- Write the result to a file ---
    output_filename = "addition_result.txt"
    try:
      # Get the absolute path of the directory where the script is located
      # __file__ is a special variable that holds the path to the current script
      script_directory = os.path.dirname(os.path.abspath(__file__))
      # Construct the full path to the output file
      output_filepath = os.path.join(script_directory, output_filename)

      # Open the file in write mode ('w').
      # This will create the file if it doesn't exist, or overwrite it if it does.
      # Using 'with' ensures the file is properly closed even if errors occur.
      with open(output_filepath, "w") as file:
        file.write(result_message + "\n") # Add a newline for better readability in the file

      print(f"Result successfully written to: {output_filepath}")

    except (IOError, OSError) as file_error:
      # Handle potential errors during file operations (e.g., permission issues)
      print(f"Error: Could not write result to file '{output_filename}'. Reason: {file_error}")
    except NameError:
      # This handles the edge case where __file__ might not be defined (e.g., in some interactive environments)
      print(f"Error: Could not determine script directory to save '{output_filename}'.")
      print("The result was not saved to a file.")


  except KeyboardInterrupt:
    # Handle the case where the user cancels the input process (Ctrl+C)
    # Message for input cancellation is already printed by get_valid_float_input if it originated there
    print("Addition process cancelled.")
  except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred during the addition process: {e}")

# Example of how to call the function:
if __name__ == "__main__":
  add_numbers_from_user_input()