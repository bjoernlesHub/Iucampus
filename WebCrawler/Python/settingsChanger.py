def set_new_settings(settings, parameters):
    #print(str(parameters))

    count_of_values=0
    count_of_onekey_parameter=0
    onekey_parameters_string=""
    print("------------")
    
    for parameter in parameters:

        if parameter != "WebCrawler.py":

            key_val=parameter.split("=")

            if len(key_val)>1:
                #print(key_val[0]+"="+key_val[1])
                if key_val[1] != "":
                    count_of_values=count_of_values+1

                    if key_val[0] == "use_sql_sqlite":
                        settings["use_sql_sqlite"]=key_val[1]
                        print("Using "+key_val[1]+" as database")
                    elif key_val[0] == "sql_host":
                        settings["sql_host"]=key_val[1]
                    elif key_val[0] == "sql_user":
                        settings["sql_user"]=key_val[1]
                    elif key_val[0] == "sql_pass":
                        settings["sql_pass"]=key_val[1]
                    elif key_val[0] == "sql_db":
                        settings["sql_db"]=key_val[1]
                    #elif key_val[0] == "url":
                        #settings["jobs"][0]["url"]=key_val[1] 
                        #print("Using url: "+key_val[1])
                    elif key_val[0] == "subpage":
                        settings["jobs"][0]["subpage"]=key_val[1] 
                        print("Using subpage: "+key_val[1])    
                    elif key_val[0] == "plz":
                        settings["jobs"][0]["plz"]=key_val[1] 
                        print("Using plz: "+key_val[1])   
                    elif key_val[0] == "plzRadius":
                        settings["jobs"][0]["plzRadius"]=key_val[1] 
                        print("Using radius: "+key_val[1])                          
                    elif key_val[0] == "words":
                        key_val[1]=key_val[1].replace("³"," ")
                        print("Using words: "+key_val[1])
                        wordsstring=""
                        for word in key_val[1].replace(" ","").split(","):
                            wordsstring+="'"+word+"' "
                        print("That's "+str(len(key_val[1].replace(" ","").split(",")))+" words("+wordsstring+").")
                        settings["jobs"][0]["words"]=key_val[1]

                    elif key_val[0] == "send_mail":
                        settings["jobs"][0]["mail_settings"][0]["send_mail"]=key_val[1]
                    elif key_val[0] == "mail_from":
                        settings["jobs"][0]["mail_settings"][0]["mail_from"]=key_val[1]
                    elif key_val[0] == "mail_to":
                        settings["jobs"][0]["mail_settings"][0]["mail_to"]=key_val[1]
                    elif key_val[0] == "mail_host":
                        settings["jobs"][0]["mail_settings"][0]["mail_host"]=key_val[1]
                    elif key_val[0] == "mail_port":
                        settings["jobs"][0]["mail_settings"][0]["mail_port"]=key_val[1]
                    elif key_val[0] == "mail_pwd":
                        settings["jobs"][0]["mail_settings"][0]["mail_pwd"]=key_val[1]
                    
                    elif key_val[0] == "skype_send_message":
                        settings["jobs"][0]["skype_settings"][0]["skype_send_message"]=key_val[1]
                    elif key_val[0] == "skype_message_from":
                        settings["jobs"][0]["skype_settings"][0]["skype_message_from"]=key_val[1]
                    elif key_val[0] == "skype_pwd":
                        settings["jobs"][0]["skype_settings"][0]["skype_pwd"]=key_val[1]
                    elif key_val[0] == "skype_f_group_t_person":
                        settings["jobs"][0]["skype_settings"][0]["skype_f_group_t_person"]=key_val[1]
                    elif key_val[0] == "skype_message_to":
                        settings["jobs"][0]["skype_settings"][0]["skype_message_to"]=key_val[1]

            elif len(key_val)==1:
                count_of_onekey_parameter+=1
                onekey_parameters_string+="'"+key_val[0]+"', "
    onekey_parameters_string=onekey_parameters_string[:-2]
    print(str(count_of_values)+" given key-value pairs for running this Job.")
    if count_of_onekey_parameter>1:
        print(str(count_of_onekey_parameter)+" given values for running this Job. ("+onekey_parameters_string+")")
    

    return settings
    #for parameter in parameters:
        #print(parameter+"\n")