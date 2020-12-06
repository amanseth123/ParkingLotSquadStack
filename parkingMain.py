from collections import defaultdict
class Solution:
    def __init__(self): # constructor to initialise data structures 
        self.ageSlot=defaultdict(list) # maps age against slots (dictionary are a kind of key:value mapping), here list is passed as an object to store list as values in the mapping
        self.regSlot=defaultdict(list) # maps registration against slots 
        self.regAge=[] # representing slots, mapping like ["registrationNumber","age"]

    def park(self,regNum,age):
        alreadyParkedBool=False 
        # base case to check if entered registration number is already available in one of the slots if yes, alreadyParkedBool will become true
        for i in range(len(self.regAge)):
            if self.regAge[i][0]==regNum:
                alreadyParkedBool=True
                print('Car with registration number '+ '"{}"'.format(regNum) + ' is already parked at slot '+ '{}'.format(self.regSlot[regNum][0]))
        if len(self.regAge)==0: # if initially the parking slots are fully empty simply enter the upcoming vehicle
            self.regAge.append([regNum,age])
            self.ageSlot[age].append(len(self.regAge))
            self.regSlot[regNum].append(len(self.regSlot))
            print('Car with vehicle registration number '+ '"{}"'.format(regNum)+ ' has been parked at slot number ' + '{}'.format(len(self.regSlot)))
        else:
            c=True
            # checking if there is any slot already available [0,0] represents left slot by another vehicle
            for i in range(len(self.regAge)):
                if self.regAge[i]==[0,0] and not alreadyParkedBool: # if there is any slot avialble and the given vehicle registration number is not already parked before 
                    self.regAge[i][0]=regNum
                    self.regAge[i][1]=age
                    self.ageSlot[age].append(len(self.regAge)) # looks like {"age":[slotNumber1,slotNumber2, .....]}
                    self.regSlot[regNum].append(len(self.regSlot))
                    print('Car with vehicle registration number ' + '"{}"'.format(regNum)+ ' has been parked at slot number ' + '{}'.format(i+1))
                    c=False # denotes that the previously left slot is now occupied by another vehicle
            else:
                if c and alreadyParkedBool==False: #if all previous slots are filled and given vehicle registration number is not already present in the parking area
                    self.regAge.append([regNum,age]) # append the data at the last available slot
                    # simultaneously also updating the other 2 data structure for fast retrieval later 
                    self.ageSlot[age].append(len(self.regAge)) # looks like {"age":[slotNumber1,slotNumber2, .....]}
                    self.regSlot[regNum].append(len(self.regSlot)) # looks like {"regNum":[slotNumber1,slotNumber2, ....]}
                    print('Car with vehicle registration number ' + '"{}"'.format(regNum)+ ' has been parked at slot number ' + '{}'.format(len(self.regAge)))
    
    def slotAge(self,age):
        if age in self.ageSlot: # if given age is present in the self.ageSlot dictionary data structure simply return 
            return self.ageSlot[age]
        #the else part is handled in the main function where this function is called
    
    def slot_carNumber(self,regNumber):# if given vehicle registration number is present in the self.regSlot dictionary data structure simply return 
        if regNumber in self.regSlot:
            return self.regSlot[regNumber]
        #the else part is handled in the main function where this function is called

    def leave(self,index): # this function empty the slot at given index 
        index=int(index)
        if len(self.regAge)>=index-1 and index>0: # trying to empty space in range with the alloted slot size
            print('Slot number {} vacated, the car with vehicle registration number '.format(index)+ '"{}"'.format(self.regAge[index-1][0]) +' left the space, the driver of the car was of age {}'.format(self.regAge[index-1][1]))
            regnumber=self.regAge[index-1][0] # because of 0 based indexing required to do index-1
            del self.regSlot[regnumber]
            self.regAge[index-1]=[0,0] # vacating the space and alloting [0,0] as a vacant value
        else: # 
            print("Out of Bound slot index ")
    
    def vehicle(self,age): # function to get all vehicle registration number with given age 
        self.ans=[] # for storing the final result
        for i,j in self.regAge:
            if j==age:
                self.ans.append(i)
        return self.ans # returning the result

    def execute(self,com): # function to execute all the commands 1 each line from the txt file
        com=com.split(" ") # splitting the line with space and storing it into a com list 

        # below are the variant of commands expected from the text file
        if com[0]=="Create_parking_lot":
            self.size=int(com[1])
            print("Created parking of {} slots ".format(self.size))
        elif com[0]=="Park":
            if len(self.regAge)<self.size:
                regNumber=com[1]
                age=com[3]
                self.park(regNumber,age)
            else:
                print("The parking lot is full already !!")
            
        elif com[0]=="Slot_numbers_for_driver_of_age":
            age=com[1]
            ans=self.slotAge(age)
            if ans:
                print(*ans,sep=',') # return
            else:
                print("Sorry, there is no slot available with this given age ") 
        elif com[0]=="Slot_number_for_car_with_number":
            regNumber=com[1]
            ans=self.slot_carNumber(regNumber)
            if ans:
                print(*ans,sep=',')
            else:
                print("Sorry, there is no slot available with this given registration number ")
        elif com[0]=="Leave":
            index=com[1]
            self.leave(index)
        elif com[0]=="Vehicle_registration_number_for_driver_of_age":
            try:
                age=com[1]
                x=self.vehicle(age)
                if x:
                    print(*x,sep=',') # unpacking the answer list 
                else:
                    print("Sorry, there are no available parked vehicle with this given age ")
            except:
                print("There is some error fetching the age ")
        else:
            print("Sorry, this error could be either because you have an empty new line in the input file or typed a wrong command !! ")

    def starter(self,filename):
        try:
            commands=[] # set of commands from the file to store in a list
            f=open(filename,"r")# opening the txt file in read mode
            for i in f:
                i=i.strip('\n') # eliminating the default "\n" from the commands 
                commands.append(i) # storing all the executable commands in an commands list 
            for i in commands:
                self.execute(i) # executing each commands per line of the file as stored in commands list 
        except:
            f.close()
            print("Something went wrong while reading the file !")

ob=Solution()
try:
    filename=input("Please Enter the text input file: ") # enter here the input text file name
    n=len(filename)
    if filename[n-4:n]!='.txt':
        print("Enter a valid text file name")
except:
    print("Write a proper filename")

ob.starter(filename)




