from traceback import print_tb

#
# def my_function(a,b):
#    return a+b
#
# print(my_function(2,3))

# def format_name(f_name,l_name):
# #     # print(f_name.title())
# #     # print(l_name.title())
# #
# #     formate_f_name=f_name.title()
# #     formate_l_name=l_name.title()
# #
# #     return f"{formate_f_name} {formate_l_name}"
# #
# # format_string=format_name("jaHid","maRuf")
# # print(format_string)
# #
# #
# #
# # output=len("Jahid hasan")



def function_1(text):
    return text+text

def function_2(text):
    return text.title()

output=function_2(function_1("maruf"))
print(output)
