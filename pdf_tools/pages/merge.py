# pdf_tools/pages/merge.py
import streamlit as st
from ..core.pdf_merger import PDFMerger
from ..utils.file_handlers import FileHandler
from ..utils.validators import FileValidator


def show():
    st.header("PDF合并工具")

    # 添加说明
    st.info("上传多个PDF文件，调整顺序后合并为一个文件。")

    # 文件上传区域
    uploaded_files = st.file_uploader(
        "拖放或选择PDF文件",
        type="pdf",
        accept_multiple_files=True,
        help="支持多个PDF文件，单个文件大小不超过50MB",
    )

    if uploaded_files:
        # 显示上传的文件列表
        st.write("### 上传的文件")
        for i, file in enumerate(uploaded_files, 1):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"{i}. {file.name}")
            with col2:
                st.write(f"{file.size/1024/1024:.1f} MB")

        # 合并按钮
        if st.button("合并PDF", type="primary"):
            with st.spinner("正在合并文件..."):
                try:
                    # 验证文件
                    if not all(
                        FileValidator.validate_file(file) for file in uploaded_files
                    ):
                        st.error(f"部分文件超过大小限制（50MB）")
                        return

                    # 执行合并
                    merged_pdf = PDFMerger.merge_pdfs(uploaded_files)

                    # 创建下载链接
                    st.markdown(
                        FileHandler.create_download_link(merged_pdf, "merged.pdf"),
                        unsafe_allow_html=True,
                    )
                    st.success("PDF合并完成！")

                except Exception as e:
                    st.error(f"合并失败：{str(e)}")
