"""Streamlit download page for HIPPIE Linux and Windows builds."""

from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="Download HIPPIE", page_icon="🧠")
st.title("Download HIPPIE")
st.write("Choose the version for your operating system.")

linux_file = next(
    (path for name in ("HIPPIE", "HIPPIE(2)")
     if (path := BASE_DIR / name).is_file()),
    None,
)
windows_file = BASE_DIR / "HIPPIE.exe"

linux_col, windows_col = st.columns(2)

with linux_col:
    st.subheader("🐧 Linux")
    if linux_file is not None:
        with linux_file.open("rb") as f:
            st.download_button(
                label="Download HIPPIE for Linux",
                data=f,
                file_name="HIPPIE",
                mime="application/octet-stream",
                icon=":material/download:",
                type="primary",
                use_container_width=True,
            )
        st.caption("After downloading: `chmod +x HIPPIE && ./HIPPIE`")
    else:
        st.warning("Linux executable not found. Put HIPPIE or HIPPIE(2) next to this script.")

with windows_col:
    st.subheader("🪟 Windows")
    if windows_file.is_file():
        with windows_file.open("rb") as f:
            st.download_button(
                label="Download HIPPIE for Windows",
                data=f,
                file_name="HIPPIE.exe",
                mime="application/octet-stream",
                icon=":material/download:",
                type="primary",
                use_container_width=True,
            )
    else:
        st.info("Windows version not available yet (HIPPIE.exe not found).")
