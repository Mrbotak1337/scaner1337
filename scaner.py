#!/usr/bin/python

# c0dEd By Mr.b0t4k

# We Are Bitch

# for tuto ethical hacking and tools visit us in : www.facebook.com/

# we Are Dog

# Greetz To :  ./Xi4u7 ~ xGans ~ Dro!der_404 ~ Mr_/bon'007 ~ Deadrz_404 ~ Mr.Holmes ~ V-Z3R0 ~ Anb3rSecID ~ Mr.b0t4k ~ ID_OUT96 ~ J_Lynx69 ~ ASynCroRa ~ Elang X-CoderID ~ Silen7 ~ Mr.Falcon./404 ~ C4bnL ~ X-Mr.R4h1M ~ MR.DRMN404 ~ /Ms_L4zDy ~ AndrGhost ~ M1nic0de ~ N07_4L0N3 ~ Exten5i0n ~  SQL47- ID ~ Mrs.C4pun9 ~ CynoWhite

import sys

import time

import httplib



mtucx = 1

dzx = 4



print '**********************************************************'

print '*   ___  ___ _             __   __                       *'

print '*   |  \/  || |            \ \ / /                       *'

print '*   | .  . || |_ _   _  ___ \ V /                        *'

print '*   | |\/| || __| | | |/ __|/   \                        *'

print '*   | |  | || |_| |_| | (__/ /^\ \                       *'

print '*   \_|  |_(_)__|\__,_|\___\/   \/                       *'

print '* We Are :  ./Xi4u7 ~ xGans ~ Dro!der_404 ~ Mr_/bon'007 ~ Deadrz_404 ~ Mr.Holmes ~ V-Z3R0 ~ Anb3rSecID ~ Mr.b0t4k ~ ID_OUT96 ~ J_Lynx69 ~ ASynCroRa ~ Elang X-CoderID ~ Silen7 ~ Mr.Falcon./404 ~ C4bnL ~ X-Mr.R4h1M ~ MR.DRMN404 ~ /Ms_L4zDy ~ AndrGhost ~ M1nic0de ~ N07_4L0N3 ~ Exten5i0n ~  SQL47- ID ~ Mrs.C4pun9 ~ CynoWhite  *'

print '* visit us in: https://www.facebook.com/WelcomeToMr.b0t4kTamvan         *'

print '*                    pyhthon wordpress.py www.target.com *'

print '**********************************************************'



BAD_RESP = [400,401,404]







def main(path):



    print "Scan:",host.split("/",1)[1]+path



    try:



        h = httplib.HTTP(host.split("/",1)[0])



        h.putrequest("HEAD", "/"+host.split("/",1)[1]+path)



        h.putheader("Host", host.split("/",1)[0])



        h.endheaders()



        resp, reason, headers = h.getreply()



        return resp, reason, headers.get("Server")



    except(), msg:



        print "Error Occurred:",msg



        pass







def timer():



    now = time.localtime(time.time())



    return time.asctime(now)





dzx = { "wp-content/themes/linenity/functions/download.php?imgurl=1" : ["LFI WordPress Theme LineNity"], "career-details-2/?jobid=1" : ["SQl injection (Career2)"], "career-details/?jobid=" : ["SQl Injection (Career)"],"wp-content/themes/dandelion/" : ["www.exploit-db.com/exploits/31571/"],"wp-content/uploads/feuGT_uploads/feuGT_1790_43000000_948109840.php" : ["http://www.exploit-db.com/exploits/31570/"] , "wp-content/plugins/formcraft/form.php?id=1" : ["Wordpress formcraft Plugin Sql Injection"],"wp-content/themes/kernel-theme/functions/upload-handler.php" : ["http://www.exploit-db.com/exploits/29482/"], "wp-content/themes/saico/framework/_scripts/valums_uploader/php.php" : ["http://www.exploit-db.com/exploits/29150/"],"wp-content/themes/ThinkResponsive/includes/uploadify/upload_settings_image.php" : ["http://www.exploit-db.com/exploits/29332/"],"wp-content/themes/rockstar-theme/functions/upload-handler.php" :["http://www.exploit-db.com/exploits/29946/"],"wp-content/plugins/page-flip-image-gallery/upload.php" : ["http://www.exploit-db.com/exploits/30084/"],"wp-content/plugins/dzs-videogallery/deploy/designer/preview.php?swfloc=" : ["(dzs-videogallery) 3.1.3 Plugins Remote and LFD Vulnerability"],"wp-content/themes/area53/framework/_scripts/valums_uploader/php.php" : ["http://www.exploit-db.com/exploits/29068/"],"wp-content/plugins/wp-realty/index_ext.php?action=contact_friend&popup=yes&listing_id=1" : ["wp-realty - MySQL Time Based Injection"],"wp-content/plugins/lazy-seo/lazyseo.php" : ["Lazy SEO plugin Shell Upload Vulnerability"],"wp-content/plugins/complete-gallery-manager/frames/upload-images.php" : ["http://www.exploit-db.com/exploits/28377/"] , "wp-content/plugins/proplayer/playlist-controller.php?id=1" : ["ProPlayer Plugin SQL Injection"]}







if len(sys.argv) != 2:



    sys.exit(1)







host = sys.argv[1].replace("http://","").rsplit("/",1)[0]



if host[-1] != "/":



    host = host+"/"







print "\nTarget:",host



print "\nScanning Exploit\n"



for xpl,(poc) in dzx.items():



    resp,reason,server = main(xpl)



    if resp not in BAD_RESP:



        print ""



        print "\nResult:",resp, reason



        print "\nVuln",poc



    else:



        print ""



        print "\nResult:",resp, reason



        print



print "\nEnd\n"