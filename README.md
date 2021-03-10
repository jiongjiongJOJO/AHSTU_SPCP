<div align="center">
<h1 align="center">安徽科技学院疫情填报和体温填报每日自动执行</h1>
<img src="https://img.shields.io/github/issues/jiongjiongJOJO/AHSTU_SPCP?color=green">
<img src="https://img.shields.io/github/stars/jiongjiongJOJO/AHSTU_SPCP?color=yellow">
<img src="https://img.shields.io/github/forks/jiongjiongJOJO/AHSTU_SPCP?color=orange">
<img src="https://img.shields.io/github/license/jiongjiongJOJO/AHSTU_SPCP?color=ff69b4">
<img src="https://img.shields.io/github/search/jiongjiongJOJO/AHSTU_SPCP/main?color=blue">
<img src="https://img.shields.io/github/languages/code-size/jiongjiongJOJO/AHSTU_SPCP?color=critical">
</div>

# 简介


安徽科技学院自动完成学生健康情况填报、每日健康监测。

开源不易，如果本项目对你有帮助，那么就请给个star吧。😄

# 目录

- [简介](#简介)
- [目录](#目录)
- [功能](#功能)
- [使用方式](#使用方式)
  - [Github Actions（推荐）](#github-actions推荐)
    - [1.fork本项目](#1fork本项目)
    - [2.准备需要的参数](#2准备需要的参数)
    - [3.将参数填到Secrets](#3将参数填到secrets)
    - [4.开启Actions](#4开启actions)
    - [5.进行一次push操作](#5进行一次push操作)
- [通知推送方式](#通知推送方式)
- [申明](#申明)
- [参考项目](#参考项目)

# 功能

* [x] 自动填报三次随机体温（36.0~36.9）
* [x] 自动填报学生健康情况

# 使用方式

## Github Actions

### 1.fork本项目

项目地址：[jiongjiongJOJO/AHSTU_SPCP](https://github.com/jiongjiongJOJO/AHSTU_SPCP)
点击右上角Fork按钮，将项目fork到自己的仓库。

### 2.准备需要的参数

学号、密码、`Data`。

其中`Data`的获取:

+ 第一步：打开“学生健康情况填报”，填写正确的健康信息
![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/1.jpg)
+ 第二步：打开浏览器的开发者工具（在学生健康情况填报页面按下键盘的F12按钮），并选择标签页的Network（网络）标签
![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/2.jpg)
+ 第三步：回到页面，提交“学生健康情况填报”信息，接着打开 开发者工具
![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/3.jpg)
+ 第四步：在开发者工具页面找到“Index”字样，右键点击后选择Copy - Copy as cURL(bash)
+ ![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/4.jpg)
+ 第五步：打开[Convert cURL command syntax](https://curl.trillworks.com/),粘贴刚刚复制的内容
+ ![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/5.jpg)
+ 第六步：在右侧找到如下格式的信息，并将内容复制（包括前后两个大括号“{}”）
> data = {
>   xxx:xxx,
>   xxx:xxx,
>   xxx:xxx
> }
![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/6.jpg)
 
### 3.将参数填到Secrets

在`Secrets`中的`Name`和`Value`格式如下：

Name | Value
-|-
DATA | 上一步中复制的内容
USERID | 学号
PASSWORD | 密码
SEND | push推送的token（选填）
![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/7.jpg)
![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/8.jpg)

### 4.开启Actions

默认`Actions`处于禁止状态，在`Actions`选项中开启`Actions`功能，把那个绿色的长按钮点一下。如果看到左侧工作流上有黄色`!`号，还需继续开启。

![](https://github.com/jiongjiongJOJO/AHSTU_SPCP/img/9.jpg)

### 5.进行一次push操作

`push`操作会触发工作流运行。

删除掉`README.md`中的😄即可。完成后，每天将自动完成每日任务。



# 通知推送方式

## pushplus机器人
！！！此功能暂未修改，目前使用的是server酱，过几天会修改为pushplus
类似于钉钉机器人，只需要一个`token`，参考[获取pushplus的token](http://pushplus.hxtrip.com/doc/guide/api.html#%E4%B8%80%E3%80%81%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF%E6%8E%A5%E5%8F%A3)。

# 申明

本项目仅用于学习。

# 参考项目

[srcrs/UnicomTask](https://github.com/srcrs/UnicomTask)，参考了该项目的README.md文档



