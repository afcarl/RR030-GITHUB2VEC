

from __future__ import print_function
import os, sys
#import neat
#import visualize
#import subprocess
import time
import math

from shutil import copyfile
from subprocess import call
import time



#output_tmp = open( 'MD_copy_A.out' , 'w' )
output_tmp = open( 'WP_copy_b.out' , 'w' )

#output_tmp_MISSSING = open( 'JUGS_SPEED_CHART_MISSING_DATA.out' , 'w' )

#input_tmp = open( 'output_md.out', 'r' )
#input_tmp = open( 'output_html_081918.dat', 'r' )
input_tmp = open( 'output_1000.dat', 'r' )

test_input_tmp = input_tmp.readline()

#L:\Local_Git\zero-to-jupyterhub-k8s\doc\source\users-list.md
while test_input_tmp:

    str1a = test_input_tmp.replace(".html","").strip('\n')
    str1 = test_input_tmp.strip('\n')
    str1 = 'L:\\Local_Git\\' + str1
    #print("str1 = ", str1)
    #sys.exit(0)
    str2 = "\\"
    i_find = str1.rfind( str2 )
    str2_path = str1[0:i_find+1]
    str2_MD_filename = str1[i_find+1:]
    #print("str2_path = ", str2_path)
    #print("str2_MD_filename = ", str2_MD_filename)

    #str3_path = str2_path.replace('L:\\Local_Git\\','L:\\Local_Git\\0_MD\\')
    str3_path = str2_path.replace('L:\\Local_Git\\','L:\\Local_Git\\0_hold\\github.com\\afcarl\\')
    
    str4 = str3_path + str2_MD_filename
    #print("str3_path = ", str3_path)
    #print("str4 = ", str4)
    #sys.exit(0)
    

    try:
    #if 1 == 1:
        if not os.path.exists( str3_path ):
            os.makedirs( str3_path )
            src = str1
            dst = str4
            #try:
        #copyfile(src, dst)
        #pandoc test1.md -f markdown -t html -s -o test1.html
        ii_find = str4.rfind( '.' )
        str5 = str4[0:ii_find] + '.html'
        #print("str5 = ", str5)
        #sys.exit(0)
    
        #cmd = "pandoc " + str4 + " -f markdown -t html -s -o " + str5
        #cmd = "pandoc " + str1 + " -f markdown -t html -s -o " + str5
        #cmd = "python webpage2html.py " + "'https://github.com//afcarl//" + str1a + "' > " +  str4
        #cmd =  "pandoc -s -r html https://github.com//afcarl//" + str1a + " -o " + str4
        #cmd =  "pandoc -s -r html https://github.com//afcarl//"  + str1a + " -o  .//github.com//afcarl//" + str2_MD_filename
        cmd =  "pandoc -s -r html https://github.com//afcarl//"  + str1a + " -o  .//github.com//afcarl//" + str2_MD_filename + ".html"
        print("cmd = ", cmd)
        #sys.exit(0)
        os.system( cmd )
        time.sleep(0.100)
        sys.exit(0)
    except:
    #else:
        pass

    #sys.exit(0)
    #list_tmp = []
    #list_tmp = test_input_tmp.strip('\n').split(',')
    output_tmp.write( str5 + '\n' )
    test_input_tmp = input_tmp.readline()

input_tmp.close()

output_tmp.close()
print("DONE")

