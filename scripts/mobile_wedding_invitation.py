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
            font-family: 'YeojuCeramic';
            src: url('scripts/fonts/YeojuCeramic.woff') format('woff'),
            src: url('scripts/fonts/YeojuCeramic.woff2') format('woff2'),
            src: url('scripts/fonts/YeojuCeramic.ttf') format('truetype');
            src: url('scripts/fonts/YeojuCeramic.otf') format('opentype');
        }

        @font-face {
            font-family: 'PyeongChang-Regular';
            src: url('scripts/fonts/PyeongChang-Regular.ttf') format('truetype'),
            src: url('scripts/fonts/PyeongChang-Regular.woff') format('woff'),
            src: url('scripts/fonts/PyeongChang-Regular.woff2') format('woff2');
        }

        @font-face {
            font-family: 'KimjungchulMyungjo';
            src: url('scripts/fonts/KimjungchulMyungjo-Light.ttf') format('truetype'),
            src: url('scripts/fonts/KimjungchulMyungjo-Light.otf') format('opentype'),
            src: url('scripts/fonts/KimjungchulMyungjo-Light.woff') format('woff'),
            src: url('scripts/fonts/KimjungchulMyungjo-Light.woff2') format('woff2');
        }

        @font-face {
            font-family: 'gamtanroad_tantan';
            src: url('scripts/fonts/gamtanroad_tantan.ttf') format('truetype'),
            src: url('scripts/fonts/gamtanroad_tantan.woff') format('woff'),
            src: url('scripts/fonts/gamtanroad_tantan.woff2') format('woff2'),
            src: url('scripts/fonts/gamtanroad_tantan.otf') format('opentype');
        }

        @font-face {
            font-family: 'museumclassic';
            src: url('scripts/fonts/museumclassic.ttf') format('truetype'),
            src: url('scripts/fonts/museumclassic.woff') format('woff'),
            src: url('scripts/fonts/museumclassic.woff2') format('woff2');
            src: url('scripts/fonts/museumclassic.otf') format('opentype');
        }

        @font-face {
            font-family: 'HakgyoansimBareonbatangB';
            src: url('scripts/fonts/HakgyoansimBareonbatangB.ttf') format('truetype'),
            src: url('scripts/fonts/HakgyoansimBareonbatangB.woff') format('woff'),
            src: url('scripts/fonts/HakgyoansimBareonbatangB.woff2') format('woff2');
        }

        @font-face {
            font-family: 'GwangyangSunshine';
            src: url('scripts/fonts/GwangyangSunshineRegular.ttf') format('truetype'),
            src: url('scripts/fonts/GwangyangSunshineRegular.woff') format('woff'),
            src: url('scripts/fonts/GwangyangSunshineRegular.woff2') format('woff2');
        }

        @font-face {
            font-family: 'romant';
            src: url('scripts/fonts/romant.ttf') format('truetype'),
            src: url('scripts/fonts/romant.woff') format('woff'),
            src: url('scripts/fonts/romant.woff2') format('woff2');
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

        .additional-loading, .greeting {
            font-family: 'YeojuCeramic', sans-serif;
            font-size: 60px;
            text-align: center;
            transform: scale(1);
            opacity: 0;
            transition: opacity 1s ease, transform 1s ease;
        }

        .additional-loading-show {
            opacity: 1;
        }

        .start_content {
            opacity: 0;
            transform: scale(0.5);
            transition: opacity 1s ease;
        }

        .greeting-grow {
            transform: scale(2);
            opacity: 0;
        }

        .greeting-origin {
            transform: scale(0);
            opacity: 0;
        }

        .start_content-show {
            transform: scale(1);
            opacity: 1;
        }

        #loader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }

        loader {
            font-family: 'GwangyangSunshine', sans-serif;
            font-size: 35px;
            color: #999999;
            line-height: 1.0;
            font-weight: bold;
        }

        loader_aux {
            font-family: 'PyeongChang-Regular', sans-serif;
            font-size: 15px;
            color: #777777;
            line-height: 1.6;
            font-weight: 200;
        }

        .hidden {
            opacity: 0;
        }

        .visible {
            opacity: 1;
        }

        main_name {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 33px;
            color: #777777;
            line-height: 1.6;
            font-weight: 900;
        }

        aux_title {
            font-family: 'romant', sans-serif;
            font-size: 40px;
            color: #BBBBBB;
            line-height: 1.0;
            font-style: italic;
            font-weight: 400;
        }

        aux_title_line1 {
            font-family: 'romant', sans-serif;
            margin-left: -20%;
            font-size: 40px;
            color: #BBBBBB;
            line-height: 1.0;
            font-style: italic;
            font-weight: 400;
        }

        aux_title_line2 {
            font-family: 'romant', sans-serif;
            margin-left: 0%;
            font-size: 40px;
            color: #BBBBBB;
            line-height: 1.0;
            font-style: italic;
            font-weight: 400;
        }

        aux_title_line3 {
            font-family: 'romant', sans-serif;
            margin-left: 20%;
            font-size: 40px;
            color: #BBBBBB;
            line-height: 1.0;
            font-style: italic;
            font-weight: 400;
        }

        groom_bride_name {
            font-family: 'PyeongChang-Regular', sans-serif;
            font-size: 26px;
            color: #777777;
            line-height: 1.6;
            font-weight: bold;
        }
        
        parent_name {
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
            max-width: 330px;
            display: inline-block;
            text-align: left;
            margin: 0px;
        }

        .account_container {
            width: 100%;
            max-width: 470px;
            display: inline-block;
            text-align: center;
            margin: 0px;
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
            font-family: 'GwangyangSunshine', sans-serif;
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

        wedding_info {
            font-family: 'YeojuCeramic', sans-serif;
            font-size: 20px;
            color: #999999;
            line-height: 0.5;
            font-weight: 10;
        }

        main_info {
            font-family: 'GwangyangSunshine', sans-serif;
            font-size: 30px;
            color: #999999;
            line-height: 0.5;
            font-weight: 100;
        }
        
        sub_info_thin {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 16px;
            color: #777777;
            line-height: 0.1;
            font-weight: 300;
        }

        sub_info_bold {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 16px;
            color: #777777;
            line-height: 0.1;
            font-weight: 900;
        }

        sub_info_withbg {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 16px;
            color: #777777;
            line-height: 0.1;
            font-weight: 900;
            background-color: #E6E6E6;
            border-radius: 5px;
            padding: 2px;
        }

        .clickcopy {
            align-items: center;
            margin: 10px;
            cursor: pointer;
        }

        .addloadtap {
            display: block;
            margin: 350px;
        }

        .greetingtap {
            display: block;
            margin: 300px;
        }

        .starttap {
            display: block;
            margin: -350px;
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

        .halfbreak {
            display: block;
            margin: 10px;
        }
    </style>
</head>

<body>
    <div id="loader">
        <p>
            <loader>
                페이지 불러오는 중...
            </loader>
            <span class="break"></span>
            <loader_aux>
                사용자 환경에 따라 1~5초 가량 소요됩니다.
            </loader_aux>
        </p>
    </div>

    <div class="additional-loading" id="additional-loading">
        <span class="addloadtap"></span>
        <p>
            <loader>
                페이지 불러오는 중...
            </loader>
            <span class="break"></span>
            <loader_aux>
                사용자 환경에 따라 1~5초 가량 소요됩니다.
            </loader_aux>
        </p>
    </div>

    <div class="greeting" id="greeting">
        <span class="greetingtap"></span>
        결혼합니다.
    </div>

    <span class="starttap"></span>
    <div class="start_content" id="start_content">
        <!-- 상단 배경이 제거된 PNG 이미지 -->
        <img src="https://github.com/user-attachments/assets/3e8425ce-a7bd-4f97-8299-796c7f43bef8" alt="배경 이미지" class="header-img">
        
        <!-- 메인 이미지 -->
        <img src="https://github.com/user-attachments/assets/da473233-f40e-46ab-a716-9bef7223d64a" alt="메인 이미지" class="main-img">
        <!-- 초대 텍스트 부분 -->
        <div class="content">
            <aux_title>BE OUR GUEST</aux_title>
            <span class="break"></span>
            <main_name>천선우  ㆍ  김은혜</main_name>
            <span class="break"></span>
            <div class="details">
                <wedding_info>2026. 11.12 SAT 12:00 PM<br>유성컨벤션웨딩홀 4층 블룸홀</wedding_info>
            </div>
        </div>

        <!-- 인삿말 -->
        <div class="content">
            <aux_title_line1>WE ARE</aux_title_line1>
            <span class="halfbreak"></span>
            <aux_title_line2>GETTING</aux_title_line2>
            <span class="halfbreak"></span>
            <aux_title_line3>MARRIED</aux_title_line3>
            <p>연인으로 시작하여<br>이제는 부부로서<br>함께한 시간보다<br>더 영원한 시간을<br>마주하기로 했습니다.<br>두 사람의 여정이<br>온전한 하나가 되는 날<br>축하와 격려로<br>자리를 빛내주세요</p>
        </div>

        <div class="content">
            <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px;">
            <p>
                <parent_name>천병찬 ㆍ 최동숙의</parent_name> 장남 <groom_bride_name>선우</groom_bride_name>
            </p>
            <p>
                <parent_name>김헌수 ㆍ 원지영의</parent_name> 차녀 <groom_bride_name>은혜</groom_bride_name>
            </p>
            <div class="details">
                <wedding_info>2026. 11.12 SAT 12:00 PM<br>유성컨벤션웨딩홀 4층 블룸홀</wedding_info>
            </div>
        </div>
        
        <!-- 사진첩 -->
        <div class="content">
            <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
            <span class="break"></span>
            <main_info>사진첩</main_info>
            <span class="break"></span>

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
            <span class="break"></span>
            <main_info>오시는 길</main_info>
            <span class="break"></span>
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
            <span class="halftap"></span>
            <main_info>마음 전하실 곳</main_info>

            <span class="break"></span>
            <div class="account_container">
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;신랑</sub_info_thin> <sub_info_bold>천선우</sub_info_bold> 
                </div>
                <div class="clickcopy" onclick="copyText('603-311890-59726')">
                    <sub_info_thin>하나은행</sub_info_thin> <sub_info_bold>603-311890-59726&nbsp;&nbsp;</sub_info_bold>
                    <sub_info_withbg><img src="https://github.com/user-attachments/assets/6b1b77a1-ded1-4b43-af9f-5bcb47ef5d6a" alt="copy1" style="width: 100%; max-width: 18px;"> 복사</sub_info_withbg>
                </div>
            </div>

            <span class="break"></span>
            <div class="account_container">
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;신부</sub_info_thin> <sub_info_bold>김은혜</sub_info_bold> 
                </div>
                <div class="clickcopy" onclick="copyText('719203-83-374781')">
                    <sub_info_thin>국민은행</sub_info_thin> <sub_info_bold>719203-83-374781&nbsp;&nbsp;</sub_info_bold>
                    <sub_info_withbg><img src="https://github.com/user-attachments/assets/6b1b77a1-ded1-4b43-af9f-5bcb47ef5d6a" alt="copy1" style="width: 100%; max-width: 18px;"> 복사</sub_info_withbg>
                </div>
            </div>
        </div>
    </div>
    
    <!-- 함수 구현부 -->
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(function() {
                document.getElementById("loader").classList.add("hidden");
                document.getElementById("additional-loading").style.opacity = 1;
                setTimeout(function() {
                    document.getElementById("additional-loading").style.display = "none";
                    document.getElementById("greeting").style.opacity = 1;

                    setTimeout(function() {
                        document.getElementById("greeting").classList.add("greeting-grow");

                        setTimeout(function() {
                            document.getElementById("greeting").style.opacity = 0;
                            document.getElementById("start_content").classList.add("start_content-show");

                            setTimeout(function() {
                                document.getElementById("greeting").classList.remove("greeting-grow");
                                document.getElementById("greeting").style.transform = "scale(1)";
                            }, 800);
                        }, 100);
                    }, 2500);
                }, 2000);
            }, 1000);
        });
    </script>

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
                threshold: 0.4
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