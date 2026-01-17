import streamlit as st
from PIL import Image

# 1. 設定頁面配置 (必須是第一個 st 指令)
st.set_page_config(
    page_title="圖片顯示器",
    layout="wide"  # 使用寬螢幕模式，讓左右分欄更明顯
)

# 2. 標題
st.title("📸 圖片上傳與顯示 App")
st.write("請在左側上傳圖片，圖片將會顯示在 **右方螢幕**。")

# 3. 建立左右兩欄
# col1 是左邊 (用於上傳與設定)
# col2 是右邊 (用於顯示圖片)
col1, col2 = st.columns([1, 1]) 

# --- 左側欄位內容 ---
with col1:
    st.header("1. 上傳區域")
    uploaded_file = st.file_uploader("請選擇一張圖片 (jpg, png, jpeg)", type=["jpg", "png", "jpeg"])
    
    # 可以在左側加一些說明或參數
    st.info("上傳後，圖片會自動顯示在右側 👉")

# --- 右側欄位內容 ---
with col2:
    st.header("2. 顯示區域")
    
    if uploaded_file is not None:
        try:
            # 使用 PIL 開啟圖片
            image = Image.open(uploaded_file)
            
            # 顯示圖片
            # use_container_width=True 會讓圖片自動填滿右側欄位的寬度
            st.image(image, caption='您上傳的圖片', use_container_width=True)
            
            st.success("圖片讀取成功！")
        except Exception as e:
            st.error(f"讀取圖片時發生錯誤: {e}")
    else:
        # 當還沒上傳圖片時顯示的預留位置
        st.markdown(
            """
            <div style="border: 2px dashed grey; padding: 100px; text-align: center; color: grey;">
                圖片將顯示於此
            </div>
            """, 
            unsafe_allow_html=True
        )
