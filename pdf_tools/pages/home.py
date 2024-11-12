# pdf_tools/pages/home.py
import streamlit as st


def show():
    st.title("PDF工具集")

    # 使用基础的列布局替代卡片
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("PDF合并")
        st.markdown(
            """
        - 合并多个PDF文件
        - 支持拖拽排序
        - 支持预览
        """
        )

    with col2:
        st.subheader("文本提取")
        st.markdown(
            """
        - 提取PDF中的文本
        - 支持表格识别
        - 格式化导出
        """
        )

    with col3:
        st.subheader("PDF分析")
        st.markdown(
            """
        - 分析基本信息
        - 查看文件元数据
        - 统计页面信息
        """
        )

    st.markdown("---")

    st.header("使用说明")
    st.markdown(
        """
    1. 从左侧菜单选择所需功能
    2. 上传相关PDF文件
    3. 设置所需参数
    4. 点击处理按钮
    """
    )

    st.header("注意事项")
    st.warning(
        """
    - 单个文件大小限制：50MB
    - 仅支持PDF格式
    - 处理后的文件会自动提供下载链接
    """
    )
