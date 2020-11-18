import re
def arithmetic_arranger(problems, to_solve = False):
  if(len(problems)>5):
    return "Error: Too many problems."
  x = []
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  gap = '    '
  for i in problems:
    x.append(i.split(' '))
    if(re.findall("[^0-9a-zA-Z\s+-]", i)):
      return "Error: Operator must be '+' or '-'."
    elif(re.findall("[^0-9\s+-]", i)):
      return "Error: Numbers must only contain digits."
  for i in x: 
    if(len(i[0]) > 4 or len(i[2]) > 4):
      return "Error: Numbers cannot be more than four digits."   
    width = max(len(i[0]),len(i[2]))
    line1 = line1+ (i[0]).rjust(width+2) + gap
    line2 = line2+ (i[1]+' ').ljust(2) + (i[2]).rjust(width) + gap
    line3 = line3 + ''.center(width+2,'-') + gap
    if (i[1]=='+'):
      result = int(i[0])+int(i[2])
    else: 
      result = int(i[0])-int(i[2])
    line4 = line4 + (str(result)).rjust(width+2) + gap
  answer = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip()
  if(to_solve):
    return answer + '\n' + line4.rstrip()
  else:
    return answer
