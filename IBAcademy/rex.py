# #!/usr/bin/python
#
# import re
# import sys
# import base64
# import os
#
# filename = "ch30.bin"
#
# # f = os.popen("objdump -d %s -M intel" % filename).readlines()
# f = open('new_data.txt', 'r').readlines()
# start = 0
#
# for line in f:
#
#     if '00401514 <_check>:' in line:
#         start += 1
#         break
#
#     start += 1
#
# ar = list()
#
# f = f[start:]
#
# data = "\n"
#
# for line in f:
#
#     data += line + "\n"
#
#     if 'check' in line:
#         ar.append(data)
#         data = "\n"
#
# cnt = 0
# ans = list()
#
# for data in ar:
#
#     data = data.splitlines()
#     xr = 0
#     mv = 0
#
#     for d in data:
#         if 'mov    DWORD PTR [ebp-0x10]' in d:
#             mv = int(d.split(',')[-1], 0x10)
#         if 'xor' in d:
#             xr = int(d.split(',')[-1], 0x10)
#
#     ans.append(chr(mv ^ xr))
#
# print (''.join(ans))

# print("total_len: ", len(ar))
# print("cnt: ", cnt)

# for miss in missing:
#	print(miss)


x = "Ｃhｏose  a  jοｂ  yоu  lονｅ,  and  you  ｗіｌl  ｎeｖｅｒ  have  tο  ｗｏrk  a  day  in  yοur  lіfｅ"

print(x)