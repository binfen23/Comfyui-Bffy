import urllib.request
import json

class bffanyi:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "default":"",
                    "multiline": True
                    }),
            },
        }
    #输出点的类型
    RETURN_TYPES = ("STRING",)
    #输出点的名称
    RETURN_NAMES = ("翻译后",)
    #执行的函数
    FUNCTION = "translate_text"
    #右键显示的分组名
    CATEGORY = "缤纷翻译"

    #函数，self这个参数必须有，第二个参数为传参，在required字典定义的text中的default就是data
    def translate_text(self,text):
        # 构造请求数据
        url = 'https://transmart.qq.com/api/imt'
        data = {
            "header": {
                "fn": "auto_translation",
                "session": "",
                "client_key": "browser-edge-chromium-113.0.1774-Windows_10",
                "user": ""
            },
            "type": "plain",
            "model_category": "normal",
            "text_domain": "",
            "source": {
                "lang": "zh",
                "text_list": [text]
            },
            "target": {
                "lang": "en"
            }
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1774.0 Safari/537.36'
        }

        # 将数据转换为JSON格式
        data = json.dumps(data).encode('utf-8')

        # 创建请求对象
        req = urllib.request.Request(url, data=data, headers=headers)

        # 发送请求并获取响应
        with urllib.request.urlopen(req) as response:
            # 读取响应数据
            result = response.read().decode('utf-8')
            # 解析JSON
            json_result = json.loads(result)
            # 提取ret_code的值
            ret_code = json_result['header']['ret_code']
            # 判断ret_code的值
            if ret_code == "succ":
                # ret_code为"succ"，存储auto_translation的第一个值
                auto_translation_value = json_result['auto_translation'][0]
                # 将翻译结果中的中文逗号、句号替换为英文逗号，并去除多余的空格和逗号
                auto_translation_value = auto_translation_value.replace('，', ',').replace('。', ',').replace("  ", " ").replace(" ,", ",").replace(",,", ",").replace("!", " ")
            else:
                # ret_code不为"succ"，设置变量值为"翻译失败"
                auto_translation_value = "翻译失败"

        # 返回翻译结果
        return (auto_translation_value,)
