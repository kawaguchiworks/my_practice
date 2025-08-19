#コマンドライン引数
#位置引数の指定方法

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    args = parser.parse_args()
    print(args.target)

