import re
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# TODO(Jaden): read the data from a folder
# Then store the data in a list named "file_name_list"
filepath = r"./Harry Potter Env/"
file_name_list = os.listdir(filepath)
# file_name_list = [os.path.join(filepath, file) for file in file_name_list]    # complete path
# print(file_name_list)


class Mytext:
    def __init__(self):
        pass

    def read_file(self, filelist):
        """"
        A function for reading a file,or files if you want.
        filename: a list that represents a txt file.
        :return: file name
        """
        for each in filelist:
            print("%d: %s" % (filelist.index(each), each))
        number = int(input("Please choose a number for the file you want to process:"))
        file_name = filelist[number]
        return file_name

    def get_content(self, file_name, mode="rb"):
        """
        A function for processing the txt file
        :param file_name: the name of a file
        :return: None
        """
        ######################################
        # TODO: count the current file.      #
        # 1. number of letter                #
        # 2. number of string                #
        # 3. number of character name        #
        file_name = filepath + file_name     # add complete path
        with open(file_name, mode) as f:
            content = f.read().decode('gbk')
            # I don't know how the performance is, but  only GBK coding is feasible at present.

        # print(type(content))   # <class 'bytes'>
        # print(content[:40])    # each cell is a character,don't worry
        return content

    def num_letter(self, content):
        pattern_1 = re.compile(r"\w")        # not whitespace string
        total_str = pattern_1.findall(content)
        print(len(total_str))                # The 1st is done

    def zipf_law(self, content):
        # zipf law
        count_word = {}
        for w in content.split():
            count_word[w] = count_word.get(w, 0) + 1
            # Returns the key value if it exists and default(=0) if it does not exist.

        result = [(v, k) for k, v in count_word.items()]
        result.sort(reverse=True)                            # Sort reversely
        # print(result)
        with open('zipf.txt', 'w') as f2:
            for each in result:
                f2.write(str(each)+"\n")                     # The 2nd is done

    def num_name(self, content):
        pattern_2 = re.compile(r"\s*said (.*?)[.,;:?!]")     # i.e sb said
        name_set = set()
        for i in pattern_2.finditer(content):
            who = i.group(1)
            name_set.add(who)
        with open("num_names.txt", 'w') as f3:
            for j in name_set:
                f3.write(j + "\n")                           # the 3rd is done

    def draw_chart(self, filename, mode="rb"):
        """
        Draw the result by using matplotlib.pyplot
        :param filename: A file name
        :param mode: defalut , normally "rb"
        :return: None
        """
        with open(filename, mode) as f:
            strings = f.read().decode('gbk')
            patt = re.compile(r"\((.?),")      # The serial numbers are in the form of "(1,"
            result = patt.findall(strings)
            # print(len(result))
            plt.plot(result)
            plt.xlabel('count')
            plt.ylabel('rank')
            plt.ylim((0, 9))

            plt.show()                         # Display the result

    def daw_cloud(self, filename):
        with open(filename, 'rb') as f:
            data = f.read().decode('gbk')
            patt = re.compile(r"[\"'](.*?)[\"']")
            result = patt.findall(data)               # class list
            # print(result)                           # for debugging
            background_img = plt.imread('pika.jpg')
            wc = WordCloud(
                background_color='white',
                mask=background_img,
                max_words=2000,
                stopwords=STOPWORDS,
                max_font_size=50,
                random_state=30
            )
            wc.generate(str(result))
            # image_colors = ImageColorGenerator(background_img)
            # wc.recolor(image_colors)
            plt.imshow(wc)
            plt.axis('off')

            plt.show()


if __name__ == "__main__":
    text = Mytext()
    num_name_file_1 = r"num_names.txt"
    num_name_file_2 = r"zipf.txt"
    # file1 = text.read_file(file_name_list)
    # content = text.get_content(file1)
    # text.num_letter(content)
    # text.zipf_law(content)
    # text.num_name(content)
    # text.draw(num_name_file_1)
    text.draw_chart(num_name_file_2)
    text.daw_cloud(num_name_file_2)
