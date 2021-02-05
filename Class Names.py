our_class = "David Erick Heather Sydney Yosh Diana Jake Westley Khushi Suzette Aldo Katherine Nahomy Helaman"

daily_info = ["David climbed a lot of rocks Erick went to mexico Heather played switch Sydney got engaged Suzette Nothing Really Jake Also Nothing Wesley Also Nothing Aldo Went to Mexico Meh Naohmy Diana Went to California Catherine Went to Wyoming Josh played video games", 
              "Westley favorite food is pizza, Katherine has gone to mexico, Khushi likes science, Heather's favorite color is blue, Sydney is 21, Erick loves seafood, Nahomy walks home, Helaman works with his dad, Yosh hates school, Jake likes Fall Guys, Aldo hates science, Suzette is taking french", 
              "David 400 Suzette 2 Erick 300 Jake 1500 Katherine 150 Aldo 800 Diana 2000 Nahomy 9020 Helaman 3 Yosh 4001 Westley 643 Sydney 60000",
              "Erick Sound of Music"]

favorite_colors = [""]
def letter_occurence(ourclass):
    letter_frequency = {}
    for i in daily_info:
        for x in i.upper():
            if x in letter_frequency and x != " " and x not in "1, 2, 3, 4, 5, 6, 7, 8, 9, 0": 
                letter_frequency[x] += 1
            else: 
                letter_frequency[x] = 0
    print(sorted(letter_frequency.items(), key=lambda i: i[1]))
    
letter_occurence(daily_info)

def Erickcount(daily_info):
    erick_count = 0
    for i in daily_info:
        if "erick" in i.lower():
            erick_count += 1
    return erick_count

print("Erick has been mentioned in our daily_info " + str(Erickcount(daily_info)) +" times")

