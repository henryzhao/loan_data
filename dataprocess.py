import json
import cpca
import pandas as pd
import re
import jieba

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
    df = cpca.transform(data)
    print(df)
def testcpca():
    # print(cpca.transform("湖北省武汉市武昌区武南三村1栋车站楼2单元3层4室"))
    print(" ".join(jieba.cut("湖北省武汉市武昌区武南三村1栋车站楼2单元3层4室", cut_all=True)))
def getDetail(data):
    df = pd.read_excel('./excel/all1.xls', sheetname=0)
    # df = pd.DataFrame(data)
    print(df)

    df['栋'] = df.apply(lambda x: re.match("\\d+(?=栋)", x["项目名称"], re.M | re.I), axis=1)
    df['单元'] = df.apply(lambda x: re.match("\\d+[^\\d]+(\\d+)", x["项目名称"], re.M | re.I).group(1), axis=1)
    df['门牌号'] = df.apply(lambda x: re.match("\\d+[^\\d]+\\d+[^\\d]+(\\d+)", x["项目名称"], re.M | re.I).group(1), axis=1)
    print(df.head)
def test():
    print(re.match("\\d+(?=栋)", "1栋车站楼2单元3层4室", re.M | re.I).group())
    print(re.match("\\d+[^\\d]+(\\d+)", "1栋车站楼2单元3层4室", re.M | re.I).group(1))
    print(re.match("\\d+[^\\d]+\\d+[^\\d]+(\\d+(?=层))", "1栋车站楼2单元3层4室", re.M | re.I).group(1))
    print(re.match("\\d+[^\\d]+\\d+[^\\d]+\\d+[^\\d]+(\\d+(?=室))", "1栋车站楼2单元3层4室", re.M | re.I).group(1))
def main():
    # 加载文件
    dataPrecessed = openFile()
    # print(dataPrecessed)
    # getQu(dataPrecessed)
    # getDetail(dataPrecessed)
    test()




if __name__ == '__main__':
    main()