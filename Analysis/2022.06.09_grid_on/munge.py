import os.path
import gzip
#from itertools import izip

partners = ["Host", "Sym"]
reps = range(10,41)

header = "uid ecto_on endo_on grid_on sr update host_count sym_count free_sym_count hosted_sym_count sym_infectchance free_sym_infectchance hosted_sym_infectchance sym_val free_sym_val hosted_sym_val host_val cfu\n"

srs = [500, 1000]
outputFileName = "../grid_munged_data.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

folders = ["ectoendo", "ectoonly", "endoonly", "nointera", "off_ectoendo", "off_ectoonly", "off_endoonly", "off_nointera"]
values =  [[1,1,1], [1,0,1], [0,1,1], [0,0,1], [1,1,0], [1,0,0], [0,1,0], [0,0,0]]

for var in srs:
    for r in reps:
        for i in range(0, len(folders)):
            folder_prefix = folders[i] + "/"
            host_fname = folder_prefix + "HostValsSeed"+str(r)+"_SR" + str(var)+"_SEED"+str(r)+".data"
            fls_fname = folder_prefix +"FreeLivingSyms_Seed"+ str(r) + "_SR"+str(var)+"_SEED" + str(r)+".data"
            ecto_on = values[i][0]
            endo_on = values[i][1]
            grid_on = values[i][2]
            t = 1
            uid = str(t) + "_" + str(r)
            try:
                host_file = open(host_fname, 'r')
                fls_file = open(fls_fname, 'r')
                with open(host_fname) as host_file, open(fls_fname) as fls_file:
                    for host_line, fls_line in zip(host_file, fls_file):
                        if (host_line[0] != "u"):
                            host_line.strip()
                            fls_line.strip()
                            splitline = host_line.split(',')
                            flsline = fls_line.split(',')
                            outstring1 = "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(uid, ecto_on, endo_on, grid_on, var, splitline[0], splitline[2], flsline[1], flsline[2], flsline[3], flsline[7], flsline[8], flsline[9].strip(), flsline[4], flsline[5],flsline[6], splitline[1], splitline[3])
                            outFile.write(outstring1)
            except IOError:
    	        print "could not access files of type " + host_fname
outFile.close()
