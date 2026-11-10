seth_data = {
    "name": "Seth",
    "age": 16,
    "fav_anim": "wolf",
    "bucket_list": "Snowboard in Switzerland",
    "height": " 6ft 1in"
}

print(seth_data["bucket_list"])

seth_data["bucket_list"] = "Do a wheelie in his wheelchair"
print(seth_data["bucket_list"])

seth_data["alergy"] = "cats"

print(seth_data["alergy"])

del seth_data["bucket_list"]    #remooves a key value pair by key


print("\n---------------------\n")

for key in seth_data:
    print(key)
    print(seth_data[key])
    print(key + ": " + str(seth_data[key]))