import sys

# 引数の種類
    # 1. 正規文字列
    # 2. 処理ファイル
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("Argument is not long enough")
    else:
        # 正規文字をparserに送る
        # ファイルの文字列をvmに送る
