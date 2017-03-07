mystring = "my name is saikrishna im lived in hyderabad";
str = mystring.encode('base64','strict');
print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')
