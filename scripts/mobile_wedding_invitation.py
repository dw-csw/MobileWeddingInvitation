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

        .slider img {
            width: 100%;
            max-width: 600px;
            height: auto;
            display: block;
        }

        .slider img:first-child {
            display: block;
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            margin-top: -22px;
            padding: 16px;
            color: white;
            font-weight: bold;
            font-size: 24px;
            transition: 0.6s ease;
            border-radius: 0 3px 3px 0;
            user-select: none;
        }

        .prev {
            left: 0;
            border-radius: 3px 0 0 3px;
        }

        .next {
            right: 0;
            border-radius: 3px 0 0 3px;
        }

        .thumbnails {
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding: 10px 0;
            scroll-behavior: smooth;
            cursor: grab;
        }

        .thumbnails img {
            width: 100px;
            height: 100px;
            object-fit: cover;
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .thumbnails img:hover {
            transform: scale(1.1);
        }

        .thumbnails:active {
            cursor: grabbing;
        }

        .modal {
            display: none; /* 기본적으로 숨김 */
            position: fixed;
            z-index: 1000; /* 모달을 최상위로 설정 */
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            max-width: 80%;
            max-height: 80%;
            position: relative;
        }

        /* 닫기 버튼 스타일 */
        .close {
            position: absolute;
            top: calc(50% - 400px);
            left: calc(50% + 250px);
            z-index: 1100;
            color: white;
            font-size: 25px;
            font-weight: bold;
            cursor: pointer;
            background-color: rgba(0, 0, 0, 0.5);
            width: 40px;
            height: 40px;
            padding: 1px;
            border-radius: 30%;
        }

        @media (max-width: 460px) {
            .close {
                top: calc(50% - 190px);
                left: calc(50% + 110px);
                z-index: 1100;
                color: white;
                font-size: 20px;
                font-weight: bold;
                cursor: pointer;
                background-color: rgba(0, 0, 0, 0.5);
                width: 30px;
                height: 30px;
                border-radius: 30%;
            }

            .modal-content {
                max-width: 80%;
                max-height: 80%;
                position: relative;
            }
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
                <div class="slider" id="mainSlider">
                    <img src="https://github.com/user-attachments/assets/5c2895f7-d1ea-40ac-a93c-9dfa246e71b7" alt="Image1">
                    <img src="https://github.com/user-attachments/assets/e40df9f7-eb2e-49b5-9c37-ce69428437cf" alt="Image2">
                    <img src="https://github.com/user-attachments/assets/04d59236-fab2-43bc-b0a4-c8d5e7ec5a0e" alt="Image3">
                    <img src="https://github.com/user-attachments/assets/efa7d4ae-102e-4c2a-a68c-337802289b9a" alt="Image4">
                    <img src="https://github.com/user-attachments/assets/a3a54774-4a74-4c6c-9dcb-f0acebfcbadb" alt="Image5">
                    <img src="https://github.com/user-attachments/assets/baad8058-4a90-464a-9f6c-aaa2c40aa7a8" alt="Image6">
                    <img src="https://github.com/user-attachments/assets/5d3b548a-deb9-4c8f-b0ae-4cd826711bef" alt="Image7">
                    <img src="https://github.com/user-attachments/assets/7ae23853-d8dd-4cb7-9d59-313d9a2276ae" alt="Image8">
                </div>
                <a class="prev" onclick="changeSlide(-1)">&#10094;</a>
                <a class="next" onclick="changeSlide(1)">&#10095;</a>
            </div>

            <span class="break"></span>

            <div class="thumbnails" id="thumbnailContainer">
                <img src="https://github.com/user-attachments/assets/5c2895f7-d1ea-40ac-a93c-9dfa246e71b7" alt="Thumbnail1" onclick="showMainImage(this)">
                <img src="https://github.com/user-attachments/assets/e40df9f7-eb2e-49b5-9c37-ce69428437cf" alt="Thumbnail2" onclick="showMainImage(this)">
                <img src="https://github.com/user-attachments/assets/04d59236-fab2-43bc-b0a4-c8d5e7ec5a0e" alt="Thumbnail3" onclick="showMainImage(this)">
                <img src="https://github.com/user-attachments/assets/efa7d4ae-102e-4c2a-a68c-337802289b9a" alt="Thumbnail4" onclick="showMainImage(this)">
                <img src="https://github.com/user-attachments/assets/a3a54774-4a74-4c6c-9dcb-f0acebfcbadb" alt="Thumbnail5" onclick="showMainImage(this)">
                <img src="https://github.com/user-attachments/assets/baad8058-4a90-464a-9f6c-aaa2c40aa7a8" alt="Thumbnail6" onclick="showMainImage(this)">
                <img src="https://github.com/user-attachments/assets/5d3b548a-deb9-4c8f-b0ae-4cd826711bef" alt="Thumbnail7" onclick="showMainImage(this)">
                <img src="https://github.com/user-attachments/assets/7ae23853-d8dd-4cb7-9d59-313d9a2276ae" alt="Thumbnail8" onclick="showMainImage(this)">
            </div>
        </div>

        <div id="imageModal" class="modal">
            <span class="close" onclick="closeModal()">&times;</span>
            <img class="modal-content" id="popupImage" alt="Popup Image">
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
                        }, 1000);
                    }, 2500);
                }, 2000);
            }, 1000);
        });
    </script>

    <!-- FIXME: 1. 241015 좌우버튼으로 메인이미지 바꿀 때 currentSlide = 0일 때 메인 이미지 안바뀜 -->
    <!-- 2. 좌우 버튼으로 메인 이미지 바꾼 후 썸네일을 누르면 메인 이미지가 안바뀜(currentSlide 문제같음) -->
    <!-- "ChatGPT HTML 이미지 슬라이더 코드" 부분 참조 -->

    <script>
        let currentSlide = 0;
        const mainSlider = document.getElementById('mainSlider');
        const mainImage = mainSlider.querySelector('img');
        const slides = document.querySelectorAll('.slider img');

        function changeSlide(direction) {
            slides[currentSlide].style.display = 'none';
            currentSlide = (currentSlide + direction + slides.length) % slides.length;
            
            slides[currentSlide].style.display = 'block';
            mainImage.src = slides[currentSlide].src
            console.log(' >> 1 Current slide index:', currentSlide);
        }

        function showMainImage(thumbnail) {
            // 메인 이미지의 src를 썸네일의 src로 변경
            mainImage.src = thumbnail.src;

            // currentSlide 값을 업데이트하여 좌우 버튼과 동기화
            currentSlide = Array.from(slides).findIndex(slide => slide.src === thumbnail.src);
            console.log(' >> 2 Current slide index:', currentSlide);
        }

        // 메인 이미지 클릭 시 팝업으로 크게 보기
        const mainSliderElement = document.getElementById('mainSlider');
        mainSliderElement.addEventListener('click', function() {
            const modal = document.getElementById('imageModal');
            const popupImage = document.getElementById('popupImage');

            const slides = document.querySelectorAll('.slider img'); // 슬라이더 안의 모든 이미지
            const mainImage = slides[currentSlide]; // 현재 슬라이드 이미지 가져오기

            popupImage.src = mainImage.src;
            modal.style.display = 'flex';
        });

        // 모달 닫기 함수
        function closeModal() {
            const modal = document.getElementById('imageModal');
            modal.style.display = 'none';
        }

        // 썸네일 드래그 스크롤 기능 추가
        const thumbnails = document.getElementById('thumbnailContainer');
        let isDown = false;
        let startX;
        let scrollLeft;

        thumbnails.addEventListener('mousedown', (e) => {
            isDown = true;
            thumbnails.classList.add('active');
            startX = e.pageX - thumbnails.offsetLeft;
            scrollLeft = thumbnails.scrollLeft;
        });

        thumbnails.addEventListener('mouseleave', () => {
            isDown = false;
            thumbnails.classList.remove('active');
        });

        thumbnails.addEventListener('mouseup', () => {
            isDown = false;
            thumbnails.classList.remove('active');
        });

        thumbnails.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - thumbnails.offsetLeft;
            const walk = (x - startX) * 3; // 스크롤 속도 조절
            thumbnails.scrollLeft = scrollLeft - walk;
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