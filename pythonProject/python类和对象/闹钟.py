#  设计一个闹钟类
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

    # 构建闹钟让其工作
clock1 = Clock()
clock1.ring()
