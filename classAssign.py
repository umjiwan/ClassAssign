import os
import random

def classFile(fileName='class.json'):
    isClassFile = os.path.isfile(fileName)

    if isClassFile:
        with open(fileName, "r") as f:
            classFile = f.read()
        return classFile

    else:
        return None

def createClassFile(group=5 ,classFileName='class.json', friendFileName='friends.txt'):
    isFriendFile = os.path.isfile(friendFileName)

    if isFriendFile:
        with open(friendFileName, "r") as f:
            friendFile = f.read()
    
    else:
        with open(friendFileName, "w") as f:
            for i in range(1, 36):
                f.write(f"{i}.\n")
        
        return "001"

    friendList = createFriendList(friendFile)
    groupList = createGroupList(friendList, group)
    print(groupList)

def createFriendList(friendFile):
    friendList = []
    for friend in friendFile.split("\n"):
        if friend == "":
            continue

        friend = friend.split(".")
        
        friend[1] = friend[1].replace(" ", "")
        if friend[1] == "":
            continue
        else:
            friend[0] = int(friend[0])
            friendList.append(friend)

    return friendList

def createGroupList(friendList, group):
    r=0
    groupList = []
    for f in range(1, ((len(friendList) // group) + 1) + 1):
        groupList.append(friendList[r:f*group])
        r = f*group

    if groupList[-1] == []:
        groupList.pop(-1)

    return groupList

if __name__ == "__main__":
    createClassFile()

    
    
    


