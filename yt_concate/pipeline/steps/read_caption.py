import os

from pprint import pprint

from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line: # 會自動檢查是不是True, 不用寫成 = True
                        caption = line
                        captions[caption] = time
                        time_line = False # 調回False才能再次讀取下一行時間
            data[caption_file] = captions # 把data的key設定成檔名，才知道之後下載哪個字幕檔
        pprint(data)
        return data