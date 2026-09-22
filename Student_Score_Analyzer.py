class Student_Score_Analyzer:

    def __init__(self, students):
        self.students = students
        self.averages = []

    def show_all_student(self):

        for i in self.students:
            print(i["name"])
            
            

    def show_student_result(self):

        self.averages=[]
        
        for j in self.students:
            container = 0
            for i in j["scores"]:
                container += i
            avg = container / len(j["scores"])
            print(f" {j['name']} : {avg} {"Pass" if avg>=12 else "Fail"} ")

            self.averages.append({"name": j["name"], "average": avg})
            
            
            
            
            

    def show_Best_student(self):
      
        if not  self.averages:
           print("Please calculate averages first.")
      
        else:
          
          maximum = -1

          for av in self.averages:
              if av["average"] > maximum:
                  maximum = av["average"]
                  student = av["name"]

          print(f" Best student: {student} {maximum}")





    def show_Worst_student(self):
        if not self.averages:
          print("Please calculate averages first.")
          
        else:
          
          minimum = 21

          for av in self.averages:
              if av["average"] < minimum:
                  minimum = av["average"]
                  student = av["name"]

          print(f" Worst student: {student} {minimum}")
          



    def search_student(self, name):

        found = False

        for n in self.students:

            if name == n["name"]:
                found = True
                print(f"{n["name"]} is in the list and his/her scores: ")

                for j in n["scores"]:
                    print(j, end=" ")
                break

        if not found:
            print(" it is not in the list ")








dataset = Student_Score_Analyzer(
    [
        {"name": "Ali", "scores": [15, 18, 12, 20]},
        {"name": "Sara", "scores": [19, 17, 20, 18]},
        {"name": "Reza", "scores": [10, 12, 14, 11]},
        {"name": "Mina", "scores": [16, 15, 18, 17]},
    ]
)







while True:

    print("""
        
  ===== Student Score Analyzer =====

  1. Show all students
  2. Calculate and Show student average and pass/fail student
  3. Show best student
  4. Show worst student
  5. Search student
  6. Exit
  """)

    choose = input(" choose a number : ")

    if choose == "1":
        dataset.show_all_student()

    elif choose == "2":
        dataset.show_student_result()

    elif choose == "3":
        dataset.show_Best_student()

    elif choose == "4":
        dataset.show_Worst_student()

    elif choose == "5":
        name = input(
            " enter a name for searching in a list wheather is in a list or not: "
        ).capitalize()
        dataset.search_student(name)

    elif choose == "6":
        print(" you exit ")
        break
