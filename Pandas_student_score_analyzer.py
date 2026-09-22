import pandas as pd


class Student_Score_Analyzer:

    def __init__(self):
        pass


    def show_all_student(self):
        print(df["name"])
        


    def show_student_result(self):

        df["average"] = df["scores"].apply(lambda x: sum(x) / len(x))

        df["Pass/Fail"] = df["average"].apply(
            lambda x: "Passed" if x >= 12 else "Failed"
        )
        
        print(df)
        
        

    def show_Best_student(self):
        try:
            print(f"Best student average : {df["average"].max()}")
            
        except KeyError:
          print(" first Calculate the students scores average\n and after that you can use button 3")
          
            
            


    def show_Worst_student(self):
        try:
            print(f"Worst student average : {df["average"].min()}")

        except KeyError:
            print(" first Calculate the students scores average \n and after that you can use button 4")
            
            




    def show_Total_score(self):
        df["Total_score"] = df["scores"].apply(lambda x: sum(x))

        print(df)
    
    
    
    
    
    def show_sort_student_by_averages(self):
      try:
        print(df.sort_values("average" , ascending=False , ignore_index=True))
        
  
      except KeyError:
        print(" first Calculate the students scores average\n and after that you can use button 6")
        
        
        
        
    def show_the_level_of_student(self) : 
       try:
         df["Student_level"] = df["average"].apply(
           lambda x : "Excellent" if x>=18.00
           else "Good" if x>=16.00
           else "Average" if x>= 14.00
           else "Weak"
           )
         
         print(df)
            
       except KeyError:
              print(" first Calculate the students scores average\n and after that you can use button 7")
              
              
              
              
    def show_the_whole_chart_information(self):
      df.info()
      print()
      print(df.describe())
      
      
      
    def Show_each_student_scores(self):
      print(df.loc[0: , ["name" , "scores"]])
      

      
      
      
    


df = pd.DataFrame(
    {
        "name": ["Ali", "Sara", "Reza", "Mina"],
        "scores": [
            [10, 18, 8, 9],
            [19, 17, 20, 18],
            [10, 12, 14, 11],
            [16, 15, 18, 17],
        ],
    }
)


dataset = Student_Score_Analyzer()


print(df)





while True:

    print("""
        
  ===== Student Score Analyzer =====

  1. Show all students
  
  2. Calculate and Show student average and pass/fail student
  
  3. Show best student average
  
  4. Show worst student average
  
  5. Show total scores of each student
  
  6. Show_sortd_student_by_averages
  
  7. Show the  level of students
  
  8. Show the whole chart information
  
  9. Show each student scores
  
  10. Exit
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
      dataset.show_Total_score()
        
    elif choose == "6":
      dataset.show_sort_student_by_averages()
        
    elif choose == "7":
      dataset.show_the_level_of_student()
        
    
    elif choose == "8":
      dataset.show_the_whole_chart_information()
      
    
    elif choose == "9" :
      dataset.Show_each_student_scores()
      
      
    elif choose == "10":
        print(" you exit ")
        break
      
  
