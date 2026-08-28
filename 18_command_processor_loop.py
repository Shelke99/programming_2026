# 25. Implement a command processor loop that exits on "quit"/"exit"
def cmd_proc_loop():

    while True:
        cmd = input("enter the value:" )
        if cmd.strip().lower() in ['exit','quit']:
            print("program stopped")
            break
        print('you enter the value as:', cmd)
    
cmd_proc_loop()
