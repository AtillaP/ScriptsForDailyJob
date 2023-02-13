import re
import json
import sys

SWName = "VF9CG000848"
SWRootFolder = "d:\\SAFE handling\\VF9\\TBAD_2023_january\\"
SWNameWithPath = SWRootFolder + SWName
folderNames = {
    "37W" :
        {
            "ComAL_Plugin" : "ComAL_VW_MQB_37W_MP23",
            "E2E_Handler_Plugin" : "E2eHandler_VW_MQB_37W_MP23",
            "MFN_Plugin" : "MFN_VW_MQB_37W_MP23",
            "MFS_Plugin" : "MFS_VW_MQB_37W_MP23"
        },
    "Classic" :
        {
            "ComAL_Plugin" : "ComAL_VW_MQB_CLASSIC_MP23",
            "E2E_Handler_Plugin" : "E2eHandler_VW_MQB_CLASSIC_MP23",
            "MFN_Plugin" : "MFN_VW_MQB_CLASSIC_MP23",
            "MFS_Plugin" : "MFS_VW_MQB_CLASSIC_MP23"
        }
}

mfnMfnPPC = SWNameWithPath + "\\Src\EBS\\VehComP\\ComAsw\\ComAsw_plugin\\MFS_plugin\\"
mfsTypeCidl = SWNameWithPath + "\\CIDL\\MFN_plugin\\MFN_plugin_cfg_project_types.cidl"
mfsTable = SWNameWithPath + "\\Src\\EBS\\VehComP\\ComAsw\\ComAsw_generic\\MFS\Src\\mon_bus_intsig_system_cfg.c"
activeMfsTable = SWNameWithPath + "\\Src\\EBS\\VehComP\\ComAsw\\ComAsw_generic\\MFS\Src\\mon_bus_intsig_system_cfg.ppc"
psbFile =  SWNameWithPath + "\\CIDL\\ComAL_plugin\\ComAL_plugin_cfg_procstates_types.cidl"
mfnTable = SWNameWithPath + "\\Src\\EBS\\VehComP\\ComAsw\\ComAsw_plugin\\MFN_plugin\\"
codegTableQm = SWNameWithPath + "\\Src\\EBS\\VehComP\\ComAsw\\ComAsw_generic\\MFS\Src\\mon_bus_intsig_codeg_table_qm.ppc"
codegTableCd = SWNameWithPath + "\\Src\\EBS\\VehComP\\ComAsw\\ComAsw_generic\\MFS\Src\\mon_bus_intsig_codeg_table_cd.ppc"


frames = {
    "Airbag_02"
}
frameInNmonFormat = "eMON_(\w+\d\d\w+|\w+\d\d)"
enmonFormat = "eMON_\w+"
nmonArrayFormat = "nmon_maplist_s\w+\[\d\]\s+\="
psbFormat = "eRX_BUS_PROC_\w+"
mfntypes = [] # List of strings
mfsAsilQm = [] # List of QM MFS members
mfsAsilCd = [] # List of CD MFS members
nmonLists = [] # List of dicts
psbDict = {
    'QMGROUP' : [],
    'QMSIG' : [],
    'CDGROUP' : [],
    'CDSIG' : []
}
frameData = {}

# Determine correct folder names - ComAL, MFS, MFN
def detProjectFlavor():
    global mfnMfnPPC, mfnTable
    if SWName[0:3] == "VF7" or  SWName[0:3] == "VF9" or SWName[0:3] == "VFA" or SWName[0:3] == "VFC" or SWName[0:3] == "VF2":
        mfnMfnPPC += (str(folderNames["37W"]["MFS_Plugin"]) + "\\Src\\mon_bus_intsig_netmon_map_cfg_setup.ppc")
        mfnTable += (str(folderNames["37W"]["MFN_Plugin"]) + "\\Src\\network_monitor_system_cfg_setup.c")
    elif  SWName[0:3] == "VF8":
        mfnMfnPPC += (str(folderNames["Classic"]["MFS_Plugin"]) + "\\Src\\mon_bus_intsig_netmon_map_cfg_setup.ppc")
        mfnTable += (str(folderNames["Classic"]["MFN_Plugin"]) + "\\Src\\network_monitor_system_cfg_setup.c")
    else:
        sys.exit("Tool is not implemented ofr this project yet.")

# Collect MFN mmbers and their number into a list of dictionaries
def collectMfnTypes(filename):
    counter = 0
    for line in (open(filename, 'r').readlines()):
        if ("member" in line) and ("eMON_" in line) and ("description" in line):
            mfntypes.append({line[re.search(enmonFormat, line).span()[0]:re.search(enmonFormat, line).span()[1]] : counter})
            counter += 1

# Order nmonlists and their attributes into a list of dictionaries
def collectNmonLists(filename):
    fileArray = open(filename, 'r').readlines()
    for i in range(0, len(fileArray)):
        if (re.search(nmonArrayFormat, fileArray[i]) != None):
            botschaft = ""
            eNMONs = []
            startIndex = re.search(nmonArrayFormat, fileArray[i]).span()[0]
            startBracketIndex = re.search('\[', fileArray[i]).span()[0]
            closingBracketIndex = re.search('\]', fileArray[i]).span()[0]
            size = int(fileArray[i][startBracketIndex+1:closingBracketIndex])
            for j in range(i+2, i+2+size):
                if (botschaft == "") and (re.search(frameInNmonFormat, fileArray[j])):
                    botschaft = fileArray[j][re.search('eMON_', fileArray[j]).span()[1]:re.search('eMON_\w+\d+', fileArray[j]).span()[1]]
                if re.search(enmonFormat, fileArray[j]) != None:
                    eNMONs.append({fileArray[j][re.search(enmonFormat, fileArray[j]).span()[0]:re.search(enmonFormat, fileArray[j]).span()[1]]:0})
                else:
                    eNMONs.append({"NA":0})
            if list(eNMONs[0].keys())[0] != 'NA':
                nmonLists.append({
                    "NmonListArray" : str(fileArray[i][startIndex:startBracketIndex]),
                    "FSF4" : {"Bus_s" + str(fileArray[i][(startIndex+14):startBracketIndex]) : 0},
                    "Intsig" : "",
                    "Size" : size,
                    "Frame" :   botschaft,
                    "MFNs" : eNMONs
                })
            else:
                nmonLists.append({
                    "NmonListArray" : str(fileArray[i][startIndex:startBracketIndex]),
                    "FSF4" : {"Bus_s" + str(fileArray[i][(startIndex+14):startBracketIndex]) : 0},
                    "Intsig" : "",
                    "Size" : 0,
                    "Frame" : "NA",
                    "MFNs" : eNMONs
                })

# Find order in MFS table
def findMFSOrder():
    mfstable = [] # List of MFS table part
    activemfstable = [] # List of active MFS
    counter = 0
    for line in open(mfsTable, 'r').readlines():
        if ("Bus_s" in line) and ("Check_qf_intsig" in line):
            mfstable.append(line[re.search('Bus_s',line).span()[0]:re.search('\}',line).span()[0]])
    for line in open(activeMfsTable, 'r').readlines():
        for elem in mfstable:
            if elem[re.search('Check_qf_intsig_\w+'.strip(), elem).span()[0]:re.search('Check_qf_intsig_\w+'.strip(), elem).span()[1]] in line:
                activemfstable.append(elem)
    for line in activemfstable:
        for i in range(0, len(nmonLists)):
            if list(nmonLists[i]["FSF4"].keys())[0] in line:
                nmonLists[i]["FSF4"][list(nmonLists[i]["FSF4"].keys())[0]] = counter
                counter += 1
                break
                
# Find order in MFN table
def findMFNOrder():
    for i in range(0, len(nmonLists)):
        for j in range(0, nmonLists[i]['Size']):
            nmonListMFNsElemKey = list(nmonLists[i]['MFNs'][j].keys())[0]
            if nmonListMFNsElemKey != 'NA':
                for l in range(0, len(mfntypes)):
                    mfntypesKey = list(mfntypes[l].keys())[0]
                    if nmonListMFNsElemKey == mfntypesKey:
                        nmonLists[i]['MFNs'][j][nmonListMFNsElemKey] = mfntypes[l][mfntypesKey]
                        break

# INTSIG ASAP name parsing
def findMFSAsilOrder():
    for tag in nmonLists:
        notFound = True
        status = ""
        lookfor = list(tag['FSF4'].keys())[0][8:].upper()
        while notFound:
            for elem in mfsAsilCd:
                if lookfor in list(elem.keys())[0]:
                    tag['Intsig'] = 'INTSIG_*CD*' + str(list(elem.values())[0])
                    notFound = False
                    break
                else:
                    status = 'NoCD'
            for elem in mfsAsilQm:
                if lookfor in list(elem.keys())[0]:
                    tag['Intsig'] = 'INTSIG_*' + str(list(elem.values())[0])
                    notFound = False
                    break
                else:
                    status = 'NoQM'
            if status == 'NoQM':
                notFound = False

# Find order in MFS and MFN tables
def enumerate():
    findMFSOrder()
    findMFSAsilOrder()
    findMFNOrder()

# Collect PSBs and their order into 4 lists of arrrays
def setupPsbTableArrays():
    counterQmGroup, counterCdGroup, counterQmSig, counterCdSig, i = -1, -1, -1, -1, 0
    PSBFile = open(psbFile, 'r').readlines()
    while (counterQmGroup == -1) or (counterCdGroup == -1) or (counterQmSig == -1) or (counterCdSig == -1):
        if 'eRX_BUS_PROC_GRP_QM_ENUM_t' in PSBFile[i]:
            counterQmGroup = 0
            ttuple = psbArray(PSBFile, counterQmGroup, i+2, 'QMGROUP')
            i = ttuple[1]
            counterQmGroup = ttuple[0]
        elif 'eRX_BUS_PROC_SIG_QM_ENUM_t' in PSBFile[i]:
            counterQmSig = 0
            ttuple = psbArray(PSBFile, counterQmSig, i+2, 'QMSIG')
            i = ttuple[1]
            counterQmSig = ttuple[0]
        elif 'eRX_BUS_PROC_GRP_CD_ENUM_t' in PSBFile[i]:
            counterCdGroup = 0
            ttuple = psbArray(PSBFile, counterCdGroup, i+2, 'CDGROUP')
            i = ttuple[1]
            counterCdGroup = ttuple[0]
        elif 'eRX_BUS_PROC_SIG_CD_ENUM_t' in PSBFile[i]:
            counterCdSig = 0
            ttuple = psbArray(PSBFile, counterCdSig, i+2, 'CDSIG')
            i = ttuple[1]
            counterCdSig = ttuple[0]
        i += 1

def psbArray(file, order, startindex, selector):
    counting, i = True, startindex
    while counting:
        if ('member' in file[i]) and ('eRX_BUS_PROC_' in file[i]):
            if selector == 'QMGROUP':
                psbDict['QMGROUP'].append({
                    re.search('eRX_BUS_PROC_\w+',file[i]).group(0) : int(order)
                })
            elif selector == 'QMSIG':
                psbDict['QMSIG'].append({
                    re.search('eRX_BUS_PROC_\w+',file[i]).group(0) : int(order)
                })
            elif selector == 'CDGROUP':
                psbDict['CDGROUP'].append({
                    re.search('eRX_BUS_PROC_\w+',file[i]).group(0) : int(order)
                })
            elif selector == 'CDSIG':
                psbDict['CDSIG'].append({
                    re.search('eRX_BUS_PROC_\w+',file[i]).group(0) : int(order)
                })
            order += 1
        else:
            if order > 0:
                counting = False
        i += 1
    return (order, i)

def getAsilSpecifiedMfsOrder(file, startingString, llist):
    order = 0
    collect = False
    for line in open(file, 'r').readlines():
        if startingString in line:
            collect = True
        if collect and ('eINT_S' in line):
            if order < 10:
                llist.append({
                    line[re.search('eINT_S', line).span()[0]:re.search('eINT_S\w+', line).span()[1]] : '0'+str(order)
                })
            else:
                llist.append({
                    line[re.search('eINT_S', line).span()[0]:re.search('eINT_S\w+', line).span()[1]] : str(order)
                })
            order += 1            

def collectFrameData(frame):
    checkedFrame = ""
    if frame[-5:] == '_Auth':
        checkedFrame = frame[:-5]
    else:
        checkedFrame = frame
    frameData.update({frame:[]})
    for elem in nmonLists:
        if elem['Frame'] == checkedFrame:
            frameData[frame].append(elem)

def importSWDataToJson():
    json_data = json.dumps(nmonLists, indent = 5)
    with open(SWRootFolder + SWName+"_mfsmfndata.json", 'w') as outfile:
        outfile.write(json_data)
    json_data1 = json.dumps(psbDict, indent = 4)
    with open(SWRootFolder + SWName+"_psb.json", 'w') as outfile:
        outfile.write(json_data1)
    json_data1 = json.dumps(mfntypes, indent = 4)
    with open(SWRootFolder + SWName+"_NMON_ASAPs.json", 'w') as outfile:
        outfile.write(json_data1)
       
       
def importFrameDataToJson():
    for elem in list(frameData.keys()):
        json_data = json.dumps(frameData[elem], indent = 2)
        with open(SWRootFolder+SWName+"_"+str(elem)+"_framedata.json", 'w') as outfile:
            outfile.write(json_data)

def Main():
    detProjectFlavor()
    collectMfnTypes(mfsTypeCidl)
    getAsilSpecifiedMfsOrder(codegTableQm, 'MON_BUS_INTERN_SIG_TABLE_REFID_QM', mfsAsilQm)
    getAsilSpecifiedMfsOrder(codegTableCd, 'MON_BUS_INTERN_SIG_TABLE_REFID_CD', mfsAsilCd)
    collectNmonLists(mfnMfnPPC)
    enumerate()
    setupPsbTableArrays()
    for tag in frames:
        collectFrameData(tag)
    importSWDataToJson()
    importFrameDataToJson()
    
    # TEST
    #for i, j in zip(mfsAsilCd, mfsAsilQm):
    #    print(i, j)
    
if __name__ == '__main__':
    Main()