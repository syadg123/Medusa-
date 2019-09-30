#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import InformationDisclosure.Druid
import InformationDisclosure.Git
import InformationDisclosure.Phpinfo
import InformationDisclosure.PhpApc
import InformationDisclosure.Sftp
import InformationDisclosure.Svn
import InformationDisclosure.JetBrains
import InformationDisclosure.Options
import InformationDisclosure.JavaConfigurationFile
import InformationDisclosure.SensitiveFile

import ClassCongregation

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=InformationDisclosure.Druid.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.SensitiveFile.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa = InformationDisclosure.Git.medusa(Url, RandomAgent, ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.Phpinfo.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.PhpApc.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.Sftp.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.Svn.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.JetBrains.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.Options.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
    try:
        Medusa=InformationDisclosure.JavaConfigurationFile.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass