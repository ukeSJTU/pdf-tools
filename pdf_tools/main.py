# pdf_tools/main.py
import streamlit as st
from . import pages


def main():
    st.set_page_config(page_title="PDF工具集", layout="wide")

    # 侧边栏导航
    page = st.sidebar.selectbox("选择功能", ["主页", "PDF合并", "文本提取", "PDF信息"])

    # 显示选定的页面
    if page == "主页":
        pages.home.show()
    elif page == "PDF合并":
        pages.merge.show()
    elif page == "文本提取":
        pages.extract.show()
    elif page == "PDF信息":
        pages.analyze.show()

    # 添加侧边栏说明
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 使用说明")
    st.sidebar.write("1. 从上方选择所需工具")
    st.sidebar.write("2. 上传PDF文件")
    st.sidebar.write("3. 点击相应按钮进行处理")
