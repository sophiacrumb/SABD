from Main import Main
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deduplication work demonstration')
    parser.add_argument('--filepath', type=str, help='Path of the file to proceed')
    parser.add_argument('--chunk_size', type=int, help='Chunk size')
    parser.add_argument('-u', help='Upload command', action='store_true')
    parser.add_argument('-d', help='Download command', action='store_true')
    args = vars(parser.parse_args())
    Main.result_file_name = args['filepath']
    if args['u']:
        Main.upload(args['filepath'], args['chunk_size'])
    elif args['d']:
        Main.download(args['filepath'])
