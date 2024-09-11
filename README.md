# 한케어봇
## 1. 제작 동기
포장 아르바이트 중, 어느 한 사무직 직원이 반복적으로 특정 주문건을 삭제하느라 업무에 집중하지 못하는 문제를 발견했고, 이로 인해 사무직 직원에 대한 물류 직원들의 불만이 쌓이는 악순환이 발생했습니다. 

이를 해결하기 위해 파이썬으로 주문 자동 처리 프로그램을 개발해 배포했습니다.

또한, VIP 고객의 입금 상태를 자동으로 처리하는 기능을 추가해 사무직의 업무 효율을 높였으며, 이 프로그램은 현재도 회사에서 사용되고 있습니다.

## 2. 설계
![한케어봇 drawio](https://github.com/coldsteelpope/haancare_bot/assets/128117575/4284b68d-64b8-4f67-a1b8-be47854a10bc)

## 3. 사용 기술
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">

## 4. 기능
### 4.1 배송메시지 추가 및 삭제
#### 배송 메시지 추가
![배송메시지추가](https://github.com/coldsteelpope/haancare_bot/assets/128117575/88785afb-48cb-41eb-b3b6-e67e2e3750f5)

주문 건 처리를 원하는 제목을 리스트에 추가합니다. 추가된 제목이 주문 건에 포함되어 있으면, 한케어 봇은 해당 주문 건을 처리해야 할 주문 것으로 인식합니다.

#### 배송 메시지 삭제
![배송메시지삭제](https://github.com/coldsteelpope/haancare_bot/assets/128117575/99738b56-c033-4520-9825-e7feed655b82)

주문 건 처리 시 무시할 제목을 리스트에서 제거합니다.

### 4.2. 입금 처리
![입금처리](https://github.com/coldsteelpope/haancare_bot/assets/128117575/46605db4-d3f5-4006-8c96-7d543eb90799)

아직 입금 전인 VIP 고객들의 입금 처리를 자동으로 처리합니다.

### 4.3. 특정 주문건 대량 처리
#### 특정 주문건 검색
![배송준비중검색](https://github.com/coldsteelpope/haancare_bot/assets/128117575/626bf8b9-dd5a-4174-9ef8-0269da9ae5dc)

![배송중검색](https://github.com/coldsteelpope/haancare_bot/assets/128117575/8cb53f9b-d4a8-4a5f-9f2e-0ad5cd0012f9)

추가된 배송 메시지를 참고해 특정 주문건을 검색합니다.

#### 특정 주문건 처리
![배송준비중완료](https://github.com/coldsteelpope/haancare_bot/assets/128117575/255df6a3-4730-4ce1-a6aa-e700025f315e)

배송 준비중 페이지에서 검색이 모두 완료되면, 처리해야 할 주문 건에 대해 "이용할 택배 회사"와 "운송장 번호"를 자동으로 기입한 후 배송 상태를 "배송 중"으로 변경합니다.

![배송중완료처리](https://github.com/coldsteelpope/haancare_bot/assets/128117575/39a14c65-b71d-4924-9c47-a699a33fae14)

배송 중 페이지에서 검색이 모두 완료되면, 검색된 모든 주문 건을 자동으로 배송 완료로 처리합니다.
