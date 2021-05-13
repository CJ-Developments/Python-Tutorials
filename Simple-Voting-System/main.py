a = 0 #Starts Candiadate A with 0 votes
b = 0 #Starts Candiadate B with 0 votes
c = 0 #Starts Candiadate C with 0 votes
END = 0 #Starts total votes at 0
loop = 0 #keeps the while loop going
while loop == 0: #Will Repeat while loop is 0
  vote=input(" \nEnter a for Candidate A, b for Candidate B or c for Candidate C \n") #Allows the vote to input a choice
  if vote =="a": #If the voter chooses A:
    print ("Vote has been recorded") #A statement will be printed
    a = a+1 #A vote for a will be added
    END = END +1 #A total vote will be added
  elif vote =="b": #If the voter chooses b then:
    print("Vote has been recorded") #A stament will be printed
    b = b+1 #A vote for b will be added
    END = END +1 #A total vote will be added
  elif vote == "c": #If the voter choices C then:
    print("Vote has been recoreded") #A statement will be added
    c = c+1 #A vote for c will be added
    END = END +1 #A total vote will be added
  elif vote == "END": #if END is entered the stats will be displayed and the loop will stop
    print("Total Votes", END) #Prints the total votes
    print("Vote A has",a) #Prints all the votes for A
    print("Vote B has", b) #prints all the votes for B
    print("Vote C has", c) #Prints all the votes for C
  else:
    print("Error")