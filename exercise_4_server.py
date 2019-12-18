from socket import *


# 容器
class Mylist:
    def __init__(self):
        self._elem = []

    def push(self, val):
        self._elem.append(val)

    def pop(self):
        return self._elem.pop()

    def empty(self):
        return self._elem == []


class Ver:
    def __init__(self):
        self.parens = "{}[]()"  # 需要验证的字符
        self.left_parens = "{[("
        # 　验证配对是否正确
        self.opposite = {'}': '{', ']': '[', ')': '('}
        self.vessel = Mylist()

    # 负责提供遍历到的括号
    def parent(self, text):
        """
        遍历字符串,提供括号字符和其位置
        """
        # 　ｉ记录索引位置
        i, text_len = 0, len(text)
        while True:
            # 循环遍历字符串
            # 到结尾结束，遇到括号提供给ｖｅｒ
            while i < text_len and text[i] not in self.parens:
                i += 1

            if i >= text_len:
                return
            else:
                yield text[i], i
                i += 1

    # 　字符是否匹配的验证工作
    def ver(self, text):
        for pr, i in self.parent(text):
            if pr in self.left_parens:
                self.vessel.push((pr, i))  # 左括号入栈
            elif self.vessel.empty() or self.vessel.pop()[0] != self.opposite[pr]:
                return "Unmatching is found at %d for %s" % (i, pr)
        # 　ｆｏｒ循环正常结束
        if self.vessel.empty():
            return "All parentheses are matched"
        else:
            # 　剩下左括号了
            p = self.vessel.pop()
            return "Unmatching is found at %d for %s" % (p[1], p[0])


def main():
    s = socket()
    s.bind(('0.0.0.0', 8000))
    s.listen(3)
    while True:
        text = ""
        c, addr = s.accept()
        while True:
            data = c.recv(1024).decode()
            if data == '##':
                break
            text += data
        # 验证括号
        v = Ver()
        msg = v.ver(text)
        c.send(msg.encode()) # 回复结果


# 主程序只负责做括号的验证
if __name__ == '__main__':
    main()
