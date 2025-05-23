# programing_dictionary={
#     "bug": "md jahid hasan maruf",
#     "funtion":"kichu ekta",
#     "loop":"this is loop",
#
# }
#
# # print(programing_dictionary["bug"])
# #
# # programing_dictionary["aray"]="THis is arrayy"
# #
# # print(programing_dictionary)
#
# empty_dictionary={}
#
#
# # programing_dictionary={}
# #
# # print(programing_dictionary)
#
# programing_dictionary["bug"]="a moth in your computer"
#
# print(programing_dictionary)
#
# for thing in programing_dictionary:
#     print(thing)
#     print(programing_dictionary[thing])



capitals={

    "france": "paris",
    "germany": "barlin"

}

#nested list in dictionary

# travel_log={
#
#     "france": ["paris","little","dijon"],
#     "germany":["stuttgart","barlin"],
#
# }
#
# #print little
#
# print(travel_log["france"][1])

# nested_list=["a","b",["c","d"]]
#
# print(nested_list[2][0])

travel_log={

    "france": {
        "cities_visited": ["paris", "little", "dijon"],
        "total_visited":8,


    },

    "germany":
        {
            "cities_visited": ["humberg","stuttgart","barlin"],
           "total_visited":9

        },
}

print(travel_log["germany"]["cities_visited"][2])

