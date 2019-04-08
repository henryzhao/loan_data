import json
import cpca
import pandas as pd
import re
import jieba


# //加载文件
def openFile():
    # pass

    with open("./data/data.json", 'r', encoding='utf-8') as f:
        text = json.load(f)
    f.close()
    dict1 = []
    for item in text['RECORDS']:
        dict1.append(item['projectName'])
    return dict1


def getQu(data):
    df = cpca.transform(data)
    return df


def testcpca():
    # print(cpca.transform("湖北省武汉市武昌区武南三村1栋车站楼2单元3层4室"))
    print(" ".join(jieba.cut("湖北省武汉市武昌区武南三村1栋车站楼2单元3层4室", cut_all=True)))


def getDetail(data):
    df = pd.DataFrame(data)
    return df


def test(data):
    df = pd.DataFrame(data)
    print(df)
    print(df["地址"])
    df['小区'] = df.apply(lambda x: re.split("/[A-Z]?\d+(?=栋)/", str(x["地址"])), axis=1)
    df.to_excel("./excel/abc.xlsx")
    print(df.head)


def test2(data):
    dict1 = []
    dict2 = []
    dict3 = []
    dict4 = []
    for item in data:
        matcher = re.match("(.*栋)?(.*单元)?(.*层)?(.*室)?", item, re.M | re.I)
        dict1.append(matcher.group(1))
        dict2.append(matcher.group(2))
        dict3.append(matcher.group(3))
        dict4.append(matcher.group(4))
    return dict1, dict2, dict3, dict4

def success():
    # 加载文件,得到数据
    df = pd.read_excel("./excel/all.xls", sheetname=0)
    project_name = df["项目名称"]
    dataPrecessed = getQu(project_name)
    df['省'] = dataPrecessed['省']
    df['市'] = dataPrecessed['市']
    df['区'] = dataPrecessed['区']
    df['地址'] = dataPrecessed['地址']
    df['小区'] = df.apply(lambda x: re.split("(\d\-?)+(?=栋)|([A-Z]?\d)+(?=栋)", str(x["地址"]))[0], axis=1)
    df['楼栋信息'] = df.apply(lambda x: re.sub(str(x["小区"]), "", str(x["地址"])), axis=1)
    dict1, dict2, dict3, dict4 = test2(df['楼栋信息'])
    # print(dict1)
    df['栋'] = pd.DataFrame(dict1)
    df['单元'] = pd.DataFrame(dict2)
    df['层'] = pd.DataFrame(dict3)
    df['室'] = pd.DataFrame(dict4)
    df.to_excel("./excel/abc.xlsx")
    print(df.head)


def main():
    success()


if __name__ == '__main__':
    main()
