# Question: 
# Grade Calculator
# Write a Python program that calculates the grade of a student based on their scores in different subjects. The program should:
# Ask the user to input scores for 5 subjects.
# Use arithmetic operators to calculate the average score.
# Use conditional statements to determine the grade based on the average:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# Display the average score and the grade.
# Use functions to handle input, calculation, and grade determination.

def input_scores():
    # Function to input scores for 5 subjects from the user.
    scores = []
    for i in range(5):
        score = float(input(f"Enter the score for subject {i+1}: "))
        scores.append(score)
    return scores

def calculate_average(scores):
    # Function to calculate the average of the scores.
    return sum(scores) / len(scores)

def determine_grade(average):
    # Function to determine the grade based on the average score.
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

def main():
    # Main function to run the program.
    scores = input_scores()
    average = calculate_average(scores)
    grade = determine_grade(average)
    print(f"Average Score: {average:.2f}")
    print(f"Grade: {grade}")

# Run the program
main()
