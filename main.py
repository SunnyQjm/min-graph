import csv
import os
import sys

import numpy as np
from utils import extractTCPResult, TCPMeasureItem, TCPMeasureResult, extractUDPResult, UDPMeasureItem, \
    extractUDPResult2
import matplotlib
import matplotlib.pyplot as plt


def printTCPResult(title: str, result: TCPMeasureResult):
    print(f"\n{title}")
    print("bitrate_mean(Mbps)\tbitrate_std\tretr_mean\tretr_std")
    bitrates = []
    retries = []
    for item in result.groups[-1]:
        bitrates.append(item.bitrate / 1000000)
        retries.append(item.retryTime)
    print(f"{np.mean(bitrates).round(2)}\t{np.std(bitrates).round(2)}\t{np.mean(retries).round(2)}\t"
          f"{np.std(retries).round(2)}")


def printUDPResult(title: str, udpItem: UDPMeasureItem):
    print(f"\n{title}")
    print("jitter(ms)\ttotalSend\ttotalReceive\tlostRate")
    print(f"{round(udpItem.jitter, 2)}\t{round(udpItem.totalSend, 2)}\t{round(udpItem.totalReceive, 2)}"
          f"\t{round(udpItem.lostRate, 2)}")


def getRes(filePath: str):
    item = extractUDPResult(filePath)
    return [round(item.jitter, 2), round(item.totalSend, 2), round(item.totalReceive, 2), round(item.lostRate, 2)]


def printTableInfo():
    print("\n----------------- TCP Result 1500 -----------------")
    printTCPResult("NDN TCP 1 Client", extractTCPResult("result_1500/ndn_3node_buffersize4M_tcp_1.txt"))
    printTCPResult("MIN TCP 1 Client", extractTCPResult("result_1500/min_3node_buffersize4M_tcp_1.txt"))
    printTCPResult("NDN TCP 2 Client", extractTCPResult("result_1500/ndn_3node_buffersize4M_tcp_2.txt"))
    printTCPResult("MIN TCP 2 Client", extractTCPResult("result_1500/min_3node_buffersize4M_tcp_2.txt"))
    printTCPResult("NDN TCP 5 Client", extractTCPResult("result_1500/ndn_3node_buffersize4M_tcp_5.txt"))
    printTCPResult("MIN TCP 5 Client", extractTCPResult("result_1500/min_3node_buffersize4M_tcp_5.txt"))
    printTCPResult("NDN TCP 10 Client", extractTCPResult("result_1500/ndn_3node_buffersize4M_tcp_10.txt"))
    printTCPResult("MIN TCP 10 Client", extractTCPResult("result_1500/min_3node_buffersize4M_tcp_10.txt"))

    # print("\n----------------- TCP Result 8000 -----------------")
    # printTCPResult("NDN TCP 1 Client", extractTCPResult("result_8000/ndn_3node_buffersize4M_tcp_1.txt"))
    # printTCPResult("MIN TCP 1 Client", extractTCPResult("result_8000/min_3node_buffersize4M_tcp_1.txt"))
    # printTCPResult("NDN TCP 2 Client", extractTCPResult("result_8000/ndn_3node_buffersize4M_tcp_2.txt"))
    # printTCPResult("MIN TCP 2 Client", extractTCPResult("result_8000/min_3node_buffersize4M_tcp_2.txt"))
    # printTCPResult("NDN TCP 5 Client", extractTCPResult("result_8000/ndn_3node_buffersize4M_tcp_5.txt"))
    # printTCPResult("MIN TCP 5 Client", extractTCPResult("result_8000/min_3node_buffersize4M_tcp_5.txt"))
    # printTCPResult("NDN TCP 10 Client", extractTCPResult("result_8000/ndn_3node_buffersize4M_tcp_10.txt"))
    # printTCPResult("MIN TCP 10 Client", extractTCPResult("result_8000/min_3node_buffersize4M_tcp_10.txt"))

    print("\n----------------- UDP Result 1500 -----------------")
    printUDPResult("NDN 1m", extractUDPResult("result_1500/ndn_3node_buffersize4M_udp_1m.txt"))
    printUDPResult("NDN 10m", extractUDPResult("result_1500/ndn_3node_buffersize4M_udp_10m.txt"))
    printUDPResult("NDN 100m", extractUDPResult("result_1500/ndn_3node_buffersize4M_udp_100m.txt"))
    printUDPResult("NDN 200m", extractUDPResult("result_1500/ndn_3node_buffersize4M_udp_200m.txt"))
    printUDPResult("NDN 300m", extractUDPResult("result_1500/ndn_3node_buffersize4M_udp_300m.txt"))
    printUDPResult("NDN 400m", extractUDPResult("result_1500/ndn_3node_buffersize4M_udp_400m.txt"))
    printUDPResult("NDN 500m", extractUDPResult("result_1500/ndn_3node_buffersize4M_udp_500m.txt"))
    printUDPResult("MIN 1m", extractUDPResult("result_1500/min_3node_buffersize4M_udp_1m.txt"))
    printUDPResult("MIN 10m", extractUDPResult("result_1500/min_3node_buffersize4M_udp_10m.txt"))
    printUDPResult("MIN 100m", extractUDPResult("result_1500/min_3node_buffersize4M_udp_100m.txt"))
    printUDPResult("MIN 200m", extractUDPResult("result_1500/min_3node_buffersize4M_udp_200m.txt"))
    printUDPResult("MIN 300m", extractUDPResult("result_1500/min_3node_buffersize4M_udp_300m.txt"))
    printUDPResult("MIN 400m", extractUDPResult("result_1500/min_3node_buffersize4M_udp_400m.txt"))
    printUDPResult("MIN 500m", extractUDPResult("result_1500/min_3node_buffersize4M_udp_500m.txt"))

    # print("\n----------------- UDP Result 8000 -----------------")
    # printUDPResult("NDN 1m", extractUDPResult("result_8000/ndn_3node_buffersize4M_udp_1m.txt"))
    # printUDPResult("NDN 10m", extractUDPResult("result_8000/ndn_3node_buffersize4M_udp_10m.txt"))
    # printUDPResult("NDN 100m", extractUDPResult("result_8000/ndn_3node_buffersize4M_udp_100m.txt"))
    # printUDPResult("NDN 200m", extractUDPResult("result_8000/ndn_3node_buffersize4M_udp_200m.txt"))
    # printUDPResult("NDN 300m", extractUDPResult("result_8000/ndn_3node_buffersize4M_udp_300m.txt"))
    # printUDPResult("NDN 400m", extractUDPResult("result_8000/ndn_3node_buffersize4M_udp_400m.txt"))
    # printUDPResult("NDN 500m", extractUDPResult("result_8000/ndn_3node_buffersize4M_udp_500m.txt"))
    # printUDPResult("MIN 1m", extractUDPResult("result_8000/min_3node_buffersize4M_udp_1m.txt"))
    # printUDPResult("MIN 10m", extractUDPResult("result_8000/min_3node_buffersize4M_udp_10m.txt"))
    # printUDPResult("MIN 100m", extractUDPResult("result_8000/min_3node_buffersize4M_udp_100m.txt"))
    # printUDPResult("MIN 200m", extractUDPResult("result_8000/min_3node_buffersize4M_udp_200m.txt"))
    # printUDPResult("MIN 300m", extractUDPResult("result_8000/min_3node_buffersize4M_udp_300m.txt"))
    # printUDPResult("MIN 400m", extractUDPResult("result_8000/min_3node_buffersize4M_udp_400m.txt"))
    # printUDPResult("MIN 500m", extractUDPResult("result_8000/min_3node_buffersize4M_udp_500m.txt"))

    with open("udpRes.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(["Network", "Rate(Mbps)", "MTU", "jitter(ms)", "totalSend", "totalReceive", "lostRate"])
        # w.writerow(["NDN", 1, 1500] + getRes("result_1500/ndn_3node_buffersize4M_udp_1m.txt"))
        # w.writerow(["NDN", 10, 1500] + getRes("result_1500/ndn_3node_buffersize4M_udp_10m.txt"))
        w.writerow(["NDN", 100, 1500] + getRes("result_1500/ndn_3node_buffersize4M_udp_100m.txt"))
        w.writerow(["NDN", 200, 1500] + getRes("result_1500/ndn_3node_buffersize4M_udp_200m.txt"))
        w.writerow(["NDN", 300, 1500] + getRes("result_1500/ndn_3node_buffersize4M_udp_300m.txt"))
        w.writerow(["NDN", 400, 1500] + getRes("result_1500/ndn_3node_buffersize4M_udp_400m.txt"))
        w.writerow(["NDN", 500, 1500] + getRes("result_1500/ndn_3node_buffersize4M_udp_500m.txt"))
        # w.writerow(["MIN", 1, 1500] + getRes("result_1500/min_3node_buffersize4M_udp_1m.txt"))
        # w.writerow(["MIN", 10, 1500] + getRes("result_1500/min_3node_buffersize4M_udp_10m.txt"))
        w.writerow(["MIN", 100, 1500] + getRes("result_1500/min_3node_buffersize4M_udp_100m.txt"))
        w.writerow(["MIN", 200, 1500] + getRes("result_1500/min_3node_buffersize4M_udp_200m.txt"))
        w.writerow(["MIN", 300, 1500] + getRes("result_1500/min_3node_buffersize4M_udp_300m.txt"))
        w.writerow(["MIN", 400, 1500] + getRes("result_1500/min_3node_buffersize4M_udp_400m.txt"))
        w.writerow(["MIN", 500, 1500] + getRes("result_1500/min_3node_buffersize4M_udp_500m.txt"))
        # w.writerow(["NDN", 1, 8000] + getRes("result_8000/ndn_3node_buffersize4M_udp_1m.txt"))
        # w.writerow(["NDN", 10, 8000] + getRes("result_8000/ndn_3node_buffersize4M_udp_10m.txt"))
        # w.writerow(["NDN", 100, 8000] + getRes("result_8000/ndn_3node_buffersize4M_udp_100m.txt"))
        # w.writerow(["NDN", 200, 8000] + getRes("result_8000/ndn_3node_buffersize4M_udp_200m.txt"))
        # w.writerow(["NDN", 300, 8000] + getRes("result_8000/ndn_3node_buffersize4M_udp_300m.txt"))
        # w.writerow(["NDN", 400, 8000] + getRes("result_8000/ndn_3node_buffersize4M_udp_400m.txt"))
        # w.writerow(["NDN", 500, 8000] + getRes("result_8000/ndn_3node_buffersize4M_udp_500m.txt"))
        # # w.writerow(["MIN", 1, 8000] + getRes("result_8000/min_3node_buffersize4M_udp_1m.txt"))
        # # w.writerow(["MIN", 10, 8000] + getRes("result_8000/min_3node_buffersize4M_udp_10m.txt"))
        # w.writerow(["MIN", 100, 8000] + getRes("result_8000/min_3node_buffersize4M_udp_100m.txt"))
        # w.writerow(["MIN", 200, 8000] + getRes("result_8000/min_3node_buffersize4M_udp_200m.txt"))
        # w.writerow(["MIN", 300, 8000] + getRes("result_8000/min_3node_buffersize4M_udp_300m.txt"))
        # w.writerow(["MIN", 400, 8000] + getRes("result_8000/min_3node_buffersize4M_udp_400m.txt"))
        # w.writerow(["MIN", 500, 8000] + getRes("result_8000/min_3node_buffersize4M_udp_500m.txt"))


def getXY(filepath: str):
    x, y = [], []
    items = extractTCPResult(filepath).groups[-1]
    for item in items:
        x.append(item.endTime)
        y.append(item.bitrate / (1000 * 1000))
    return x, y


def getJitterXY(filepath: str):
    x, y = [], []
    items = extractUDPResult2(filepath)
    for idx, item in enumerate(items):
        x.append(idx + 1)
        y.append(item.jitter)
    return x, y


def getLostRateXY(filepath: str):
    x, y = [], []
    items = extractUDPResult2(filepath)
    for idx, item in enumerate(items):
        x.append(idx + 1)
        y.append(item.lostRate)
    return x, y


def draw(ndnResultFile: str, minResultFile: str, savePath: str, getXYFun=getXY,
         xlabel="Time(s)", ylabel='Bitrate(Mbps)', title: str = "", ylim=-1):
    x1, y1 = getXYFun(ndnResultFile)
    x2, y2 = getXYFun(minResultFile)

    l2 = plt.plot(x2, y2, 'g', label='MIN', linestyle='dotted', marker='^',
                  markerfacecolor='none', markersize=4)
    l1 = plt.plot(x1, y1, 'r', label='NDN', linestyle='dotted', marker='o',
                  markerfacecolor='none', markersize=4)

    fontSize = 24
    if title:
        plt.title(title)
    plt.xlabel(xlabel, fontsize=fontSize)
    plt.xticks(fontsize=fontSize)
    plt.ylabel(ylabel, fontsize=fontSize)
    plt.yticks(fontsize=fontSize)
    if ylim >= 0:
        plt.ylim(ylim)
    # plt.ylim(60, 80)  # 实验0专用
    plt.legend(loc=0, fontsize=fontSize - 4)
    plt.rc('font', family='Times New Roman')

    # save pictures
    full_path = os.getcwd() + "/" + savePath  # 将图片保存到当前目录，记得斜杠；可更改文件格式（.tif），不写的话默认“.png ”
    print(full_path)
    plt.savefig(full_path, bbox_inches='tight', pad_inches=0)  # 存储路径+设置图片分辨率dpi=960
    plt.close()


if __name__ == '__main__':
    matplotlib.rcParams['text.usetex'] = True
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_tcp_1.txt",
        minResultFile="result_1500/min_3node_buffersize4M_tcp_1.txt",
        savePath="tcp_1_client.pdf",
        getXYFun=getXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_tcp_2.txt",
        minResultFile="result_1500/min_3node_buffersize4M_tcp_2.txt",
        savePath="tcp_2_client.pdf",
        getXYFun=getXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_tcp_5.txt",
        minResultFile="result_1500/min_3node_buffersize4M_tcp_5.txt",
        savePath="tcp_5_client.pdf",
        getXYFun=getXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_tcp_10.txt",
        minResultFile="result_1500/min_3node_buffersize4M_tcp_10.txt",
        savePath="tcp_10_client.pdf",
        getXYFun=getXY
    )

    # jitter
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_100m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_100m.txt",
        savePath="udp_jitter_100M.pdf",
        ylabel="jitter(ms)",
        getXYFun=getJitterXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_200m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_200m.txt",
        savePath="udp_jitter_200M.pdf",
        ylabel="jitter(ms)",
        getXYFun=getJitterXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_300m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_300m.txt",
        savePath="udp_jitter_300M.pdf",
        ylabel="jitter(ms)",
        getXYFun=getJitterXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_400m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_400m.txt",
        savePath="udp_jitter_400M.pdf",
        ylabel="jitter(ms)",
        getXYFun=getJitterXY
    )

    # lost rate
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_100m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_100m.txt",
        savePath="udp_lost_rate_100M.pdf",
        ylabel="lost rate(%)",
        ylim=0,
        getXYFun=getLostRateXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_200m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_200m.txt",
        savePath="udp_lost_rate_200M.pdf",
        ylabel="lost rate(%)",
        getXYFun=getLostRateXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_300m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_300m.txt",
        savePath="udp_lost_rate_300M.pdf",
        ylabel="lost rate(%)",
        getXYFun=getLostRateXY
    )
    draw(
        ndnResultFile="result_1500/ndn_3node_buffersize4M_udp_400m.txt",
        minResultFile="result_1500/min_3node_buffersize4M_udp_400m.txt",
        savePath="udp_lost_rate_400M.pdf",
        ylabel="lost rate(%)",
        getXYFun=getLostRateXY
    )
