import re
import statistics


class TCPMeasureItem:
    def __init__(self):
        self.startTime = 0  # 起始时间
        self.endTime = 0  # 终止时间
        self.transferBytes = 0  # 这段时间内传输的字节数，单位 Bytes
        self.bitrate = 0  # 这段时间内传输的速率，单位bps
        self.retryTime = 0  # 这段时间内TCP重传的次数
        self.cwnd = 0  # TCP窗口的大小，单位 Bytes


class UDPMeasureItem:
    def __init__(self):
        self.jitter = 0  # 网络抖动，单位 ms
        self.totalSend = 0  # 总的发出的UDP包数量
        self.totalReceive = 0  # 总的接收到的UDP包数量
        self.lostRate = 0  # 丢包率


def getNum(v: str):
    """
    1G = 1000000000
    1M = 1000000
    1K = 1000
    :param v:
    :return:
    """
    if v.endswith('G'):
        return float(v[:-1]) * 1000000000
    elif v.endswith('M'):
        return float(v[:-1]) * 1000000
    elif v.endswith('K'):
        return float(v[:-1]) * 1000
    else:
        return float(v)


class TCPMeasureResult:

    def __init__(self):
        # 多组并行测试结果
        self.groups: [[TCPMeasureItem]] = []
        self.StatisticalResult = {}
        self.groupMap = {}

    def appendItem(self, groups: [str]):
        """
        [' 13', '58.00-59.00  ', '  1.39 M', '  11.7 M', '257', '  1.41 K']
        ['SUM', '58.00-59.00  ', '  3.88 M', '  32.6 M', '724']
        :param groups:
        :return:
        """
        # 清除掉无用字符串
        for i in range(len(groups)):
            groups[i] = groups[i].strip()

        # 判断属于哪一组
        groupNum = 0
        # 判断是不是一个新的组别
        if groups[0] not in self.groupMap:
            self.groups.append([])
            self.groupMap[groups[0]] = len(self.groups) - 1
            groupNum = len(self.groups) - 1
        else:
            groupNum = self.groupMap[groups[0]]

        item = TCPMeasureItem()
        item.startTime = float(groups[1].split('-')[0])
        item.endTime = float(groups[1].split('-')[1])
        item.transferBytes = getNum(groups[2])
        item.bitrate = getNum(groups[3])
        item.retryTime = getNum(groups[4])
        if len(groups) > 5:
            # [' 13', '58.00-59.00  ', '  1.39 M', '  11.7 M', '257', '  1.41 K']
            item.cwnd = getNum(groups[5])
            pass
        elif len(groups) == 5:
            # ['SUM', '58.00-59.00  ', '  3.88 M', '  32.6 M', '724']
            pass
        self.groups[groupNum].append(item)


def extractTCPResult(filePath: str) -> TCPMeasureResult:
    rule1 = r'\[(.*?)\]\s*(.*?)sec(.*?)Bytes(.*?)bits/sec\s*(\d*)\s(.*?)Bytes'
    rule2 = r'\[SUM\]\s*(.*?)sec(.*?)Bytes(.*?)bits/sec\s*(\d*)\s'
    result = TCPMeasureResult()
    with open(filePath) as file:
        # 先读取到头部
        lines = file.readlines()
        cur = 0
        # 去掉头部
        for i in range(cur, len(lines)):
            cur += 1
            if lines[i].startswith("[ ID]"):
                break

        # 读取测试数据
        for i in range(cur, len(lines)):
            res = re.match(rule1, lines[i], re.M | re.I)
            if res:
                result.appendItem(list(res.groups()))
            else:
                # SUM
                res = re.match(rule2, lines[i], re.M | re.I)
                if res:
                    result.appendItem(['SUM'] + list(res.groups()))
                    # print(['SUM'] + list(res.groups()))
            # print(line)
            # if line.startswith("[ ID]"):
            #     break
            cur += 1
            if lines[i].startswith("[ ID]"):
                break

    # 最后读取统计数据
    return result


def extractUDPResult(filePath: str) -> UDPMeasureItem:
    senderRule = r'(.*?)bits/sec(.*?)ms(.*?)\((.*?)\%\)(.*?)sender'
    receiverRule = r'(.*?)bits/sec(.*?)ms(.*?)\((.*?)\%\)(.*?)receiver'
    udpItem = UDPMeasureItem()
    senderData = []
    receiverData = []
    with open(filePath) as file:
        # 先读取到头部
        lines = file.readlines()
        for line in lines[-6:]:
            senderRes = re.match(senderRule, line, re.M | re.I)
            if senderRes:
                senderData = senderRes.groups()
            receiverRes = re.match(receiverRule, line, re.M | re.I)
            if receiverRes:
                receiverData = receiverRes.groups()
    udpItem.jitter = float(receiverData[1].strip())
    udpItem.totalReceive = float(receiverData[2].strip().split("/")[1]) - float(receiverData[2].strip().split("/")[0])
    udpItem.totalSend = float(senderData[2].strip().split("/")[1])
    udpItem.lostRate = (udpItem.totalSend - udpItem.totalReceive) / udpItem.totalSend
    return udpItem


def extractUDPResult2(filePath: str) -> [UDPMeasureItem]:
    rule = r'(.*?)bits/sec(.*?)ms(.*?)\((.*?)\%\)'
    result = []
    with open(filePath) as file:
        # 先读取到头部
        lines = file.readlines()
        cur = 0
        # 去掉头部
        for i in range(cur, len(lines)):
            cur += 1
            if lines[i].startswith("[ ID]"):
                break

        # 读取测试数据
        for i in range(cur, len(lines)):
            res = re.match(rule, lines[i], re.M | re.I)
            if res:
                item = UDPMeasureItem()
                data = res.groups()
                item.jitter = float(data[1].strip())
                item.totalSend = float(data[2].strip().split("/")[1])
                item.totalReceive = float(data[2].strip().split("/")[0])
                item.lostRate = float(data[3].strip())
                result.append(item)
            cur += 1
            if lines[i].startswith("[ ID]"):
                break
    return result
