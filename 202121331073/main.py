import jieba
import jieba.analyse
import hashlib

org_file_path = 'org.txt'
org_add_file_path = 'org_add.txt'
ans_path = 'ans.txt'

class simhash_check():
    #文件读取与分词
    def __init__(self,org_file_path,org_add_file_path):
        with open(org_file_path,"r",encoding='utf-8') as o:
            self.org_data = o.read()
        with open(org_add_file_path,"r",encoding='utf-8') as od:
            self.org_add_data = od.read()

    # jieba TF-IDF权重
    def tf_idf(self):
        self.org_tags = jieba.analyse.extract_tags(self.org_data,topK = 20,withWeight = True)    # noqa: E501
        self.org_add_tags = jieba.analyse.extract_tags(self.org_add_data,topK = 20,withWeight = True)  # noqa: E501

    # MD5 hash加密计算
    def MD5Hash(self,string):
        md5 = hashlib.md5()
        md5.update(string.encode("utf-8"))
        return bin(int(md5.hexdigest()[8:-8],16))[2:].zfill(64) # 转化为64bit 2进制

    # Hash加权、合并、降维
    def simhash(self,packetlist):
        whash = [0] * 64 # 64bit
        # 将求得的64bithash值加权求和
        for hash,(word,weights) in packetlist:
            for i,n in enumerate(hash):
                t = weights if n == '1' else (-weights)
                whash[i] += t
        # 降维
        for i,val in enumerate(whash):
            whash[i] = 1 if val > 0 else 0
        return whash
        
    # Hamming距离
    def hamming(self,org_hash,org_add_hash):
        ans =  0
        for (i,j) in list(zip(org_hash,org_add_hash)):
            ans += i ^ j
        return 1-(ans / len(org_hash))
    
    def check(self):
        self.tf_idf()
        org_hashlist = []
        org_add_hashlist = []
        for word,weight in self.org_tags:
            org_hashlist.append(self.MD5Hash(word))
        for word,weight in self.org_add_tags:
            org_add_hashlist.append(self.MD5Hash(word))
        org_plist = list(zip(org_hashlist,self.org_tags))
        org_add_plist = list(zip(org_add_hashlist,self.org_tags))
        org_hash = self.simhash(org_plist)
        org_add_hash = self.simhash(org_add_plist)
        return self.hamming(org_hash,org_add_hash)


sim = simhash_check(org_file_path,org_add_file_path)
similar = sim.check()
with open(ans_path,"w",encoding = 'utf-8') as f:
    f.write('相似度为'+str(format(similar,'.2f')))
print("Success check")


