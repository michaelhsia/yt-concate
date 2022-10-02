from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils) # 把step裡的各個步驟都執行process這個method
            except StepException as e:
                print('Exception happened:', e)
                break
