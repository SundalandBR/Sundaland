
import sys
import simhash

if len(sys.argv) != 4:
    print("未输入完整文件路径")
    sys.exit(1)

if (sys.argv[1].endswith(".txt") and sys.argv[2].endswith(".txt") and sys.argv[3].endswith(".txt")) is not True:  # noqa: E501
    print("输入文件中有非txt文件")
    sys.exit(1)

org_file_path = sys.argv[1]
org_add_file_path = sys.argv[2]
ans_path = sys.argv[3]
sim = simhash.simhash_check(org_file_path,org_add_file_path)
similar = sim.check()
with open(ans_path,"w",encoding = 'utf-8') as f:
    f.write('相似度为：'+str(format(100*similar,'.2f'))+'%')
print(similar)
print("Success check")


