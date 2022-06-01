from openpyxl import Workbook #importing our library

your_workbook = Workbook() #creating the workbook
sheet = your_workbook.active
sheet["A1"] = "Hello"
sheet["B1"] = "Sectionio!"
sheet["A2"] = "EngEd"
sheet["B2"] = "is!"
sheet["C2"] = "Two"

your_workbook.save(filename="hello_world_openpyxl.xlsx") #saving the file with the 'xlsx' excel extension
