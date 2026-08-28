# 27. Draw a horizontal/vertical bar chart using user input.
def hor_vert_bar():
    import matplotlib.pyplot as plt
    subjects = []
    marks = []
    for i in range(3):
        sub = input("Enter the subjects name: ")
        mark = int(input("Enter the marks: "))
        subjects.append(sub)
        marks.append(mark)

    plt.bar(subjects, marks, color = 'salmon')
    plt.xlabel('subjects')
    plt.ylabel('marks')
    plt.title("vertical baar chart:")
    plt.show()
hor_vert_bar()