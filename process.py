from multiprocessing import Process, Queue
import time


# 消费者进程
class ConsumerProcess(Process):
    def __init__(self, name, args):
        super().__init__(group=None)
        self.name = name
        self.queue = args[0]

    def run(self):
        while True:
            v = self.queue.get(True)
            if v == 'finish':
                break

            print(f'消费{v}')

            time.sleep(0.1)


# 生产者进程
class ProducerProcess(Process):
    def __init__(self, name, args):
        super().__init__(group=None)
        self.name = name
        self.queue = args[0]

    def run(self):
        for v in range(100):
            print(f'生产{v}')
            self.queue.put(v)
            # time.sleep(0.1)
        self.queue.put('finish')


# 写入队列，指定最多100个
queue = Queue(10)


w = ProducerProcess(name='生产者', args=(queue,))
r = ConsumerProcess(name='消费者', args=(queue,))

w.start()
r.start()

w.join()
r.join()

print('finish')
