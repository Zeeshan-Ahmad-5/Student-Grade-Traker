def initialize_grades():
    """Initialize an empty dictionary to store subjects and grades."""
    global grades
    grades = {}  # Dictionary to store subjects and their grades (e.g., {"Math": [90, 85], "Science": [88, 92]})

def add_subject():
    """Prompt the user to add a subject and grades."""
    global grades
    while True:
        try:
            subject = input("\nEnter the subject name (or 'done' to finish): ").strip().capitalize()
            if subject.lower() == 'done':
                if not grades:
                    print("No subjects added yet. Please add at least one subject.")
                    continue
                break
            if not subject:
                raise ValueError("Subject name cannot be empty!")
            if subject in grades:
                print(f"Subject '{subject}' already exists. You can add grades to it.")
            else:
                grades[subject] = []
            add_grades(subject)
        except KeyboardInterrupt:
            print("\nInput interrupted by user. Stopping subject entry.")
            break
        except Exception as e:
            print(f"Error adding subject: {e}")

def add_grades(subject):
    """Prompt the user to add grades for a specific subject."""
    global grades
    print(f"\nEntering grades for {subject}. Enter 'done' to finish adding grades for this subject.")
    while True:
        try:
            grade_input = input(f"Enter a grade for {subject} (0-100, or 'done' to finish): ").strip().lower()
            if grade_input == 'done':
                if not grades[subject]:
                    print(f"No grades added for {subject}. Adding at least one grade is recommended.")
                break
            grade = float(grade_input)
            if not (0 <= grade <= 100):
                raise ValueError("Grade must be between 0 and 100!")
            grades[subject].append(grade)
            print(f"Grade {grade} added for {subject}.")
        except ValueError as e:
            if "float" in str(e):
                print("Invalid input: Please enter a number or 'done'.")
            else:
                print(f"Invalid grade: {e}")
        except Exception as e:
            print(f"Error adding grade: {e}")

def calculate_subject_average(subject):
    """Calculate the average grade for a specific subject."""
    global grades
    try:
        subject_grades = grades[subject]
        if not subject_grades:
            return 0.0
        return sum(subject_grades) / len(subject_grades)
    except KeyError:
        print(f"Subject '{subject}' not found!")
        return 0.0
    except Exception as e:
        print(f"Error calculating average for {subject}: {e}")
        return 0.0

def calculate_overall_average():
    """Calculate the overall average across all subjects."""
    global grades
    try:
        all_grades = [grade for subject_grades in grades.values() for grade in subject_grades]
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)
    except Exception as e:
        print(f"Error calculating overall average: {e}")
        return 0.0

def display_grades():
    """Display all subjects, their grades, and averages."""
    global grades
    try:
        if not grades:
            print("\nNo grades to display.")
            return
        print("\n--- Grade Summary ---")
        for subject, subject_grades in grades.items():
            avg = calculate_subject_average(subject)
            print(f"{subject}: Grades = {subject_grades}, Average = {avg:.2f}")
        overall_avg = calculate_overall_average()
        print(f"\nOverall Average Across All Subjects: {overall_avg:.2f}")
    except Exception as e:
        print(f"Error displaying grades: {e}")

def main():
    """Main function to run the grade tracker."""
    initialize_grades()  # Initialize the grades dictionary
    print("Welcome to the Student Grade Tracker!")
    print("You can add subjects and grades, and view averages.")

    while True:
        try:
            add_subject()  # Add subjects and grades
            display_grades()  # Display the summary

            # Ask if the user wants to continue
            play_again = input("\nWould you like to add more subjects or grades? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("\nThank you for using the Student Grade Tracker! Goodbye.")
                break
            initialize_grades()  # Reset grades for a new session
        except Exception as e:
            print(f"Unexpected error in main loop: {e}")
            break

if __name__ == "__main__":
    main()