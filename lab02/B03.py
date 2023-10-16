import re

v_pattern=r'\b\w*((kurw)|(jeba)|(pierdol)|(huj)|(pizd)|(gówn)|(fuck)|(shit)|(twat))\w*\b'

with open('./B03input.txt','r') as f_input:
    with open('./B03output.txt','w') as f_output:
        for line in f_input:
            # line2 = line.split()
            # for word in line2:
            #     if re.match(v_pattern,word):
            #         print(word)
            censored_line = re.sub(v_pattern,"---",line)
            f_output.write(censored_line)

f_input.close()
f_output.close() 