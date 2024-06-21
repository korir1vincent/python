# myname="eMobilis"
# for i in myname:
#     if i != "k":
#         print(i)
#
# try:
#     #code that might raise exception
#     result = 1/0
# except ZeroDivisionError as e :
#     print(f"An error has occured {e}")
#     # code to handle exception
# finally:
#     #code that runs no matter what
#     print("This will always be printed")

try:
    jina=['banana','oranges','mangoes']
    for i in range(5):
        print(i,jina[i])
except:
    print("index out of range")
finally:
    print("This will always run")