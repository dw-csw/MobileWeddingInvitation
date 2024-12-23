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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <title>천선우 ♥ 김은혜 결혼합니다</title>
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
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .slider {
            display: flex;
            overflow: hidden;
            transition: transform 0.5s ease-in-out;
            width: 100%;
        }

        .slider img {
            width: 100%;
            max-width: 600px;
            height: auto;
            display: none;
        }

        .slider img.active {
            display: block;
        }

        .prev, .next {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: rgba(0, 0, 0, 0.2); /* 반투명한 검정 배경 */
            color: white;
            border: none;
            padding: 12px;
            font-size: 18px;
            cursor: pointer;
            border-radius: 50%; /* 둥근 모양 */
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5); /* 그림자 */
            transition: transform 0.2s ease, background-color 0.2s ease;
        }

        .prev {
            left: -30px;
            border-radius: 3px 0 0 3px;
        }

        .next {
            right: -30px;
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
            transition: opacity 0.5s ease-in-out;
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
            top: -4%;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            justify-content: center;
            align-items: center;
        }

        @media (max-width: 460px) {
            .modal {
                display: none; /* 기본적으로 숨김 */
                position: fixed;
                z-index: 1000; /* 모달을 최상위로 설정 */
                left: 0;
                top: -6%;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.8);
                justify-content: center;
                align-items: center;
            }
        }
        
        .modal-content {
            max-width: 100%;
            max-height: 80%;
            position: relative;
        }

        /* 닫기 버튼 스타일 */
        .close {
            position: absolute;
            top: calc(50% - 250px);
            left: calc(50% + 150px);
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
                top: calc(50% - 240px);
                left: calc(50% + 150px);
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
            overflow: hidden;
            width: 100%;
            max-width: 470px;
            max-height: 0;
            display: inline-block;
            text-align: center;
            transition: opacity 0.5s ease, visibility 0.3s ease, max-height 0.5s ease, padding 0.5s ease;
            margin: 0px;
            opacity: 0;
            visibility: visible;
            padding: -10px;
        }

        .account_container.expanded {
            max-height: 300px;
            opacity: 1;
            padding: 0px;
        }

        .copy_container {
            width: 100%;
            background-color: #FFFFFF;
            display: inline-block;
            text-align: center;
        }

        #GROOM_toggleButton {
            background-color: #E7E2D5;
            color: #777777;
            padding: 10px 10px;
            font-size: 16px;
            font-weight: bold;
            border: 5px;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease, transform 0.2s ease;
            font-family: 'KimjungchulMyungjo', sans-serif;
        }

        #GROOM_toggleButton::after {
            content: " ▼"; /* 기본 아이콘 */
            font-size: 14px;
            transition: transform 0.3s ease;
        }

        #GROOM_toggleButton.expanded::after {
            content: " ▲"; /* 펼쳤을 때 아이콘 변경 */
        }

        #BRIDE_toggleButton {
            background-color: #E7E2D5;
            color: #777777;
            padding: 10px 10px;
            font-size: 16px;
            font-weight: bold;
            border: 5px;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease, transform 0.2s ease;
            font-family: 'KimjungchulMyungjo', sans-serif;
        }

        #BRIDE_toggleButton::after {
            content: " ▼"; /* 기본 아이콘 */
            font-size: 14px;
            transition: transform 0.3s ease;
        }

        #BRIDE_toggleButton.expanded::after {
            content: " ▲"; /* 펼쳤을 때 아이콘 변경 */
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
            font-weight: bold;
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

        copy_right_thin {
            font-family: 'KimjungchulMyungjo', sans-serif;
            font-size: 13px;
            color: #777777;
            line-height: 0.1;
            font-weight: 200;
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

        .last-image-container {
            position: relative;
        }

        .overlay-text {
        font-family: 'KimjungchulMyungjo', sans-serif;
            position: absolute;
            top: 22%;
            left: 40%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 20px;
            font-weight: 590;
            line-height: 1.5;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); /* 텍스트 그림자 추가 */
        }

        @media (max-width: 430px) {
            .overlay-text {
            font-family: 'KimjungchulMyungjo', sans-serif;
                position: absolute;
                top: 21%;
                left: 41%;
                transform: translate(-50%, -50%);
                color: white;
                font-size: 11px;
                font-weight: 300;
                line-height: 1.5;
                text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); /* 텍스트 그림자 추가 */
            }
        }

        .link-copy-button {
            display: inline-flex;
            background-color: #E7E2D5;
            color: #777777;
            padding: 10px 10px;
            font-size: 16px;
            font-weight: bold;
            border: 5px;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            font-family: 'KimjungchulMyungjo', sans-serif;
        }

        .link-copy-button i {
            margin-right: 8px; /* 아이콘과 텍스트 사이 간격 */
            font-size: 18px; /* 아이콘 크기 */
        }
        
        .info-copy-button {
            display: inline-flex;
            background-color: #E7E2D5;
            color: #777777;
            align-items: center;
            padding: 7px 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            font-family: 'KimjungchulMyungjo', sans-serif;
        }
        
        .fas.fa-copy {
            font-size: 16px;
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
            <span class="break"></span>
            <img src="https://github.com/user-attachments/assets/f4cfbb6c-3792-4b1a-bd04-9de8bf7ab237" alt="메인 이미지" class="main-img">
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
                    <img src="https://github.com/user-attachments/assets/fe8e9f11-58b2-4c61-ac2f-e01de76ab039" alt="Image0">
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

        <!-- 지도 연결 -->
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
        
        <!-- 길 안내 -->
        <div class="content">
            <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
            <div class="details">
                <span class="halftap"></span>
                <main_info>자가용</main_info>
                <span class="break"></span>
                <sub_info_thin>대전광역시 유성구 온천북로 77<br>(봉명동 692-4)<br>T. 042-825-7070</sub_info_thin>
                <span class="halfbreak"></span>
                <sub_info_thin>400여대 수용 가능한 주차타워가 마련되어 있습니다.</sub_info_thin>
                <span class="halfbreak"></span>
                <sub_info_thin>(1층에서 주차정산 하셔야 2시간30분 무료주차 가능합니다.)</sub_info_thin>
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

        <!-- 화환 거절 -->
        <div class="content">
            <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
            <div class="details">
                <span class="halftap"></span>
                <main_info>화환 거절</main_info>
                <span class="break"></span>
                <sub_info_thin>축하하는 마음으로 보내주시는</sub_info_thin>
                <span class="halfbreak"></span>
                <sub_info_thin>화환은 환경보호를 위해</sub_info_thin>
                <span class="halfbreak"></span>
                <sub_info_thin>정중히 사양하고자 합니다.</sub_info_thin>
                <span class="halfbreak"></span>
                <sub_info_thin>마음으로만 감사히 받겠습니다.</sub_info_thin>
                <span class="break"></span>
            </div>
        </div>

        <!-- 식사 안내 -->
        <div class="content">
            <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
            <div class="details">
                <span class="halftap"></span>
                <main_info>식사 안내</main_info>
                <span class="break"></span>
                <sub_info_thin>식사는 웨딩홀 2층에서 뷔페식으로 진행됩니다.</sub_info_thin>
                <span class="halfbreak"></span>
                <sub_info_thin>식권을 꼭 지참하셔서 맛있게 식사하시기 바랍니다.</sub_info_thin>
                <span class="halfbreak"></span>
                <sub_info_thin>식사시간은 예식 30분 전부터 총 2시간입니다.</sub_info_thin>
                <span class="break"></span>
            </div>
        </div>

        <!-- 마음 전하는 곳 -->
        <div class="content">
            <img src="https://github.com/user-attachments/assets/cf80fb23-0b6d-4f01-9cff-077d2703fd44" alt="구분 기호" style="width: 100%; max-width: 500px; class="separate-img"">
            <span class="halftap"></span>
            <main_info>마음 전하실 곳</main_info>
            <span class="break"></span>
            <sub_info_thin>참석이 어려우신 분들을 위해</sub_info_thin>
            <span class="halfbreak"></span>
            <sub_info_thin>계좌번호를 기재하였습니다.</sub_info_thin>
            <span class="halfbreak"></span>
            <sub_info_thin>너그러운 마음으로 양해 부탁드립니다.</sub_info_thin>
            <span class="halftap"></span>

            <span class="break"></span>
            <button id="GROOM_toggleButton" onclick="GROOM_toggleAccountInfo()">신랑측 마음 전하실 곳</button>
            <span class="break"></span>
            <div class="account_container" id="GROOM_accountContainer">
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;신랑</sub_info_thin> <sub_info_bold>천선우</sub_info_bold> 
                </div>
                <div class="clickcopy">
                    <sub_info_thin>하나은행</sub_info_thin> <sub_info_bold>603-311890-59726&nbsp;&nbsp;</sub_info_bold>
                    <button class="info-copy-button" onclick="copyText('603-311890-59726')">
                        <i class="fas fa-copy"></i> 복사
                    </button>
                </div>
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;아버지</sub_info_thin> <sub_info_bold>천병찬</sub_info_bold> 
                </div>
                <div class="clickcopy">
                    <sub_info_thin>하나은행</sub_info_thin> <sub_info_bold>604-317288-37098&nbsp;&nbsp;</sub_info_bold>
                    <button class="info-copy-button" onclick="copyText('604-317288-37098')">
                        <i class="fas fa-copy"></i> 복사
                    </button>
                </div>
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;어머니</sub_info_thin> <sub_info_bold>최동숙</sub_info_bold> 
                </div>
                <div class="clickcopy">
                    <sub_info_thin>하나은행</sub_info_thin> <sub_info_bold>601-910789-24196&nbsp;&nbsp;</sub_info_bold>
                    <button class="info-copy-button" onclick="copyText('601-910789-24196')">
                        <i class="fas fa-copy"></i> 복사
                    </button>
                </div>
            </div>

            <span class="halfbreak"></span>
            <button id="BRIDE_toggleButton" onclick="BRIDE_toggleAccountInfo()">신부측 마음 전하실 곳</button>
            <span class="break"></span>
            <div class="account_container" id="BRIDE_accountContainer">
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;신부</sub_info_thin> <sub_info_bold>김은혜</sub_info_bold> 
                </div>
                <div class="clickcopy">
                    <sub_info_thin>국민은행</sub_info_thin> <sub_info_bold>719203-83-374781&nbsp;&nbsp;</sub_info_bold>
                    <button class="info-copy-button" onclick="copyText('719203-83-374781')">
                        <i class="fas fa-copy"></i> 복사
                    </button>
                </div>
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;아버지</sub_info_thin> <sub_info_bold>김헌수</sub_info_bold> 
                </div>
                <div class="clickcopy">
                    <sub_info_thin>국민은행</sub_info_thin> <sub_info_bold>76781-87-549768&nbsp;&nbsp;</sub_info_bold>
                    <button class="info-copy-button" onclick="copyText('76781-87-549768')">
                        <i class="fas fa-copy"></i> 복사
                    </button>
                </div>
                <div class="account_name_container">
                    <sub_info_thin>&nbsp;&nbsp;어머니</sub_info_thin> <sub_info_bold>원지영</sub_info_bold> 
                </div>
                <div class="clickcopy">
                    <sub_info_thin>국민은행</sub_info_thin> <sub_info_bold>71342-82-429461&nbsp;&nbsp;</sub_info_bold>
                    <button class="info-copy-button" onclick="copyText('71342-82-429461')">
                        <i class="fas fa-copy"></i> 복사
                    </button>
                </div>
            </div>
        </div>

        <!-- 맺음 인사 -->
        <div class="content">
            <div class="last-image-container">
                <img src="https://github.com/user-attachments/assets/db1a5013-43e1-4df1-961a-015f50b4d3bd" alt="메인 이미지" class="main-img">
                <div class="overlay-text">
                    축하해주신 모든 분들께 감사드리며
                    <br>
                    보답하는 마음으로 행복하게 살겠습니다.
                </div>
                <div class="details">
                    <span class="halftap"></span>
                    <button class="link-copy-button" onclick="copyCurrentLink()">
                        <i class="fas fa-link"></i> 링크주소 복사하기
                    </button>
                </div>
            </div>
            <span class="break"></span>
            <copy_right_thin>Copyright 2024. DearWorld. All rights reserved</copy_right_thin>
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
        let currentSlide = 1;
        const mainSlider = document.getElementById('mainSlider');
        const mainImage = mainSlider.querySelector('img');
        const slides = document.querySelectorAll('.slider img');
        const thumbnails = document.querySelectorAll('#thumbnailContainer img');

        slides[currentSlide].classList.add('active');

        // 모든 슬라이드를 초기화하는 함수
        function resetSlides() {
            slides.forEach(slide => {
                slide.style.display = 'none'; // 슬라이드를 기본적으로 숨김
                slide.style.opacity = '0';    // 슬라이드를 보이지 않게 함
                slide.style.transition = 'opacity 0.5s ease-in-out'; // 전환 효과 추가
            });
        }

        function changeSlide(direction) {
            resetSlides(); // 모든 슬라이드를 숨김
            
            console.log('Debug 3', currentSlide, direction);

            if (currentSlide == 1 && direction == -1) {
                currentSlide = 8
            }
            else if (currentSlide == 8 && direction == 1) {
                currentSlide = 1
            }
            else {
                currentSlide = (currentSlide + direction + slides.length) % slides.length; // 슬라이드 순환
            }
            slides[currentSlide].style.display = 'block'; // 선택된 슬라이드만 표시
            setTimeout(() => {
                slides[currentSlide].style.opacity = '1'; // 슬라이드를 점차적으로 보이게 함
            }, 10); // 살짝 지연을 주어 display 전환 후 opacity 전환이 일어나게 함

            mainImage.src = slides[currentSlide].src;
            console.log('Current slide index:', currentSlide);
        }

        function showMainImage(thumbnail) {
            resetSlides(); // 모든 슬라이드를 숨김
            mainImage.src = thumbnail.src; // 메인 이미지의 src를 썸네일의 src로 변경

            currentSlide = Array.from(thumbnails).indexOf(thumbnail) + 1;
            
            // 선택된 슬라이드만 보이게 함
            if (currentSlide !== -1) {
                slides[currentSlide].style.display = 'block';
                slides[currentSlide].style.opacity = '1';
            }

            console.log('Thumbnail clicked, current slide index:', currentSlide);
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
        const thumbnails4drag = document.getElementById('thumbnailContainer');
        let isDown = false;
        let startX;
        let scrollLeft;

        thumbnails4drag.addEventListener('mousedown', (e) => {
            isDown = true;
            thumbnails4drag.classList.add('active');
            startX = e.pageX - thumbnails4drag.offsetLeft;
            scrollLeft = thumbnails4drag.scrollLeft;
        });

        thumbnails4drag.addEventListener('mouseleave', () => {
            isDown = false;
            thumbnails4drag.classList.remove('active');
        });

        thumbnails4drag.addEventListener('mouseup', () => {
            isDown = false;
            thumbnails4drag.classList.remove('active');
        });

        thumbnails4drag.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - thumbnails4drag.offsetLeft;
            const walk = (x - startX) * 3; // 스크롤 속도 조절
            thumbnails4drag.scrollLeft = scrollLeft - walk;
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
        function GROOM_toggleAccountInfo() {
            const GROOM_accountContainer = document.getElementById("GROOM_accountContainer");
            const GROOM_toggleButton = document.getElementById("GROOM_toggleButton");

            GROOM_accountContainer.classList.toggle("expanded");

            // 버튼 상태에 따라 클래스 추가/제거
            GROOM_toggleButton.classList.toggle("expanded");

            // 버튼 텍스트 변경
            if (GROOM_toggleButton.classList.contains("expanded")) {
                GROOM_toggleButton.textContent = "내용 숨기기";
            } else {
                GROOM_toggleButton.textContent = "신랑측 마음 전하실 곳";
            }
        }
    </script>

    <script>
        function BRIDE_toggleAccountInfo() {
            const BRIDE_accountContainer = document.getElementById("BRIDE_accountContainer");
            const BRIDE_toggleButton = document.getElementById("BRIDE_toggleButton");

            BRIDE_accountContainer.classList.toggle("expanded");

            // 버튼 상태에 따라 클래스 추가/제거
            BRIDE_toggleButton.classList.toggle("expanded");

            // 버튼 텍스트 변경
            if (BRIDE_toggleButton.classList.contains("expanded")) {
                BRIDE_toggleButton.textContent = "내용 숨기기";
            } else {
                BRIDE_toggleButton.textContent = "신부측 마음 전하실 곳";
            }
        }
    </script>

    <script>
        function copyCurrentLink() {
            const link = window.location.href; // 현재 페이지 링크 가져오기
            navigator.clipboard.writeText(link).then(() => {
                alert('모바일 청첩장 링크가 복사되었습니다!'); // 링크 복사 완료 후 알림
            }).catch(err => {
                console.error('링크 복사 실패:', err);
            });
        }
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