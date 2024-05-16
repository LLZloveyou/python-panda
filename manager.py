# 导入相关处理包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 读取候选人信息，由于原始数据没有表头，需要添加表头
candidates = pd.read_csv("weball20.txt", sep = '|',names=['CAND_ID','CAND_NAME','CAND_ICI','PTY_CD','CAND_PTY_AFFILIATION','TTL_RECEIPTS',
                                                          'TRANS_FROM_AUTH','TTL_DISB','TRANS_TO_AUTH','COH_BOP','COH_COP','CAND_CONTRIB',
                                                          'CAND_LOANS','OTHER_LOANS','CAND_LOAN_REPAY','OTHER_LOAN_REPAY','DEBTS_OWED_BY',
                                                          'TTL_INDIV_CONTRIB','CAND_OFFICE_ST','CAND_OFFICE_DISTRICT','SPEC_ELECTION','PRIM_ELECTION','RUN_ELECTION'
                                                          ,'GEN_ELECTION','GEN_ELECTION_PRECENT','OTHER_POL_CMTE_CONTRIB','POL_PTY_CONTRIB',
                                                          'CVG_END_DT','INDIV_REFUNDS','CMTE_REFUNDS'])
# 读取候选人和委员会的联系信息
ccl = pd.read_csv("ccl.txt", sep = '|',names=['CAND_ID','CAND_ELECTION_YR','FEC_ELECTION_YR','CMTE_ID','CMTE_TP','CMTE_DSGN','LINKAGE_ID'])
# 关联两个表数据
ccl = pd.merge(ccl,candidates)
# 提取出所需要的列
ccl = pd.DataFrame(ccl, columns=[ 'CMTE_ID','CAND_ID', 'CAND_NAME','CAND_PTY_AFFILIATION'])
# 读取个人捐赠数据，由于原始数据没有表头，需要添加表头
# 提示：读取本文件大概需要5-10s
itcont = pd.read_csv('itcont_2020_20200722_20200820.txt', sep='|',names=['CMTE_ID','AMNDT_IND','RPT_TP','TRANSACTION_PGI',
                                                                                  'IMAGE_NUM','TRANSACTION_TP','ENTITY_TP','NAME','CITY',
                                                                                  'STATE','ZIP_CODE','EMPLOYER','OCCUPATION','TRANSACTION_DT',
                                                                                  'TRANSACTION_AMT','OTHER_ID','TRAN_ID','FILE_NUM','MEMO_CD',
                                                                                  'MEMO_TEXT','SUB_ID'])

# 将候选人与委员会关系表ccl和个人捐赠数据表itcont合并，通过 CMTE_ID
c_itcont =  pd.merge(ccl,itcont)
# 提取需要的数据列
c_itcont = pd.DataFrame(c_itcont, columns=[ 'CAND_NAME','NAME', 'STATE','EMPLOYER','OCCUPATION',
                                           'TRANSACTION_AMT', 'TRANSACTION_DT','CAND_PTY_AFFILIATION'])
#空值处理，统一填充 NOT PROVIDED
c_itcont['STATE'].fillna('NOT PROVIDED',inplace=True)
c_itcont['EMPLOYER'].fillna('NOT PROVIDED',inplace=True)
c_itcont['OCCUPATION'].fillna('NOT PROVIDED',inplace=True)
# 对日期TRANSACTION_DT列进行处理
c_itcont['TRANSACTION_DT'] = c_itcont['TRANSACTION_DT'] .astype(str)
# 将日期格式改为年月日  7242020	
c_itcont['TRANSACTION_DT'] = [i[3:7]+i[0]+i[1:3] for i in c_itcont['TRANSACTION_DT'] ]


# 从所有数据中取出支持拜的数据
biden = c_itcont[c_itcont['CAND_NAME']=='BIDEN, JOSEPH R JR']
# 统计各州对拜的捐款总数
biden_state = biden.groupby('STATE').sum().sort_values("TRANSACTION_AMT", ascending=False)
q=np.array(biden_state) #创建ndarray 对象
number_b=len(q)   #支持拜州的数量

# 从所有数据中取出支持特朗的数据
trump = c_itcont[c_itcont['CAND_NAME']=='TRUMP, DONALD J.']
# 统计各州对特朗的捐款总数
trump_state = trump.groupby('STATE').sum().sort_values("TRANSACTION_AMT", ascending=False)
w=np.array(trump_state)  #创建ndarray 对象
number_t=len(w)  #支持特朗州的数量


#pivot_table作用是按职业和捐赠数额聚合数据,index=['STATE']取出捐赠人所在的职业，values=['TRANSACTION_AMT']取出捐赠人捐赠的数额，aggfunc='sum'计算相同州的总额
by_occupation=pd.pivot_table(c_itcont,index=['STATE'],values=['TRANSACTION_AMT'],aggfunc='sum')                                                                                                 
number=len(by_occupation)  #州的数量

# 从所有数据中取出支持拜的数据
biden = c_itcont[c_itcont['CAND_NAME']=='BIDEN, JOSEPH R JR']
# 统计各职业对拜的捐款总数
biden_state = biden.groupby('OCCUPATION').sum().sort_values("TRANSACTION_AMT", ascending=False)
e=np.array(biden_state)   #创建ndarray 对象

# 从所有数据中取出支持特朗的数据
biden = c_itcont[c_itcont['CAND_NAME']=='TRUMP, DONALD J.']
# 统计各职业对特朗的捐款总数
biden_state = biden.groupby('OCCUPATION').sum().sort_values("TRANSACTION_AMT", ascending=False)  
r=np.array(biden_state)    #创建ndarray 对象



#pivot_table作用是按职业和捐赠数额聚合数据,index=['OCCUPATION']取出捐赠人所在的职业，values=['TRANSACTION_AMT']取出捐赠人捐赠的数额，aggfunc='sum'计算相同职业的总额
by_occupation=pd.pivot_table(c_itcont,index=['OCCUPATION'],values=['TRANSACTION_AMT'],aggfunc='sum')                                                                                                 
number_j=len(by_occupation) #职业的总数量

print('州的总数:{}'.format(number))
print('支持BIDEN, JOSEPH R JR州的数量:{}'.format(number_b))
print('支持特朗州的数量:{}'.format(number_t))

print('职业的总数:{}'.format(number_j))
print('支持BIDEN, JOSEPH R JR的数量：{}'.format(len(e)))
print('支持特朗的数量:{}'.format(len(r)))