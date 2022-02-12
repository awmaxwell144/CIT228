#nested list
riversCountries = {"Nile":['Egypt','Tanzania','Rwanda','Kenya'],
        "Mississippi":"United States",
        "Amazon":['Brazil','Bolivia','Peru','Ecuador']}

for key, value in riversCountries .items():
    if type(value)==list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print("\t\t\t\t",v)
    else:
        print(f"The {key.title()} river flows through {value.title()}")