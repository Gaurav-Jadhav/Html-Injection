# -*- coding: utf-8 -*-
#Gaurav
#  This program is free ; you can redistribute it and/or modify
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY;
#Author details
# Created this simple html scaner file according to my use hope it will be useful

__author__ = "Gaurav Jadhav"
__version__ = "0.0.1"

from urllib.parse import parse_qsl, urlencode, urlsplit
import sys ,requests, re,time,argparse,getopt,sys,logs,json,html
import urllib.parse
import  socket,hashlib,os,datetime
from sys import argv, exit, version_info

timestamp= datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
cwd = os.path.dirname(os.path.abspath( __file__ ))
sys.path.insert(0,cwd+'/..')


work_dir = cwd +'/logs/'
print (work_dir)



def scan_html(payload,url):
        param = dict(parse_qsl(urlsplit(url).query))
        tainted_params = {x: payload for x in param}
        logs.create_log(logs_des,"Params : "+str(tainted_params))
        if len(tainted_params) > 0:
                attack_url = urlsplit(url).geturl() + urlencode(tainted_params)
                resp = requests.post(url=attack_url, data = payload)
                if resp.status_code == 200:
                        if payload in resp.text:
                                attack_encode=html.escape(attack_url)
                                logs.create_log(logs_des,"HTML Injection Found : "+str(attack_url))
                                print("HTML Injection at %s\nInjection",attack_url)
                        else:
                                logs.create_log(logs_des,"No HTML Injection Found  : "+str(url))
                                print("This URL is not Vulnerable" )

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument('-url',  help='Plase enter valid URL example: http://testphp.vulnweb.com/listproducts.php?cat=2')
        parser.add_argument('-ul',help='Plase provide URL List File ')
        parser.add_argument('-d',  required=True,help='Domain Name example: esds.co.in')
        args = parser.parse_args()
        url_s = args.url
        url_file = args.ul
        domain =args.d

        #store logs with domain name and timestamp
        logs_des = work_dir+str(domain)+timestamp+'.txt'

        logs.create_log(logs_des,"Scanning Started for : "+str(domain))
        payload="<h1><a href='https://www.google.com/'> Vulnerable Link </a></h1>"
        logs.create_log(logs_des,"Payload Used : "+str(payload))

        ''''Execute for multiple URL'S'''
        if url_file:
            #read url list file and strip \n and close file
            fh=open(url_file)
            test = [line.rstrip() for line in fh.readlines()]
            fh.close()

            #REGEX that will match applicable urls ex: "php?cat=2"
            url_s = []
            pattern = '.*\?((.*=.*)(&?))+'
            print(test)
            for urls in test:
                    if re.match(pattern,urls):
                            apl_length = len(test)
                            logs.create_log(logs_des,"Applicable urls count."+str(apl_length))
                            scan_html(payload,urls)
                    else:
                            print ("No applicable URL's found  ")
                            logs.create_log(logs_des,"No Applicable URLs found."+str(urls))

        else:
            scan_html(payload,url_s)
