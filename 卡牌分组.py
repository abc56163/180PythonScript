'''
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。
'''

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) > 1:
            b = {}
            l = []
            for i in deck:
                if i in b.keys():
                    b[i] += 1
                else:
                    b[i] = 1
            for v in b.items():
                l.append(v)
            if len(v) > 1:
                print(False)
            else:
                print(True)
        else:
            print(False)
if __name__ == '__main__':
    a = [1, 1, 1, 2, 2, 2, 3, 3]
    k = Solution()
    k.hasGroupsSizeX(a)










