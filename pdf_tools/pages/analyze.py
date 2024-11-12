# pdf_tools/pages/analyze.py
import streamlit as st
from ..core.pdf_analyzer import PDFAnalyzer
from ..utils.validators import FileValidator


def show():
    st.header("PDF文件分析")

    # 添加说明
    st.info("分析PDF文件的基本信息和元数据。")

    # 文件上传
    uploaded_file = st.file_uploader(
        "选择PDF文件", type="pdf", help="支持单个PDF文件，大小不超过50MB"
    )

    if uploaded_file:
        if st.button("分析文件", type="primary"):
            with st.spinner("正在分析..."):
                try:
                    if not FileValidator.validate_file(uploaded_file):
                        st.error("文件大小超过限制（50MB）")
                        return

                    # 获取文件信息
                    info = PDFAnalyzer.get_pdf_info(uploaded_file)

                    # 使用卡片布局显示信息
                    col1, col2 = st.columns(2)

                    with col1:
                        st.card(
                            title="基本信息",
                            text=f"""
                            - 文件名：{uploaded_file.name}
                            - 文件大小：{uploaded_file.size/1024/1024:.1f} MB
                            - 页数：{info['页数']}
                            - 页面大小：{info['页面大小']}
                            """,
                        )

                    with col2:
                        st.card(
                            title="文档元数据",
                            text="\n".join(
                                f"- {k}: {v}"
                                for k, v in info["文档信息"].items()
                                if v  # 只显示非空值
                            ),
                        )

                except Exception as e:
                    st.error(f"分析失败：{str(e)}")
