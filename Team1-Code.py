import xlrd
def code():
   
    wb = xlrd.open_workbook('Team1-Table.xls')
    sh = wb.sheet_by_index(0)
    x = 16
    y = 64
    my_file = open('TextInput.txt')
    myString = my_file.read()
    characters = myString
    Char2Bin = {}
    for i in range(x):
        char = sh.cell(i,0).value
        binVal = sh.cell(i,1).value
        Char2Bin[char] = binVal
       
    for i in range(y):
        char2 = sh.cell(i,2).value
        if char2 == "\\n":
            char2 = "\n"
        binVal2 = sh.cell(i,3).value
        Char2Bin[char2] = binVal2
   
    binString = ""
    check = False
    for i in range(len(characters)):
        if check:
            check = False
            continue
        if i != len(characters) - 1:
            if characters[i:i+2] in Char2Bin:
                binString += Char2Bin[characters[i:i+2]]
                check = True
            else:
                binString += Char2Bin[characters[i]]
        else:
            binString += Char2Bin[characters[i]]
       

    with open("BinOutput.txt", "w") as f:
        f.write(str(len(binString))+"."+binString)
code()