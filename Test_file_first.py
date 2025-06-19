# Import 'os' for OS-dependent functionality, used for path manipulations (saving output file).
import os

# Import 'diagrams' for cloud system architecture diagrams.
# Currently unused; consider removal if not planned for future use.
import diagrams

# Initial test print or part of script's startup.
# Git Commit Check 2
# Testing commit 6th Commit

print("hi there")

def get_valid_float_input(prompt_message: str) -> float:
  """
  Prompts for input, re-prompts until a valid float is entered.
  Args: prompt_message. Returns: valid float.
  """
  while True:
    try:
      user_input_str = input(prompt_message)
      return float(user_input_str)
    except ValueError:
      print("Invalid input. Please enter a valid number (e.g., 10, -5.5, or 3.14).")
    except KeyboardInterrupt:
      print("\nInput cancelled by user. Exiting number input.")
      raise # Re-raise KeyboardInterrupt for main function handling.

def add_numbers_from_user_input():
  """
  Prompts for two numbers, validates input, adds them, prints sum to console,
  and writes result to 'addition_result.txt' in script's directory.
  """
  print("\nLet's add two numbers!")
  try:
    # Get valid float input for the first number.
    num1 = get_valid_float_input("Enter the first number: ")

    # Get valid float input for the second number.
    num2 = get_valid_float_input("Enter the second number: ")

    # Calculate sum and prepare result message.
    total_sum = num1 + num2
    result_message = f"The sum of {num1} and {num2} is: {total_sum}"

    # Print result to console.
    print(result_message)

    # --- Write the result to a file ---
    output_filename = "addition_result.txt"
    try:
      # Determine script directory and output file path using __file__.
      script_directory = os.path.dirname(os.path.abspath(__file__))
      output_filepath = os.path.join(script_directory, output_filename)

      # Open/create/overwrite 'addition_result.txt' using 'with' for auto-close.
      with open(output_filepath, "w") as file:
        file.write(result_message + "\n") # Write result with a newline.

      print(f"Result successfully written to: {output_filepath}")

    except (IOError, OSError) as file_error:
      # Handle IOError/OSError during file operations.
      print(f"Error: Could not write result to file '{output_filename}'. Reason: {file_error}")
    except NameError:
      # Handle NameError if __file__ is undefined (e.g., in some interactive environments).
      print(f"Error: Could not determine script directory to save '{output_filename}'.")
      print("The result was not saved to a file.")

  except KeyboardInterrupt:
    # Handle user cancellation (Ctrl+C).
    print("Addition process cancelled.")
  except Exception as e:
    # Handle other unexpected errors.
    print(f"An unexpected error occurred during the addition process: {e}")

# Example call to add_numbers_from_user_input for script execution.
if __name__ == "__main__":
  add_numbers_from_user_input()