from sys import argv
from graphic_util import Window
from logging import Log

def main(args):
    log = Log(args[1], (args[2].lower() == "true" or args[2].lower() != "false"))
    win = Window(10, "480x270", log)
    win.add_button()
    win.run()
    log.write_event("Program exited successfuly")


if __name__ == '__main__':
    for i in range(3 - len(argv)): argv.append("")
    main(argv)