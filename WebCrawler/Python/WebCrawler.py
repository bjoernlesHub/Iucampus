#########################################################################################################################
#This Python App sending mails if one word of a list existing in a ebay-kleinanzeigen.de "for free" list item			
#
#Author: Björn Leue
#########################################################################################################################

import communication
import sql
import crawler
import files
import system
import globals
import sqlite
import settingsChanger

import json
import sys

current_path=globals.get_current_path()
settings_json=globals.get_settings_json()

main_url="https://www.ebay-kleinanzeigen.de"
if len(sys.argv) > 1:
    settings_json=settingsChanger.set_new_settings(settings_json,sys.argv)
    #print('Argument List:', str(sys.argv))
    #print(settings_json["jobs"][0]["words"])
    #for arg in sys.argv:
        #print(arg)

#print(current_path)


if settings_json["use_sql_sqlite"]=="sql":
    sql.delete_old_rows(current_path,"ebaykleinanzeigenzeugs","datetime")
elif settings_json["use_sql_sqlite"]=="sqlite":
    sqlite.delete_old_rows(current_path,"ebaykleinanzeigenzeugs","datetime")
elif settings_json["use_sql_sqlite"]=="both":
    sqlite.delete_old_rows(current_path,"ebaykleinanzeigenzeugs","datetime")
    sql.delete_old_rows(current_path,"ebaykleinanzeigenzeugs","datetime")

#communication.get_skype_recent_contacts("bjoernle@gentlemansclub.de", "MicrosoftPwd18")
current_item_url=""
current_item_name=""
before_found_items=0
current_found_items=0
current_count_real_items=0

#settings_json["jobs"]=[]
for job in settings_json["jobs"]:
    cnt=0
    collection=[]
    searchfor=job["words"].split(",")

    #if job["name"] != "blubb":
    if job["name"] == "bjoerns ebay-kleinanzeigen suche":
        print("Job: "+job["name"])
        print("Search for: "+job["words"])
        radius="r"        
        if int(job["radius"]) > 0:
            radius+=job["radius"]
        url=job["url"]+"/"+job["subpage"]+"/"+job["plz"]+"/c272l17124"+radius

#get collection from website        
        collection=crawler.get_value_from_website_by_class(url, job["html_element"], job["html_class"])
        searchfor=str(job["words"]).split(",")
        if len(collection) > 0:
            from bs4 import BeautifulSoup
            from datetime import datetime, timedelta
    
            mail_text_list=[]
            print("Quantity of all items: "+str(len(collection)))
            for entity in collection:
                cnt=cnt+1

                if str(type(entity)) != "<class 'bs4.element.Tag'>":
                    entity = BeautifulSoup(entity)

                name = entity.find("a", class_="ellipsis")
                description = entity.find("p", class_="aditem-main--middle--description")
                if name is not None or description is not None:
                    current_count_real_items+=1
                    long_string=name.text+" "+description.text
                    if any(word in long_string.upper() for word in map(str.upper, searchfor)):
                        #print(str(entity))
                        
                        print("Found word")
                        print("------------- actually line "+str(cnt)+" ----------------")  
                        current_item_name=name.text
                        name_text=(name.text).replace("'","").replace("\"","").replace(".","").replace(",","(komma)")
                        description = (description.text).replace("'","").replace("\"","").replace(".","").replace(",","(komma)")
                        #print(name_text)
                        
#beautifying input
                        image_url = entity.find("div", class_="imagebox srpimagebox")
                        if image_url is not None:
                            image_url = image_url.get("data-imgsrc")
                            print("Image: "+image_url)
                        else:
                            image_url=""
                            print("No image was found")
                        #print("Description: "+description.text)

                        item_url = entity.find("a", class_="ellipsis")
                        if item_url is not None:
                            item_url=main_url+item_url.get("href").strip()
                            current_item_url=item_url

                        wo = entity.find("div", class_="aditem-main--top--left")
                        if wo is not None:
                            wo=wo.text.strip().replace("                                               ","").replace("\n","")

                        wann = entity.find("div", class_="aditem-main--top--right")
                        if wann is not None:
                            wann_string=wann.text.strip()
                            wann_string=wann_string.replace("Heute,",datetime.today().strftime('%d-%m-%Y')).replace("Gestern,",(datetime.today() - timedelta(days=1)).strftime('%d-%m-%Y'))
                        
#send stuff
                        if settings_json["use_sql_sqlite"]=="sql":
                            sql_rows=sql.get_sql_vals_by_columns_and_values("ebaykleinanzeigenzeugs","name, datetimeorig", str(name_text)+", "+str(wann_string))
                        elif settings_json["use_sql_sqlite"]=="sqlite":
                            sqlite_rows=sqlite.get_sqlite_vals_by_columns_and_values(current_path, "ebaykleinanzeigenzeugs","name, datetimeorig", str(name_text)+", "+str(wann_string))
                        elif settings_json["use_sql_sqlite"]=="both":
                            sqlite_rows=sqlite.get_sqlite_vals_by_columns_and_values(current_path, "ebaykleinanzeigenzeugs","name, datetimeorig", str(name_text)+", "+str(wann_string))
                            sql_rows=sql.get_sql_vals_by_columns_and_values("ebaykleinanzeigenzeugs","name, datetimeorig", str(name_text)+", "+str(wann_string))

                        if len(sqlite_rows)==0:
                            if settings_json["use_sql_sqlite"]=="sqlite":
                                print("insert to sqlite")
                                sqlite.insert_to_sqlite_table(current_path, "ebaykleinanzeigenzeugs","name, description, datetimeorig, url, image_url", str(name_text)+","+str(description)+","+str(wann_string)+","+str(item_url)+","+str(image_url))
                            if settings_json["use_sql_sqlite"]=="sql":
                                print("insert to sql")
                                sql.insert_to_sql_table("ebaykleinanzeigenzeugs","name, description, datetimeorig, url, image_url", str(name_text)+","+str(description)+","+str(wann_string)+","+str(item_url)+","+str(image_url))
                            if settings_json["use_sql_sqlite"]=="both":
                                print("insert to sql and sqlite")
                                sql.insert_to_sql_table("ebaykleinanzeigenzeugs","name, description, datetimeorig, url, image_url", str(name_text)+","+str(description)+","+str(wann_string)+","+str(item_url)+","+str(image_url))

                                sqlite.insert_to_sqlite_table(current_path, "ebaykleinanzeigenzeugs","name, description, datetimeorig, url, image_url", str(name_text)+","+str(description)+","+str(wann_string)+","+str(item_url)+","+str(image_url))
                                #
                            mail_text_list.append(name_text+"<br><br>"+wo+"<br><br>"+description+"<br><br><img src='"+image_url+"' alt='img' /><br><br><a href='"+item_url+"'>Link zum Item</a><br><br>"+wann_string)
                        else:
                            before_found_items+=1
                        print()
                        
            print("Quantity of usable items was: "+str(current_count_real_items))
            print("Quantity of items which was saved before: "+str(before_found_items))
            print("Quantity of actual items with given searchwords: "+str(current_found_items))
            
            mailtext=""
            if len(mail_text_list)>0:
                for text in mail_text_list:
                    mailtext+=text+"\n-------------\n\n"
            for transport_setting in job:
                if job["mail_settings"][0]["send_mail"]=="true" or job["skype_settings"][0]["skype_send_message"]=="true":
                    for mail_settings in job["mail_settings"]:        
                        if mail_settings["send_mail"] == "true" and mailtext!="":
                            mail_from = str(mail_settings["mail_from"])
                            mail_to = str(mail_settings["mail_to"])
                            mail_host = str(mail_settings["mail_host"])
                            mail_port = str(mail_settings["mail_port"])
                            mail_pass = str(mail_settings["mail_pwd"])
                            communication.send_mail(mailtext, job['name'], mail_from, mail_to, mail_host, mail_port, mail_pass)
                        #elif(mail_settings["send_mail"] == "false" and mailtext!=""):
                            #print("You choosed no mail transport.")
                    
                    #for skype_settings in job["skype_settings"]:
                        #if skype_settings["skype_send_message"] == "true" and mailtext!="":
                            #skype_from = str(skype_settings["skype_message_from"])
                            #skype_pwd = str(skype_settings["skype_pwd"])
                            #skype_to = str(skype_settings["skype_message_to"])
                            #communication.send_to_skype_group(skype_from, skype_pwd, skype_to, current_item_name+"\n\n"+current_item_url)
            if job["mail_settings"][0]["send_mail"]=="false" and job["skype_settings"][0]["skype_send_message"]=="false" and current_found_items>0:
                    print("Are you sure that you choosed no communication? There where "+str(current_found_items)+" item(s) that wasn't sended")
        else:
            print("Quantity of items from website was 0")
#system.clear_screen()