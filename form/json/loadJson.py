import json

input_file = open ('API.json')
json = json.load(input_file)

print("MQTT_ServerIP: {0}".format(json["MQTT_ServerIP"]))
print("main_TP_Alive: {0}".format(json["main"]["TP_Alive"]))
print("main_nodeList: {0}".format(json["main"]["nodeList"]))
