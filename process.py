from multiprocessing import Process, Queue
import time


class Reader(Process):
    def __init__(self, name, args):
        super().__init__(group=None)
        self.name = name
        self.args = args

    def run(self):
        while True:
            v = self.args[0].get(True)
            print(f'读取{v}')
            if v == 99:
                break

            time.sleep(0.2)


class Writer(Process):
    def __init__(self, name, args):
        super().__init__(group=None)
        self.name = name
        self.args = args

    def run(self):
        for v in range(100):
            print(f'写入{v}')
            self.args[0].put(v)
            # time.sleep(0.1)


# 写入队列，指定最多100个
q = Queue(10)


w = Writer(name='writer', args=(q,))
r = Reader(name='reader', args=(q,))

w.start()
r.start()

w.join()
r.join()

print('finish')
