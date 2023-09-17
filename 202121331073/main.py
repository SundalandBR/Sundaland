import jieba
import jieba.analyse
import hashlib

org_file_path = 'org.txt'
org_add_file_path = 'org_add.txt'

#文件读取与分词
def readfile():
    with open(org_file_path,"r",encoding='utf-8') as o:
        org_data = o.read()
    with open(org_add_file_path,"r",encoding='utf-8') as od:
        org_add_data = od.read()
    return org_data,org_add_data

# jieba TF-IDF权重
def weights(org_data,org_add_data):
    org_tags = jieba.analyse.extract_tags(org_data,topK = 20,withWeight = True,allowPOS=0)
    org_add_tags = jieba.analyse.extract_tags(org_add_data,topK = 20,withWeight = True,allowPOS=0)
    return org_tags,org_add_tags

# MD5HASH值计算
def MD5Hash(string):
    md5 = hashlib.md5()
    md5.update(string.encode("utf-8"))
    return bin(int(md5.hexdigest()[8:-8],16))[2:].zfill(64) # 转化为64bit 2进制

# Hash加权、合并、降维
def simhash(packetlist):
    whash = [0] * 64 # 64bit
    # 将求得的64bithash值加权求和
    for hash,(word,weights) in packetlist:
        for i,n in enumerate(hash):
            t = weights if n == '1' else (-weights)
            whash[i] += t
    # 降维
    for i,val in enumerate(whash):
        whash[i] = 1 if val>0 else 0
    return whash
    

org_hashlist = []
org_add_hashlist = []
od,oad = readfile()
org_tag,orgadd_tag = weights(od,oad)
for word,weight in org_tag:
    org_hashlist.append(MD5Hash(word))
for word,weight in orgadd_tag:
    org_add_hashlist.append(MD5Hash(word))
packlist = list(zip(org_add_hashlist,orgadd_tag))
print(simhash(packlist))

#精确模式



