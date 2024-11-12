# pdf_tools/pages/extract.py
import streamlit as st
from ..core.pdf_extractor import PDFExtractor
from ..utils.validators import FileValidator


def show():
    st.header("PDF文本提取工具")

    # 添加说明
    st.info("从PDF文件中提取文本内容，支持导出为TXT格式。")

    # 文件上传
    uploaded_file = st.file_uploader(
        "选择PDF文件", type="pdf", help="支持单个PDF文件，大小不超过50MB"
    )

    if uploaded_file:
        # 显示文件信息
        st.write(f"文件名：{uploaded_file.name}")
        st.write(f"文件大小：{uploaded_file.size/1024/1024:.1f} MB")

        # 提取选项
        with st.expander("提取选项"):
            include_page_numbers = st.checkbox("包含页码", value=True)
            remove_empty_lines = st.checkbox("移除空行", value=False)

        # 提取按钮
        if st.button("提取文本", type="primary"):
            with st.spinner("正在提取文本..."):
                try:
                    if not FileValidator.validate_file(uploaded_file):
                        st.error("文件大小超过限制（50MB）")
                        return

                    # 提取文本
                    text = PDFExtractor.extract_text(uploaded_file)

                    # 后处理
                    if remove_empty_lines:
                        text = "\n".join(
                            line for line in text.splitlines() if line.strip()
                        )

                    # 显示提取结果
                    st.text_area("提取的文本", text, height=400)

                    # 下载按钮
                    st.download_button(
                        label="下载文本文件",
                        data=text.encode(),
                        file_name=f"{uploaded_file.name}.txt",
                        mime="text/plain",
                    )

                except Exception as e:
                    st.error(f"提取失败：{str(e)}")
