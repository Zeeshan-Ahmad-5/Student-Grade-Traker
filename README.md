# Student Grade Tracker

The **Student Grade Tracker** is a simple Python command-line program that allows users to track students' grades across multiple subjects. It enables adding subjects, recording multiple grades for each subject, calculating average grades, and displaying a comprehensive summary.

---

## Features
- **Add Subjects:** Prompt users to enter the names of subjects.
- **Record Grades:** For each subject, users can add multiple grades between 0 and 100.
- **Calculate Averages:** Automatically calculates the average for each subject and an overall average across all subjects.
- **Display Summary:** Presents a summary of all subjects, grades, and their corresponding averages.
- **User-Friendly Prompts:** Guides users with clear instructions and validations to avoid incorrect inputs.

---

## How to Use

1. **Run the Program:**
   Execute the script in a terminal:
   ```bash
   python grade_tracker.py
   ```

2. **Add Subjects:**
   - Enter the name of a subject when prompted.
   - Type `done` to finish adding subjects.

3. **Add Grades:**
   - For each subject, enter grades one by one (from 0 to 100).
   - Type `done` to finish adding grades for a subject.

4. **View Summary:**
   - The program will display each subject with its grades and average.
   - It also shows the overall average across all subjects.

5. **Continue or Exit:**
   - After viewing the summary, you can choose to continue adding more data or exit the program.

---

## Example Output
```
Welcome to the Student Grade Tracker!
You can add subjects and grades, and view averages.

Enter the subject name (or 'done' to finish): Math

Entering grades for Math. Enter 'done' to finish adding grades for this subject.
Enter a grade for Math (0-100, or 'done' to finish): 85
Grade 85.0 added for Math.
Enter a grade for Math (0-100, or 'done' to finish): 90
Grade 90.0 added for Math.
Enter a grade for Math (0-100, or 'done' to finish): done

--- Grade Summary ---
Math: Grades = [85.0, 90.0], Average = 87.50

Overall Average Across All Subjects: 87.50

Would you like to add more subjects or grades? (yes/no): no

Thank you for using the Student Grade Tracker! Goodbye.
```

---

## Requirements
- Python 3.x

No additional libraries are required.

---

## Error Handling
- **Invalid Inputs:** If non-numeric input is given when a grade is expected, the program will prompt the user again.
- **Grade Validation:** Grades must be between 0 and 100.
- **Subject Validation:** Subject names cannot be empty.
- **Keyboard Interruptions:** The program handles unexpected keyboard interruptions gracefully.

---

## Contributing
Feel free to fork this repository and submit pull requests to enhance the program!

---

## License
This project is licensed under the MIT License.

---

## Author
Zeeshan Ahmad

