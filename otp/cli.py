#!/usr/bin/env python3
import argparse
from otp import time_based_otp


def generate(args):
    print(time_based_otp.generate_otp(args.password))


def verify(args):
    print(time_based_otp.verify_otp(args.password, args.otp))


def main():
    parser = argparse.ArgumentParser(description="OTP management")

    subparser = parser.add_subparsers()

    generate_parser = subparser.add_parser('generate')
    verify_parser = subparser.add_parser('verify')

    generate_parser.add_argument('--password',
                                 type=str,
                                 required=True,
                                 help='user password')
    generate_parser.set_defaults(func=generate)

    verify_parser.add_argument('--password',
                               type=str,
                               required=True,
                               help='user password')
    verify_parser.add_argument('--otp',
                               type=str,
                               required=True,
                               help='OTP to verify')
    verify_parser.set_defaults(func=verify)

    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        print("The function need arguments. To know the arguments use --help")



main()
