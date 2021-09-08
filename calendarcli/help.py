from calendarcli.path import fullPath
print(fullPath('data/Document.txt'))
try:
    with open(fullPath('data/Document.txt'),'r') as f:
        print(f.read())
except Exception as e :
    import webbrowser
    print("Plaes read Documentation...")
    webbrowser.open_new_tab("https://github.com/VillSource/calendar-cli")


# print('data/Document.txt')
# try:
#     with open('data/Document.txt','r') as f:
#         print(f.read())
# except Exception as e :
#     import webbrowser
#     print("Plaes read Documentation...")
#     webbrowser.open_new_tab("https://github.com/VillSource/calendar-cli")
print("love")