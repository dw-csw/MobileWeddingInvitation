import os

home_path = os.path.expanduser("~")
path = os.path.join(home_path, "git/MobileWeddingInvitation")
fonts = os.path.join(path, "scripts/fonts")
print(fonts)
target_file = os.path.join(path, "index.html")

# Python 코드로 HTML 파일 생성
html_content = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>모바일 청첩장</title>
    <style>
        @font-face {
            font-family: 'GhanaChocolate';
            src: url('scripts/fonts/Ghanachocolate.woff') format('woff'),
            src: url('scripts/fonts/Ghanachocolate.woff2') format('woff2'),
            src: url('scripts/fonts/Ghanachocolate.ttf') format('truetype');
        }

        @font-face {
            font-family: 'KimjungchulMyungjo';
            src: url('scripts/fonts/KimjungchulMyungjo-Light.ttf') format('truetype'),
            src: url('scripts/fonts/KimjungchulMyungjo-Light.otf') format('opentype'),
            src: url('scripts/fonts/KimjungchulMyungjo-Light.woff') format('woff'),
            src: url('scripts/fonts/KimjungchulMyungjo-Light.woff2') format('woff2');
        }

        @font-face {
            font-family: 'GwangyangSunshine';
            src: url('scripts/fonts/Gwangyang Sunshine Regular.woff') format('woff'),
            src: url('scripts/fonts/Gwangyang Sunshine Regular.woff2') format('woff2'),
            src: url('scripts/fonts/Gwangyang Sunshine Regular.ttf') format('truetype');
        }
    
    
        body {
            margin: 0;
            padding: 0;
            background-color: #E7E2D5;
            text-align: center;
        }
        
        .header-img {
            width: 100%;
            max-width: 1200px;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        
        .main-img {
            width: 90%;
            max-width: 600px;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        
        .separate-img {
            width: 100%;
            max-width: 500px;
            height: auto;
            display: block;
            margin: 30px auto 0 auto;
        }
        
        h1 {
            font-size: 28px;
            font-weight: 100;
            color: #999999;
        }
        
        name {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 26px;
            color: #777777;
            line-height: 1.6;
            font-weight: bold;
        }

        p {
            font-family: 'GwangyangSunshine', sans-serif;
            font-size: 20px;
            color: #777777;
            line-height: 2;
            font-weight: 300;
        }
        
        pos {
            font-size: 20px;
            color: #777777;
            line-height: 3;
            font-weight: 300;
        }
        
        sub {
            font-size: 20px;
            color: #999999;
            line-height: 0.8;
        }
        
         .slider-container {
            position: relative;
            width: 80%;
            max-width: 800px;
            margin: 0 auto;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .slider {
            display: flex;
            transition: transform 0.5s ease-in-out;
            width: 100%;
        }

        .slide {
            min-width: 100%;
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .slide img {
            width: 100%;
            max-width: 600px;
            height: auto;
            display: block;
        }

        button {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            font-size: 24px;
        }

        .prev {
            left: 10px;
        }

        .next {
            right: 10px;
        }
        
        .separator {
            border-top: 2px dashed #333;
            margin: 20px 0;
        }

        .content {
            padding: 20px;
            background-color: #DBD7CA;
            border-radius: 10px;
            margin: 5px auto;
            max-width: 600px;
            opacity: 0;
            transition: opacity 0.5s ease;
        }

        .content.visible {
            opacity: 1;
        }
        
        .container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            width: 100%;
        }

        .account_name_container {
            width: 100%;
            max-width: 325px;
            display: inline-block;
            text-align: left;
            margin: 10px;
        }

        .account_container {
            width: 100%;
            max-width: 450px;
            display: inline-block;
            text-align: center;
            margin: 10px;
        }

        .copy_container {
            width: 100%;
            background-color: #FFFFFF;
            display: inline-block;
            text-align: center;
        }

        .item {
            display: inline-block;
            text-align: center;
            margin: 10px;
        }

        .map-link {
            margin-top: 8px;
        }

        .map-link a {
            display: inline-block;
            padding: 5px 2px;
            color: black;
            background-color: #D6D2C6;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            font-family: 'Ghanachocolate';
        }

        .map-link a:hover {
            background-color: #FFF9EB;
        }

        .details {
            font-weight: bold;
            font-size: 30px;
            color: #333333;
            margin: 5px;
            line-height: 1.0;
        }

        main_info {
            font-size: 30px;
            color: #999999;
            line-height: 0.5;
            font-weight: 600;
        }
        
        sub_info_thin {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 18px;
            color: #777777;
            line-height: 0.1;
            font-weight: 300;
        }

        sub_info_bold {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 18px;
            color: #777777;
            line-height: 0.1;
            font-weight: 900;
        }

        sub_info_withbg {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 18px;
            color: #777777;
            line-height: 0.1;
            font-weight: 900;
            background-color: #E9E9E9;
            border-radius: 5px;
            padding: 2px;
        }

        .clickcopy {
            align-items: center;
            margin: 10px;
            cursor: pointer;
        }

        .tap {
            display: block;
            margin: 60px;
        }

        .halftap {
            display: block;
            margin: 30px;
        }
        
        .break {
            display: block;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- 상단 배경이 제거된 PNG 이미지 -->
    <img src="https://github.com/user-attachments/assets/3e8425ce-a7bd-4f97-8299-796c7f43bef8" alt="배경 이미지" class="header-img">
    
    <!-- 메인 이미지 -->
    <img src="https://github.com/user-attachments/assets/da473233-f40e-46ab-a716-9bef7223d64a" alt="메인 이미지" class="main-img">

    <!-- 초대 텍스트 부분 -->
    <div class="content">
        <img src="https://github.com/user-attachments/assets/3955cd6a-fce7-49a6-8e39-18383d1bb4af" alt="구분 기호" style="width: 100%; max-width: 300px;">
        <span class="break"></span>
        <p>
            <name>천선우  ㆍ  김은혜</name>
        </p>
        <span class="break"></span>
        <div class="details">
            <sub>2026. 11.12 SAT 12:00 PM<br>유성컨벤션웨딩홀 4층 블룸홀</sub>
        </div>
    </div>
    
    <!-- 인삿말 -->
    <div class="content">
        <img src="https://github.com/user-attachments/assets/f01eb8ea-0471-4254-a589-f1ebdafe9a98" alt="구분 기호" style="width: 100%; max-width: 400px;">
        <p>연인으로 시작하여<br>이제는 부부로서<br>함께한 시간보다<br>더 영원한 시간을<br>마주하기로 했습니다.<br>두 사람의 여정이<br>온전한 하나가 되는 날<br>축하와 격려로<br>자리를 빛내주세요</p>
    </div>

    <div class="content">
        <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px;">
        <p>
            <name>천병찬 ㆍ 최동숙의</name> 장남 <name>선우</name>
        </p>
        <p>
            <name>김헌수 ㆍ 원지영의</name> 차녀 <name>은혜</name>
        </p>
        <div class="details">
            <sub>2026. 11.12 SAT 12:00 PM<br>유성컨벤션웨딩홀 4층 블룸홀</sub>
        </div>
    </div>
    
    <!-- 사진첩 -->
    <div class="content">
        <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
        <h1>사진첩</h1>
        <div class="slider-container">
            <div class="slider">
                <div class="slide"><img src="https://github.com/user-attachments/assets/4f6bd269-c5cd-4b7d-9340-c2709bf66682" alt="Image1"></div>
                <div class="slide"><img src="https://github.com/user-attachments/assets/e0d2b383-0898-412a-b7f1-2a48e02e7702" alt="Image2"></div>
                <div class="slide"><img src="https://github.com/user-attachments/assets/628dddb3-0878-460d-a984-d94484844314" alt="Image3"></div>
                <div class="slide"><img src="https://github.com/user-attachments/assets/95ceb200-526d-4957-919b-e665087a5af7" alt="Image4"></div>
                <div class="slide"><img src="https://github.com/user-attachments/assets/e658e12d-3f6b-49ad-88a4-4922f324662c" alt="Image4"></div>
            </div>
        </div>
    </div>
    
    <!-- 길안내 -->
    <div class="content">
        <p></p>
        <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
        <h1>오시는 길</h1>
        <img src="https://github.com/user-attachments/assets/6f216bef-dd02-4bda-a53b-96835d9a34b3" alt="구분 기호" style="width: 100%; max-width: 600px;">

        <div class="container">
                <div class="item">
                    <img src="https://github.com/user-attachments/assets/bc620826-6e4c-4ea0-89c4-76342b364349" alt="Image 1" style="width: 100%; max-width: 30px;">
                    <div class="map-link">
                        <a href="https://map.naver.com/p/entry/place/19882195?c=15.00,0,0,0,dh" target="_blank">네이버 지도</a>
                    </div>
                </div>
                <div class="item">
                    <img src="https://github.com/user-attachments/assets/58845f64-fcf6-4a3d-a73d-a4541847eedc" alt="Image 2" style="width: 100%; max-width: 20px;">
                    <div class="map-link">
                        <a href="https://maps.app.goo.gl/syAk93zQ2d74QdMH7" target="_blank">구글 지도</a>
                    </div>
                </div>
                <div class="item">
                    <img src="https://github.com/user-attachments/assets/92fb32b2-e882-4158-9abb-f4497e75f489" alt="Image 3" style="width: 100%; max-width: 30px;">
                    <div class="map-link">
                        <a href="https://kko.to/jUMa0NPXOy" target="_blank">카카오 지도</a>
                    </div>
                </div>
            </div>
    </div>
    
    <!-- 마음 전하는 곳 -->
    <div class="content">
        <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
        <div class="details">
            <span class="halftap"></span>
            <main_info>주소</main_info>
            <span class="break"></span>
            <sub_info_thin>대전광역시 유성구 온천북로 77<br>(봉명동 692-4)<br>T. 042-825-7070</sub_info_thin>
            <span class="break"></span>

            <span class="tap"></span>
            <main_info>지하철</main_info>
            <span class="break"></span>
            <sub_info_thin>유성온천역 7번 출구에서 도보 17분</sub_info_thin>
            <span class="break"></span>

            <span class="tap"></span>
            <main_info>버스</main_info>
            <span class="break"></span>
            <sub_info_thin>홈플러스유성점 정류장 도보 8분<br>102, 106, 706,113</sub_info_thin>
            <span class="break"></span>
        </div>
    </div>
    
    <div class="content">
        <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
        <span class="tap"></span>
        <main_info>마음 전하실 곳</main_info>

        <span class="break"></span>
        <div class="account_container">
            <div class="account_name_container">
                <sub_info_thin>&nbsp;&nbsp;신랑</sub_info_thin> <sub_info_bold>천선우</sub_info_bold> 
            </div>
            <div class="clickcopy" onclick="copyText('603-311890-59726')">
                <sub_info_thin>하나은행</sub_info_thin> <sub_info_bold>603-311890-59726&nbsp;&nbsp;</sub_info_bold>
                <sub_info_withbg><img src="https://github.com/user-attachments/assets/6b1b77a1-ded1-4b43-af9f-5bcb47ef5d6a" alt="Image 4" style="width: 100%; max-width: 20px;"> 복사</sub_info_withbg>
            </div>
        </div>

        <span class="break"></span>
        <div class="account_container">
            <div class="account_name_container">
                <sub_info_thin>&nbsp;&nbsp;신부</sub_info_thin> <sub_info_bold>김은혜</sub_info_bold> 
            </div>
            <div class="clickcopy" onclick="copyText('719203-83-374781')">
                <sub_info_thin>국민은행</sub_info_thin> <sub_info_bold>719203-83-374781&nbsp;&nbsp;</sub_info_bold>
                <sub_info_withbg><img src="https://github.com/user-attachments/assets/6b1b77a1-ded1-4b43-af9f-5bcb47ef5d6a" alt="Image 4" style="width: 100%; max-width: 20px;"> 복사</sub_info_withbg>
            </div>
        </div>
    </div>
    

    <!-- 함수 구현부 -->
    <script>
        let currentIndex = 0;

        function moveSlide(step) {
            const slides = document.querySelectorAll('.slide');
            const totalSlides = slides.length;
            currentIndex = (currentIndex + step + totalSlides) % totalSlides;
            const slider = document.querySelector('.slider');
            slider.style.transform = `translateX(-${currentIndex * 100}%)`;
        }

        // Initialize the slider
        document.addEventListener('DOMContentLoaded', () => {
            const slides = document.querySelectorAll('.slide');
            if (slides.length > 0) {
                setInterval(() => moveSlide(1), 3000);
            }
        });
    </script>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const contents = document.querySelectorAll('.content');

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    } 
                    else if (entry.boundingClientRect.top < 0) {
                        entry.target.classList.add('visible');
                    }
                    else {
                        entry.target.classList.remove('visible');
                    }
                });
            }, {
                threshold: 0.3
            });

            contents.forEach(content => {
                observer.observe(content);
            });
        });
    </script>

    <script>
        function copyText(text) {
            const textarea = document.createElement('textarea');
            textarea.value = text;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            alert('클립보드에 복사되었습니다 : ' + text);
        }
    </script>
</body>
</html>
'''
home_path = os.path.expanduser("~")
path = os.path.join(home_path, "git/MobileWeddingInvitation")
target_file = os.path.join(path, "index.html")
# 파일 저장
with open(target_file, "w", encoding="utf-8") as file:
    file.write(html_content)

print("모바일 청첩장이 생성되었습니다: index.html")