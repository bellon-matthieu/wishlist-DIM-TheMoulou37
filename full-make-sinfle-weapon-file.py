import os

def check_file_existence(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

	
if __name__ == "__main__":

	with open("raw-text.txt") as raw_text_file:
		raw_text = raw_text_file.readlines()

	print(raw_text)

	first_item = True
	perks = [[],[],[],[],[]]

	for line in raw_text:

		actual_text_reading = ""
		actual_id_item = ""
		column_number = 0
		perk_number = ""

		

		for character in line:

			if actual_text_reading == "dimwishlist:item=":
				if character != '&':
					actual_id_item += character
				else:

					if first_item:
							first_item = False
							id_item = actual_id_item

					if actual_id_item != id_item:
						print("Les items ne correspondent pas")
						break

					actual_text_reading = ""
					continue

			elif actual_text_reading == "perks=":
				if character != "," and character != "\n":
					perk_number += character
				else:
					if perk_number == "":
						continue
					perks[column_number].append(perk_number)
					column_number += 1
					perk_number = ""
					continue
			else:
				actual_text_reading += character

	perks[column_number].append(perk_number)


		


	print(id_item)
	print(perks)
	output_mix = []


	for perk1 in perks[0]:
		for perk2 in perks[1]:
			for perk3 in perks[2]:
				for perk4 in perks[3]:
					for perk5 in perks[4]:
						output_mix.append("dimwishlist:item="+id_item+"&perks="+perk1+','+perk2+','+perk3+','+perk4+','+perk5)
		

	print(output_mix)
	print(len(output_mix))

with open('output.txt', 'w') as f:
    for line in output_mix:
       	f.write(f"{line}\n")
