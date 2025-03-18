#!/usr/bin/env python3

# I have modified the script from shadeebhossain (here is commented # )

###### ORIGINAL SCRIPT ######################

#to open the file BRCA1 BA that contains the nucleotide for breast cancer and
# downloaded from BRCA1 "nucleotide" section number 53 with over 15k
#nucleotide.
# It is saved as text file and r for read
#gene =open("BRCA1.BA.txt","r")
#set the values to zero since all the nucleotides are labelled as
# G, A , C, T
#g=0;
#a=0;
#c=0;
#t=0;
#skip the first line of header
#gene.readline()
#for line in gene:
 #   line =line.lower()
 #   for char in line:
 #       if char == "g":
 #           g+=1
 #       if char == "a":
 #           a+=1
 #       if char == "c":
 #          c+=1
 #       if char == "t":
 #          t+=1
#print "number of g's " +str(g)
#print "number of a's " +str(a)
#print "number of c's " +str(c)
#print "number of t's " +str(t)
# 0. = convert to floating points
#gc=(g+c+0.)/(a+t+c+g+0.)
#print "number of gc content is  " +str(t)


############# MODIFIED VERSION (Claudia's version) ###################

############# I will improve this version with addtional funcionalities:
###1. More accurate GC content (the original script prints t instead of GC content)
###2. Generate complementary DNA sequence
###3. Better print formatting (use f-strings)

with open("BRCA1.BA.txt", "r") as gene:
	#skip the header line
	gene.readline()
	
	#Initialize nucleotide counts
	g = a = c = t = 0

	# Store the sequence for reverse complement functionality
	complementary_seq = ""

	# Process each line
	for line in gene:
		line = line.strip().lower() # Remove extra spaces and lowercases
		complementary_seq = complementary_seq + line # Store sequence for later analysis
		# Count each nucleotide:
		for char in line:
			if char == "g":
				g = g + 1
			elif char == "c":
				c = c + 1
			elif char == "t":
				t = t + 1
			elif char == "a":
				a = a +1

	# Compute GC content
	total = g + a + c + t
	gc_content = (g + c) / total * 100 if total > 0 else 0

	# Generate complementary sequence
	complementarity = {"a":"t", "t":"a", "c":"g", "g":"c"}
	reverse_complementary_seq = "".join(complementarity[base] for base in reversed(complementary_seq)) 
	
	# Display results
	print(f"Number of G's: {g}")
	print(f"Number of C's: {c}")
	print(f"Number of A's: {a}")
	print(f"Number of T's: {t}")
	print(f"GC content: {gc_content:.2f}%")
	print(f"Reverse complement: {reverse_complementary_seq[:50]}")


