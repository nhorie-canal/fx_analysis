import queue
import time


class Trading(object):
    def __init__(self, events, strategy, execution):
        self.events = events
        self.strategy = strategy
        self.execution = execution

    def trade(self):
        heartbeat = 0.5  # 0.5秒間隔
        while True:
            try:
                event = self.events.get(False)
            except queue.Empty:
                pass
            else:
                if event is not None:
                    if event.type == 'TICK':
                        self.strategy.calculate_signals(event)
                    elif event.type == 'ORDER':
                        print("Executing order!")
                        self.execution.execute_order(event)
            time.sleep(heartbeat)
