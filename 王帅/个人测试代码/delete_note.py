# -*- coding: GBK -*-
#py�ļ�ȥע��

import re
import os
import configparser

Python='CleanNote'
SrcPath='E:\python\py_pick\\result'
DescPath='E:\python\py_pick\\result'

def ReadIni(path,section,option):#�ļ�·�����½ڣ��ؼ���
  #��ȡini
  cf=configparser.ConfigParser()
  cf.read(path)
  value=cf.get(section,option)#�����getint()��ֱ�Ӷ�ȡ����������Ϊ����
  return value

def IsPassLine(strLine):
  #�Ƿ��ǿ��Ժ��Ե���
  #�ɺ����е�������ʽ�б�
  RegularExpressions=["""/'.*#.*/'""","""/".*#.*/""",
            """/'/'/'.*#.*/'/'/'""","""/"/"/".*#.*/"/"/"""]
  for One in RegularExpressions:
    zz=re.compile(One)
    if re.search(zz,strLine)==None:
      continue
    else:
      return True#��ƥ�� �����
    return False

def ReadFile(FileName):
  #��ȡ�������ļ�
  fobj=open(FileName,'r',encoding='utf-8')
  AllLines=fobj.readlines()
  fobj.close()
  NewStr=''
  LogStr='/n%20s/n'%(FileName.split('//')[-1])#�������־
  nline=0
  for eachline in AllLines:
    index=eachline.find('#')#��ȡ��ע�;䡮#'��λ������
    if index==-1 or nline<3 or IsPassLine(eachline):
      if eachline.strip()!='':#�ų����յ���
        NewStr=NewStr+eachline
    else:
      if index!=0:
        #NewStr=NewStr+eachline[:index]+'/n'#��ȡ�����ע�Ͳ���
        NewStr = NewStr + eachline[:index]  # ��ȡ�����ע�Ͳ���
        LogStr+="ChangeLine: %s/t%s"%(nline,eachline[index:])
    nline+=1
  return NewStr,LogStr

def MakeCleanFile(SrcPath,DescPath,FileList):
  fLog=open(DescPath+'//'+'CleanNoteLog.txt','w',encoding='utf-8')
  for File in FileList:
    curStr,LogStr=ReadFile(SrcPath+'//'+File)
    fNew=open(DescPath+'//without_note_'+File,'w',encoding='utf-8')
    fNew.write(curStr)
    fNew.close()
    fLog.write(LogStr)
  fLog.close()

def Main():
  #���Բ������ַ�ʽ����ʱ����
  #��ini��ȡԴ�ļ��м�Ŀ���ļ���·��
  '''
  IniPath = 'CleanNote.ini'
  SrcPath=ReadIni(IniPath,'CleanNote','SrcPath')#Դ�ļ���
  DescPath=ReadIni(IniPath,'CleanNote','DescPath')#Ŀ���ļ���
  '''

  #���Ŀ���ļ��в����ڣ�����֮
  if not os.path.exists(DescPath):
    os.makedirs(DescPath)
  FileList=[]
  for files in os.walk(SrcPath):
    for FileName in files[2]:
      if FileName.split('.')[-1]=='py':
        FileList.append(FileName)
  print(FileList)
  MakeCleanFile(SrcPath,DescPath,FileList)
if __name__=='__main__':
  Main()
  print('>>>End<<<')
  os.system('pause')

