voted_yes = int(input("How many people voted 'yes'?"))
print(str(type(voted_yes)))
voted_no = int(input("How many people voted 'no'?"))
print(str(type(voted_no)))
blank_votes = int(input("How many blank votes"))
print(str(type(blank_votes)))

total = voted_yes + voted_no + blank_votes
print((voted_yes/total)*100,"%")
print((voted_no/total)*100,"%")
print((blank_votes/total)*100,"%")