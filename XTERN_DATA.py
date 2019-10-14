file = open("XTERN_DATA.txt", "r")
contents = file.readlines()
file.close()

for i in range(len(contents)):
    contents[i] = contents[i].strip("\n")


##This is as far as we have gotten in class so far, I still have 8 weeks left, then another Python class next semester.
##So I am going to show a pseudo code for what I need to do:

##First I need to find the most popular X and Y coordinate

def count_x_cord(cord, contents):
    cord_count_x = 0
    for i in range(len(contents)):
        if round(contents[i], 3) == round(cord, 3):
            cord_count_x += 1
            print(cord_count_x)

def count_y_cord(cord, contents):
    cord_count_y = 0
    for i in range(len(contents)):
        if round(contents[i], 3) == round(cord, 3):
            cord_count_y += 1
            print(cord_count_y)

for i in range(len(contents)):
    count_x_cord(i, contents)
    count_y_cord(i, contents)
