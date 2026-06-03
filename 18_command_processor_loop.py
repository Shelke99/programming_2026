# 25. Implement a command processor loop that exits on "quit"/"exit"
def cmd_proc_loop():

    while (n := int(input("enter the value:" ))) != 'exit':
        print('you enter the value as:', n)
    print("program stopped")
cmd_proc_loop()
