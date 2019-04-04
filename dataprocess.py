import json

    # //加载文件
def openFile():
    with open("./data/data.json", 'r', encoding='utf-8') as f:
        text = json.load(f)
        # print(text['RECORDS'])
    f.close()
    dict = []
    for item in text['RECORDS']:
        dict.append(item['projectName'])
    # print(dict)
    return dict

def getQu(data):
    pass
def main():
    # 加载文件
    dataPrecessed = openFile()
    print(dataPrecessed)
    for i in dataPrecessed:
        pass


if __name__ == '__main__':
    main()