# Description: This script stores and updates mailing address information
# Author: Sam Q. Newprogrammer

# 1. Create dictionary

contact_info = {
    "name": "Lesley Alberto",
    "address": "123 Main Street",
    "city": "Concord",
    "state": "NC",
    "zip": "28025"
}

# 2. Print formatted mailing address

print(f"""\
{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")

# 3. Remove key:value pair for name

del contact_info["name"]

# 4. Create full_name dictionary

full_name = {
    "first name": "Lesley",
    "last name": "Alberto"
}

# 5. Add honorific using update()

full_name.update({"honorific": "Ms."})

# 6. Add full_name to contact_info

contact_info.update({"full_name": full_name})

# 7. Print updated formatted address

print(f"""\
{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")