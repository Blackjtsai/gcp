設置IAM管理員 -- 把權利裝進籠子
=======================

## 知識點

避免使用root根帳號，應該分配適當有權帳號進行工作管理

## 區別用戶

## Root根帳號

+ 控制其他管理帳號時
+ 帳號契約解約時
+ 帳號付款時

## 普通管理員

+ 管理一般用戶 (User , Group , Role)
+ 管理AWS資源(EC2,RDB....)

## 普通成員

+ AWS資源使用

## 實戰演習

### IAM( Identity and Access Management )

+ 簡化用戶登入URL - blackjlearnaws
+ 建立管理員組 - lcadmin-group -> 點 AdminstratorAccess (除了root外的最大權限)
+ 建立普通管理員 - lcadmin (先選 AWS管理控制台訪問 - 編程訪問日後再說)

  + 標籤管理策略 可以分很多組來控制成本

