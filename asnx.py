#!/usr/bin/python3

###############################
## Author: AliSh3ikhi (~_^)  ##
## Date: 05/23/2023          ##
## Modify: 05/23/2023 - v01  ##
## Usage: Run on all subs    ##
###############################


import subprocess
import argparse
import socket
import re


def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        return output.decode('utf-8')
    else:
        return error.decode('utf-8')



def is_domain(input_string):
    domain_pattern = r'^([a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}$'
    if re.match(domain_pattern, input_string):
        return True
    else:
        return False

def is_ip_address(input_string):
    try:
        socket.inet_aton(input_string)
        return True
    except socket.error:
        return False


def process_bgpview_ip(ips,args):
    for ip in ips:
        print(f'[+] {ip}:')
        if args.asn:
            command = f'curl -s https://api.bgpview.io/ip/{ip} | jq -r \'.data.prefixes[] | {{prefix: .prefix, ASN: .asn.asn}}\' | grep ASN | awk \'{{print $2}}\' | sed -e \'s/"//g\' -e \'s/,//g\' '
        elif args.prefix:
            command = f'curl -s https://api.bgpview.io/ip/{ip} | jq -r \'.data.prefixes[] | {{prefix: .prefix, ASN: .asn.asn}}\' | grep prefix | awk \'{{print $2}}\' | sed -e \'s/"//g\' -e \'s/,//g\' '
        else:
            command = f'curl -s https://api.bgpview.io/ip/{ip} | jq -r \'.data.prefixes[] | {{prefix: .prefix, ASN: .asn.asn}}\''
        output = run_command(command)
        print(output)


def main():
    parser = argparse.ArgumentParser(description='Process IPs or subdomains using BGPView API')
    
    parser.add_argument('-u', '--url', help='Single URL to check')
    parser.add_argument('-l', '--list', help='List of URLs to check')
    parser.add_argument('-asn', '--asn', action='store_true', help='Only print ASNs of target IP')
    parser.add_argument('-prefix', '--prefix', action='store_true', help='Only print prefixes of target IP')
    args = parser.parse_args()


    if args.url:
        urls = [args.url]
    elif args.list:
        with open(args.list, 'r') as f:
            urls = [line.strip() for line in f.readlines()]

    for url in urls:
        if is_domain(url):
            command = f'dig +short A {url}'
            output = run_command(command)
            IPs = output.splitlines()
            process_bgpview_ip(IPs,args)
        elif is_ip_address(url):
            IPs = [url]
            process_bgpview_ip(IPs,args)
        else:
            print(f'[!] The \'{url}\' is not my type :)')
            continue



if __name__ == '__main__':
    main()
