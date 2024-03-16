def get_user_input(message):
  """Prompts the user for input with a given message"""
  while True:
    try:
      value = float(input(message))
      return value
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  # Get user input for ingredients
  flour_cups = get_user_input("Enter amount of flour (cups): ")
  sugar_cups = get_user_input("Enter amount of sugar (cups - white or brown): ")
  butter_sticks = get_user_input("Enter number of sticks of butter (softened): ")
  eggs = get_user_input("Enter number of eggs: ")
  chocolate_chips_cups = get_user_input("Enter amount of chocolate chips (cups): ")

  # Print recipe steps
  print("\n**SuperDuper Cookies Recipe**")
  
  print("\n1. Preheat oven to 375 degrees Fahrenheit.")
  print("2. Cream together", butter_sticks, "sticks of softened butter and", sugar_cups, "cups of sugar until light and fluffy.")
  print("3. Beat in", eggs, "eggs one at a time.")
  print("4. In a separate bowl, whisk", flour_cups, "cups of flour.")
  print("5. Gradually add the dry ingredients to the wet ingredients, mixing until just combined.")
  print("6. Fold in", chocolate_chips_cups, "cups of chocolate chips.")
  print("7. Line baking sheets with parchment paper.")
  print("8. Scoop dough balls onto baking sheets, leaving space for spreading.")
  print("9. Bake for 10-12 minutes, or until golden brown.")
  print("10. Let cookies cool on baking sheets for a few minutes before transferring to a wire rack to cool completely.")
  print("\nEnjoy your delicious SuperDuper Cookies!")

if __name__ == "__main__":
  main()