
## care enough to send an exit code:
import time
import sys

def main():
    confirm = input('Are you sure you want to format C: [ yes, NO]?')
    if not confirm or confirm != 'yes':
        print('Format cancelled')
        sys.exit(1)
    
    for _ in range(40):
        time.sleep(.15)
        print('.', end='')
        sys.stdout.flush()
    print()
    print('Format completed sucessfully.Enjoy the new hard drive space')

main()

