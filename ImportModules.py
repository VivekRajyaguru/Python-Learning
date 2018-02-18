
import re;

value = "THIS IS CAPITAL this is small This's has single quote";
# print only Caps
newValue = re.sub('[A-Z]', '', value);
print(newValue);
# print only small
newValue = re.sub('[a-z]', '', value);
print (newValue);
# remove all spaces and single quote
newValue = re.sub('[..\'+" "]', '', value);
print (newValue);