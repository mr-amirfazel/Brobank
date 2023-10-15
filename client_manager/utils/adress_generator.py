user_info = {}
def file_address_generator(raw_address):
    global user_info
    nat_code = user_info["national_code"]
    return [f"./assets/{raw_address}", f"{nat_code}{raw_address}"]

def get_s3_addresses(user):
    global user_info
    user_info = user
    print("user:", user)
    return list(map(file_address_generator, [user_info["image1_name"], user_info["image2_name"]]))
