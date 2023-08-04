"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            onesword={1:'one',2: 'two',3:'three',4: 'four', 5:'five',6 :'six', 7: 'seven', 8:'eight',9: 'nine', 10: 'ten', 11:'eleven', 12:'twelve', 13: 'thirteen',14:'fourteen',15:'fifteen', 16: 'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
            tensword = {20: 'twenty', 30:'thirty', 40: 'forty',50:'fifty'}
            output="It's "
            ampm=True
            hour= input_time[:2]
            if (int(hour))>(12):
                hour= int(hour)%12
                ampm=False
            output+= onesword[hour] +' '
            minute= input_time[len(input_time)-2: len(input_time)]
            print(minute)
            if minute[0] ==0:
                output+='oh '
            else:
                output+= tensword[int(minute[0])*10] +' '
            output+= onesword[int(minute[1])]+' '
            if(ampm):
                output+= 'am'
            else:
                output+= 'pm'
            #TODO: Write code below to return a string with the solution to the prompt.
            return output

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()