# 切分: 利用快慢指針，fast走兩步slow走一步，當fast走到底，slow的剛好是後半段的head
# 還需要建立一個prev記住前一個slow，用prev.next = None切開兩個list
# 合併: 建立dummy head，連接head和slow兩個list