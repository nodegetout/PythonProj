# 引论

## pythonic conception

definition,code style,standard library,library or framework

>> * 美胜丑 | 显胜隐 | 简胜杂 | 杂胜乱 | 平胜陡 | 疏胜密
>> * 简单问题的一个方法也是唯一方法
>> * 好主意易于解释

            --- Zen Of Python
``` python
a = 1 , b = 2
# not good
temp = a
a = b
b = temp
# good
a , b = b , a
```
>> * 包和框架的名字用小写以及单数形式，并且短小
>> * 包通常只作为命名空间

## pythonic coding

### 避免劣化代码

>> * 避免只用大小写区分不同对象
>> * 避免使用容易混淆的名字
>> * 不要害怕过长的变量名

### 深入理解python

>> * 语言特性和库特性 Official Languange Reference and Library Reference
>> * 知识更行（版本差异）
>> * Pythonic的框架  Flask gevent request

## python与C语言的不同

>> * 代码缩进和{}

>> * ' 和 "

>> * 三元操作符

 C风格      ————  ? :  
 Python风格 ———— X if conditions else statement

>> * switch语句

``` c
switch(){
    case :
        break;
    case :
        break;
    default:
        break;
}
```

```python
if :
elif : 
elif : 
else :
# 或者
def f(x):
    return {
        0: "you typed zero!",
        1: "you are in top!",
        2: "n is an even-number!",
    }.get(x,"Only single-digital numbers are allowed.\n")

```

## 代码中添加适当注释

## 函数四原则
> * 短小，嵌套不宜过深
> * 函数声明合理 简单 和易用
> * 考虑向下兼容
> * 函数语句粒度的一致性（一个函数只做一件事情）

## 将常量集中在一个文件中

