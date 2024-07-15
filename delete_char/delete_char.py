mac_file = list(open('sample.txt'))
new_mac = []
for i in range(len(mac_file)):
    # print(mac_list[i].strip('\n'))
    new_mac.append(mac_file[i].replace(":",""))
#for i in range(len(new_mac)):
    with open('removed_char.txt', 'a') as newfile:
        newfile.write(new_mac[i])