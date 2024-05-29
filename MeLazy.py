import os
""" Aight, so basically heres what this does. Im very lazy, and had 300 and something line file. 
I needed to find specific line and change that with something else for 28 things to make 
a table of contents link up properly. Maybe you could re-use this? Idk."""

with open("./tos.html", "r") as f:
    lines = f.readlines()

topics = [
    "1. OUR SERVICES",
    "2. INTELLECTUAL PROPERTY RIGHTS",
    "3. USER REPRESENTATIONS",
    "4. USER REGISTRATION",
    "5. PURCHASES AND PAYMENT",
    "6. SUBSCRIPTIONS",
    "7. SOFTWARE",
    "8. PROHIBITED ACTIVITIES",
    "9. USER GENERATED CONTRIBUTIONS",
    "10. CONTRIBUTION LICENSE",
    "11. GUIDELINES FOR REVIEWS",
    "12. THIRD-PARTY WEBSITES AND CONTENT",
    "13. SERVICES MANAGEMENT",
    "14. PRIVACY POLICY",
    "15. TERM AND TERMINATION",
    "16. MODIFICATIONS AND INTERRUPTIONS",
    "17. GOVERNING LAW",
    "18. DISPUTE RESOLUTION",
    "19. CORRECTIONS",
    "20. DISCLAIMER",
    "21. LIMITATIONS OF LIABILITY",
    "22. INDEMNIFICATION",
    "23. USER DATA",
    "24. ELECTRONIC COMMUNICATIONS, TRANSACTIONS, AND SIGNATURES",
    "25. SMS TEXT MESSAGING",
    "26. CALIFORNIA USERS AND RESIDENTS",
    "27. MISCELLANEOUS",
    "28. CONTACT US"
]

ids = [
    "services",
    "ip",
    "userreps",
    "userreg",
    "purchases",
    "subscriptions",
    "software",
    "prohibited",
    "ugc",
    "license",
    "reviews",
    "thirdparty",
    "sitemanage",
    "ppyes",
    "terms",
    "modifications",
    "law",
    "disputes",
    "corrections",
    "disclaimer",
    "liability",
    "indemnification",
    "userdata",
    "electronic",
    "sms",
    "california",
    "misc",
    "contact"
]

newdoc = ""
index = 0

for line in lines:
    if index >= len(topics):
        break
    
    if "<p><strong>" + topics[index] + "</strong></p>" in line:
        # Replace the topic with the modified version including the id
        line = line.replace("<p><strong>" + topics[index] + "</strong></p>", "<p id=\"" + ids[index] + "\"><strong>" + topics[index] + "</strong></p>")
        index += 1
        print(line)
        newdoc += line
    else:
        newdoc += line
        print(False)

print(len(lines))
print(index)

with open("modified_tos.html", "w") as f_out:
    f_out.write(newdoc)