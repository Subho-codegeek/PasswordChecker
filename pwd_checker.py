import requests
import sys
import hashlib

def api_data(character):
    url = 'https://api.pwnedpasswords.com/range/' + character
    res = requests.get(url)
    if res.status_code!= 200:
        raise RuntimeError(f'Error:{res.status_code} , Check api and try again')
    return res


def password_hacked_count(hashes , hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0



def password_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_char , tail = sha1password[:5] , sha1password[5:]
    response = api_data(first_5_char)
    return password_hacked_count(response , tail)


def main(args):
    for password in args:
        count = password_check(password)
        if count:
            print (f'{password} is hacked {count} times. Its not safe to use!!')
        else:
            print(f'{password} is not hacked. You can use it.')
    return 'Done!!'



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))








