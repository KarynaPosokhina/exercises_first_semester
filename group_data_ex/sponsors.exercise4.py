total_certificate = 0
with open("sponsors.txt", 'r') as file:
    sponsor_list = file.readlines()
    sponsor_list.sort()

print("Overview gifts")
print("Number\tSponsor")

i = 0
fields = sponsor_list[i].rstrip().split("*")

while i < len(sponsor_list):
    sponsor_id = fields[0]
    total_per_sponsor = 0
    receive_form = ''
    print(str(sponsor_id) + "\t" + fields[1] + ' ' + fields[2], end='')

    while i < len(sponsor_list) and fields[0] == sponsor_id:
        total_per_sponsor += int(fields[3])
        i += 1
        if i < len(sponsor_list):
            fields = sponsor_list[i].rstrip().split('*')
    if total_per_sponsor >= 40:
        total_certificate += 1
        receive_form = "**"
    print('\t' + str(total_per_sponsor) + '\t' + receive_form)

print(f'There are {total_certificate}, tax certificates to be sent.')