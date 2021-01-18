class DNA:
	def __init__(self, nucleotides):
		self.nucleotides = nucleotides

	def count_nucleotides(self):
		nucleotide_dict = dict()	
		nucleotide_dict.update({"A":self.nucleotides.count("A")})
		nucleotide_dict.update({"C":self.nucleotides.count("C")})
		nucleotide_dict.update({"G":self.nucleotides.count("G")})
		nucleotide_dict.update({"T":self.nucleotides.count("T")})
		return nucleotide_dict

	def calculate_complement(self):
		complement = ""
		for i in range(len(self.nucleotides)):
			if self.nucleotides[i] == "A":
				complement = complement + "T"
			elif self.nucleotides[i] == "T":
				complement = complement + "A"
			elif self.nucleotides[i] == "C":
				complement = complement + "G"
			elif self.nucleotides[i] == "G":
				complement = complement + "C"				

		return complement

	def count_point_mutations(self, dna):
		hamming_distance = 0
		for i in range((len(dna))):
			if dna[i] != self.nucleotides[i]:
				hamming_distance += 1
		return hamming_distance

	def find_motif(self, dna):
		
		locations = list()
		j = -1
		for i in range(self.nucleotides.count(dna)):
			j += 1
			j = self.nucleotides.index(dna[j:])
			locations.append(j)
		return locations

dna1 = DNA("ACGTTGCAACGTTACG")
print(dna1.count_nucleotides())
print(dna1.calculate_complement())
print(dna1.count_point_mutations("AGCTTTTTACGTTACG"))
print(dna1.find_motif("ACG"))			

