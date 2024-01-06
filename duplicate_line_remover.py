import hashlib



# path of the input and output files
OutFile = 'test_output.txt'
InFile = r'test.txt'

# holding the line which is already seen
lines_present = set()

# opening the output file in write mode to write in it
The_Output_File = open(OutFile, "w")

# loop for opening the file in read mode
for l in open(InFile, "r"):
      
   # finding the hash value of the current line
      # Before performing the hash, we remove any blank spaces and new lines from the end of the line.
      # Using hashlib library determine the hash value of a line.
      hash_value = hashlib.md5(l.rstrip().encode('utf-8')).hexdigest()
      if hash_value not in lines_present:
         The_Output_File.write(l)
         lines_present.add(hash_value)

# closing the output text file
The_Output_File.close()
