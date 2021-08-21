import json

a_file = open("secret.json", "r")
json_object = json.load(a_file)
# a_file.close()
#print(json_object)

json_object["IS_NEW_TERM"] = False

a_file = open("secret.json", "w")
json.dump(json_object, a_file, sort_keys=True, indent=4)
a_file.close()