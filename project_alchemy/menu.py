from project_alchemy.crud.grades import (
    get_grades_by_lesson,
    create_grade
)
from project_alchemy.crud.teacher import (
    get_teacher_by_id,
    create_teacher,
    get_teacher_by_credentials
)
from project_alchemy.crud.student import (
    create_student,
    get_student_by_credentials, get_lessons_by_student, get_grades_by_student, get_grades_all
)
from project_alchemy.crud.lessons import (
    create_lesson, get_lessons_by_teacher
)
from project_alchemy.database import Session


def main_menu():
    while True:
        print("\n=== Главное меню ===")
        print("1. Получить учителя по ID")
        print("2. Создать учителя")
        print("3. Создать студента")
        print("4. Создать урок")
        print("5. Выход по имени и паролю")
        print("0. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            teacher_id = int(input("Введите ID учителя: "))
            session = Session()
            result = get_teacher_by_id(session, teacher_id)
            if result:
                print(f"Имя учителя: {result.name} {result.surname}")
                print("Уроки:")
                for lesson in result.lessons:
                    print(f"- {lesson.subject}")
            else:
                print("Учитель не найден!")

        elif choice == "2":
            name = input("Введите имя учителя: ")
            surname = input("Введите фамилию учителя: ")
            email = input("Введите email учителя: ")
            password = input("Введите пароль учителя: ")
            session = Session()
            create_teacher(session, name, surname, email, password)
            print("Учитель успешно создан!")

        elif choice == "3":
            name = input("Введите имя студента: ")
            surname = input("Введите фамилию студента: ")
            group = input("Введите группу студента: ")
            email = input("Введите email студента: ")
            password = input("Введите пароль студента: ")
            session = Session()
            create_student(session, name, surname, group, email, password)
            print("Студент успешно создан!")

        elif choice == "4":
            subject = input("Введите предмет урока: ")
            date = input("Введите дату урока (ГГГГ-ММ-ДД): ")
            teacher_id = int(input("Введите ID учителя для урока: "))
            session = Session()
            create_lesson(session, subject, date, teacher_id)
            print("Урок успешно создан!")

        elif choice == "5":
            role = input("Вы учитель или студент? (t/s): ")
            name = input("Введите имя: ")
            password = input("Введите пароль: ")
            session = Session()

            if role.lower() == "t":
                teacher = get_teacher_by_credentials(session, name, password)
                if teacher:
                    while True:
                        print("\n=== Меню учителя ===")
                        print("1. Создать оценку")
                        print("2. Посмотреть оценку")
                        print("3. Расписание уроков")
                        print('4. Посмотреть оценки всех студентов')
                        print("0. Вернуться в главное меню")

                        teacher_choice = input("Введите ваш выбор: ")

                        if teacher_choice == "1":
                            student_id = int(input("Введите ID студента: "))
                            lesson_id = int(input("Введите ID урока: "))
                            grade_value = int(input("Введите значение оценки: "))
                            comments = input("Введите комментарии к оценке: ")
                            create_grade(session, student_id, lesson_id, grade_value, comments)
                            print("Оценка успешно создана!")

                        elif teacher_choice == "2":
                            student_id = int(input("Введите ID студента: "))
                            lesson_id = int(input("Введите ID урока: "))
                            result = get_grades_by_lesson(session, lesson_id, student_id)
                            if result:
                                print(f"Оценка студента {student_id} по уроку {lesson_id}: {result.grade_value}")
                            else:
                                print("Оценка не найдена!")

                        elif teacher_choice == "3":
                            teacher_id = teacher.teacher_id
                            lessons = get_lessons_by_teacher(session, teacher_id)
                            if lessons:
                                print("Расписание уроков:")
                                for lesson in lessons:
                                    print(f"{lesson.date} - {lesson.subject}")
                            else:
                                print("У учителя пока нет уроков!")

                        elif choice == "3":
                            session = Session()
                            all_grades = get_grades_all(session)
                            if all_grades:
                                print("Оценки всех студентов:")
                                for grade in all_grades:
                                    print(
                                        f"Студент ID: {grade.student_id}, "
                                        f"Урок ID: {grade.lesson_id}, "
                                        f"Оценка: {grade.grade_value}")

                        elif teacher_choice == "0":
                            break

                        else:
                            print("Неверный выбор. Пожалуйста, попробуйте снова.")

                else:
                    print("Неверное имя или пароль!")

            elif role.lower() == "s":
                student = get_student_by_credentials(session, name, password)
                if student:
                    while True:
                        print("\n=== Меню студента ===")
                        print("1. Посмотреть оценки")
                        print("2. Расписание уроков")
                        print('3. Посмотреть оценки всех студентов')
                        print("0. Вернуться в главное меню")

                        student_choice = input("Введите ваш выбор: ")

                        if student_choice == "1":
                            student_id = student.student_id
                            grades = get_grades_by_student(session, student_id)
                            if grades:
                                print("Оценки:")
                                for grade in grades:
                                    print(f"Урок {grade.lesson_id}: {grade.grade_value}")
                            else:
                                print("У студента пока нет оценок!")

                        elif student_choice == "2":
                            lessons = get_lessons_by_student(session, student_id)
                            if lessons:
                                print("Расписание уроков:")
                                for lesson in lessons:
                                    print(f"{lesson.date} - {lesson.subject}")
                            else:
                                print("У студента пока нет уроков!")

                        elif choice == "3":
                            session = Session()
                            all_grades = get_grades_all(session)
                            if all_grades:
                                print("Оценки всех студентов:")
                                for grade in all_grades:
                                    print(
                                        f"Студент ID: {grade.student_id}, "
                                        f"Урок ID: {grade.lesson_id}, "
                                        f"Оценка: {grade.grade_value}")


                            else:
                                print("Оценки студентов не найдены!")

                        elif student_choice == "0":
                            break

                        else:
                            print("Неверный выбор. Пожалуйста, попробуйте снова.")

                else:
                    print("Неверное имя или пароль!")

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main_menu()
