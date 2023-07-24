import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os

def main():
    out_dir = 'plot'
    try:
        os.makedirs(out_dir)
    except:
        pass

    input_file = sys.argv[1]
    interval = int(sys.argv[2])
    bound = int(sys.argv[3])
    out_fig = './plot/' + input_file[:-4] + '.png'

    # read data from file
    x_list = []
    y_list = []
    with open(input_file) as f:
        for line in f:
            x, y = line.strip().split()
            if int(y) < bound:
                x_list.append(int(x))
                y_list.append(int(y))
    print(x_list)
    # plot the figure
    plt.figure(figsize=(6.4, 2))
    # y轴的文本
    plt.ylabel("Latency (cycles)")
    plt.plot(x_list, y_list)
    # 仅在y轴添加网格线
    plt.grid(axis='y')
    
    # 画出垂直的边界线，方便显示前后差异
    for i in range(math.ceil(len(x_list)/interval)):
        bar = interval * i
        plt.axvline(x=bar, color='y')
    # x轴的文本
    plt.xlabel("Num of experiments")
    plt.tight_layout()
    plt.savefig(out_fig, dpi=600)
    # 清空图纸
    plt.clf()

if __name__ == "__main__":
    main()