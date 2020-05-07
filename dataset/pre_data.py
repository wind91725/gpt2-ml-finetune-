### 转换成支持prepare_data 处理的数据格式，将文本生成1024长度的训练数据，stride为768
# python pre_data.py --filepath /data/home/share1/gpt2-ml-Finetune/data-mayun_xiugai --outfile /data/home/share1/gpt2-ml-Finetune/data/22.json
import re
import json
import argparse
import os
def get_data(filepath,outfile):
    for root, dirs, files in os.walk(filepath):
        for each in files:
            filename = os.path.join(root,each)
            f = open(filename, 'r', encoding='utf-8')
            data = f.read()
            strid = 768
            max_length = 1024
            data_list = []
            strat = 0
            end = 1024
            pattern1 =  r"^[^。！？]*"
            pattern2 = r'.*[。！？]'
            f_json = open(outfile,'a',encoding='utf-8')
            while strat<= len(data) :
                data_list.append((strat,end))
                if (data_list[-1][1]-data_list[-1][0])< max_length:
                    break
                strat += strid
                end = min(strat+max_length,len(data))
            for each in data_list:
                tmp ={}
                text = data[each[0]:each[1]]
                text2 = re.sub(pattern1,'',text)
                if text2.startswith('。') or text2.startswith('！') or text2.startswith('？'):
                    text3 =text2[1:]
                else:
                    text3 = text2
                #print(re.findall(pattern2,text3))
                text4_list = re.findall(pattern2,text3)
                text4 = '\n'.join(text4_list)
                tmp['text'] = text4

                json_data = json.dumps(tmp,ensure_ascii=False)
                f_json.write(json_data)
                f_json.write('\n')
    print('finish')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', default='/data/home/share1/gpt2-ml-Finetune/data-mayun_xiugai', type=str, required=False, help='数据集目录地址')
    parser.add_argument('--outfile', default='/data/home/share1/gpt2-ml-Finetune/data/22.json', type=str, required=False,help='生成文件地址')
    args = parser.parse_args()
    print('args:\n' + args.__repr__())
    filepath = args.filepath
    outfile = args.outfile
    get_data(filepath,outfile)


if __name__ == '__main__':
    main()
