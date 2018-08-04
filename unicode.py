# encoding=utf-8
import io

f = io.open('code.txt', 'wt', encoding='utf-8')
f.write(u"Image non-English 我爱刷豆瓣")
f.close()

text = io.open('code.txt', encoding='utf-8')
print(text.read())
