import re
import xlsxwriter

frame = "Motor_20"
snapshots = [
    "d:\\SAFE handling\\VF8\\Dani_TBAD\\verif_reproduction\\retest_with_VF8FG002580\\" + frame + "_snapshot1.txt",
    "d:\\SAFE handling\\VF8\\Dani_TBAD\\verif_reproduction\\retest_with_VF8FG002580\\" + frame + "_snapshot2.txt",
    "d:\\SAFE handling\\VF8\\Dani_TBAD\\verif_reproduction\\retest_with_VF8FG002580\\" + frame + "_snapshot3.txt",
    "d:\\SAFE handling\\VF8\\Dani_TBAD\\verif_reproduction\\retest_with_VF8FG002580\\" + frame + "_snapshot4.txt",
    "d:\\SAFE handling\\VF8\\Dani_TBAD\\verif_reproduction\\retest_with_VF8FG002580\\" + frame + "_snapshot5.txt",
    "d:\\SAFE handling\\VF8\\Dani_TBAD\\verif_reproduction\\retest_with_VF8FG002580\\" + frame + "_snapshot6.txt"
]
checkedASAPs = []
asapTime = "\d+\,\d+\ss"

# First timestamp
def appendASAPAndFirstValue(file):
    for i in range(0, len(file)):
        snp = ""
        if str(file[i][re.search(asapTime, file[i]).span()[1] + 1:])[-1:] == '\n':
            snp = file[i][re.search(asapTime, file[i]).span()[1] + 1:-1]
        else:
            snp = file[i][re.search(asapTime, file[i]).span()[1] + 1:]
        checkedASAPs.append(
            {"ASAPNAME" : str(file[i][:re.search(asapTime, file[i]).span()[0]-2]),
            "values" : [int(snp)]}
        )

# Up to the first timestamp
def appendASAPRestValues(file, index):
    for i in range(0, len(file)):
        snp = ""
        if str(file[i][re.search(asapTime, file[i]).span()[1] + 1:])[-1:] == '\n':
            snp = file[i][re.search(asapTime, file[i]).span()[1] + 1:-1]
        else:
            snp = file[i][re.search(asapTime, file[i]).span()[1] + 1:]
        checkedASAPs[i]['values'].append(int(snp))

def writeToExcel():
    workbook = xlsxwriter.Workbook('d:\\SAFE handling\\VF8\\Dani_TBAD\\verif_reproduction\\retest_with_VF8FG002580\\\DAS.xlsx')
    worksheet = workbook.add_worksheet()
    
    for i in range(0, len(checkedASAPs)):
        worksheet.write_string(i+1, 0, checkedASAPs[i]["ASAPNAME"])
        for j in range(0, len(checkedASAPs[i]['values'])):
            worksheet.write_number(i+1, j+1, checkedASAPs[i]["values"][j])
    workbook.close()

# Test the array of dictionaries
def TEST():
    for i in range(0, len(checkedASAPs)):
        print(checkedASAPs[i]["ASAPNAME"]+":")
        print("-------------------------")
        for j in range(0, len(checkedASAPs[i]['values'])):
            print("   " + str(checkedASAPs[i]['values'][j]))
        print("=========================")

def Main():
    for ll in range(0, len(snapshots)):
        if ll == 0:
            appendASAPAndFirstValue(open(snapshots[ll], 'r').readlines())
        else:
            appendASAPRestValues(open(snapshots[ll], 'r').readlines(), ll)
    writeToExcel()
    #TEST()
    
if __name__ == '__main__':
    Main()