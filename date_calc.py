import datetime
import time


def date_calculation_click(event, text):
    """[计算过程的实现]
    
    Arguments:
        event {['event']} -- [点击事件]
        text {['str']} -- [点击或者显示的文本]
    
    Returns:
        [str] -- [显示组件显示的文本]
    """

    if event.widget["text"] == "=" and text is not None:
        if "-" in text:
            if "." in text.split("-")[1]:  # 以减号进行分割，提取第二个元素(2019.12.9类型的)
                b = []
                c = []
                for i in text.split("-"):  # 以减号进行分割
                    b.append(i.replace(".", "-"))
                    for j in b:
                        d = time.mktime(time.strptime(j, "%Y-%m-%d"))  # 字符串格式化
                        c.append(d)
                day = int(max(c) - min(c)) / (24 * 60 * 60)
                text = str(day) + "天"
            else:
                text = str(
                    datetime.datetime.strptime(
                        text.split("-")[0].replace(".", "-"), "%Y-%m-%d"
                    )
                    - datetime.timedelta(int(text.split("-")[1]))
                )[:10]
        elif "+" in text:
            text = str(
                datetime.datetime.strptime(
                    text.split("+")[0].replace(".", "-"), "%Y-%m-%d"
                )
                + datetime.timedelta(int(text.split("+")[1]))
            )[:10]

    return text
