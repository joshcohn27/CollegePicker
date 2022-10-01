"""
College Ranker

Working on adjusting it so all information about schools is taken from a CSV file, and your results are outputted to a new CSV file


@Author: Josh Cohn
Made for APCSP Exam 2021
    Updating with new coding knowledge for fun
"""

#lists
sch_list= []
pop_list = []
aid_list = []
size_list = []
loc_list = []
greek_list = []
uniq_list = []
ratio_list = []
envis_list = []
major_list = []
honors_list = []
score_list = []


num = 0


#Function for multiplying score to be out of 100
def divid(x):
    float(x)
    x = x / 1.1
    x = round(x, 2)
    return x

#Function for swapping positions to put the lists in order
def swap(y):
    #school
    temp = sch_list[y]
    sch_list[y] = sch_list[y+1]
    sch_list[y+1] = temp
    
    #score
    temp = score_list[y]
    score_list[y] = score_list[y+1]
    score_list[y+1] = temp
    


#To String function to output
def toString(scores, schools, g):
    print("\n\n\nHere is your ranking of schools:\n ")
    print("|Rank  |School                 |Score |")
    for f in range (g):
        h = f + 1
        if f > 0:
            if float(scores[f]) == float(scores[f - 1]):
                h = f
        print("|"+str(h)+ "." + " "*(4-len(str(h))),"|"+ str(schools[f])," "*(21-len(str(schools[f]))),"|"+str(scores[f])," "*(5-len(str(scores[f])))+"|")


def main():
    name = input("Enter your name: ")



    #Original Questions
    print("\nHello " + name + "! Please answer the following questions about what you want in a college.\n")

    #size
    while True:
        size = input("What size school do you want? (S- <5000 students; M- 5000-10000 students; L- 10001-15000 students; XL- 15001-20000 students; XXL- >20000 students): ")
        size = size.upper()
        if size != 'S' and size != 'M' and size != 'L' and size != "XL" and size != "XXL":
            print("Please enter either S, M, L, XL, or XXL")
            continue
        else:
            break

    #place
    while True:
        location = input("\nWhich is your first choice for school location? \nA) In a city \nB) Very close to a city \nC) Not near a city/Rural area\n")
        location = location.upper()
        if location != 'A' and location != 'B' and location != 'C':
            print("Please enter either A, B, or C")
            continue
        break

    if location == 'A':
        while True:
            loc2 = input("\nWhich is your second choice for school location? \nA) Very close to a city \nB) Not near a city/Rural area\n")
            loc2 = loc2.upper()
            if loc2 != 'A' and loc2 != 'B':
                print("Please enter either A or B")
                continue
            if loc2 == 'A':
                secondChoice = "Close"
            if loc2 == 'B':
                secondChoice = "No"
            break
    if location == 'B':
        while True:
            loc2 = input("\nWhich is your second choice for school location? \nA) In a city\nB) Not near a city/Rural area\n")
            loc2 = loc2.upper()
            if loc2 != 'A' and loc2 != 'B':
                print("Please enter either A or B")
                continue
            if loc2 == 'A':
                secondChoice = "Yes"
            if loc2 == 'B':
                secondChoice = "No"
            break
    if location == 'C':
        while True:
            loc2 = input("\nWhich is your second choice for school location? \nA) In a city\nB) Very close to a city\n")
            loc2 = loc2.upper()
            if loc2 != 'A' and loc2 != 'B':
                print("Please enter either A or B")
                continue
            if loc2 == 'A':
                secondChoice = "Yes"
            if loc2 == 'B':
                secondChoice = "Close"
            break


    #program/major
    major = input("\nWhat program do you want to major in? (If undecided, please put a field you are interested in possibly studying): ")

    #Greek Life
    while True:
        greek = input("\nIs Greek Life a must have? (Y/N) ")
        greek = greek.upper()
        if greek[0] == "Y" or greek[0] == "N":
            if greek[0] == "Y":
                greekDecision = True
            else:
                greekDecision = False
            break
        else:
            print('Please enter either "Y" for yes or "N" for no')
            continue

    #Male/Female
    while True:
        mfr = input("\nWhat is your ideal Male to Female Ratio? \nA)100% Woman/0% Men \nB)67-99% Woman/1-33% Men \nC)34-66% Woman/34-66% Men \nD)1-33% Woman/67-99% Men \nE)0% Woman/100% Men\n")
        mfr = mfr.upper()
        if mfr != 'A' and mfr != 'B' and mfr != 'C' and mfr != 'D' and mfr != 'E':
            print("Please enter either A, B, C, D, or E")
            continue
        break


    print("\n\nNow that we know a little bit about what you want in a school, let's talk aboout the specific colleges you applied to.")


    while True:
        #name of school
        while True:
            sch_name = input("\n\nEnter the name of a college you are considering (max. 20 characters): ")
            if len(sch_name) > 20:
                print("There is a max of 20 characters. Please enter an abbreviation.")
                continue
            sch_list.append(sch_name)
            break

        #Is it a well known school? (If you were to ask a random person on the street if they knew the school, would they know it and where it is?)
        while True:
            popular = input("\nIs " + sch_name + " a well known school? (If you were to ask a random person on the street if they knew the school, would they know it and where it is?) ")
            popular = popular.upper()
            if popular[0] != "Y" and popular[0] != "N":
                print('Please enter either "Y" for yes or "N" for no ')
                continue
            pop_list.append(popular[0])
            break
        
        #What is the average cost after aid?
        while True:
            aid = input("\nWhat is the cost per year? (if you don't know, put the average cost after aid) $")
            try:
                float(aid)
            except:
                print("Please enter a number ")
                continue
            aid_list.append(aid)
            break

        #What is the size of the school?
        while True:
            undergrad = input("\nHow many undergraduate students are attending? ")
            try:
                int(undergrad)
            except:
                print("Please enter a number ")
                continue
            size_list.append(undergrad)
            break

        #Major
        while True:
            prog = input("\nDoes " + sch_name + " have a good " + major + " program? (Y/N) ")
            prog = prog.upper()
            if prog[0] != "Y" and prog[0] != "N":
                print('Please enter either "Y" for yes or "N" for no ')
                continue
            major_list.append(prog[0])
            break
            
        #Is the school in a city?
        while True:
            city = input("\nIs " + sch_name + " in a city? (Y/N) ")
            city = city.upper()
            if city[0] != "Y" and city[0] != "N":
                print('Please enter either "Y" for yes or "N" for no ')
                continue
            if city[0] == "Y":
                loc_list.append("Yes")
            else:
                #If no, is it near a city?
                while True:
                    city2 = input('\nIs it near a city (enter "Y") or is it not near a city (enter "N")? ')
                    city2 = city2.upper()
                    if city2[0] != "Y" and city2[0] != "N":
                        print('Please enter either "Y" or "N" ')
                        continue
                    if city2[0] == "Y":
                        loc_list.append("Close")
                        break
                    else:
                        loc_list.append("No")
                    break
            break

        #Does the school have Greek Life? (if yes)
        if greekDecision == True:
            while True:
                grk = input("\nDoes " + sch_name + " have Greek Life? (Y/N) ")
                grk = grk.upper()
                if grk[0] != "Y" and grk[0] != "N":
                    print('Please enter either "Y" for yes or "N" for no ')
                    continue
                greek_list.append(grk[0])
                break

        #Male/Female Ratio
        while True:
            ratio = input("\nWhat % of " + sch_name + " students are Female? (please round to nearest whole number) ")
            try:
                int(ratio)
            except:
                print("Please enter just a whole number ")
                continue
            if int(ratio) < 0 or int(ratio) > 100:
                print("Please enter a number from 0-100 ")
                continue
            str(ratio)
            ratio_list.append(ratio)
            break

        #Honors
        while True:
            honors = input("\nDid you get accepted into " + sch_name + "'s Honors Program? (Y/N) ")
            honors = honors.upper()
            if honors[0] != "Y" and honors[0] != "N":
                print('Please enter either "Y" for yes or "N" for no ')
                continue
            honors_list.append(honors[0])
            break

        #Give this school a grade from 1-5 on how unique it is (your opinion)
        while True:
            opinion = input("\nGive " + sch_name + " a grade from 1-5 on how unique it is (your opinion) ")
            try:
                int(opinion)
            except:
                print("Please enter a number from 1-5")
                continue
            temp = int(opinion)
            if temp < 1 or temp > 5:
                print("Please enter a number from 1-5")
                continue
            uniq_list.append(opinion)
            break

        #Can you envision yourself at this school?
        while True:
            envision = input("\nCan you see yourself at " + sch_name + "? (Y/N) ")
            envision = envision.upper()
            if envision[0] != "Y" and envision[0] != "N":
                print('Please enter either "Y" for yes or "N" for no ')
                continue
            envis_list.append(envision[0])
            break


        #Go again?
        choice = input("\nThat's all we need to know about " + sch_name + ". Do you want to add another college? (Y/N) ")
        choice = choice.upper()
        if choice[0] == "Y" or choice[0] == "N":
            if choice[0] == "Y":
                num = num + 1
                continue
        break



    counter = len(sch_list)

    #Scorer
    for i in range (counter):
        score = 0   
        #Popular
        if pop_list[i] == 'Y':
            score = score + 10

        #Money
        money1 = float(aid_list[i])
        if money1 <= 10000:
            score = score + 15
        if money1 > 10000 and money1 <= 20000:
            score = score + 12
        if money1 > 20000 and money1 <= 30000:
            score = score + 9
        if money1 > 30000 and money1 <= 40000:
            score = score + 6
        if money1 > 40000 and money1 <= 50000:
            score = score + 3

        #Size
        pop = int(size_list[i])
        if size == 'S':
            if pop < 5000:
                score = score + 15
            if pop <= 10000 and pop >= 5000:
                score = score + 13
            if pop <= 15000 and pop >= 10001:
                score = score + 10
            if pop <= 20000 and pop >= 15001:
                score = score + 5
        if size == 'M':
            if pop < 5000:
                score = score + 13
            if pop <= 10000 and pop >= 5000:
                score = score + 15
            if pop <= 15000 and pop >= 10001:
                score = score + 13
            if pop <= 20000 and pop >= 15001:
                score = score + 10
            if pop > 20000:
                score = score + 5
        if size == 'L':
            if pop < 5000:
                score = score + 10
            if pop <= 10000 and pop >= 5000:
                score = score + 13
            if pop <= 15000 and pop >= 10001:
                score = score + 15
            if pop <= 20000 and pop >= 15001:
                score = score + 13
            if pop > 20000:
                score = score + 10
        if size == 'XL':
            if pop < 5000:
                score = score + 5
            if pop <= 10000 and pop >= 5000:
                score = score + 10
            if pop <= 15000 and pop >= 10001:
                score = score + 13
            if pop <= 20000 and pop >= 15001:
                score = score + 15
            if pop > 20000:
                score = score + 13
        if size == 'XXL':
            if pop <= 10000 and pop >= 5000:
                score = score + 5
            if pop <= 15000 and pop >= 10001:
                score = score + 10
            if pop <= 20000 and pop >= 15001:
                score = score + 13
            if pop > 20000:
                score = score + 15

        #Location
        place = loc_list[i]
        if location == "A":
            if place == "Yes":
                score = score + 10
            if place == secondChoice:
                score = score + 5
        if location == 'B':
            if place == "Close":
                score = score + 10
            if place == secondChoice:
                score = score + 5
        if location == 'C':
            if place == "No":
                score = score + 10
            if place == secondChoice:
                score = score + 5

        #Male/Female
        rat = int(ratio_list[i])
        if mfr == 'A':
            if rat == 100:
                score = score + 10
            if rat <= 99 and rat >= 67:
                score = score + 7
            if rat <= 66 and rat >= 34:
                score = score + 3
        if mfr == 'B':
            if rat == 100:
                score = score + 7
            if rat <= 99 and rat >= 67:
                score = score + 10
            if rat <= 66 and rat >= 34:
                score = score + 7
            if rat <= 33 and rat >= 1:
                score = score + 3
        if mfr == 'C':
            if rat == 100:
                score = score + 3
            if rat <= 99 and rat >= 67:
                score = score + 7
            if rat <= 66 and rat >= 34:
                score = score + 10
            if rat <= 33 and rat >= 1:
                score = score + 7
            if rat == 0:
                score = score + 3
        if mfr == 'D':
            if rat <= 99 and rat >= 67:
                score = score + 3
            if rat <= 66 and rat >= 34:
                score = score + 7
            if rat <= 33 and rat >= 1:
                score = score + 10
            if rat == 0:
                score = score + 7
        if mfr == 'E':
            if rat <= 66 and rat >= 34:
                score = score + 3
            if rat <= 33 and rat >= 1:
                score = score + 7
            if rat == 0:
                score = score + 10


                
        #Uniqueness
        uniqueness = int(uniq_list[i])
        score = score + uniqueness

        #Envision
        if envis_list[i] == 'Y':
            score = score + 10

        #Major
        if major_list[i] == 'Y':
            score = score + 20

        #Honors
        if honors_list[i] == 'Y':
            score = score + 5
        
        #Greek
        if greekDecision == True:
            if greek_list[i] == 'Y':
                score = score + 10
                score = divid(score)
            

        str(score)
        score_list.append(score)
            



    #Fix order; Breaks once it doesn't have to fix anything
    while True:
        cnt = 0
        for a in range (counter - 1):
            if float(score_list[a]) < float(score_list[a+1]):
                swap(a)
                cnt = cnt + 1
        if cnt == 0:
            break



    toString(score_list, sch_list, counter)



if __name__ == "__main__":
    main()