"""正则表达式：用来使用某种规则匹配字符串子串"""
'''
re是regular expression正则表达式的简写
Match object;span(4,8)匹配的对象，匹配到的子字符串索引位置是4到8
正则表达式里面的元字符：[abc]
'''
import re

m_string='yuzewang123456'
pattern= 'wang'
result=re.search(pattern=pattern,string=m_string)
#匹配对象
print(result)
#得到最终的结果，默认值为0
#要得到匹配的字符串，一定要加group()
print(result.group(0))
#[abc]从中括号中任选一个字符匹配都是可以的
my_string='yuzew2ng123456'
pattern='w[abc123]ng'
result=re.search(pattern=pattern,string=my_string)
print(result)
#.表示匹配任意字符
y_string='yuzew2ng123456'
pattern='yuz.'
result=re.search(pattern=pattern,string=y_string)
print(result)
#{m,n}匹配m~n次，最少m次，最多n次;{m}匹配m次
y_string='yuzew2ng123456'
pattern='.{6,9}'
result=re.search(pattern=pattern,string=y_string)
print(result)
# '#.{,}#'左边是0，右边无穷大
y_string='{"mobile_phone":"#investor_phone#"，"mobile_pwd":"#investor_pwd#"}'
pattern='#.{,}#'
result=re.search(pattern=pattern,string=y_string)
print(result)
# \w表示匹配1个字母
y_string='{"mobile_phone":"#investor_phone#"，"mobile_pwd":"#investor_pwd#"}'
pattern='\w'
result=re.search(pattern=pattern,string=y_string)
print(result)
# \d表示匹配一个数字
y_string='{"mobile_phone":"#investor_phone#"，"mobile_pwd":"#investor_pwd#"}'
pattern='\d'
result=re.search(pattern=pattern,string=y_string)
print(result)
# *号匹配前面的字符0次或多次；
#.*号表示匹配任意字符0次或多次；
# ？号表示0次或者1次（非贪婪模式），尽可能少的匹配
#.*?常用组合，表示匹配任意字符0次或多次，非贪婪模式；search只会找一次
y_string='{"mobile_phone":"#investor_phone#"，"pwd":"#investor_pwd#"}'
pattern='#.*?#'
result=re.search(pattern=pattern,string=y_string)
print(result)
#finditer找多个匹配数据
class Data:
    investor_phone='13788881111'
    investor_pwd='123456'
y_string='{"mobile_phone":"#investor_phone#"，"pwd":"#investor_pwd#"}'
pattern='#(.*?)#'
results=re.finditer(pattern=pattern,string=y_string)
for result in results:
    old=result.group()
    key=result.group(1)
    #获取Data类下面键的属性值
    new=getattr(Data,key,'')
    y_string=y_string.replace(old,new)
print(y_string)
#group(1)获取括号当中的内容
#group(0)获取整个匹配内容
#有1个括号就有group(1)，有2个括号就有group(2)，有两个括号的情况很少





