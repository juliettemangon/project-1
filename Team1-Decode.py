import pandas as pd


def Decode(code_file, table_file, output_file):
    with open(code_file, 'r') as f:
        code = f.read().split('.')[1]


    df = pd.read_excel(table_file, dtype=str, header=None)


    df_5 = df.iloc[:, [0, 1]].dropna(axis=0)
    df_5_dict = {}
    for i in range(len(df_5)):
        df_5_dict[df_5.iloc[i, 1]] = df_5.iloc[i, 0]


    df_7 = df.iloc[:, [2, 3]].dropna(axis=0)
    df_7_dict = {}
    for i in range(len(df_7)):
        df_7_dict[df_7.iloc[i, 1]] = df_7.iloc[i, 0]


    index = 0
    res = r''
    while index < len(code):
        if code[index] == '0':
            if code[index:index + 5] in df_5_dict:
                res += df_5_dict[code[index:index + 5]]
                index += 5
        elif code[index] == '1':
            if code[index:index + 7] in df_7_dict:
                val = df_7_dict[code[index:index + 7]].replace('\\n', '\n')
                res += val
                index += 7


    with open(output_file, 'w') as f:
        f.write(res)
        print(f)


if __name__ == '__main__':
    Decode('BinInput.txt', 'Team1-Table.xlsx', 'TextOutput.txt')

