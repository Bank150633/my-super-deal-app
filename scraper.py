import json

# ตรงนี้คือส่วนที่บอทจะทำงาน (อนาคตใส่ API Shopee ตรงนี้)
def get_real_deals():
    return [
        {
            "name": "คีย์บอร์ดไร้สาย ราคาพิเศษ",
            "price": "590",
            "oldPrice": "1,200",
            "img": "https://images.unsplash.com/photo-1587829741301-dc798b83aca2?w=400"
        },
        {
            "name": "พัดลมพกพา ลด 50%",
            "price": "150",
            "oldPrice": "300",
            "img": "https://images.unsplash.com/photo-1535572290543-960a8046f5af?w=400"
        }
    ]

if __name__ == "__main__":
    deals = get_real_deals()
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(deals, f, ensure_ascii=False)
