def printing_logo():
    print("  ######### ###### ###   ### #########                     ")
    print("  ######### ######  ### ###  #########                     ")
    print("     ###    ###      #####      ###                        ")
    print("     ###    ######    ###       ###                        ")
    print("     ###    ###      #####      ###                        ")
    print("     ###    ######  ### ###     ###                        ")
    print("     ###    ###### ###   ###    ###                        ")
    print("                                                           ")
    print("            ###### ### ###     ### ######                  ")
    print("            ###### ### ####    ### #######                 ")
    print("            ###    ### #####   ### ###   ##                ")
    print("            ###    ### ### ##  ### ###    ##               ")
    print("            ###### ### ### ### ### ###   ##                ")
    print("            ###    ### ###  ###### ###  ##                 ")
    print("            ###    ### ###   ##### ######                  ")
    print("\n\n\n")










printing_logo()

file_name = input('Enter file name :')
file_handle = open(file_name)
search = input('Enter the word you want to search :')



list_data = [] 

for line in file_handle:
    line = line.rstrip() #for handling the right newline 
    line = line.lower()  #for generalized search
    
    
    xlist = line.split()
    #print(mlist)
    
    #now i will parse for the http string:
    for x in xlist:
        if(x.startswith(search.lower())):
            print(x)
            list_data.append(x)#also storing it in an empty list



#now saving the data in an external text file

file_handle = open('output_data.txt' ,'w')
for values in list_data:
    file_handle.writelines(values+'\n')



print('There are',len(list_data),'matches in the file')

endline = 'There are '+str(len(list_data))+' word matches in the file'
file_handle.writelines(endline)

file_handle.close()


