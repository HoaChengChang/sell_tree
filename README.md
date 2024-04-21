個人於本專案是運用Django、Bootstrap製作，管理者可以運用後台上傳最新照片及修改照片說明、最新消息及介紹字體，可大大減少工程師修改專案的次數，而後端是運用MySQL 做為存放訂購人資訊的資料庫，並嵌入訂購人於訂購時會自動傳送mail通知完成訂購及自動通知賣家訂購消息功能。服務架設是租借GCP虛擬機，並運用Docker、Docker-compose將Django、Redis、MySQL 、Nginx、uwsgi等服務建立。

<img width="720" alt="截圖 2024-03-03 下午1 32 26" src="https://github.com/HoaChengChang/sell_tree/assets/93926929/f43c6722-5041-4f8a-8ba7-f96e0ab26817">

後端設計，分為最新消息、段落、產品、訂購資訊及訪問人數等五部分：
<img width="˙720" alt="截圖 2024-04-21 下午1 33 23" src="https://github.com/HoaChengChang/sell_tree/assets/93926929/97f0c942-eab6-4e51-a433-4c2dad3fb2b0">

最新消息
<img width="720" alt="截圖 2024-04-21 下午1 33 38" src="https://github.com/HoaChengChang/sell_tree/assets/93926929/707d078c-635e-4dc6-9870-b839ea1363f6">

段落
<img width="720" alt="截圖 2024-04-21 下午1 34 07" src="https://github.com/HoaChengChang/sell_tree/assets/93926929/2263f007-f47a-461a-a763-6326d266257c">

產品
<img width="720" alt="截圖 2024-04-21 下午1 34 16" src="https://github.com/HoaChengChang/sell_tree/assets/93926929/6a972983-c625-46dc-954f-e4f611ac543c">

訂購資訊
<img width="720" alt="截圖 2024-04-21 下午1 35 09" src="https://github.com/HoaChengChang/sell_tree/assets/93926929/e2f064dd-fb05-4504-b51c-5e3f46ae98ed">

訪問人數
<img width="720" alt="截圖 2024-04-21 下午1 35 21" src="https://github.com/HoaChengChang/sell_tree/assets/93926929/a1e5c824-ed4b-4cea-9c6d-c0448f712c4d">
