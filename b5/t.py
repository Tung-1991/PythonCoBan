print("Chương trình quản lý sinh viên Python")


def addStudent():
    """Hàm thêm một sinh viên"""

    print("*** THÊM SINH VIÊN ***")

    # Danh sách sinh viên
    global listStudents

    # Cấu trúc lưu trữ một sinh viên
    infor = {
        'id': '',
        'name': ''
    }

    # Nhập ID, có kiểm tra trùng ID thì nhập lại
    print("Nhập ID sinh viên:")
    id = input()

    while True:
        student = findStudent(id)
        if student != False:
            print("ID này đã tồn tại, vui lòng nhập lại:")
            id = input()
        else:
            break

    infor['id'] = id

    # Nhập tên
    print("Nhập tên sinh viên:")
    infor['name'] = input()

    # Lưu vào danh sách sv
    listStudents.append(infor)


def findStudent(id):
    """Hàm tìm một sinh viên"""
    global listStudents
    for i in range(0, len(listStudents)):
        if listStudents[i]['id'] == id:
            # Trả về mảng gồm 2 phần tử,
            # 0 là vị trí tìm thấy và 1 là dữ liệu
            return [i, listStudents[i]]
    return False


def deleteStudent():
    """Hàm xóa sih viên"""
    print("*** XÓA SINH VIÊN ***")
    print("Nhập ID sinh viên cần xóa:")
    id = input()

    global listStudents
    student = findStudent(id)

    if student != False:
        listStudents.remove(student[1])
        print("Xóa sinh viên thành công")
    else:
        print("Không tìm thấy sinh viên cần xóa")


def showStudents():
    """Hàm hiển thị danh sách sv"""
    print("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***")
    global listStudents
    for i in range(0, len(listStudents)):
        print("[", listStudents[i]['id'], "]", "[", listStudents[i]['name'], "]", )


def editStudent():
    """Hàm sửa sinh viên"""
    print("*** SỬA THÔNG TIN SINH VIÊN ***")
    global listStudents
    print("Nhập ID sinh viên cần sửa")
    id = input()
    student = findStudent(id)
    if student == False:
        print("Không tìm thấy sinh viên ", id)
    else:
        print("Nhập tên sinh viên")
        name = input()
        student[1]['name'] = name
        listStudents[student[0]] = student[1]


# CHƯƠNG TRÌNH CHÍNH
listStudents = []
action = 0

while action >= 0:
    if action == 1:
        addStudent()
    elif action == 2:
        deleteStudent()
    elif action == 3:
        editStudent()
    elif action == 4:
        showStudents()

    print("Chọn chức năng muốn thực hiện:")
    print("Nhập 1: Thêm sinh viên")
    print("Nhập 2: Xóa sinh viên")
    print("Nhập 3: Sửa sinh viên")
    print("Nhập 4: Xem danh sách sinh viên")
    print("Nhập 0: Thoát khỏi chương trình")
    action = int(input())
    if action == 0:
        break