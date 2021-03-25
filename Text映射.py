import os
path=os.getcwd()
path2=path+"/Text/out_t"
ch=open("char映射.txt",'r')
char=ch.readlines()
outpath=os.getcwd()+"/Text/out_t_映射"
for file in os.listdir(path2):
    if file.split(".")[-1]=="txt":
#        print(file)
        f=open(path2+"/"+file,'r')
        o=open(outpath+"/"+file,'w+')
        line = f.readline()
        while line:
            data=""
            line=line.replace('姉','姐').replace('嶺','岭').replace("▲彼女＊＊＊▲","▲彼女＊＊▲").replace("▲彼＊＊＊＊▲","▲彼女＊＊▲")
            for num in range(len(line)):
                for c in char:
                    if c[1]==line[num]:
                        data=data+c[0]
                        break
                    elif c[0]=='e':
                        data=data+line[num]
#                print(c[1],c[0])
            line=data
            line=line.replace("▲姫ヶ屋＊▲","▲姉ヶ崎＊▲").replace("▲衰誹＊＊▲","▲高嶺＊＊▲").replace("▲寧散屓＊▲","▲小早川＊▲")
            line=line.replace("▲妃奔＊＊▲","▲彼女＊＊▲").replace("▲移子▲","▲苗字▲").replace("▲呗利▲","▲名前▲")
            line=line.replace("▲乏令允＊▲","▲主人公＊▲").replace("▲時初▲","▲時刻▲").replace("▲デート場場▲","▲デート場所▲")
#            line=line.replace("▲八澱コンテスト件旺・力蕉俵＊▲","▲写真コンテスト今月・募集中＊▲")
#            line=line.replace("▲八澱コンテスト僮旺＊＊＊＊＊▲","▲写真コンテスト先月＊＊＊＊＊▲")
            line=line.replace("選調談","選択肢").replace("淹悉選調談","生成選択肢")
            line=line.replace("▲紹任南達受▲","▲紹介友達名▲").replace("▲旺▲","▲月▲").replace("▲敗▲","▲日▲")
                
            o.write(line)
            line=f.readline()
        f.close()
        o.close()
print("完成")
