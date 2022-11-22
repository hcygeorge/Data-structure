# 雙指針

## 說明
用兩個指針遍歷資料，按照指針移動的方向可分為對撞指針和快慢指針。

### 對撞指針(反方向)
left, right兩個指針分別從資料兩端往中間移動，常用於在sorted array下**需要比大小**題型

相關題型
- squares of a sorted array
- remove element

### 快慢指針(同方向)
兩個指針都從同方向開始移動，但慢指針只有在滿足條件下移動，常用於**要求inplace操作**array的問題

相關題型
- sub sequence
- remove duplicates from sorted array
- remove element

## 筆記
對撞指針看起來適合處理有排序的array或linked list\
快慢指針適合需要in-place修改已經遍歷過的元素問題

## 參考資料
https://ithelp.ithome.com.tw/articles/10263103

