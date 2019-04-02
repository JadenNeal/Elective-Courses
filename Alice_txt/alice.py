import re
import matplotlib.pyplot as plt

file_name = r"alice.txt"                                   # 要处理的文件名
with open(file_name, 'rt') as f:
    content = f.read()                                     # 'rt'模式读取后为str类型
# print(type(content))
print('Alice文件共有字符数为：', len(content))

word = content.split()                                     # 以空格切分
word_num = len(word)
print('Alice文件共有单词数为：', word_num)


def zipf_law():
    # zipf law
    word_count = {}
    for w in word:
        word_count[w] = word_count.get(w, 0) + 1

    res = [(v, k) for k, v in word_count.items()]
    res.sort()                                             # 数字排序
    # print(type(res))
    with open('zipf_law.txt', 'w') as f1:
        for each in res:
            f1.write(str(each) + "\n")                     # 得到zipf-law文件


def draw(filename):
    # 绘制zipf-law曲线
    with open(filename, 'rt') as f2:
        data = f2.read()                                   # 得到zipf-law的数据
        res = re.findall(r"\((.?),", data)                 # 数字位于(和,之间
        res.sort(reverse=True)                             # 从大到小排序

        # plt.xlim((0, 9))
        x = [i for i in range(4860)]
        plt.plot(x, res)
        plt.xlabel('count')
        plt.ylabel('rank')
        plt.show()


def person_name():
    patt = re.compile(r"\s*said (.*?)[.,;:]")              # 找出所有的人名
    name_set = set()
    for i in patt.finditer(content):
        who = i.group(1)
        name_set.add(who)
    with open("person_name.txt", 'w') as f3:               # 写入文件
        for j in name_set:
            f3.write(j + "\n")


filename = "zipf_law.txt"
# zipf_law()
draw(filename)
person_name()
