# python-panda

基于Pandas揭秘美国选民的总统喜好


**数据介绍**
1.所有候选人信息
该文件为每个候选人提供一份记录，并显示候选人的信息、总收入、从授权委员会收到的转账、付款总额、给授权委员会的转账、库存现金总额、贷款和债务以及其他财务汇总信息。

CAND_ID :候选人ID

CAND_NAME :候选人姓名

CAND_PTY_AFFILIATION: 候选人党派
数据来源:[https://www.fec.gov/files/bulk-downloads/2020/weball20.zip](https://www.fec.gov/files/bulk-downloads/2020/weball20.zip)

2.候选人委员会链接信息
该文件显示候选人的身份证号码、候选人的选举年份、联邦选举委员会选举年份、委员会识别号、委员会类型、委员会名称和链接标识号。

CAND_ID 候选人ID

CAND_ELECTION_YR 候选人选举年份

CMTE_ID 委员会ID
数据来源:[https://www.fec.gov/files/bulk-downloads/2020/ccl20.zip](https://www.fec.gov/files/bulk-downloads/2020/ccl20.zip)

3.个人捐款档案信息
【注意】由于文件较大，本数据集只包含2020.7.18-2020.8.1的相关数据，如果需要更全数据可以通过数据来源中的地址下载。

CMTE_ID 委员会ID

NAME 捐款人姓名

CITY 捐款人所在市

State 捐款人所在州

EMPLOYER 捐款人雇主/公司

OCCUPATION 捐款人职业
数据来源:[https://www.fec.gov/files/bulk-downloads/2020/indiv20.zip](https://www.fec.gov/files/bulk-downloads/2020/indiv20.zip)
