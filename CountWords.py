import requests
import json

def countwords(sentence):
    '''
    input:
        sentence: (str) 漢字の混じった文
    output:
        (int): ひらがなに直した際の文字数
    '''
    with open("api_keys.json","r") as f:
        subscription_info=json.load(f)
    app_id = subscription_info["app_id"]

    target_url = "https://labs.goo.ne.jp/api/hiragana"
    headers ={"content-type":"application/json"}
    obj={"app_id": app_id, "sentence": sentence, "output_type":"hiragana"}
    json_data=json.dumps(obj).encode("utf-8")

    post_result = requests.post(target_url, json_data, headers=headers)
    # print(post_result.text)
    json_obj=post_result.json()
    raw_data = json_obj["converted"]
    non_space_sentence = raw_data.replace(" ", "")
    return len(non_space_sentence)

if __name__ == "__main__":
    sentence="漢字が混じっている文章"
    print(countwords(sentence))