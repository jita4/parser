import argparse
parser=argparse.ArgumentParser(description='You can replace any letter on letter')
parser.add_argument('-l1', '--letter_in', type=str, help='letter in text')
parser.add_argument('-l2', '--letter_out', type=str, help='your letter')
args=parser.parse_args()
def text_change(letter_in, letter_out):
    print('You will change all letters', letter_in, ' on ', letter_out)
    print()
    with open ('text.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(letter_in, letter_out)
    with open ('text.txt', 'w') as f:
        f.write(new_data)
    print(new_data)
    print()
    print('How do you like it?')

if __name__=='__main__':
    text_change(args.letter_in, args.letter_out)
