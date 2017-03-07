
'''The method index() determines if string str occurs in string, or in a substring of string if starting indexbeg and ending index end are given.
This method is same as find(), but raises an exception if sub is not found.'''
str1 = "this is string example....wow!!!";
str2 = "exam";
print str1.find(str2);
print str1.find(str2, 10);
print len(str1)

print str1.find(str2, 40);
