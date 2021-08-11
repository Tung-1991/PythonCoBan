#nhap tu dien voi key va value tu ban phim nhan K de dung lai
d = {}
kt = 0
while kt != "k":
    kt = str(input("an k de dung: "))
    if (kt == "k"):
        print("ket thuc")
    else:
        k = str(input("nhap Key: "))
        v = str(input("nhap Value: "))
        D[k]=v
print("tu dien",d)


#nhap value voi key cho truoc
class_list = []
while (True):
    name = input("Give the name of the user you want to add: ")
    homework = [int(i) for i in input("Homework marks (seperated by spaces): ").split(" ")]
    quizzes = [int(i) for i in input("Quiz marks (seperated by spaces): ").split(" ")]
    tests = [str(i) for i in input("Test marks (seperated by spaces): ").split(" ")]
    class_list.append({
        "name": name,
        "homework": homework,
        "quizzes": quizzes,
        "tests": tests
    })
    cont = input("Want to add another? (Y/N)")
    if cont == "N":
        break;
print(class_list)