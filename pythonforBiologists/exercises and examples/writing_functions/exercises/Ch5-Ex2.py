#! /usr/local/bin python3

def my_function(aa_seq, aa_list = ['a', 'i', 'l', 'm', 'f', 'w', 'v']):
	print(aa_seq)
	print(aa_list)
	aa_count = 0
	for aa in aa_list:
		print(aa)
		aa_count = aa_count + aa_seq.upper().count(aa.upper())
	aa_percent = (aa_count / len(aa_seq)) * 100
	print(aa_percent)
	return round(aa_percent, 2)

assert my_function("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65

print("All functions passed")
	
