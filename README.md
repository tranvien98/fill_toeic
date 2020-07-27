# Giới thiệu 
Là một project trong khóa học [DeepLearning cơ bản](https://www.facebook.com/nttuan8.AI4E/?__tn__=kCH-R&eid=ARCVEBbsNJSKTAxpOakWW1pS_pvp3I7Qh0tqGxfWH3iTjL3sZ1Gfh8eO13HhbFIteFh91G_q1braC4_p&hc_ref=ARSQJWMW3NUGV1PZwAseB03md_x7pzQBBoJRfK0aLRLIIqersXHPfM5si8nt1YUsYsk&fref=nf&__xts__[0]=68.ARA8YwP3b0DPAD3veQ4g2Gr43ZWreKWQyovUbdLdZdinPji0fllUFJpX3HuNC0AQ3K4NhlOOOIRHlBC5GH5mwwxeYe9-J54Or0a5ctB5oOEIKl-vPsI8rIOQML-7_xKQu_kouGI9gRzfnSM-XmTUt6oxTDdv2deuPjNyZg-xiW_Ssv9vAMkLsqg4kZsAZcEXR4EWuC3XP4jbU2qwyJXixcTi3iWr-kiWH0eD1FeKOwxm3DnSemylrRsGcPYnTV1-mKmF-G7j6_HAD1i0YbT73cOKGXCorDe8yFw98PH8BX_SWndzP254grBfgShon9v33gKRnMT5I5uDtMsw5R7ghwU)
bao gồm 3 thành viên.

Trần Văn Viên

Nguyễn Quốc Trọng

Vương Đình Công

Độ chính xác 90% trong việc dự đoán từ cần điền vào chỗ trống sử dụng pretrain bert.

```
Mr. Hardin --- additional images of the office building he is interested in leasing. 
(A) informed
(B) asked
(C) advised
(D) requested (answer)
```
Dữ liệu sưu tầm được để trong file `data.json` gồm 3625 câu 

```
    "3625": {
        "1": "across",
        "2": "into",
        "3": "between",
        "4": "despite",
        "anwser": "across",
        "question": "Employees ___ several departments have been encouraged to minimize costs."
    }
```
## Cài đặt 

1. Cài đăt thư viện 

```
pip install -r requirements.txt
```

2. Chạy chương trình 

```
python main.py
```

Quá trình chạy có thể mất nhiều thời gian. 


Giao diện của chương trình hiển thị localhost:4040
![Giao diện chương trình](https://i.imgur.com/uhXJQZC.png)

Câu hỏi phải nhập đúng định dạng như trong tab example thì mới có thể dự đoán được kết quả. Phần cần điền để 3 dấu _ . Các lựa chọn được phải bắt đầu bằng (A|B|C|D)

Để biết chi tiết hơn tham khảo trên blog [Deeplearning cơ bản](https://nttuan8.com/bert-for-toeic/?fbclid=IwAR2Bc91wEDp2F4ROQSHMVrEtna9OJu3ChbKt1kwKioauzAlFLed931ELZWI)
