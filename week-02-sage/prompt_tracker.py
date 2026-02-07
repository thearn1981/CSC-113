# We'll keep the filename in a variable so it's easy to change later
FILENAME = "my-prompts.txt"

def main():
    ALLOWED_CATEGORIES = ["learning", "creating", "evaluating", "other"]
    # This 'while True' loop keeps the program running until the user chooses to quit
    while True:
        print("\n--- PROMPT TRACKER MENU ---")
        print("1. Add Prompt")
        print("2. View Prompts")
        print("3. Search Prompts")
        print("4. Quit")
        # Here is your requested change! 
        # Using "-" * 30 is a Python trick that repeats the dash 30 times.
        print("-" * 27)
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("\n>> ADDING NEW PROMPT")
            text = input("Enter the prompt text: ")
            
            # --- NEW CATEGORY VALIDATION LOGIC ---
            # We start an inner loop that only stops when we get a valid category
            while True:
                # We show the options clearly so the student doesn't have to guess
                cat_options = "/".join(ALLOWED_CATEGORIES)
                category = input(f"Category ({cat_options}): ").lower().strip()

                if category in ALLOWED_CATEGORIES:
                    # If it's valid, we 'break' out of THIS inner loop
                    break
                else:
                    # If not, we give them a helpful error and the loop repeats
                    print(f"(!) Invalid category. Please type exactly: {cat_options}")
            
            note = input("When should you use this? ")

            with open(FILENAME, "a") as file:
                file.write(f"{text}|{category}|{note}\n")
            print("...Success! Prompt saved.")

        elif choice == "2":
            # --- VIEW PROMPTS ---
            print("\n--- ALL SAVED PROMPTS ---")
            try:
                with open(FILENAME, "r") as file:
                    # We read the file line by line
                    for line in file:
                        # .strip() removes the invisible newline character at the end
                        # .split("|") turns the string back into a list [text, category, note]
                        parts = line.strip().split("|")
                        
                        # We make sure the line has all 3 parts before printing
                        if len(parts) == 3:
                            p_text, p_cat, p_note = parts
                            print(f"[{p_cat.upper()}] {p_text}")
                            print(f"   Note: {p_note}")
                            print("-" * 20)
            except FileNotFoundError:
                print("No prompts found yet. Try adding one first!")

        elif choice == "3":
            # --- SEARCH PROMPTS ---
            keyword = input("Enter a keyword to search for: ").lower()
            found = False
            
            try:
                with open(FILENAME, "r") as file:
                    for line in file:
                        # Check if the keyword exists anywhere in that line
                        if keyword in line.lower():
                            parts = line.strip().split("|")
                            if len(parts) == 3:
                                p_text, p_cat, p_note = parts
                                
                                # --- THE FIX IS HERE ---
                                # I'm adding the note to the output so you actually see it!
                                print(f"\nMATCH FOUND:")
                                print(f"Category: {p_cat.upper()}")
                                print(f"Prompt:   {p_text}")
                                print(f"Note:     {p_note}")
                                print("-" * 20)
                                found = True
                
                if not found:
                    print(f"No prompts matched '{keyword}'.")
            except FileNotFoundError:
                print("No file found to search. Add a prompt first!")
        elif choice == "4":
            # --- QUIT ---
            print("Goodbye! Happy prompting.")
            break # This breaks the 'while' loop and ends the program

        else:
            print("Invalid choice, please try again.")

# This line tells Python to run our main function
if __name__ == "__main__":
    main()