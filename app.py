import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
import base64

st.set_page_config(page_title="YouTube 영상 다운로드", layout="centered")
st.title("🎬 YouTube 영상 다운로드 앱")

# URL 입력받기
url = st.text_input("📎 유튜브 URL을 입력하세요")

if url:
    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        st.subheader("📄 영상 정보")
        st.write("**제목:**", yt.title)
        st.write("**채널명:**", yt.author)
        st.write("**길이:**", f"{yt.length}초")
        st.write("**조회수:**", f"{yt.views:,}회")

        if st.button("📥 고화질 다운로드"):
            with st.spinner("영상 다운로드 중...⏳"):
                ys = yt.streams.get_highest_resolution()
                ys.download(filename="downloaded_video.mp4")

                with open("downloaded_video.mp4", "rb") as f:
                    video_bytes = f.read()

                st.success("✅ 다운로드 완료!")
                st.video(video_bytes)  # 영상 미리보기

                st.download_button(
                    label="📥 영상 저장하기 (MP4)",
                    data=video_bytes,
                    file_name="downloaded_video.mp4",
                    mime="video/mp4"
                )

    except Exception as e:
        st.error(f"❌ 오류 발생: {e}")

