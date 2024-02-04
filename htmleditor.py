import htmlgenerator as hgen

title = "9-best-beaches-in-the-world"

# Open a file for writing
file = open(f"{title}.html", "w")

# Write content to the file

a = hgen.initial(title)
b = hgen.boilerplate()
c = hgen.AMPstandalone(title,'TRA00269','beach','30th March 2023')
d = hgen.page('TRA00201','Baia-do-Sancho','Baia do Sancho, Brazil',"Located in the Fernando de Noronha archipelago, Baia do Sancho is consistently ranked as one of the world's best beaches for its pristine white sand, clear blue waters, and dramatic cliffs.",1)
e = hgen.page('TRA00202','Grace-Bay','Grace Bay, Turks and Caicos','With its turquoise waters and powdery sand, Grace Bay is a favorite among travelers for its calm and serene atmosphere.',2)
f = hgen.page('TRA00203','Anse-Lazio','Anse Lazio, Seychelles',"Situated on the island of Praslin, Anse Lazio is a breathtaking beach surrounded by lush tropical forests and granite boulders.",3)
g = hgen.page('TRA00204','Pink-Sands-Beach','Pink Sands Beach, Bahamas',"As its name suggests, this beach is famous for its stunning pink sand, which creates a unique and memorable landscape.",4)
h = hgen.page('TRA00205','Navagio-Beach','Navagio Beach, Greece',"Accessible only by boat, Navagio Beach is a hidden gem located on the Greek island of Zakynthos, with crystal-clear waters and a dramatic cove surrounded by towering cliffs.",5)
i = hgen.page('TRA00206','Whitehaven-Beach','Whitehaven Beach, Australia',"Located on Whitsunday Island in the Great Barrier Reef, Whitehaven Beach is a paradise of white sand, turquoise waters, and untouched nature.",6)
j = hgen.page('TRA00207','Matira-Beach','Matira Beach, French Polynesia',"Situated on the island of Bora Bora, Matira Beach is known for its soft white sand, shallow turquoise waters, and stunning sunsets.",7)
k = hgen.page('TRA00208','Tulum-Beach','Tulum Beach, Mexico',"This picturesque beach in the Riviera Maya offers a stunning combination of clear turquoise waters, white sand, and dramatic Mayan ruins.",8)
l = hgen.page('TRA00209','Lanikai-Beach','Lanikai Beach, Hawaii',"Located on the island of Oahu, Lanikai Beach is a hidden gem known for its turquoise waters, soft white sand, and breathtaking views of the nearby islands.",9)
n = hgen.ending()

file.write(a)
file.write(b)
file.write(c)
file.write(d)
file.write(e)
file.write(f)
file.write(g)
file.write(h)
file.write(i)
file.write(j)
file.write(k)
file.write(l)
file.write(n)

# Close the file
file.close()