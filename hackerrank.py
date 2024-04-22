"""When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains , the number of testcases.
Each testcase contains  lines, representing time"""

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Parse timestamps
    dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    # Calculate time difference in seconds
    delta_seconds = abs((dt1 - dt2).total_seconds())
    
    return str(int(delta_seconds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Program-2
def average_marks(student_marks, query_name):
    # Check if the query_name exists in the student_marks dictionary
    if query_name in student_marks:
        # Calculate the average of marks for the given student
        average = sum(student_marks[query_name]) / len(student_marks[query_name])
        # Print the average marks rounded to 2 decimal places
        print("{:.2f}".format(average))
    else:
        print("Student {} not found.".format(query_name))

if __name__ == '__main__':
    n = int(input())  # Number of students' records
    student_marks = {}  # Dictionary to store student names and marks

    # Read student records
    for _ in range(n):
        line = input().split()
        name = line[0]
        marks = list(map(float, line[1:]))  # Convert marks to float
        student_marks[name] = marks

    query_name = input()  # Name of the student to query
    average_marks(student_marks, query_name)
