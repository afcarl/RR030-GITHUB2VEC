

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

#import naivehtmlparser as NaiveHTMLParser
"""
Python 3.x HTMLParser extension with ElementTree support.
"""

from html.parser import HTMLParser
from xml.etree import ElementTree
from ehp import *
from copy import *

import validators
import re

from collections import defaultdict

        

def zpickle( obj, fname ):
    import pickle, gzip
    pickle.dump(obj=obj, file=gzip.open(fname, 'wb', compresslevel=3), protocol=2)

def zunpickle( fname ):
    import pickle, gzip
    return pickle.load(gzip.open(fname, "rb"))
    

class NaiveHTMLParser(HTMLParser):
    """
    Python 3.x HTMLParser extension with ElementTree support.
    @see https://github.com/marmelo/python-htmlparser
    """

    def __init__(self):
        self.root = None
        self.tree = []
        HTMLParser.__init__(self)

    def feed(self, data):
        HTMLParser.feed(self, data)
        return self.root

    def handle_starttag(self, tag, attrs):
        if len(self.tree) == 0:
            element = ElementTree.Element(tag, dict(self.__filter_attrs(attrs)))
            self.tree.append(element)
            self.root = element
        else:
            element = ElementTree.SubElement(self.tree[-1], tag, dict(self.__filter_attrs(attrs)))
            self.tree.append(element)

    def handle_endtag(self, tag):
        self.tree.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)
        pass

    def handle_data(self, data):
        if self.tree:
            self.tree[-1].text = data

    def get_root_element(self):
        return self.root

    def __filter_attrs(self, attrs):
        return filter(lambda x: x[0] and x[1], attrs) if attrs else []




#===========================
#===========================
i_1000_flag = 1
#i_1000_flag = 0
#===========================
#===========================




#output_tmp = open( 'MD_copy_A.out' , 'w' )
#output_tmp = open( 'html_parse_A.out' , 'w' )
#output_tmp = open( 'html_parse_F.out' , 'w' )
if i_1000_flag == 0:
    output_tmp = open( 'html_parse_H.out' , 'w' )
else:
    output_tmp = open( 'html_parse_H_1000.out' , 'w' )

#output_tmp_GITHUB = open( 'html_parse_A_GITHUB.out' , 'w' )
#output_tmp_GITHUB = open( 'html_parse_F_GITHUB.out' , 'w' )
if i_1000_flag == 0:
    output_tmp_GITHUB = open( 'html_parse_H_GITHUB.out' , 'w' )
else:
    output_tmp_GITHUB = open( 'html_parse_H_GITHUB_1000.out' , 'w' )

#output_tmp_GITHUB_AWESOME = open( 'html_parse_A_GITHUB_AWESOME.out' , 'w' )
#output_tmp_GITHUB_AWESOME = open( 'html_parse_F_GITHUB_AWESOME.out' , 'w' )
if i_1000_flag == 0:
    output_tmp_GITHUB_AWESOME = open( 'html_parse_H_GITHUB_AWESOME.out' , 'w' )
else:
    output_tmp_GITHUB_AWESOME = open( 'html_parse_H_GITHUB_AWESOME_1000.out' , 'w' )


#src_folder = 'L:/Local_Git/0_hold/github.com/afcarl/'
src_folder = './github.com/afcarl/'


output_tmp_GITHUB_set = set()
output_tmp_GITHUB_AWESOME_set = set()


#input_tmp = open( 'output_md.out', 'r' )
#input_tmp = open( 'out_html.out', 'r' )
if i_1000_flag == 0:
    #input_tmp = open( 'output_html_081918.dat', 'r' )
    input_tmp = open( 'output.dat', 'r' )
else:
    #input_tmp = open( 'output_html_081918_1000.dat', 'r' )
    input_tmp = open( 'output_1000.dat', 'r' )

test_input_tmp = input_tmp.readline()
#test_input_tmp = test_input_tmp.strip('\n') + ".html"

del_str = [0] * 70
#del_str = [0] * 69
del_str[ 0 ] = "GitHub is home to over 28 million developers working together to host and review code, manage projects, and build software together."
del_str[ 1 ] = "If nothing happens, download the GitHub extension for Visual Studio and try again."
del_str[ 2 ] = "You signed in with another tab or window. Reload to refresh your session."
del_str[ 3 ] = "You signed out in another tab or window. Reload to refresh your session."
del_str[ 4 ] = "If nothing happens, download GitHub Desktop and try again."
del_str[ 5 ] = "Use Git or checkout with SVN using the web URL."
del_str[ 6 ] = "If nothing happens, download Xcode and try again."
del_str[ 7 ] = "Cannot retrieve the latest commit at this time."
del_str[ 8 ] = "Press h to open a hovercard with more details."
del_str[ 9 ] = "You can’t perform that action at this time."
del_str[ 10 ] = "Failed to load latest commit information."
del_str[ 11 ] = "No suggested jump to results"
del_str[ 12 ] = "Launching GitHub Desktop..."
del_str[ 13 ] = "Launching Visual Studio..."
del_str[ 14 ] = "Fetching latest commit…"
del_str[ 15 ] = "Fetching contributors"
del_str[ 16 ] = "Switch branches/tags"
del_str[ 17 ] = "© 2018 GitHub, Inc."
del_str[ 18 ] = "Skip to content"
del_str[ 19 ] = "In this repository"
del_str[ 20 ] = "All GitHub"
del_str[ 21 ] = "Jump to"
del_str[ 22 ] = "Sign in"
del_str[ 23 ] = "Sign up"
del_str[ 24 ] = "Pull requests"
del_str[ 25 ] = "Join GitHub today"
del_str[ 26 ] = "Sign up"
del_str[ 27 ] = "Nothing to show"
del_str[ 28 ] = "Nothing to show"
del_str[ 29 ] = "New pull request"
del_str[ 30 ] = "Find file"
del_str[ 31 ] = "Clone or download"
del_str[ 32 ] = "Clone with HTTPS"
del_str[ 33 ] = "Download ZIP"
del_str[ 34 ] = "Go back"
del_str[ 35 ] = "Launching Xcode..."
del_str[ 36 ] = "Pull request"
del_str[ 37 ] = "Contact GitHub"
del_str[ 38 ] = "Features"
del_str[ 39 ] = "Business"
del_str[ 40 ] = "Explore"
del_str[ 41 ] = "Marketplace"
del_str[ 42 ] = "Pricing"
del_str[ 43 ] = "Watch"
del_str[ 44 ] = "Star"
del_str[ 45 ] = "Fork"
del_str[ 46 ] = "Code"
del_str[ 47 ] = "Projects"
del_str[ 48 ] = "Insights"
del_str[ 49 ] = "Dismiss"
del_str[ 50 ] = "commits"
del_str[ 51 ] = "branches"
del_str[ 52 ] = "releases"
del_str[ 53 ] = "Branch:"
del_str[ 54 ] = "master"
del_str[ 55 ] = "Permalink"
del_str[ 56 ] = "Tags"
del_str[ 57 ] = "Compare"
del_str[ 58 ] = "Terms"
del_str[ 59 ] = "Privacy"
del_str[ 60 ] = "Security"
del_str[ 61 ] = "Status"
del_str[ 62 ] = "Help"
del_str[ 63 ] = "Pricing"
del_str[ 64 ] = "API"
del_str[ 65 ] = "Training"
del_str[ 66 ] = "Blog"
del_str[ 67 ] = "About"
del_str[ 68 ] = "Branches"
del_str[ 69 ] = u'\u21b5'
#del_str[ 69 ] = "↵"
#del_str[ 69 ] = " or "


#output_tmp_tmp_out_all = open('html_parse_E_ALL.txt','w')
#output_tmp_tmp_out_all = open('html_parse_F_ALL.txt','w')
if i_1000_flag == 0:
    output_tmp_tmp_out_all = open('html_parse_H_ALL.txt','w')
else:
    output_tmp_tmp_out_all = open('html_parse_H_ALL_1000.txt','w')

#output_tmp_tmp_out_all_labels = open('html_parse_E_ALL_LABELS.txt','w')
#output_tmp_tmp_out_all_labels = open('html_parse_F_ALL_LABELS.txt','w')
if i_1000_flag == 0:
    output_tmp_tmp_out_all_labels = open('html_parse_H_ALL_LABELS.txt','w')
else:
    output_tmp_tmp_out_all_labels = open('html_parse_H_ALL_LABELS_1000.txt','w')

char_set = set()

forked_author_dict = defaultdict(set)
forked_author_to_titles_dict = defaultdict(list)

repo_title_set = set()

i_stop_flag = 0
i_AWESOME_flag = 0
#L:\Local_Git\zero-to-jupyterhub-k8s\doc\source\users-list.md
while test_input_tmp:

    test_input_tmp = test_input_tmp.strip('\n') + ".html" + '\n'
        
    string_a = test_input_tmp.strip('\n').lower()
    i_find = string_a.find("awesome")
    if ( i_find != -1 ):
        i_AWESOME_flag = 1

    str1 = test_input_tmp.strip('\n')
    str2 = "\\"
    i_find = str1.rfind( str2 )
    str2_path = str1[0:i_find+1]
    str2_MD_filename = str1[i_find+1:]
    #print("str2_path = ", str2_path)
    #print("str2_MD_filename = ", str2_MD_filename)
    str3_path = str2_path.replace('L:\\Local_Git\\','L:\\Local_Git\\0_MD\\')
    str4 = str3_path + str2_MD_filename
    #print("str4 = ", str4)
    print("str1 = ", str1)
    

    '''try:
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
        cmd = "pandoc " + str1 + " -f markdown -t html -s -o " + str5
        os.system( cmd )
        time.sleep(0.100)
    except:
        pass'''

    #try:
    if 1==1:
        i_tmp = 0
        data = None
        try:
            with open( src_folder + str1 , 'r') as myfile:
                html = myfile.read()
        except:
            try:
                with open( src_folder + str1 , 'r', encoding="utf8") as myfile:
                    html = myfile.read()
            except:
                pass
            #i_tmp += 1
            #print("i_tmp = ", i_tmp, html)
        #print(html)
        #output_tmp.write(str(html) + '\n' )

        
        '''try: 
            from BeautifulSoup import BeautifulSoup
        except ImportError:
            from bs4 import BeautifulSoup
        #html = #the HTML code you've written above
        parsed_html = BeautifulSoup(html)
        print( parsed_html.body.find('div', attrs={'class':'container'}).text)        
        sys.exit(0)'''
        '''test.replace('try','xxx')
        print("test = ", test )
        i_find = test.find('try')
        print("i_find = ", i_find)
        test.replace('try','xxx')
        i_find = test.find('try')
        print("i_find = ", i_find)'''
        

        htmll = Html()
        data = html
        dom = htmll.feed(data)
        #print(dom.text())
        #output_tmp.write(str( dom.text() ) + '\n' )
        #print("str1 = ", str1)
        #print("type(dom.text()) = ",type(dom.text()))
        #print("len(dom.text()) = ",len(dom.text()))
        list_tmp = dom.text().splitlines()
        i_accum = 0
        #for s_tmp in dom.text():
        for s_tmp in list_tmp:
            i_accum += 1
            #output_tmp.write( "i_accum = " + str( i_accum ) + "   s_tmp = " + str( s_tmp ) + '\n' )
            if s_tmp.find( "forked from" ) >= 0:
            #if s_tmp.find( "Press h to" ) != -1:
                #print("s_tmp = ",s_tmp)
                s_tmp = s_tmp.replace( "forked from " , "")
                #print("s_tmp = ",s_tmp)
                list_tmp_tmp = s_tmp.split("/")
                #list_tmp_tmp = s_tmp.split("/").replace(" ","")
                #print("list_tmp_tmp = ",list_tmp_tmp)
                repo_author = list_tmp_tmp[ 0 ].replace(" ","")
                #print("repo_author = ",repo_author)
                #repo_name = str1.strip(".html").strip('\n').replace(" ","")
                repo_name = str1.replace(" ","").replace(".html","").strip('\n')
                if repo_author == "EricSchles":
                    #print("repo_author = ",repo_author)
                    #print("str1 = ",str1)
                    #print("repo_name = ", repo_name)
                    #print("list_tmp_tmp = ", list_tmp_tmp)
                    #print("list_tmp_tmp[ 0 ] = ", list_tmp_tmp[ 0 ])
                    output_tmp.write( repo_author + ' ' + repo_name + ' ' + str1 + '\n' )
                    #if repo_name.upper() == "HEURISTICS":
                    #    output_tmp.flush()
                    #    sys.exit(0)
                    #if str1 == "alert_system.html":
                    #    output_tmp.flush()
                    #    sys.exit(0)

                #print("repo_name = ",repo_name)
                forked_author_dict[ repo_name ].add( repo_author )
                forked_author_to_titles_dict[ repo_author ].append( repo_name )
                #sys.exit(0)
        #sys.exit(0)
        #dom_text_working = deepcopy(dom.text())
        dom_text_working = deepcopy(dom.text()).encode("utf-8")
        
        output_tmp_tmp = open('tmp.tmp','w')
        #output_tmp_tmp.write( str(dom.text()) + '\n')

        #string_X = (dom.text()).replace(u"\u21b5", " ")
        string_X = dom_text_working
        '''string_X = dom_text_working.replace(u"\u21b5", " ")
        string_X = string_X.replace(u"\u2197", " ")
        string_X = string_X.replace(u"\U0001f4f7", " ")
        string_X = string_X.replace(u"\U0001f47e", " ")
        string_X = string_X.replace(u"\U0001f3b2", " ")
        string_X = string_X.replace(u"\U0001f48e", " ")
        string_X = string_X.replace(u"\U0001f48a", " ")'''
        #string_X = (string_X.decode("utf-8")).encode("ascii")
        
        #output_tmp_tmp.write( (dom.text()).replace(u"\u21b5", " ").replace(u"\u2197", " ").replace(u"\U0001f4f7", " ").replace(u"\U0001f47e", " ") + '\n')
        #output_tmp_tmp.write( string_X + '\n')
        #output_tmp_tmp.write( str(string_X) + '\n')
        #string_X_tmp = str(string_X).replace('\\n',' ').replace('  ',' ')
        string_X_tmp = str(string_X)
        string_X_tmp_list = list(string_X_tmp)
        for i_char in range(0,len(string_X_tmp)):
            if string_X_tmp[i_char:i_char+2] == '\\x':
                #print(string_X_tmp[i_char:i_char+4])
                string_X_tmp_list[i_char] = ' '
                string_X_tmp_list[i_char+1] = ' '
                string_X_tmp_list[i_char+2] = ' '
                string_X_tmp_list[i_char+3] = ' '
                #sys.exit(0)
            
        #string_X = (''.join(string_X_tmp_list)).replace('  ',' ')
        #string_X = string_X.replace('  ',' ')
        #string_X = string_X.replace('  ',' ')
        #string_X = string_X.replace('  ',' ')
        #string_X = string_X.replace('  ',' ')
        #string_X = string_X.replace('  ',' ').lower()
            
        string_X = ''.join(string_X_tmp_list)
        output_tmp_tmp.write( string_X + '\n')
        
        i_start = 0
        #while string_X.find('\\n'):
        while string_X.find('\\n') != -1:
            i_find = string_X.find('\\n')
            #output_tmp_tmp.write( '\n')
            #output_tmp_tmp.write( string_X[0:i_find+2] + '\n')
            output_tmp_tmp.write( string_X[0:i_find] + '\n')
            i_start = i_find + 2
            #string_X = string_X[i_start:-1]
            string_X = string_X[i_start:]
            #output_tmp_tmp.write( "*** " + string_X + '\n')
            #sys.exit(0)        
        output_tmp_tmp.flush()
        #sys.exit(0)        

        
        #output_tmp_tmp.write( str(string_X).replace('\\n',' ').replace('  ',' ') + '\n')
        #output_tmp_tmp.write( str(''.join(string_X_tmp_list)) + '\n')
        output_tmp_tmp.write( string_X[2:-2].strip() + '\n')
        '''try:
            output_tmp_tmp.write( string_X + '\n')
        except:
            #print("string_X = ", string_X)
            print("7115 = ",string_X[7100:7120])
            print("7115 = ",string_X[7115])
            print("7116 = ",string_X[7116])
            sys.exit(0)'''
        output_tmp_tmp.close()
        
        output_tmp_tmp = open('tmp.tmp','r')
        output_tmp_tmp_out = open('tmp_out.tmp','w')
        
        i_first_time_flag = 0
        test_output_tmp_tmp = output_tmp_tmp.readline()
        while test_output_tmp_tmp:
        
            i_match_flag = 0
            for s_tmp in del_str:
                #print("s_tmp = ", s_tmp)
                #print("test_output_tmp_tmp = ", test_output_tmp_tmp)
                #if ( test_output_tmp_tmp.rfind(s_tmp) != -1 ):
                #if ( test_output_tmp_tmp.strip().find(s_tmp) != -1 ):
                if ( test_output_tmp_tmp.strip('\n').strip().find(s_tmp) != -1 ):
                    #print("s_tmp = ", s_tmp)
                    #print("test_output_tmp_tmp = ", test_output_tmp_tmp.strip('\n'))
                    #print("Compare = ", ( test_output_tmp_tmp.rfind(s_tmp) != -1 ) )
                    #string_out = test_output_tmp_tmp.replace( s_tmp , ' ' )
                    #output_tmp_tmp_out.write( string_out )
                    i_match_flag = 1
                    break

            if i_match_flag == 0:
                #output_tmp_tmp_out.write( test_output_tmp_tmp )
                #output_tmp_tmp_out.write( test_output_tmp_tmp.strip() + '\n' )
                #if len( test_output_tmp_tmp.strip() ) > 0:
                #if len( test_output_tmp_tmp.strip() ) > 1:
                if ( len( test_output_tmp_tmp.strip() ) > 1 ) and ( i_first_time_flag == 1 ):
                    #output_tmp_tmp_out.write( test_output_tmp_tmp.strip() + '\n' )
                    string_123 = test_output_tmp_tmp.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').strip()
                    #string_123 = re.sub(r'^https?:\/\/.*[\r\n]*', '', string_123, flags=re.MULTILINE)
                    URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', string_123)
                    #output_tmp_tmp_out.write( test_output_tmp_tmp.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').strip() + '\n' )
                    #output_tmp_tmp_out.write( string_123 + '\n' )
                    output_tmp_tmp_out.write( URLless_string + '\n' )
                if ( i_first_time_flag == 0 ):
                    i_first_time_flag = 1
                
            test_output_tmp_tmp = output_tmp_tmp.readline()
        output_tmp_tmp.close()
        output_tmp_tmp_out.close()
        #sys.exit(0)
                
            
        #output_tmp.write( str(dom.text()) + '\n')
        output_tmp.write( '******' + '\n')
        output_tmp.write( '******' + '\n')
        output_tmp.write( '******' + '\n')
        output_tmp_tmp_out = open('tmp_out.tmp','r')
        output_html_to_txt = open( src_folder + str1.replace('.html','.txt') , 'w')
        
        #if str1 == 'ml.html':
        #    print("str1 = ",str1)
        #    i_stop_flag = 1
        
        #repo_name_parsed = str1.strip('.html').replace('-',' ').replace('_',' ') + ' '
        repo_name_parsed = str1.strip('.html').replace('-',' ').replace('_',' ')
        output_html_to_txt.write( repo_name_parsed.lower() + ' ' )
        output_tmp_tmp_out_all.write( repo_name_parsed.lower() + ' ' )
        
        test_output_tmp_tmp_out = output_tmp_tmp_out.readline()
        URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', test_output_tmp_tmp_out)
        URLless_string = URLless_string.replace('-',' ')
        URLless_string = URLless_string.replace('/',' ')
        URLless_string = URLless_string.replace(':',' ')
        URLless_string = URLless_string.replace('.',' ')
        URLless_string = URLless_string.replace('%',' ')
        URLless_string = URLless_string.replace(',',' ')
        URLless_string = URLless_string.replace('$',' ')
        URLless_string = URLless_string.replace('(',' ').replace('@',' ').replace('|',' ')
        URLless_string = URLless_string.replace(')',' ').replace('^',' ').replace('~',' ').replace('`',' ')
        URLless_string = URLless_string.replace('#',' ').replace('*',' ').replace('"',' ').replace("'",' ').replace(";",' ').replace("=",' ').replace("+",' ').replace("\\",' ').replace("&",' ').replace("_",' ').replace("[",' ').replace("]",' ').replace("{",' ').replace("}",' ').replace("!",' ').replace("?",' ').replace("<",' ').replace(">",' ')
        #URLless_string = URLless_string.strip().replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')
        URLless_string = URLless_string.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').lower()

        for i_char in range(0,len(URLless_string)):
            char_set.add(URLless_string[i_char])



        
        while test_output_tmp_tmp_out:
            
            #output_tmp.write( test_output_tmp_tmp_out )
            output_tmp.write( URLless_string )
            
            #output_html_to_txt.write( test_output_tmp_tmp_out )
            #output_html_to_txt.write( test_output_tmp_tmp_out.replace('\n',' ').lower() )
            output_html_to_txt.write( URLless_string.replace('\n',' ').lower() )
            #output_html_to_txt.write( URLless_string.lower() )
            #output_html_to_txt.write( URLless_string.replace('\n',' ').replace('  ',' ').lower() )
            
            #output_tmp_tmp_out_all.write( test_output_tmp_tmp_out.replace('\n',' ').lower() )
            #output_tmp_tmp_out_all.write( test_output_tmp_tmp_out.replace('\n',' ').replace('  ',' ').lower() )
            #output_tmp_tmp_out_all.write( URLless_string.replace('\n',' ').replace('  ',' ').lower() )
            output_tmp_tmp_out_all.write( URLless_string.replace('\n',' ').lower() )
            #output_tmp_tmp_out_all.write( URLless_string.lower() )
            
            test_output_tmp_tmp_out = output_tmp_tmp_out.readline()
            URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', test_output_tmp_tmp_out)
            URLless_string = URLless_string.replace('-',' ')
            URLless_string = URLless_string.replace('/',' ')
            URLless_string = URLless_string.replace(':',' ')
            URLless_string = URLless_string.replace('.',' ')
            URLless_string = URLless_string.replace('%',' ')
            URLless_string = URLless_string.replace(',',' ')
            URLless_string = URLless_string.replace('$',' ')
            URLless_string = URLless_string.replace('(',' ').replace('@',' ').replace('|',' ')
            URLless_string = URLless_string.replace(')',' ').replace('^',' ').replace('~',' ').replace('`',' ')
            URLless_string = URLless_string.replace('#',' ').replace('*',' ').replace('"',' ').replace("'",' ').replace(";",' ').replace("=",' ').replace("+",' ').replace("\\",' ').replace("&",' ').replace("_",' ').replace("[",' ').replace("]",' ').replace("{",' ').replace("}",' ').replace("!",' ').replace("?",' ').replace("<",' ').replace(">",' ')
            #URLless_string = URLless_string.strip().replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')
            URLless_string = URLless_string.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').lower()

            for i_char in range(0,len(URLless_string)):
                char_set.add(URLless_string[i_char])
            
        output_tmp_tmp_out.close()
        #html_to_text_file_size = os.path.getsize( 'tmp_out.tmp' )
        output_tmp_tmp_out_all.write( '\n' )
        #output_tmp_tmp_out_all.write( "html_to_text_file_size = " + str(html_to_text_file_size) + '\n' )
        
        #output_tmp_tmp_out_all_labels.write( str1.strip('.html').strip('\n') + '\n' )
        output_tmp_tmp_out_all_labels.write( test_input_tmp.replace('.html','') )
        
        repo_title_set.add( test_input_tmp.replace('.html','').strip('\n' ) )
        
        #if i_stop_flag == 1:
        #    sys.exit(0)
        
        output_html_to_txt.write( '\n' )
        output_html_to_txt.close()
        #sys.exit(0)


        
        parser = NaiveHTMLParser()
        root = parser.feed(html)
        #root = parser.handle_data(html)
        #print("parser.feed(html) = ", parser.feed(html))
        #print("len(parser.feed(html)) = ", len(parser.feed(html)))
        parser.close()
        #sys.exit(0)
        
        #output_html_to_txt = open( src_folder + str1.replace('.html','.txt') , 'w')
        #print("output_html_to_txt = ", src_folder + str1.replace('.html','.txt') )
        #print("root = ", root )
        #print("len(root) = ", len(root) )
        #print("type(root) = ", type(root) )
        #sys.exit(0)
    
        # get all anchors
        for a in root.findall('.//a'):
        #for a in root.findtext('.//a'):
            #print(a.get('href'))
            #print(a.get('text'))
            #print(a.get('data'))
            #print("a = ",a)
            #print("a.findtext() = ",a.findtext())
            #print("type(a) = ",type(a))
            #sys.exit(0)
            output_tmp.write( "a = " + str(a) + '\n' )
            
            regex = re.compile(
                    r'^(?:http|ftp)s?://' # http:// or https://
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                    r'localhost|' #localhost...
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                    r'(?::\d+)?' # optional port
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

            if re.match(regex, str( a.get('href') ) ) is not None:

                #output_html_to_txt.write( str( a.get('href') ) + '\n' )

                #if i_AWESOME_flag == 1:
                #    output_tmp_GITHUB_AWESOME.write( str( a.get('href') ) + '\n' )



                #print( str( a.get('href') ))
                #sys.exit(0)
                #if validators.url( str( a.get('href') ) ):
                '''output_tmp.write( str( a.get('href') ) + '\n' )
                iii_find = str.lower( a.get('href') ).find("https://github.com/")
                iv_find = str.lower( a.get('href') ).find("/blob")
                v_find = str.lower( a.get('href') ).find("/master")
                vi_find = str.lower( a.get('href') ).find("/tree")
                vii_find = str.lower( a.get('href') ).find("/release")
                viii_find = str.lower( a.get('href') ).find("/wiki")
                vix_find = str.lower( a.get('href') ).find("#")
                vx_find = str.lower( a.get('href') ).find("/issues")
                vxi_find = str.lower( a.get('href') ).find("/pull")
                vxii_find = str.lower( a.get('href') ).find("/contributors")
                vxiii_find = str.lower( a.get('href') ).find("/commit/")
                vxix_find = str.lower( a.get('href') ).count("/")
                #if str.lower( a.get('href') ).find("https://github.com/") != -1:
                if ( iii_find != -1 ) and ( iii_find == 0 ) and ( iv_find == -1 ) and \
                   ( v_find == -1 ) and ( vi_find == -1 ) and ( vii_find == -1 ) and \
                   ( viii_find == -1 ) and ( vix_find == -1 ) and ( vx_find == -1 ) and \
                   ( vxi_find == -1 ) and ( vxii_find == -1 ) and ( vxiii_find == -1 ) and \
                   ( vxix_find == 4 ):
                    output_tmp_GITHUB.write( str( a.get('href') ) + '\n' )
                    output_tmp_GITHUB_set.add( str( a.get('href') ) )
                    
                    if i_AWESOME_flag == 1:
                        #output_tmp_GITHUB_AWESOME.write( str( a.get('href') ) + '\n' )
                        output_tmp_GITHUB_AWESOME_set.add( str( a.get('href') ) )'''

        #output_html_to_txt.close()
        #sys.exit(0)

    #except:
    #    pass 

    #sys.exit(0)

    #sys.exit(0)
    #list_tmp = []
    #list_tmp = test_input_tmp.strip('\n').split(',')
    #output_tmp.write( str5 + '\n' )
    test_input_tmp = input_tmp.readline()
    #test_input_tmp = test_input_tmp.strip('\n') + ".html"



print("len(forked_author_dict) = ", len(forked_author_dict) )
if i_1000_flag == 0:
    zpickle( forked_author_dict , 'forked_author_dict.zpkl' )
else:
    zpickle( forked_author_dict , 'forked_author_dict_1000.zpkl' )

print("len(forked_author_to_titles_dict) = ", len(forked_author_to_titles_dict) )
if i_1000_flag == 0:
    zpickle( forked_author_to_titles_dict , 'forked_author_to_titles_dict.zpkl' )
else:
    zpickle( forked_author_to_titles_dict , 'forked_author_to_titles_dict_1000.zpkl' )
#sys.exit(0)

output_tmp_GITHUB.write('\n' )
output_tmp_GITHUB.write('******' + '\n' )
output_tmp_GITHUB.write('\n' )
for item in output_tmp_GITHUB_set:
    output_tmp_GITHUB.write( item + '\n' )
print("len(output_tmp_GITHUB_set) = ", len(output_tmp_GITHUB_set) )

output_tmp_GITHUB_AWESOME.write('\n' )
output_tmp_GITHUB_AWESOME.write('******' + '\n' )
output_tmp_GITHUB_AWESOME.write('\n' )
for item in output_tmp_GITHUB_AWESOME_set:
    output_tmp_GITHUB_AWESOME.write( item + '\n' )
print("len(output_tmp_GITHUB_AWESOME_set) = ", len(output_tmp_GITHUB_AWESOME_set) )
    
input_tmp.close()

output_tmp.close()

output_tmp_tmp_out_all.close()
output_tmp_tmp_out_all_labels.close()


print("len(repo_title_set) = ", len(repo_title_set) )
if i_1000_flag == 0:
    zpickle( repo_title_set , 'repo_title_set.zpkl' )
else:
    zpickle( repo_title_set , 'repo_title_set_1000.zpkl' )

output_tmp_GITHUB.close()
output_tmp_GITHUB_AWESOME.close()

print()
print("char_set = ",char_set)


print("DONE")

