from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.caption_filepath, 'r') as f:
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
            yt.captions = captions

        return data