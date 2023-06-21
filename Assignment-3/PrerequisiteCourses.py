"""
Keshav Shah

Question 10: Prerequisite Courses
Given a list of courses that a student needs to take to complete their major and a map of courses to their
prerequisites, return a valid order for them to take their courses assuming they only take one course for
their major at once.

Depth-First Search

Time Complexity: O(V + E) (visit every course and its prerequisites)
Space Complexity: O(V + E) (store visited courses in a set)

Process:
    - Create mapping to store all courses and its prerequisites
    - Add the visited courses to a set to keep track and also do the same for a set
      that represents the path
    - Utilize dfs to locate prerequisite classes and then return the order of the classes

Time Spent: 39 minutes
"""

def prerequisite_courses(courses, prereqs):
    # ensure all courses are in prereqs dictionary
    for c in courses:
        if c not in prereqs:
            prereqs[c] = []

    order = []
    path = set()
    visited = set()

    def dfs(course):
        # return if course has already been visited
        if course in path or course in visited:
            return

        visited.add(course)
        path.add(course)

        # visit prereq courses before adding the current course to the order
        for pre in prereqs[course]:
            dfs(pre)

        order.append(course)
        path.remove(course)

    for cour in courses:
        dfs(cour)

    return order

def main():
    courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    prereqs = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"],
                "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }

    print(prerequisite_courses(courses, prereqs))
    # ['Intro to Programming', 'Data Structures', 'Advanced Algorithms', 'Operating Systems', 'Databases']
    # Correct Output

    courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature",
                "Plays & Screenplays"]
    prereqs2 = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"],
                 "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }

    print(prerequisite_courses(courses2, prereqs2))
    # ['Intro to Writing', 'Contemporary Literature', 'Ancient Literature', 'Comparative Literature',
    # 'Plays & Screenplays']
    # Correct Output

    courses3 = ["Math 101", "Math 102", "Math 212"]
    prereqs3 = { "Math 101": [], "Math 102": ["Math 101"], "Math 212": ["Math 101", "Math 102"] }

    print(prerequisite_courses(courses3, prereqs3))
    # ['Math 101', 'Math 102', 'Math 212']
    # Correct Output

main()
